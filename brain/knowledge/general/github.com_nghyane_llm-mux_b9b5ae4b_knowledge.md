---
id: github.com-nghyane-llm-mux-b9b5ae4b-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:05.587085
---

# KNOWLEDGE EXTRACT: github.com_nghyane_llm-mux_b9b5ae4b
> **Extracted on:** 2026-04-01 08:20:26
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519424/github.com_nghyane_llm-mux_b9b5ae4b

---

## File: `.gitignore`
```
/llm-mux
/launchdock
/launchdock.exe
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Nghia Hoang

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

## File: `README.md`
```markdown
# launchdock

[![CI](https://github.com/nghyane/launchdock/actions/workflows/ci.yml/badge.svg)](https://github.com/nghyane/launchdock/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/nghyane/launchdock)](https://github.com/nghyane/launchdock/releases/latest)
[![GitHub stars](https://img.shields.io/github/stars/nghyane/launchdock)](https://github.com/nghyane/launchdock/stargazers)

Use Claude and GPT across AI coding tools through one local gateway, with both OpenAI-compatible and Claude-native API surfaces.

`launchdock` gives you one local endpoint for tools like OpenCode, Codex, Claude Code, Droid, and Pi.

Why people use it:

- use OpenCode or Codex with the accounts you already have
- use Claude through either OpenAI-compatible chat clients or the native Claude Messages API
- avoid managing separate credentials and configs everywhere
- log in once and reuse managed auth across multiple tools
- push managed auth to a personal server when needed

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/nghyane/launchdock/main/install.sh | sh
launchdock version
```

Optional:

```bash
curl -fsSL https://raw.githubusercontent.com/nghyane/launchdock/main/install.sh | env LAUNCHDOCK_VERSION=v0.1.1 sh
curl -fsSL https://raw.githubusercontent.com/nghyane/launchdock/main/install.sh | env INSTALL_DIR=/usr/local/bin sh
```

## Quickstart

```bash
launchdock auth login claude
launchdock auth login openai

launchdock auth list
launchdock start
launchdock launch opencode --config
```

`launchdock launch <tool>` checks credentials, starts the local runtime if needed, writes tool config when required, and launches the tool.

Check the local API:

```bash
curl http://localhost:8090/v1/models
```

## Authentication

Supported auth sources:

- Claude: `launchdock auth login claude`
- OpenAI/Codex: `launchdock auth login openai`

Why this auth model is useful:

- sign in once through the native Claude/OpenAI login flow
- reuse the same managed auth across local tools and personal servers
- avoid copying API keys into multiple configs or shell environments
- keep the workflow aligned with Claude Code and Codex account-based usage

## Personal server

```bash
launchdock auth push user@server.example.com
ssh user@server.example.com '$HOME/.local/bin/launchdock start'
```

`auth push` installs or updates `launchdock` on the remote host automatically, then imports your managed credentials.

## Supported tools

- `claude-code`
- `codex`
- `opencode`
- `droid`
- `pi`

## Models

`launchdock` exposes both Claude and GPT models from one local provider.

Claude thinking aliases are also available:

- `claude-sonnet-4-6-thinking`
- `claude-opus-4-6-thinking`

These aliases automatically enable Claude thinking for OpenAI-compatible clients that do not serialize Claude thinking config reliably.

## Compatibility

`launchdock` is tested with the official OpenAI Python SDK and works across both Claude and GPT models.

Validated locally with `claude-opus-4-6` and `gpt-5.4` for:

- basic chat
- multi-turn conversations
- streaming
- tool calls
- tool result round-trips

Supported API surfaces:

- `/v1/chat/completions`
- `/v1/responses`
- `/v1/messages`

### Support matrix

| Endpoint | GPT | Claude | Semantics | Tools |
|---|---|---|---|---|
| `/v1/chat/completions` | ✅ | ✅ | OpenAI-compatible chat | ✅ |
| `/v1/responses` | ✅ | ✅ | Native OpenAI Responses semantics | ✅ |
| `/v1/messages` | — | ✅ | Native Claude Messages format | ✅ |

### Endpoint semantics

#### `/v1/chat/completions`

- standard OpenAI-compatible chat chunks
- reasoning/thinking is exposed through compatibility fields such as `choices[].delta.reasoning_content`
- best default for broad client compatibility across GPT and Claude

#### `/v1/responses`

- native OpenAI Responses semantics
- reasoning is exposed through native events/items such as:
  - `response.reasoning_summary_text.delta`
  - `reasoning` output items
  - `function_call` items/events
- preferred endpoint for the richest reasoning lifecycle

#### `/v1/messages`

- native Claude Messages request/response format
- useful for Claude-native clients or integrations that expect Anthropic-style payloads
- uses the same managed Claude account auth as the OpenAI-compatible surfaces

### Tool naming

Claude OAuth internally prefixes tool names with `mcp_` when talking to Anthropic.

`launchdock` strips that prefix before returning tool/function names to clients, so clients still see the original tool name (for example `get_weather`).

### OpenCode note

`launchdock launch opencode --config` merges into an existing OpenCode config instead of overwriting unrelated keys.

For Claude thinking in OpenCode, prefer the model aliases:

- `claude-sonnet-4-6-thinking`
- `claude-opus-4-6-thinking`

These are more reliable than trying to rely on client-side Claude thinking config through a custom OpenAI-compatible provider.

## Commands

```bash
launchdock auth
launchdock launch [tool]
launchdock start | ps | logs | restart | stop
launchdock update
```

## Technical note

`launchdock` runs on `http://localhost:8090`.

State lives in:

- `~/.launchdock/launchdock.pid`
- `~/.launchdock/launchdock.log`
- `~/.config/launchdock/config.json`

Legacy `llm-mux` code is preserved on `legacy/llm-mux`.
```

## File: `auth_cli.go`
```go
package launchdock

import (
	"fmt"
	"os"
	"strings"
	"time"

	authpkg "github.com/nghiahoang/launchdock/internal/auth"
)

func handleAuthCommand() {
	if len(os.Args) < 3 {
		if isTerminal(int(os.Stdin.Fd())) {
			handleAuthInteractive()
			return
		}
		printAuthHelp()
		os.Exit(1)
	}

	switch os.Args[2] {
	case "list":
		handleAuthList()
	case "export":
		handleAuthExport()
	case "import":
		handleAuthImport()
	case "login":
		handleAuthLogin()
	case "push":
		handleAuthPush()
	case "remove":
		handleAuthRemove()
	default:
		fmt.Fprintf(os.Stderr, "Unknown auth command: %s\n\n", os.Args[2])
		printAuthHelp()
		os.Exit(1)
	}
}

func handleAuthRemove() {
	if len(os.Args) < 4 {
		fmt.Fprintln(os.Stderr, "Usage: launchdock auth remove <credential-id>")
		os.Exit(1)
	}
	id := os.Args[3]
	if err := authpkg.RemoveConfigCredential(id); err != nil {
		fmt.Fprintf(os.Stderr, "Remove failed: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("Removed managed credential: %s\n", id)
}

func handleAuthList() {
	views := LoadCredentialViews()
	if len(views) == 0 {
		fmt.Println("No credentials found.")
		return
	}
	for i, v := range views {
		fmt.Println(authListLine(i, v))
	}
}

func handleAuthLogin() {
	provider := "claude"
	if len(os.Args) >= 4 {
		provider = strings.ToLower(os.Args[3])
	}
	switch provider {
	case "claude", "anthropic":
		label := "Claude Account"
		if len(os.Args) >= 5 {
			label = os.Args[4]
		}
		cred, err := authpkg.RunOAuthFlow(label)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Auth failed: %v\n", err)
			os.Exit(1)
		}
		fmt.Fprintf(os.Stderr, "\nAuthenticated: %s\n", cred.Label)
		fmt.Fprintf(os.Stderr, "Token expires: %s\n", cred.ExpiresAt.Format(time.RFC3339))
		fmt.Fprintf(os.Stderr, "Saved to: %s\n", authpkg.ConfigPath())
	case "openai", "codex":
		handleOpenAILogin()
	default:
		fmt.Fprintf(os.Stderr, "Unsupported auth provider: %s\n", provider)
		fmt.Fprintf(os.Stderr, "  Supported: claude, openai\n")
		os.Exit(1)
	}
}

func handleOpenAILogin() {
	cred, err := authpkg.RunOpenAIOAuthFlow("OpenAI Account")
	if err != nil {
		fmt.Fprintf(os.Stderr, "Auth failed: %v\n", err)
		os.Exit(1)
	}
	fmt.Fprintf(os.Stderr, "\nAuthenticated: %s\n", cred.Label)
	if !cred.ExpiresAt.IsZero() {
		fmt.Fprintf(os.Stderr, "Token expires: %s\n", cred.ExpiresAt.Format(time.RFC3339))
	}
	if cred.AccountID != "" {
		fmt.Fprintf(os.Stderr, "Account ID: %s\n", cred.AccountID)
	}
	fmt.Fprintf(os.Stderr, "Saved to: %s\n", authpkg.ConfigPath())
}

func printAuthHelp() {
	fmt.Fprint(os.Stderr, `Usage:
  launchdock auth                          Interactive credential manager
  launchdock auth list
  launchdock auth export [credential-id ...]
  launchdock auth import
  launchdock auth login claude [label]
  launchdock auth login openai
  launchdock auth push <ssh-target> [credential-id ...]
  launchdock auth remove <credential-id>

`)
}
```

## File: `auth_manager.go`
```go
package launchdock

import (
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strings"
	"time"

	authpkg "github.com/nghiahoang/launchdock/internal/auth"
)

type CredentialView struct {
	ID              string
	Label           string
	Email           string
	Provider        string
	AuthType        authpkg.AuthType
	Source          string
	SourceKind      string
	Managed         bool
	Disabled        bool
	Status          string
	StatusMessage   string
	AccountID       string
	CompatibleTools []string
}

func LoadCredentialViews() []CredentialView {
	var views []CredentialView

	if creds, err := authpkg.LoadFromKeychain(); err == nil {
		for _, cred := range creds {
			views = append(views, externalCredentialView(cred, "claude"))
		}
	}

	home, _ := os.UserHomeDir()
	if home != "" {
		if creds, err := authpkg.LoadFromFile(filepath.Join(home, ".codex", "auth.json")); err == nil {
			for _, cred := range creds {
				views = append(views, externalCredentialView(cred, "codex"))
			}
		}
	}

	for _, cc := range authpkg.LoadConfig().Credentials {
		views = append(views, managedCredentialView(cc))
	}

	sort.SliceStable(views, func(i, j int) bool {
		if views[i].Managed != views[j].Managed {
			return views[i].Managed
		}
		if views[i].Provider != views[j].Provider {
			return views[i].Provider < views[j].Provider
		}
		return views[i].Label < views[j].Label
	})

	enrichViewEmails(views)

	return views
}

func enrichViewEmails(views []CredentialView) {
	byAccount := map[string]string{}
	for _, v := range views {
		if v.AccountID != "" && v.Email != "" {
			byAccount[v.Provider+":"+v.AccountID] = v.Email
		}
	}
	for i := range views {
		if views[i].Email != "" || views[i].AccountID == "" {
			continue
		}
		if email := byAccount[views[i].Provider+":"+views[i].AccountID]; email != "" {
			views[i].Email = email
		}
	}
}

func externalCredentialView(cred authpkg.Credential, sourceKind string) CredentialView {
	status := "healthy"
	message := "available"
	if cred.IsExpired() {
		status = "expired"
		message = "access token expired"
	}
	if cred.AuthType == authpkg.AuthAPIKey {
		message = "api key available"
	}
	if sourceKind == "claude" {
		profile := authpkg.LoadClaudeProfile()
		if cred.Email == "" {
			cred.Email = profile.Email
		}
		if cred.Label == "Claude Keychain" && profile.DisplayName != "" {
			cred.Label = profile.DisplayName
		} else if cred.Label == "Claude Keychain" && profile.SubscriptionType != "" {
			cred.Label = humanizeClaudeSubscription(profile.SubscriptionType)
		}
	}
	return CredentialView{
		ID:              cred.Source,
		Label:           cred.Label,
		Email:           cred.Email,
		Provider:        cred.Provider,
		AuthType:        cred.AuthType,
		Source:          cred.Source,
		SourceKind:      sourceKind,
		Status:          status,
		StatusMessage:   message,
		AccountID:       cred.AccountID,
		CompatibleTools: compatibleToolsForProvider(cred.Provider),
	}
}

func humanizeClaudeSubscription(raw string) string {
	raw = strings.ToLower(raw)
	switch {
	case strings.Contains(raw, "max"):
		return "Claude Max"
	case strings.Contains(raw, "pro"):
		return "Claude Pro"
	case strings.Contains(raw, "team"):
		return "Claude Team"
	default:
		return "Claude"
	}
}

func managedCredentialView(cc authpkg.ConfigCredential) CredentialView {
	v := CredentialView{
		ID:              cc.ID,
		Label:           cc.Label,
		Email:           cc.Email,
		Provider:        cc.Provider,
		Source:          "config:" + authpkg.ConfigPath(),
		SourceKind:      "managed",
		Managed:         true,
		Disabled:        cc.Disabled,
		AccountID:       cc.AccountID,
		CompatibleTools: compatibleToolsForProvider(cc.Provider),
	}
	if cc.APIKey != "" {
		v.AuthType = authpkg.AuthAPIKey
		if cc.Disabled {
			v.Status = "disabled"
			v.StatusMessage = "disabled in launchdock"
		} else {
			v.Status = "healthy"
			v.StatusMessage = "managed api key"
		}
		return v
	}
	v.AuthType = authpkg.AuthOAuth
	if cc.Disabled {
		v.Status = "disabled"
		v.StatusMessage = "disabled in launchdock"
		return v
	}
	if cc.RefreshToken == "" {
		v.Status = "invalid"
		v.StatusMessage = "missing refresh token"
		return v
	}
	if cc.AccessToken != "" {
		exp := parseManagedExpiresAt(cc.ExpiresAt)
		if exp.IsZero() || exp.After(time.Now().Add(30*time.Second)) {
			v.Status = "healthy"
			v.StatusMessage = "access token available"
			return v
		}
	}
	var err error
	if cc.Provider == "anthropic" {
		_, _, _, err = authpkg.RefreshClaudeOAuth(cc.RefreshToken)
	} else if cc.Provider == "openai" {
		_, _, _, err = authpkg.RefreshOpenAIOAuth(cc.RefreshToken)
	}
	if err != nil {
		v.Status = "stale"
		v.StatusMessage = "login again or remove this account"
		return v
	}
	v.Status = "healthy"
	v.StatusMessage = "refreshable"
	return v
}

func parseManagedExpiresAt(v string) time.Time {
	if v == "" {
		return time.Time{}
	}
	t, err := time.Parse(time.RFC3339, v)
	if err != nil {
		return time.Time{}
	}
	return t
}

func compatibleToolsForProvider(provider string) []string {
	switch provider {
	case "anthropic":
		return []string{"claude-code", "opencode", "droid", "pi"}
	case "openai":
		return []string{"codex", "opencode", "droid", "pi"}
	default:
		return []string{"opencode", "droid", "pi"}
	}
}

func authStatusLabel(v CredentialView) string {
	switch {
	case v.Disabled:
		return "disabled"
	case v.Status == "healthy":
		return "ready"
	case v.Status == "stale":
		return "relogin"
	case v.Status == "expired":
		return "expired"
	case v.Status == "invalid":
		return "invalid"
	default:
		return v.Status
	}
}

func authProviderLabel(provider string) string {
	switch provider {
	case "anthropic":
		return "Claude"
	case "openai":
		return "OpenAI"
	default:
		return providerDisplayName(provider)
	}
}

func authListLine(i int, v CredentialView) string {
	line := fmt.Sprintf("%d. %-24s %-9s %-8s %s", i+1, truncateAuth(authDisplayName(v), 24), authStatusLabel(v), authProviderLabel(v.Provider), authSourceLabel(v))
	if v.Managed {
		line += fmt.Sprintf(" [id: %s]", v.ID)
	}
	return line
}

func authDisplayName(v CredentialView) string {
	if v.Email != "" {
		return v.Email
	}
	if v.AuthType == authpkg.AuthAPIKey {
		return "API key"
	}
	return v.Label
}

func authSourceLabel(v CredentialView) string {
	switch v.SourceKind {
	case "managed":
		return "Launchdock"
	case "claude":
		return "Claude Code"
	case "codex":
		return "Codex"
	case "env":
		return "Environment"
	default:
		return v.SourceKind
	}
}

func truncateAuth(s string, max int) string {
	if len(s) <= max {
		return s
	}
	if max <= 1 {
		return s[:max]
	}
	return s[:max-1] + "…"
}
```

## File: `auth_transfer.go`
```go
package launchdock

import (
	"bytes"
	"crypto/sha256"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
	"strings"
	"time"

	authpkg "github.com/nghiahoang/launchdock/internal/auth"
	httpxpkg "github.com/nghiahoang/launchdock/internal/httpx"
)

type authExportPayload struct {
	Version     int                        `json:"version"`
	ExportedAt  string                     `json:"exported_at"`
	Credentials []authpkg.ConfigCredential `json:"credentials"`
}

func exportableCredentials(ids []string) ([]authpkg.ConfigCredential, error) {
	lookup := map[string]bool{}
	if len(ids) > 0 {
		for _, id := range ids {
			lookup[id] = true
		}
	}

	var out []authpkg.ConfigCredential
	seen := map[string]bool{}

	appendCred := func(cc authpkg.ConfigCredential) {
		key := cc.Provider + "|" + cc.AccountID + "|" + cc.Email + "|" + cc.Label
		if seen[key] {
			return
		}
		seen[key] = true
		out = append(out, cc)
	}

	// Managed credentials first.
	managed, err := managedConfigCredentials(nil)
	if err == nil {
		for _, cc := range managed {
			if len(lookup) > 0 && !lookup[cc.ID] {
				continue
			}
			appendCred(cc)
			delete(lookup, cc.ID)
		}
	}

	// Export local OAuth credentials too.
	for _, cred := range authpkg.LoadAllCredentials() {
		if cred.AuthType != authpkg.AuthOAuth {
			continue
		}
		if cred.RefreshToken == "" {
			continue
		}
		if len(lookup) > 0 && cred.ID != "" && !lookup[cred.ID] {
			continue
		}
		appendCred(authpkg.ConfigCredential{
			ID:           authpkg.GenerateCredentialID(),
			Label:        cred.Label,
			Provider:     cred.Provider,
			Kind:         cred.Kind,
			AccessToken:  cred.AccessToken,
			ExpiresAt:    authpkg.FormatExpiresAt(cred.ExpiresAt),
			RefreshToken: cred.RefreshToken,
			AccountID:    cred.AccountID,
			Email:        cred.Email,
			Disabled:     false,
		})
		if cred.ID != "" {
			delete(lookup, cred.ID)
		}
	}

	if len(ids) > 0 && len(lookup) > 0 {
		var missing []string
		for id := range lookup {
			missing = append(missing, id)
		}
		return nil, fmt.Errorf("unknown credential ids: %s", strings.Join(missing, ", "))
	}
	if len(out) == 0 {
		return nil, fmt.Errorf("no credentials to export")
	}
	return out, nil
}

func managedConfigCredentials(ids []string) ([]authpkg.ConfigCredential, error) {
	cfg := authpkg.LoadConfig()
	if len(ids) == 0 {
		if len(cfg.Credentials) == 0 {
			return nil, fmt.Errorf("no managed credentials to export")
		}
		return cfg.Credentials, nil
	}
	lookup := map[string]bool{}
	for _, id := range ids {
		lookup[id] = true
	}
	var out []authpkg.ConfigCredential
	for _, cc := range cfg.Credentials {
		if lookup[cc.ID] {
			out = append(out, cc)
			delete(lookup, cc.ID)
		}
	}
	if len(lookup) > 0 {
		var missing []string
		for id := range lookup {
			missing = append(missing, id)
		}
		return nil, fmt.Errorf("unknown credential ids: %s", strings.Join(missing, ", "))
	}
	return out, nil
}

func exportManagedCredentials(ids []string) ([]byte, error) {
	creds, err := exportableCredentials(ids)
	if err != nil {
		return nil, err
	}
	payload := authExportPayload{
		Version:     1,
		ExportedAt:  nowRFC3339(),
		Credentials: creds,
	}
	return json.MarshalIndent(payload, "", "  ")
}

func importManagedCredentials(r io.Reader) (int, error) {
	var payload authExportPayload
	if err := json.NewDecoder(r).Decode(&payload); err != nil {
		return 0, fmt.Errorf("parse import payload: %w", err)
	}
	if payload.Version != 1 {
		return 0, fmt.Errorf("unsupported payload version: %d", payload.Version)
	}
	if len(payload.Credentials) == 0 {
		return 0, fmt.Errorf("no credentials in import payload")
	}
	return mergeImportedCredentials(payload.Credentials)
}

func mergeImportedCredentials(imported []authpkg.ConfigCredential) (int, error) {
	cfg := authpkg.LoadConfig()
	count := 0
	for _, cc := range imported {
		if cc.ID == "" {
			cc.ID = authpkg.GenerateCredentialID()
		}
		match := -1
		for i, existing := range cfg.Credentials {
			if strings.EqualFold(existing.Provider, cc.Provider) {
				if cc.AccountID != "" && existing.AccountID != "" && cc.AccountID == existing.AccountID {
					match = i
					break
				}
				if match == -1 && cc.Email != "" && existing.Email != "" && strings.EqualFold(cc.Email, existing.Email) {
					match = i
				}
			}
		}
		if match >= 0 {
			cc.ID = cfg.Credentials[match].ID
			cfg.Credentials[match] = cc
		} else {
			if i := findByID(cfg.Credentials, cc.ID); i >= 0 {
				cfg.Credentials[i] = cc
			} else {
				cfg.Credentials = append(cfg.Credentials, cc)
			}
		}
		count++
	}
	return count, authpkg.SaveConfig(cfg)
}

func findByID(creds []authpkg.ConfigCredential, id string) int {
	for i, cc := range creds {
		if cc.ID == id {
			return i
		}
	}
	return -1
}

func handleAuthExport() {
	if isTerminal(int(os.Stdout.Fd())) {
		fmt.Fprintln(os.Stderr, "Refusing to print credential export to an interactive terminal.")
		fmt.Fprintln(os.Stderr, "Pipe it to a file or another command, for example:")
		fmt.Fprintln(os.Stderr, "  launchdock auth export > launchdock-auth.json")
		fmt.Fprintln(os.Stderr, "  launchdock auth push user@server.example.com")
		os.Exit(1)
	}
	data, err := exportManagedCredentials(os.Args[3:])
	if err != nil {
		fmt.Fprintf(os.Stderr, "Export failed: %v\n", err)
		os.Exit(1)
	}
	_, _ = os.Stdout.Write(data)
	_, _ = os.Stdout.Write([]byte("\n"))
}

func handleAuthImport() {
	n, err := importManagedCredentials(os.Stdin)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Import failed: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("Imported %d managed credential(s).\n", n)
}

func handleAuthPush() {
	if len(os.Args) < 4 {
		fmt.Fprintln(os.Stderr, "Usage: launchdock auth push <ssh-target> [credential-id ...]")
		os.Exit(1)
	}
	target := os.Args[3]
	ids := os.Args[4:]
	payload, err := exportManagedCredentials(ids)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Push failed: %v\n", err)
		os.Exit(1)
	}
	if err := ensureRemoteLaunchdock(target); err != nil {
		fmt.Fprintf(os.Stderr, "Remote install failed: %v\n", err)
		os.Exit(1)
	}
	cmd := exec.Command("ssh", target, "$HOME/.local/bin/launchdock auth import")
	cmd.Stdin = bytes.NewReader(payload)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Run(); err != nil {
		fmt.Fprintf(os.Stderr, "Push failed: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("Pushed credential(s) to %s\n", target)
}

func ensureRemoteLaunchdock(target string) error {
	if err := installCurrentBinary(target); err == nil {
		return nil
	}

	version := currentVersion()
	if version == "" || version == "dev" {
		version = latestReleaseVersion()
	}
	check := exec.Command("ssh", target, "$HOME/.local/bin/launchdock version 2>/dev/null || launchdock version 2>/dev/null || true")
	out, _ := check.Output()
	remoteVersion := strings.TrimSpace(string(out))
	if remoteVersion == version && remoteVersion != "" {
		return nil
	}
	return installRemoteLaunchdock(target, version)
}

func installCurrentBinary(target string) error {
	bin, cleanup, err := buildBinaryForRemote(target)
	if err != nil {
		return err
	}
	defer cleanup()
	tmp := "/tmp/launchdock-upload"
	copy := exec.Command("scp", bin, target+":"+tmp)
	copy.Stdout = os.Stdout
	copy.Stderr = os.Stderr
	if err := copy.Run(); err != nil {
		return err
	}
	install := exec.Command("ssh", target, "mkdir -p $HOME/.local/bin && install "+tmp+" $HOME/.local/bin/launchdock && $HOME/.local/bin/launchdock version >/dev/null")
	install.Stdout = os.Stdout
	install.Stderr = os.Stderr
	return install.Run()
}

func buildBinaryForRemote(target string) (string, func(), error) {
	out, err := exec.Command("ssh", target, "uname -s && uname -m").Output()
	if err != nil {
		return "", func() {}, err
	}
	parts := strings.Fields(string(out))
	if len(parts) < 2 {
		return "", func() {}, fmt.Errorf("could not detect remote platform")
	}
	osName := strings.ToLower(parts[0])
	arch := strings.ToLower(parts[1])
	switch arch {
	case "x86_64", "amd64":
		arch = "amd64"
	case "aarch64", "arm64":
		arch = "arm64"
	}
	tmp := filepath.Join(os.TempDir(), fmt.Sprintf("launchdock-%s-%s", osName, arch))
	cmd := exec.Command("go", "build", "-o", tmp, "./cmd/launchdock")
	cmd.Env = append(os.Environ(), "GOOS="+osName, "GOARCH="+arch)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	cmd.Dir = mustGetwd()
	if err := cmd.Run(); err != nil {
		return "", func() {}, err
	}
	return tmp, func() { _ = os.Remove(tmp) }, nil
}

func mustGetwd() string {
	wd, err := os.Getwd()
	if err != nil {
		return "."
	}
	return wd
}

func installRemoteLaunchdock(target, version string) error {
	if version == "" {
		return fmt.Errorf("could not resolve launchdock release version")
	}
	installScript := fmt.Sprintf(`set -e
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)
case "$ARCH" in
  x86_64|amd64) ARCH=amd64 ;;
  arm64|aarch64) ARCH=arm64 ;;
  *) echo "unsupported arch: $ARCH" >&2; exit 1 ;;
esac
NAME="launchdock-%s-${OS}-${ARCH}"
URL="https://github.com/nghyane/launchdock/releases/download/%s/${NAME}.tar.gz"
CHECKSUM_URL="https://github.com/nghyane/launchdock/releases/download/%s/checksums-${OS}-${ARCH}.txt"
mkdir -p "$HOME/.local/bin" "$HOME/.cache/launchdock"
command -v curl >/dev/null 2>&1 || { echo "missing required command: curl" >&2; exit 1; }
command -v tar >/dev/null 2>&1 || { echo "missing required command: tar" >&2; exit 1; }
command -v install >/dev/null 2>&1 || { echo "missing required command: install" >&2; exit 1; }
ARCHIVE_PATH="$HOME/.cache/launchdock/${NAME}.tar.gz"
ASSET_NAME="${NAME}.tar.gz"
curl -fsSL "$URL" -o "$ARCHIVE_PATH"
curl -fsSL "$CHECKSUM_URL" -o "$HOME/.cache/launchdock/checksums.txt"
cd "$HOME/.cache/launchdock"
if command -v sha256sum >/dev/null 2>&1; then
  sha256sum -c checksums.txt --ignore-missing
elif command -v shasum >/dev/null 2>&1; then
  EXPECTED=$(awk -v asset="$ASSET_NAME" '$2 == asset {print $1}' checksums.txt)
  ACTUAL=$(shasum -a 256 "$ARCHIVE_PATH" | awk '{print $1}')
  [ "$EXPECTED" = "$ACTUAL" ] || { echo "checksum mismatch" >&2; exit 1; }
elif command -v openssl >/dev/null 2>&1; then
  EXPECTED=$(awk -v asset="$ASSET_NAME" '$2 == asset {print $1}' checksums.txt)
  ACTUAL=$(openssl dgst -sha256 "$ARCHIVE_PATH" | awk '{print $NF}')
  [ "$EXPECTED" = "$ACTUAL" ] || { echo "checksum mismatch" >&2; exit 1; }
else
  echo "missing checksum tool: sha256sum, shasum, or openssl" >&2
  exit 1
fi
rm -rf "$HOME/.cache/launchdock/unpack"
mkdir -p "$HOME/.cache/launchdock/unpack"
tar -xzf "$ARCHIVE_PATH" -C "$HOME/.cache/launchdock/unpack"
install "$HOME/.cache/launchdock/unpack/launchdock" "$HOME/.local/bin/launchdock"
$HOME/.local/bin/launchdock version >/dev/null
`, version, version, version)
	cmd := exec.Command("ssh", target, installScript)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	return cmd.Run()
}

func currentVersion() string {
	if version != "" && version != "dev" {
		return version
	}
	cmd := exec.Command("git", "describe", "--tags", "--exact-match")
	out, err := cmd.Output()
	if err == nil {
		return string(bytes.TrimSpace(out))
	}
	return version
}

func latestReleaseVersion() string {
	req, err := http.NewRequest(http.MethodGet, "https://api.github.com/repos/nghyane/launchdock/releases/latest", nil)
	if err != nil {
		return ""
	}
	req.Header.Set("User-Agent", "launchdock/"+currentVersion())
	req.Header.Set("Accept", "application/vnd.github+json")
	resp, err := httpxpkg.APIClient.Do(req)
	if err != nil {
		return ""
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusOK {
		return ""
	}
	var result struct {
		TagName string `json:"tag_name"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return ""
	}
	return result.TagName
}

func handleUpdateCommand() {
	version := ""
	args := os.Args[2:]
	for i, arg := range args {
		if arg == "--version" && i+1 < len(args) {
			version = args[i+1]
		}
	}
	current := currentVersion()
	if version == "" {
		version = latestReleaseVersion()
	}
	if version == "" {
		fmt.Fprintln(os.Stderr, "Update failed: could not resolve release version")
		os.Exit(1)
	}
	fmt.Printf("Current: %s\nLatest:  %s\n", current, version)
	if current == version && current != "dev" {
		fmt.Println("Already up to date.")
		return
	}
	if runtime.GOOS == "windows" {
		fmt.Fprintln(os.Stderr, "Update is not supported automatically on Windows yet.")
		os.Exit(1)
	}
	if err := installLocalLaunchdock(version); err != nil {
		fmt.Fprintf(os.Stderr, "Update failed: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("Updated launchdock to %s\n", version)
}

func handleVersionCommand() {
	fmt.Println(currentVersion())
}

func installLocalLaunchdock(version string) error {
	asset := releaseAssetName(version, runtime.GOOS, runtime.GOARCH)
	if asset == "" {
		return fmt.Errorf("unsupported platform: %s/%s", runtime.GOOS, runtime.GOARCH)
	}
	url := fmt.Sprintf("https://github.com/nghyane/launchdock/releases/download/%s/%s", version, asset)
	checksumURL := fmt.Sprintf("https://github.com/nghyane/launchdock/releases/download/%s/%s", version, releaseChecksumAsset(runtime.GOOS, runtime.GOARCH))
	tmpDir, err := os.MkdirTemp("", "launchdock-update-")
	if err != nil {
		return err
	}
	defer os.RemoveAll(tmpDir)
	archivePath := filepath.Join(tmpDir, asset)
	if err := downloadFile(url, archivePath); err != nil {
		return err
	}
	checksumPath := filepath.Join(tmpDir, "checksums.txt")
	if err := downloadFile(checksumURL, checksumPath); err != nil {
		return err
	}
	if err := verifyChecksum(archivePath, checksumPath); err != nil {
		return err
	}
	binPath, err := extractReleaseBinary(archivePath, tmpDir)
	if err != nil {
		return err
	}
	execPath, err := os.Executable()
	if err != nil {
		return err
	}
	if err := os.Rename(binPath, execPath+".new"); err != nil {
		return err
	}
	return os.Rename(execPath+".new", execPath)
}

func releaseChecksumAsset(goos, goarch string) string {
	return fmt.Sprintf("checksums-%s-%s.txt", goos, goarch)
}

func releaseAssetName(version, goos, goarch string) string {
	switch goos {
	case "linux", "darwin":
		if goarch == "amd64" || goarch == "arm64" {
			return fmt.Sprintf("launchdock-%s-%s-%s.tar.gz", version, goos, goarch)
		}
	case "windows":
		if goarch == "amd64" {
			return fmt.Sprintf("launchdock-%s-%s-%s.zip", version, goos, goarch)
		}
	}
	return ""
}

func downloadFile(url, path string) error {
	req, err := http.NewRequest(http.MethodGet, url, nil)
	if err != nil {
		return err
	}
	req.Header.Set("User-Agent", "launchdock/"+currentVersion())
	resp, err := httpxpkg.APIClient.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	if resp.StatusCode != 200 {
		body, _ := io.ReadAll(io.LimitReader(resp.Body, 1024))
		return fmt.Errorf("download failed: %s: %s", resp.Status, strings.TrimSpace(string(body)))
	}
	f, err := os.Create(path)
	if err != nil {
		return err
	}
	defer f.Close()
	_, err = io.Copy(f, resp.Body)
	return err
}

func extractReleaseBinary(archivePath, dir string) (string, error) {
	cmd := exec.Command("tar", "-xzf", archivePath, "-C", dir)
	if err := cmd.Run(); err != nil {
		return "", err
	}
	path := filepath.Join(dir, "launchdock")
	if _, err := os.Stat(path); err == nil {
		return path, nil
	}
	return "", fmt.Errorf("launchdock binary not found in archive")
}

func verifyChecksum(archivePath, checksumPath string) error {
	archiveName := filepath.Base(archivePath)
	checksums, err := os.ReadFile(checksumPath)
	if err != nil {
		return err
	}
	expected := ""
	for _, line := range strings.Split(string(checksums), "\n") {
		fields := strings.Fields(line)
		if len(fields) >= 2 && fields[1] == archiveName {
			expected = fields[0]
			break
		}
	}
	if expected == "" {
		return fmt.Errorf("checksum not found for %s", archiveName)
	}
	data, err := os.ReadFile(archivePath)
	if err != nil {
		return err
	}
	sum := fmt.Sprintf("%x", sha256.Sum256(data))
	if sum != expected {
		return fmt.Errorf("checksum mismatch for %s", archiveName)
	}
	return nil
}

func nowRFC3339() string {
	return nowFunc().UTC().Format("2006-01-02T15:04:05Z07:00")
}

var nowFunc = func() time.Time { return time.Now() }
```

## File: `auth_tui.go`
```go
//go:build darwin || linux

package launchdock

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"

	authpkg "github.com/nghiahoang/launchdock/internal/auth"
)

func handleAuthInteractive() {
	views := LoadCredentialViews()
	fd := int(os.Stdin.Fd())
	oldState, err := makeRaw(fd)
	if err != nil {
		handleAuthList()
		return
	}
	defer restore(fd, oldState)
	defer fmt.Print(ansiShowCur)
	fmt.Print(ansiHideCur)

	cursor := 0
	for {
		if cursor >= len(views) && len(views) > 0 {
			cursor = len(views) - 1
		}
		renderAuthManager(views, cursor)
		key, isArrow := readKey(fd)
		if isArrow {
			switch key {
			case 'A':
				if len(views) > 0 {
					cursor--
					if cursor < 0 {
						cursor = len(views) - 1
					}
				}
			case 'B':
				if len(views) > 0 {
					cursor++
					if cursor >= len(views) {
						cursor = 0
					}
				}
			}
			continue
		}

		switch key {
		case 'q', 3:
			clearAuthScreen()
			return
		case 'k':
			if len(views) > 0 {
				cursor--
				if cursor < 0 {
					cursor = len(views) - 1
				}
			}
		case 'j':
			if len(views) > 0 {
				cursor++
				if cursor >= len(views) {
					cursor = 0
				}
			}
		case 'r':
			views = LoadCredentialViews()
		case 'a':
			oldState = suspendAuthRaw(fd, oldState, func() {
				provider := runPicker("Add credential:", []string{"Claude", "OpenAI"})
				switch provider {
				case 0:
					_, _ = authpkg.RunOAuthFlow("Claude Account")
				case 1:
					_, _ = authpkg.RunOpenAIOAuthFlow("OpenAI Account")
				}
			})
			views = LoadCredentialViews()
		case 'x':
			if len(views) == 0 || !views[cursor].Managed {
				continue
			}
			selected := views[cursor]
			oldState = suspendAuthRaw(fd, oldState, func() {
				if runConfirm("Remove managed credential " + selected.Label + "?") {
					if err := authpkg.RemoveConfigCredential(selected.ID); err != nil {
						fmt.Fprintf(os.Stderr, "Error: %v\n", err)
					}
				}
			})
			views = LoadCredentialViews()
		case 'e':
			if len(views) == 0 || !views[cursor].Managed {
				continue
			}
			_ = authpkg.ToggleConfigCredentialDisabled(views[cursor].ID)
			views = LoadCredentialViews()
		}
	}
}

func suspendAuthRaw(fd int, oldState *termios, fn func()) *termios {
	restore(fd, oldState)
	fmt.Print(ansiShowCur)
	fn()
	newState, err := makeRaw(fd)
	if err == nil {
		fmt.Print(ansiHideCur)
		return newState
	}
	return oldState
}

func renderAuthManager(views []CredentialView, cursor int) {
	clearAuthScreen()
	width := authTerminalWidth()
	height := authTerminalHeight()
	header := "Launchdock Auth"
	help := "(j/k or ↑↓ move, a add, e enable/disable, x remove, r refresh, q quit)"
	availableHelp := width - visibleWidth(header) - 1
	if availableHelp < 0 {
		availableHelp = 0
	}
	headerLine := header
	if availableHelp > 0 {
		headerLine += " " + truncate(help, availableHelp)
	}
	fmt.Printf("%s%s%s\n\n", ansiBold, truncate(headerLine, width), ansiReset)

	if len(views) == 0 {
		fmt.Println("  No credentials found.")
		fmt.Println("  Press 'a' to add Claude or OpenAI login.")
		return
	}

	nameWidth := 24
	if width < 40 {
		nameWidth = 16
	}
	statusWidth := 9
	rowSummaryWidth := width - visibleWidth("❯ ") - nameWidth - 1 - statusWidth - 1
	if rowSummaryWidth < 0 {
		rowSummaryWidth = 0
	}
	listHeight := height - 14
	if listHeight < 3 {
		listHeight = 3
	}
	start, end := authVisibleRange(len(views), cursor, listHeight)
	if start > 0 {
		fmt.Printf("  %s↑ %d more%s\n", ansiDim, start, ansiReset)
	}
	for i := start; i < end; i++ {
		v := views[i]
		prefix := "  "
		if i == cursor {
			prefix = fmt.Sprintf("%s❯%s ", ansiCyan, ansiReset)
		}
		fmt.Printf("%s%-*s %s%-*s%s %s\n", prefix, nameWidth, padRight(truncate(authDisplayName(v), nameWidth), nameWidth), authStatusColor(v), statusWidth, padRight(truncate(authStatusLabel(v), statusWidth), statusWidth), ansiReset, truncate(authRowSummary(v), rowSummaryWidth))
	}
	if end < len(views) {
		fmt.Printf("  %s↓ %d more%s\n", ansiDim, len(views)-end, ansiReset)
	}

	v := views[cursor]
	fmt.Printf("\n%sDetails%s\n", ansiBold, ansiReset)
	detailWidth := width - visibleWidth("  Label:    ")
	if detailWidth < 0 {
		detailWidth = 0
	}
	printDetailLine("Label", v.Label, detailWidth)
	if v.Email != "" {
		printDetailLine("Email", v.Email, detailWidth)
	}
	printDetailLine("Provider", authProviderLabel(v.Provider), detailWidth)
	printDetailLine("Type", string(v.AuthType), detailWidth)
	printDetailLine("Source", v.Source, detailWidth)
	if v.Managed {
		printDetailLine("ID", v.ID, detailWidth)
	}
	printDetailLineStyled("Status", authStatusColor(v), authStatusLabel(v), detailWidth)
	if v.StatusMessage != "" {
		printDetailLine("Note", v.StatusMessage, detailWidth)
	}
	if v.AccountID != "" {
		printDetailLine("Account", v.AccountID, detailWidth)
	}
	if len(v.CompatibleTools) > 0 {
		printDetailLine("Tools", strings.Join(v.CompatibleTools, ", "), detailWidth)
	}
	if v.Managed {
		printDetailLine("Actions", "e enable/disable, x remove", detailWidth)
	} else {
		printDetailLine("Actions", fmt.Sprintf("read-only (%s source)", v.SourceKind), detailWidth)
	}
}

func printDetailLine(label string, value string, width int) {
	printDetailLineStyled(label, "", value, width)
}

func printDetailLineStyled(label string, style string, value string, width int) {
	prefix := fmt.Sprintf("  %-8s ", label+":")
	available := width - visibleWidth(prefix)
	if available < 0 {
		available = 0
	}
	trimmed := truncate(value, available)
	if style == "" {
		fmt.Printf("%s%s\n", prefix, trimmed)
		return
	}
	fmt.Printf("%s%s%s%s\n", prefix, style, trimmed, ansiReset)
}

func authTerminalWidth() int {
	if cols := os.Getenv("COLUMNS"); cols != "" {
		if n, err := strconv.Atoi(cols); err == nil && n > 0 {
			return n
		}
	}
	if width, _, err := getTerminalSize(int(os.Stdout.Fd())); err == nil && width > 0 {
		return width
	}
	return 100
}

func authTerminalHeight() int {
	if lines := os.Getenv("LINES"); lines != "" {
		if n, err := strconv.Atoi(lines); err == nil && n > 0 {
			return n
		}
	}
	if _, height, err := getTerminalSize(int(os.Stdout.Fd())); err == nil && height > 0 {
		return height
	}
	return 24
}

func authVisibleRange(total int, cursor int, maxRows int) (start int, end int) {
	if total <= 0 || maxRows <= 0 || total <= maxRows {
		return 0, total
	}
	start = cursor - maxRows/2
	if start < 0 {
		start = 0
	}
	end = start + maxRows
	if end > total {
		end = total
		start = end - maxRows
		if start < 0 {
			start = 0
		}
	}
	return start, end
}

func visibleWidth(s string) int {
	return len([]rune(s))
}

func padRight(s string, width int) string {
	r := []rune(s)
	if len(r) >= width {
		return s
	}
	return s + strings.Repeat(" ", width-len(r))
}

func clearAuthScreen() {
	fmt.Print("\033[H\033[2J")
}

func authStatusColor(v CredentialView) string {
	switch authStatusLabel(v) {
	case "ready":
		return ansiGreen
	case "disabled":
		return ansiDim
	default:
		return ansiYellow
	}
}

func authRowSummary(v CredentialView) string {
	if authStatusLabel(v) == "relogin" {
		return "login again or remove this account"
	}
	if v.Managed {
		return "managed by launchdock"
	}
	return authSourceLabel(v)
}

func addManagedAPIKeyInteractive(provider string) {
	reader := bufio.NewReader(os.Stdin)
	fmt.Printf("Enter %s API key: ", providerDisplayName(provider))
	key, err := reader.ReadString('\n')
	if err != nil {
		fmt.Fprintf(os.Stderr, "Read failed: %v\n", err)
		return
	}
	key = strings.TrimSpace(key)
	if key == "" {
		fmt.Fprintln(os.Stderr, "API key is empty")
		return
	}
	label := providerDisplayName(provider) + " API key"
	if err := authpkg.SaveAPIKeyToConfig(provider, label, key); err != nil {
		fmt.Fprintf(os.Stderr, "Save failed: %v\n", err)
	}
}

func truncate(s string, max int) string {
	runes := []rune(s)
	if len(runes) <= max {
		return s
	}
	if max <= 0 {
		return ""
	}
	if max == 1 {
		return string(runes[:1])
	}
	return string(runes[:max-1]) + "…"
}
```

## File: `auth_tui_windows.go`
```go
//go:build windows

package launchdock

func handleAuthInteractive() {
	handleAuthList()
}
```

## File: `go.mod`
```
module github.com/nghiahoang/launchdock

go 1.25.0
```

## File: `install.sh`
```bash
#!/bin/sh
set -eu

REPO="nghyane/launchdock"
INSTALL_DIR="${INSTALL_DIR:-$HOME/.local/bin}"
LAUNCHDOCK_VERSION="${LAUNCHDOCK_VERSION:-}"

need_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    printf 'Missing required command: %s\n' "$1" >&2
    exit 1
  fi
}

need_cmd curl
need_cmd tar

OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)
case "$ARCH" in
  x86_64|amd64) ARCH="amd64" ;;
  arm64|aarch64) ARCH="arm64" ;;
  *)
    printf 'Unsupported architecture: %s\n' "$ARCH" >&2
    exit 1
    ;;
esac

case "$OS" in
  linux|darwin) ;;
  *)
    printf 'Unsupported OS for install.sh: %s\n' "$OS" >&2
    exit 1
    ;;
esac

if [ -z "$LAUNCHDOCK_VERSION" ]; then
  need_cmd sed
  LAUNCHDOCK_VERSION=$(curl -fsSL "https://api.github.com/repos/$REPO/releases/latest" | sed -n 's/.*"tag_name": *"\([^"]*\)".*/\1/p' | head -n 1)
fi

if [ -z "$LAUNCHDOCK_VERSION" ]; then
  printf 'Could not determine latest release version\n' >&2
  exit 1
fi

ASSET="launchdock-${LAUNCHDOCK_VERSION}-${OS}-${ARCH}.tar.gz"
CHECKSUMS="checksums-${OS}-${ARCH}.txt"
BASE_URL="https://github.com/$REPO/releases/download/$LAUNCHDOCK_VERSION"

TMP_DIR=$(mktemp -d)
cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT INT TERM

ARCHIVE_PATH="$TMP_DIR/$ASSET"
CHECKSUM_PATH="$TMP_DIR/$CHECKSUMS"

printf 'Installing launchdock %s for %s/%s\n' "$LAUNCHDOCK_VERSION" "$OS" "$ARCH"
curl -fsSL "$BASE_URL/$ASSET" -o "$ARCHIVE_PATH"
curl -fsSL "$BASE_URL/$CHECKSUMS" -o "$CHECKSUM_PATH"

EXPECTED=$(awk -v asset="$ASSET" '$2 == asset {print $1}' "$CHECKSUM_PATH")
if [ -z "$EXPECTED" ]; then
  printf 'Checksum not found for %s\n' "$ASSET" >&2
  exit 1
fi

ACTUAL=""
if command -v sha256sum >/dev/null 2>&1; then
  ACTUAL=$(sha256sum "$ARCHIVE_PATH" | awk '{print $1}')
elif command -v shasum >/dev/null 2>&1; then
  ACTUAL=$(shasum -a 256 "$ARCHIVE_PATH" | awk '{print $1}')
elif command -v openssl >/dev/null 2>&1; then
  ACTUAL=$(openssl dgst -sha256 "$ARCHIVE_PATH" | awk '{print $NF}')
else
  printf 'Need sha256sum, shasum, or openssl for checksum verification\n' >&2
  exit 1
fi

if [ "$EXPECTED" != "$ACTUAL" ]; then
  printf 'Checksum mismatch for %s\n' "$ASSET" >&2
  exit 1
fi

mkdir -p "$TMP_DIR/unpack" "$INSTALL_DIR"
tar -xzf "$ARCHIVE_PATH" -C "$TMP_DIR/unpack"
install "$TMP_DIR/unpack/launchdock" "$INSTALL_DIR/launchdock"

printf 'Installed to %s/launchdock\n' "$INSTALL_DIR"
case ":$PATH:" in
  *":$INSTALL_DIR:"*) ;;
  *)
    printf 'Add this to your shell profile if needed:\n'
    printf '  export PATH="%s:$PATH"\n' "$INSTALL_DIR"
    ;;
esac

"$INSTALL_DIR/launchdock" version || true
```

## File: `launch_cli.go`
```go
package launchdock

import (
	"fmt"
	"os"
	"strings"
)

func handleLaunchCommand() {
	var toolName, modelFlag string
	configOnly := false
	skipNext := false
	args := os.Args[2:]

	for i, arg := range args {
		if skipNext {
			skipNext = false
			continue
		}
		switch arg {
		case "--config":
			configOnly = true
		case "--port":
			skipNext = true
		case "--model":
			if i+1 < len(args) {
				modelFlag = args[i+1]
			}
			skipNext = true
		default:
			if strings.HasPrefix(arg, "--") {
				continue
			}
			if toolName == "" {
				toolName = strings.ToLower(arg)
			}
		}
	}

	if toolName == "" {
		handleLaunchInteractive()
		return
	}
	if toolName == "claude" {
		toolName = "claude-code"
	}

	t := findTool(toolName)
	if t == nil {
		fmt.Fprintf(os.Stderr, "Unknown tool: %s\n\n", toolName)
		printLaunchHelp()
		os.Exit(1)
	}
	if !isInstalled(t.Binary) {
		fmt.Fprintf(os.Stderr, "✗ %s not found in PATH\n", t.Binary)
		fmt.Fprintf(os.Stderr, "  Install %s first.\n", t.Desc)
		os.Exit(1)
	}

	cfg := resolveLaunchConfig()
	validateLaunchReadiness(cfg, t)
	if !configOnly {
		if err := ensureServerRunning(cfg); err != nil {
			fmt.Fprintf(os.Stderr, "✗ failed to start launchdock: %v\n", err)
			os.Exit(1)
		}
	}

	model := resolveLaunchModel(cfg, t, modelFlag)
	fmt.Printf("  %s%s%s → %s\n", ansiBold, t.Name, ansiReset, model)
	if t.Config != nil {
		t.Config(cfg, model)
	}
	if configOnly {
		fmt.Printf("\n  %s✓ Configured%s\n", ansiGreen, ansiReset)
		return
	}
	launchTool(t, cfg, model)
}

func validateLaunchReadiness(cfg LaunchConfig, t *Tool) {
	if !cfg.HasCreds {
		fmt.Fprintf(os.Stderr, "✗ No credentials found\n")
		fmt.Fprintf(os.Stderr, "  Run: launchdock auth login claude\n")
		os.Exit(1)
	}
	if t.Provider == "" || cfg.HasProvider(t.Provider) {
		return
	}
	fmt.Fprintf(os.Stderr, "✗ No %s credentials found for %s\n", providerDisplayName(t.Provider), t.Name)
	fmt.Fprintf(os.Stderr, "  Found providers: %s\n", strings.Join(discoveredProviders(cfg), ", "))
	if t.Provider == "anthropic" {
		fmt.Fprintf(os.Stderr, "  Run: launchdock auth login claude\n")
	} else {
		fmt.Fprintf(os.Stderr, "  Add %s credentials via local auth or env vars\n", providerDisplayName(t.Provider))
	}
	os.Exit(1)
}

func resolveLaunchModel(cfg LaunchConfig, t *Tool, forced string) string {
	if forced != "" {
		return forced
	}
	candidates := candidateModelIDs(cfg, t.Provider)
	if len(candidates) == 1 {
		return candidates[0]
	}
	if len(candidates) > 1 && isTerminal(int(os.Stdin.Fd())) {
		fmt.Printf("\n  %s⚡ %d models available%s\n\n", ansiBold, len(candidates), ansiReset)
		idx := runPicker("Select model for "+t.Name+":", candidates)
		if idx < 0 {
			fmt.Println("  Cancelled.")
			os.Exit(0)
		}
		return candidates[idx]
	}
	if len(candidates) > 0 {
		return candidates[0]
	}
	return "claude-sonnet-4-20250514"
}

func handleLaunchInteractive() {
	cfg := resolveLaunchConfig()
	if !isTerminal(int(os.Stdin.Fd())) {
		handleLaunchList(cfg)
		return
	}
	if !cfg.HasCreds {
		fmt.Fprintf(os.Stderr, "✗ No credentials found\n")
		fmt.Fprintf(os.Stderr, "  Run: launchdock auth login claude\n")
		os.Exit(1)
	}
	if err := ensureServerRunning(cfg); err != nil {
		fmt.Fprintf(os.Stderr, "✗ failed to start launchdock: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("\n  %s⚡ %d models available%s\n\n", ansiBold, len(cfg.Models), ansiReset)
	var items []checkboxItem
	var launchable []*Tool
	for i := range tools {
		t := &tools[i]
		installed := isInstalled(t.Binary)
		desc := t.Desc
		if installed {
			desc += fmt.Sprintf(" %s(✓)%s", ansiGreen, ansiReset)
		} else {
			desc += fmt.Sprintf(" %s(not found)%s", ansiDim, ansiReset)
		}
		items = append(items, checkboxItem{label: t.Name, desc: desc, disabled: !installed})
		launchable = append(launchable, t)
	}
	selected := runCheckbox("Select tool to launch:", items)
	if selected == nil || len(selected) == 0 {
		return
	}
	t := launchable[selected[0]]
	validateLaunchReadiness(cfg, t)
	model := resolveLaunchModel(cfg, t, "")
	fmt.Printf("\n  %s%s%s → %s\n", ansiBold, t.Name, ansiReset, model)
	if t.Config != nil {
		t.Config(cfg, model)
	}
	launchTool(t, cfg, model)
}

func handleLaunchList(cfg LaunchConfig) {
	fmt.Print("launchdock launch — available tools:\n\n")
	for _, t := range tools {
		status := "✗ not found"
		if isInstalled(t.Binary) {
			status = "✓ installed"
		}
		fmt.Printf("  %-12s %-25s %s\n", t.Name, t.Desc, status)
	}
	if cfg.HasCreds {
		fmt.Printf("\n  Models (%d):\n", len(cfg.Models))
		for _, m := range cfg.Models {
			fmt.Printf("    %s (%s)\n", m.ID, m.Provider)
		}
	}
	fmt.Println()
	printLaunchHelp()
}

func printLaunchHelp() {
	fmt.Print(`Usage: launchdock launch [tool] [--model MODEL] [--config] [--port PORT]

  launchdock launch                  Interactive tool & model picker
  launchdock launch <tool>           Launch tool with model picker
  launchdock launch <tool> --model X Launch tool with specific model
  launchdock launch <tool> --config  Write config only (don't launch)

Tools: claude-code (claude), codex, opencode, droid, pi

`)
}
```

## File: `main.go`
```go
package launchdock

import (
	"context"
	"crypto/rand"
	"fmt"
	"log/slog"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	authpkg "github.com/nghiahoang/launchdock/internal/auth"
	httpapipkg "github.com/nghiahoang/launchdock/internal/httpapi"
	providerspkg "github.com/nghiahoang/launchdock/internal/providers"
)

var version = "dev"

func Run() {
	// macOS Security.framework verification can fail in sandboxed/local setups;
	// force pure-Go x509 verification unless the user explicitly overrides it.
	if os.Getenv("GODEBUG") == "" {
		_ = os.Setenv("GODEBUG", "x509usecgo=0")
	}

	slog.SetDefault(slog.New(slog.NewTextHandler(os.Stderr, &slog.HandlerOptions{Level: slog.LevelInfo})))

	if len(os.Args) >= 2 {
		switch os.Args[1] {
		case "auth":
			handleAuthCommand()
			return
		case "launch":
			handleLaunchCommand()
			return
		case "start":
			handleStartCommand()
			return
		case "serve":
			break
		case "ps":
			handlePSCommand()
			return
		case "logs":
			handleLogsCommand()
			return
		case "stop":
			handleStopCommand()
			return
		case "restart":
			handleRestartCommand()
			return
		case "update":
			handleUpdateCommand()
			return
		case "version":
			handleVersionCommand()
			return
		}
	}

	creds := authpkg.LoadAllCredentials()
	if len(creds) == 0 {
		slog.Error("no credentials found", "hint", "run `launchdock auth login claude` or `launchdock auth login openai`")
		os.Exit(1)
	}
	for _, c := range creds {
		slog.Info("loaded credential", "provider", c.Provider, "type", c.AuthType, "label", c.Label, "source", c.Source)
	}

	pool := providerspkg.NewPool(creds)
	anthropicProvider := &providerspkg.AnthropicProvider{}
	openaiProvider := &providerspkg.OpenAIProvider{}
	providers := []providerspkg.Provider{anthropicProvider, openaiProvider}
	httpapipkg.ResetModelCache()

	mux := http.NewServeMux()
	mux.HandleFunc("/v1/chat/completions", httpapipkg.HandleChatCompletions(pool, providers))
	mux.HandleFunc("/v1/messages", httpapipkg.HandleMessages(pool, anthropicProvider))
	mux.HandleFunc("/v1/responses", httpapipkg.HandleResponses(pool, openaiProvider, anthropicProvider))
	mux.HandleFunc("/v1/models", httpapipkg.HandleModels(pool, anthropicProvider))
	mux.HandleFunc("/health", httpapipkg.HandleHealth(pool))
	mux.HandleFunc("/", httpapipkg.HandleHealth(pool))

	port := os.Getenv("PORT")
	if port == "" {
		port = "8090"
	}
	server := &http.Server{
		Addr:         ":" + port,
		Handler:      withCORS(withRequestID(mux)),
		ReadTimeout:  30 * time.Second,
		WriteTimeout: 10 * time.Minute,
		IdleTimeout:  120 * time.Second,
	}

	slog.Info("launchdock listening", "addr", ":"+port, "credentials", len(creds), "providers", pool.Providers())

	go func() {
		sigCh := make(chan os.Signal, 1)
		signal.Notify(sigCh, syscall.SIGINT, syscall.SIGTERM)
		sig := <-sigCh
		slog.Info("shutting down", "signal", sig)
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		defer cancel()
		if err := server.Shutdown(ctx); err != nil {
			slog.Error("shutdown error", "error", err)
		}
	}()

	if err := server.ListenAndServe(); err != http.ErrServerClosed {
		fmt.Fprintf(os.Stderr, "server error: %v\n", err)
		os.Exit(1)
	}
	slog.Info("server stopped")
}

func withRequestID(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		reqID := r.Header.Get("X-Request-ID")
		if reqID == "" {
			reqID = shortID()
		}
		w.Header().Set("X-Request-ID", reqID)
		slog.Info("request", "method", r.Method, "path", r.URL.Path, "req_id", reqID)
		next.ServeHTTP(w, r)
	})
}

func withCORS(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Access-Control-Allow-Origin", "*")
		w.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
		w.Header().Set("Access-Control-Allow-Headers", "Content-Type, Authorization, anthropic-version, anthropic-beta, x-api-key")
		if r.Method == http.MethodOptions {
			w.WriteHeader(http.StatusNoContent)
			return
		}
		next.ServeHTTP(w, r)
	})
}

func shortID() string {
	b := make([]byte, 8)
	_, _ = rand.Read(b)
	return fmt.Sprintf("%x", b)
}
```

## File: `model_capabilities.go`
```go
package launchdock

import (
	_ "embed"
	"encoding/json"
	"sync"
)

//go:embed model_capabilities.json
var modelCapabilitiesSnapshot []byte

type LaunchModelMetadata struct {
	Provider    string         `json:"provider"`
	Name        string         `json:"name"`
	Attachment  bool           `json:"attachment"`
	Reasoning   bool           `json:"reasoning"`
	ToolCall    bool           `json:"tool_call"`
	Temperature bool           `json:"temperature"`
	Limit       map[string]any `json:"limit"`
}

var (
	launchModelMetadataOnce sync.Once
	launchModelMetadata     map[string]LaunchModelMetadata
)

func lookupLaunchModelMetadata(id string) (LaunchModelMetadata, bool) {
	launchModelMetadataOnce.Do(func() {
		_ = json.Unmarshal(modelCapabilitiesSnapshot, &launchModelMetadata)
		if launchModelMetadata == nil {
			launchModelMetadata = map[string]LaunchModelMetadata{}
		}
	})
	md, ok := launchModelMetadata[id]
	return md, ok
}
```

## File: `model_capabilities.json`
```json
{
  "claude-3-haiku-20240307": {
    "provider": "anthropic",
    "name": "Claude Haiku 3",
    "attachment": true,
    "reasoning": false,
    "tool_call": true,
    "temperature": true,
    "limit": {"context": 200000, "output": 4096}
  },
  "claude-haiku-4-5-20251001": {
    "provider": "anthropic",
    "name": "Claude Haiku 4.5",
    "attachment": true,
    "reasoning": true,
    "tool_call": true,
    "temperature": true,
    "limit": {"context": 200000, "output": 64000}
  },
  "claude-opus-4-1-20250805": {
    "provider": "anthropic",
    "name": "Claude Opus 4.1",
    "attachment": true,
    "reasoning": true,
    "tool_call": true,
    "temperature": true,
    "limit": {"context": 200000, "output": 32000}
  },
  "claude-opus-4-20250514": {
    "provider": "anthropic",
    "name": "Claude Opus 4",
    "attachment": true,
    "reasoning": true,
    "tool_call": true,
    "temperature": true,
    "limit": {"context": 200000, "output": 32000}
  },
  "claude-opus-4-5-20251101": {
    "provider": "anthropic",
    "name": "Claude Opus 4.5",
    "attachment": true,
    "reasoning": true,
    "tool_call": true,
    "temperature": true,
    "limit": {"context": 200000, "output": 64000}
  },
  "claude-opus-4-6": {
    "provider": "anthropic",
    "name": "Claude Opus 4.6",
    "attachment": true,
    "reasoning": true,
    "tool_call": true,
    "temperature": true,
    "limit": {"context": 1000000, "output": 128000}
  },
  "claude-sonnet-4-20250514": {
    "provider": "anthropic",
    "name": "Claude Sonnet 4",
    "attachment": true,
    "reasoning": true,
    "tool_call": true,
    "temperature": true,
    "limit": {"context": 200000, "output": 64000}
  },
  "claude-sonnet-4-5-20250929": {
    "provider": "anthropic",
    "name": "Claude Sonnet 4.5",
    "attachment": true,
    "reasoning": true,
    "tool_call": true,
    "temperature": true,
    "limit": {"context": 200000, "output": 64000}
  },
  "claude-sonnet-4-6": {
    "provider": "anthropic",
    "name": "Claude Sonnet 4.6",
    "attachment": true,
    "reasoning": true,
    "tool_call": true,
    "temperature": true,
    "limit": {"context": 1000000, "output": 64000}
  },
  "gpt-5.1-codex-max": {
    "provider": "openai",
    "name": "GPT-5.1 Codex Max",
    "attachment": true,
    "reasoning": true,
    "tool_call": true,
    "temperature": false,
    "limit": {"context": 400000, "input": 272000, "output": 128000}
  },
  "gpt-5.1-codex-mini": {
    "provider": "openai",
    "name": "GPT-5.1 Codex mini",
    "attachment": true,
    "reasoning": true,
    "tool_call": true,
    "temperature": false,
    "limit": {"context": 400000, "input": 272000, "output": 128000}
  },
  "gpt-5.2": {
    "provider": "openai",
    "name": "GPT-5.2",
    "attachment": true,
    "reasoning": true,
    "tool_call": true,
    "temperature": false,
    "limit": {"context": 400000, "input": 272000, "output": 128000}
  },
  "gpt-5.2-codex": {
    "provider": "openai",
    "name": "GPT-5.2 Codex",
    "attachment": true,
    "reasoning": true,
    "tool_call": true,
    "temperature": false,
    "limit": {"context": 400000, "input": 272000, "output": 128000}
  },
  "gpt-5.3-codex": {
    "provider": "openai",
    "name": "GPT-5.3 Codex",
    "attachment": true,
    "reasoning": true,
    "tool_call": true,
    "temperature": false,
    "limit": {"context": 400000, "input": 272000, "output": 128000}
  },
  "gpt-5.4": {
    "provider": "openai",
    "name": "GPT-5.4",
    "attachment": true,
    "reasoning": true,
    "tool_call": true,
    "temperature": false,
    "limit": {"context": 1050000, "input": 922000, "output": 128000}
  }
}
```

## File: `models.go`
```go
package launchdock

import (
	"fmt"
	"log/slog"
	"os"

	authpkg "github.com/nghiahoang/launchdock/internal/auth"
	httpapipkg "github.com/nghiahoang/launchdock/internal/httpapi"
	providerspkg "github.com/nghiahoang/launchdock/internal/providers"
)

type LaunchModel struct {
	ID       string
	Provider string
}

type LaunchConfig struct {
	BaseURL  string
	RawURL   string
	APIKey   string
	Models   []LaunchModel
	HasCreds bool
}

func (c LaunchConfig) ModelIDs() []string {
	var ids []string
	for _, m := range c.Models {
		ids = append(ids, m.ID)
	}
	return ids
}

func (c LaunchConfig) FilterModels(provider string) []LaunchModel {
	if provider == "" {
		return append([]LaunchModel(nil), c.Models...)
	}
	var out []LaunchModel
	for _, m := range c.Models {
		if m.Provider == provider {
			out = append(out, m)
		}
	}
	return out
}

func (c LaunchConfig) HasProvider(provider string) bool {
	return len(c.FilterModels(provider)) > 0
}

func providerDisplayName(provider string) string {
	switch provider {
	case "anthropic":
		return "Anthropic"
	case "openai":
		return "OpenAI"
	default:
		return provider
	}
}

func discoveredProviders(cfg LaunchConfig) []string {
	seen := map[string]bool{}
	var providers []string
	for _, m := range cfg.Models {
		if !seen[m.Provider] {
			seen[m.Provider] = true
			providers = append(providers, providerDisplayName(m.Provider))
		}
	}
	if len(providers) == 0 {
		return []string{"none"}
	}
	return providers
}

func resolveLaunchConfig() LaunchConfig {
	cfg := resolveRuntimeConfig()

	slog.SetDefault(slog.New(slog.NewTextHandler(os.Stderr, &slog.HandlerOptions{
		Level: slog.LevelError,
	})))

	creds := authpkg.LoadAllCredentials()
	cfg.HasCreds = len(creds) > 0
	if !cfg.HasCreds {
		return cfg
	}

	pool := providerspkg.NewPool(creds)
	for _, m := range httpapipkg.FetchAllModels(pool, &providerspkg.AnthropicProvider{}) {
		id, _ := m["id"].(string)
		owner, _ := m["owned_by"].(string)
		if id != "" {
			cfg.Models = append(cfg.Models, LaunchModel{ID: id, Provider: owner})
			if owner == "anthropic" {
				switch id {
				case "claude-opus-4-6", "claude-sonnet-4-6":
					cfg.Models = append(cfg.Models, LaunchModel{ID: id + "-thinking", Provider: owner})
				}
			}
		}
	}
	return cfg
}

func resolveRuntimeConfig() LaunchConfig {
	port := "8090"
	for i, arg := range os.Args {
		if arg == "--port" && i+1 < len(os.Args) {
			port = os.Args[i+1]
		}
	}
	if p := os.Getenv("PORT"); p != "" {
		port = p
	}

	raw := fmt.Sprintf("http://localhost:%s", port)
	return LaunchConfig{
		BaseURL: raw + "/v1",
		RawURL:  raw,
		APIKey:  "launchdock",
	}
}
```

## File: `runtime_cli.go`
```go
package launchdock

import (
	"fmt"
	"os"

	runtimepkg "github.com/nghiahoang/launchdock/internal/runtime"
)

func ensureServerRunning(cfg LaunchConfig) error { return runtimepkg.EnsureServerRunning(cfg.RawURL) }

func handlePSCommand() {
	cfg := resolveRuntimeConfig()
	status, pid := runtimepkg.DaemonStatus(cfg.RawURL)
	fmt.Print("launchdock ps\n\n")
	fmt.Printf("status: %s\n", status)
	if pid > 0 {
		fmt.Printf("pid:    %d\n", pid)
	}
	fmt.Printf("url:    %s\n", cfg.RawURL)
	fmt.Printf("log:    %s\n\n", runtimepkg.DaemonLogPath())
}

func handleStopCommand() {
	if err := runtimepkg.StopServer(); err != nil {
		fmt.Fprintf(os.Stderr, "✗ %v\n", err)
		os.Exit(1)
	}
	fmt.Println("✓ launchdock stopped")
}

func handleRestartCommand() {
	cfg := resolveRuntimeConfig()
	_ = runtimepkg.StopServer()
	if err := runtimepkg.EnsureServerRunning(cfg.RawURL); err != nil {
		fmt.Fprintf(os.Stderr, "✗ %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("✓ launchdock restarted at %s\n", cfg.RawURL)
}

func handleStartCommand() {
	cfg := resolveRuntimeConfig()
	if err := runtimepkg.EnsureServerRunning(cfg.RawURL); err != nil {
		fmt.Fprintf(os.Stderr, "✗ %v\n", err)
		os.Exit(1)
	}
	status, pid := runtimepkg.DaemonStatus(cfg.RawURL)
	if pid > 0 {
		fmt.Printf("✓ launchdock %s at %s (pid %d)\n", status, cfg.RawURL, pid)
		return
	}
	fmt.Printf("✓ launchdock %s at %s\n", status, cfg.RawURL)
}

func handleLogsCommand() {
	path := runtimepkg.DaemonLogPath()
	data, err := os.ReadFile(path)
	if err != nil {
		if os.IsNotExist(err) {
			fmt.Fprintf(os.Stderr, "✗ no log file at %s\n", path)
			os.Exit(1)
		}
		fmt.Fprintf(os.Stderr, "✗ read log failed: %v\n", err)
		os.Exit(1)
	}
	fmt.Print(string(data))
}
```

## File: `tools.go`
```go
package launchdock

import (
	"encoding/json"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
)

type Tool struct {
	Name     string
	Desc     string
	Binary   string
	Provider string
	Config   func(LaunchConfig, string)
	ExecArgs func(LaunchConfig, string) ([]string, []string)
}

var tools = []Tool{
	{Name: "claude-code", Desc: "Claude Code CLI", Binary: "claude", Provider: "anthropic", ExecArgs: execClaudeCode},
	{Name: "codex", Desc: "OpenAI Codex CLI", Binary: "codex", Provider: "openai", Config: configCodex, ExecArgs: execCodex},
	{Name: "opencode", Desc: "OpenCode", Binary: "opencode", Config: configOpenCode, ExecArgs: execOpenCode},
	{Name: "droid", Desc: "Factory Droid CLI", Binary: "droid", Config: configDroid, ExecArgs: execDroid},
	{Name: "pi", Desc: "Pi agent", Binary: "pi", Config: configPi, ExecArgs: execPi},
}

func findTool(name string) *Tool {
	for i := range tools {
		if tools[i].Name == name {
			return &tools[i]
		}
	}
	return nil
}

func isInstalled(binary string) bool {
	_, err := exec.LookPath(binary)
	return err == nil
}

func candidateModelIDs(cfg LaunchConfig, provider string) []string {
	models := cfg.FilterModels(provider)
	if len(models) == 0 {
		models = cfg.Models
	}
	var ids []string
	for _, m := range models {
		ids = append(ids, m.ID)
	}
	return ids
}

func launchTool(t *Tool, cfg LaunchConfig, model string) {
	args, env := t.ExecArgs(cfg, model)
	cmd := exec.Command(args[0], args[1:]...)
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	cmd.Env = append(os.Environ(), env...)

	fmt.Printf("  Launching: %s %s\n\n", t.Binary, strings.Join(args[1:], " "))
	if err := cmd.Run(); err != nil {
		if exitErr, ok := err.(*exec.ExitError); ok {
			os.Exit(exitErr.ExitCode())
		}
		fmt.Fprintf(os.Stderr, "✗ exec failed: %v\n", err)
		os.Exit(1)
	}
	os.Exit(0)
}

func execClaudeCode(cfg LaunchConfig, model string) ([]string, []string) {
	return []string{"claude", "--model", model}, []string{
		"ANTHROPIC_BASE_URL=" + cfg.RawURL,
		"ANTHROPIC_AUTH_TOKEN=" + cfg.APIKey,
	}
}

func configCodex(cfg LaunchConfig, model string) {
	home, _ := os.UserHomeDir()
	dir := filepath.Join(home, ".codex")
	path := filepath.Join(dir, "config.toml")
	existing, _ := os.ReadFile(path)
	cleaned := stripCodexProviderBlock(string(existing), "launchdock")
	cleaned = stripCodexProviderBlock(cleaned, "llm-mux")
	_ = os.MkdirAll(dir, 0755)
	block := fmt.Sprintf("\n[model_providers.launchdock]\nname = \"launchdock\"\nbase_url = \"%s\"\nenv_key = \"LAUNCHDOCK_KEY\"\n", cfg.BaseURL)
	content := strings.TrimRight(cleaned, "\n") + "\n" + block
	if err := os.WriteFile(path, []byte(content), 0644); err != nil {
		fmt.Fprintf(os.Stderr, "  ✗ Write error: %v\n", err)
		return
	}
	fmt.Printf("  ✓ Wrote %s\n", path)
}

func execCodex(cfg LaunchConfig, model string) ([]string, []string) {
	return []string{"codex", "-c", `model_provider="launchdock"`, "--model", model}, []string{"LAUNCHDOCK_KEY=" + cfg.APIKey}
}

func stripCodexProviderBlock(content, provider string) string {
	lines := strings.Split(content, "\n")
	var out []string
	skip := false
	for _, line := range lines {
		trimmed := strings.TrimSpace(line)
		if trimmed == fmt.Sprintf("model_provider = %q", provider) {
			continue
		}
		if trimmed == fmt.Sprintf("[model_providers.%s]", provider) {
			skip = true
			continue
		}
		if skip {
			if strings.HasPrefix(trimmed, "[") && strings.HasSuffix(trimmed, "]") {
				skip = false
			} else {
				continue
			}
		}
		out = append(out, line)
	}
	return strings.Join(out, "\n")
}

func configOpenCode(cfg LaunchConfig, model string) {
	home, _ := os.UserHomeDir()
	dir := filepath.Join(home, ".config", "opencode")
	path := filepath.Join(dir, "opencode.json")
	models := map[string]any{}
	for _, m := range cfg.Models {
		entry := map[string]any{"name": m.ID}
		baseID := strings.TrimSuffix(m.ID, "-thinking")
		if md, ok := lookupLaunchModelMetadata(baseID); ok {
			entry["id"] = m.ID
			entry["name"] = md.Name
			if strings.HasSuffix(m.ID, "-thinking") {
				entry["name"] = md.Name + " Thinking"
			}
			entry["tool_call"] = md.ToolCall
			entry["temperature"] = md.Temperature
			entry["reasoning"] = md.Reasoning
			entry["attachment"] = md.Attachment
			entry["limit"] = md.Limit
		}
		models[m.ID] = entry
	}
	config := map[string]any{}
	if existing, err := os.ReadFile(path); err == nil && len(existing) > 0 {
		if err := json.Unmarshal(existing, &config); err != nil {
			fmt.Fprintf(os.Stderr, "  ✗ Read error: invalid JSON in %s: %v\n", path, err)
			return
		}
	}
	config["$schema"] = "https://opencode.ai/config.json"
	providers, _ := config["provider"].(map[string]any)
	if providers == nil {
		providers = map[string]any{}
	}
	providers["launchdock"] = map[string]any{
		"npm":     "@ai-sdk/openai-compatible",
		"name":    "launchdock",
		"options": map[string]any{"baseURL": cfg.BaseURL},
		"models":  models,
	}
	config["provider"] = providers
	writeJSONConfig(path, dir, config)
}

func execOpenCode(cfg LaunchConfig, model string) ([]string, []string) {
	return []string{"opencode"}, nil
}

func configDroid(cfg LaunchConfig, model string) {
	home, _ := os.UserHomeDir()
	dir := filepath.Join(home, ".factory")
	path := filepath.Join(dir, "config.json")
	var customModels []map[string]any
	for _, m := range cfg.Models {
		customModels = append(customModels, map[string]any{
			"model_display_name": m.ID + " [launchdock]",
			"model":              m.ID,
			"base_url":           cfg.BaseURL + "/",
			"api_key":            cfg.APIKey,
			"provider":           "generic-chat-completion-api",
			"max_tokens":         128000,
		})
	}
	writeJSONConfig(path, dir, map[string]any{"custom_models": customModels})
}

func execDroid(cfg LaunchConfig, model string) ([]string, []string) { return []string{"droid"}, nil }

func configPi(cfg LaunchConfig, model string) {
	home, _ := os.UserHomeDir()
	dir := filepath.Join(home, ".pi", "agent")
	var modelIDs []map[string]any
	for _, m := range cfg.Models {
		modelIDs = append(modelIDs, map[string]any{"id": m.ID})
	}
	writeJSONConfig(filepath.Join(dir, "models.json"), dir, map[string]any{
		"providers": map[string]any{
			"launchdock": map[string]any{
				"baseUrl": cfg.BaseURL,
				"api":     "openai-completions",
				"apiKey":  cfg.APIKey,
				"models":  modelIDs,
			},
		},
	})
	writeJSONConfig(filepath.Join(dir, "settings.json"), dir, map[string]any{
		"defaultProvider": "launchdock",
		"defaultModel":    model,
	})
}

func execPi(cfg LaunchConfig, model string) ([]string, []string) { return []string{"pi"}, nil }

func writeJSONConfig(path, dir string, config any) {
	data, _ := json.MarshalIndent(config, "", "  ")
	_ = os.MkdirAll(dir, 0755)
	if _, err := os.Stat(path); err == nil {
		fmt.Printf("  ⚠ %s exists — overwriting\n", path)
	}
	if err := os.WriteFile(path, data, 0644); err != nil {
		fmt.Fprintf(os.Stderr, "  ✗ Write error: %v\n", err)
		return
	}
	fmt.Printf("  ✓ Wrote %s\n", path)
}
```

## File: `tui_darwin.go`
```go
//go:build darwin

package launchdock

import (
	"fmt"
	"os"
	"strings"
	"syscall"
	"unsafe"
)

type winsize struct {
	Row    uint16
	Col    uint16
	Xpixel uint16
	Ypixel uint16
}

// --- ANSI helpers ---

const (
	ansiReset     = "\033[0m"
	ansiBold      = "\033[1m"
	ansiDim       = "\033[2m"
	ansiCyan      = "\033[36m"
	ansiGreen     = "\033[32m"
	ansiYellow    = "\033[33m"
	ansiClearLine = "\033[2K"
	ansiHideCur   = "\033[?25l"
	ansiShowCur   = "\033[?25h"
)

// --- Raw terminal (no external deps) ---

type termios syscall.Termios

func tcGet(fd int) (*termios, error) {
	var t termios
	_, _, errno := syscall.Syscall6(syscall.SYS_IOCTL, uintptr(fd),
		uintptr(syscall.TIOCGETA), uintptr(unsafe.Pointer(&t)), 0, 0, 0)
	if errno != 0 {
		return nil, errno
	}
	return &t, nil
}

func tcSet(fd int, t *termios) error {
	_, _, errno := syscall.Syscall6(syscall.SYS_IOCTL, uintptr(fd),
		uintptr(syscall.TIOCSETA), uintptr(unsafe.Pointer(t)), 0, 0, 0)
	if errno != 0 {
		return errno
	}
	return nil
}

func makeRaw(fd int) (*termios, error) {
	old, err := tcGet(fd)
	if err != nil {
		return nil, err
	}
	raw := *old
	// cfmakeraw equivalent
	raw.Iflag &^= syscall.IGNBRK | syscall.BRKINT | syscall.PARMRK | syscall.ISTRIP |
		syscall.INLCR | syscall.IGNCR | syscall.ICRNL | syscall.IXON
	raw.Oflag &^= syscall.OPOST
	raw.Lflag &^= syscall.ECHO | syscall.ECHONL | syscall.ICANON | syscall.ISIG | syscall.IEXTEN
	raw.Cflag &^= syscall.CSIZE | syscall.PARENB
	raw.Cflag |= syscall.CS8
	raw.Cc[syscall.VMIN] = 1
	raw.Cc[syscall.VTIME] = 0
	if err := tcSet(fd, &raw); err != nil {
		return nil, err
	}
	return old, nil
}

func restore(fd int, old *termios) {
	tcSet(fd, old)
}

// --- Raw terminal input ---

// readKey reads a single keypress from stdin in raw mode.
// Returns the key byte. isArrow=true when it's an arrow escape sequence.
func readKey(fd int) (byte, bool) {
	buf := make([]byte, 3)
	n, err := os.Stdin.Read(buf)
	if err != nil || n == 0 {
		return 0, false
	}
	// Arrow keys: ESC [ A/B/C/D
	if n == 3 && buf[0] == 0x1b && buf[1] == '[' {
		return buf[2], true // 'A'=up, 'B'=down
	}
	return buf[0], false
}

// --- Checkbox multi-select ---

type checkboxItem struct {
	label    string
	desc     string
	checked  bool
	disabled bool // grayed out if not installed
}

// runCheckbox shows a multi-select checkbox list.
// Returns indices of selected items, or nil if cancelled (Ctrl+C/q).
func runCheckbox(title string, items []checkboxItem) []int {
	fd := int(os.Stdin.Fd())
	oldState, err := makeRaw(fd)
	if err != nil {
		// Fallback: can't do raw mode, return all non-disabled
		var result []int
		for i, item := range items {
			if !item.disabled {
				result = append(result, i)
			}
		}
		return result
	}
	defer restore(fd, oldState)
	defer fmt.Print(ansiShowCur)
	fmt.Print(ansiHideCur)

	cursor := 0
	// Find first non-disabled item
	for cursor < len(items) && items[cursor].disabled {
		cursor++
	}
	if cursor >= len(items) {
		cursor = 0
	}

	render := func() {
		var sb strings.Builder
		sb.WriteString(fmt.Sprintf("\r%s%s%s %s(↑↓ move, space toggle, enter confirm, a all, q quit)%s\r\n",
			ansiBold, title, ansiReset, ansiDim, ansiReset))
		for i, item := range items {
			sb.WriteString("\r")
			// Cursor indicator
			if i == cursor {
				sb.WriteString(fmt.Sprintf("%s❯%s ", ansiCyan, ansiReset))
			} else {
				sb.WriteString("  ")
			}
			// Checkbox
			if item.disabled {
				sb.WriteString(fmt.Sprintf("%s□ %-14s %s%s", ansiDim, item.label, item.desc, ansiReset))
			} else if item.checked {
				sb.WriteString(fmt.Sprintf("%s◉%s %-14s %s", ansiGreen, ansiReset, item.label, item.desc))
			} else {
				sb.WriteString(fmt.Sprintf("○ %-14s %s", item.label, item.desc))
			}
			sb.WriteString("\r\n")
		}
		fmt.Print(sb.String())
	}

	clearRender := func() {
		lines := len(items) + 1 // title + items
		for i := 0; i < lines; i++ {
			fmt.Printf("\033[A" + ansiClearLine)
		}
	}

	render()

	for {
		key, isArrow := readKey(fd)
		if isArrow {
			switch key {
			case 'A': // up
				for {
					cursor--
					if cursor < 0 {
						cursor = len(items) - 1
					}
					if !items[cursor].disabled {
						break
					}
				}
			case 'B': // down
				for {
					cursor++
					if cursor >= len(items) {
						cursor = 0
					}
					if !items[cursor].disabled {
						break
					}
				}
			}
		} else {
			switch key {
			case ' ': // toggle
				if !items[cursor].disabled {
					items[cursor].checked = !items[cursor].checked
				}
			case 'a': // toggle all
				allChecked := true
				for _, item := range items {
					if !item.disabled && !item.checked {
						allChecked = false
						break
					}
				}
				for i := range items {
					if !items[i].disabled {
						items[i].checked = !allChecked
					}
				}
			case 13: // enter
				clearRender()
				var result []int
				for i, item := range items {
					if item.checked {
						result = append(result, i)
					}
				}
				return result
			case 'q', 3: // q or Ctrl+C
				clearRender()
				return nil
			case 'k': // vim up
				for {
					cursor--
					if cursor < 0 {
						cursor = len(items) - 1
					}
					if !items[cursor].disabled {
						break
					}
				}
			case 'j': // vim down
				for {
					cursor++
					if cursor >= len(items) {
						cursor = 0
					}
					if !items[cursor].disabled {
						break
					}
				}
			}
		}
		clearRender()
		render()
	}
}

// --- Single-select picker ---

// runPicker shows a single-select list.
// Returns selected index, or -1 if cancelled.
func runPicker(title string, options []string) int {
	fd := int(os.Stdin.Fd())
	oldState, err := makeRaw(fd)
	if err != nil {
		return 0 // fallback: first option
	}
	defer restore(fd, oldState)
	defer fmt.Print(ansiShowCur)
	fmt.Print(ansiHideCur)

	cursor := 0

	render := func() {
		var sb strings.Builder
		sb.WriteString(fmt.Sprintf("\r%s%s%s %s(↑↓ move, enter select, q quit)%s\r\n",
			ansiBold, title, ansiReset, ansiDim, ansiReset))
		for i, opt := range options {
			sb.WriteString("\r")
			if i == cursor {
				sb.WriteString(fmt.Sprintf("  %s❯ %s%s", ansiCyan, opt, ansiReset))
			} else {
				sb.WriteString(fmt.Sprintf("    %s", opt))
			}
			sb.WriteString("\r\n")
		}
		fmt.Print(sb.String())
	}

	clearRender := func() {
		lines := len(options) + 1
		for i := 0; i < lines; i++ {
			fmt.Printf("\033[A" + ansiClearLine)
		}
	}

	render()

	for {
		key, isArrow := readKey(fd)
		if isArrow {
			switch key {
			case 'A': // up
				cursor--
				if cursor < 0 {
					cursor = len(options) - 1
				}
			case 'B': // down
				cursor++
				if cursor >= len(options) {
					cursor = 0
				}
			}
		} else {
			switch key {
			case 13: // enter
				clearRender()
				return cursor
			case 'q', 3: // q or Ctrl+C
				clearRender()
				return -1
			case 'k':
				cursor--
				if cursor < 0 {
					cursor = len(options) - 1
				}
			case 'j':
				cursor++
				if cursor >= len(options) {
					cursor = 0
				}
			}
		}
		clearRender()
		render()
	}
}

// --- Confirm prompt ---

// runConfirm shows a yes/no prompt. Returns true for yes.
func runConfirm(prompt string) bool {
	fd := int(os.Stdin.Fd())
	oldState, err := makeRaw(fd)
	if err != nil {
		return true // fallback
	}
	defer restore(fd, oldState)

	fmt.Printf("\r%s%s%s %s[Y/n]%s ", ansiBold, prompt, ansiReset, ansiDim, ansiReset)

	for {
		key, isArrow := readKey(fd)
		if isArrow {
			continue
		}
		switch key {
		case 'y', 'Y', 13: // yes or enter
			fmt.Printf("%syes%s\r\n", ansiGreen, ansiReset)
			return true
		case 'n', 'N':
			fmt.Printf("%sno%s\r\n", ansiYellow, ansiReset)
			return false
		case 'q', 3: // q or Ctrl+C
			fmt.Printf("%sno%s\r\n", ansiYellow, ansiReset)
			return false
		}
	}
}

// isTerminal checks if fd is a terminal
func isTerminal(fd int) bool {
	_, err := tcGet(fd)
	return err == nil
}

func getTerminalSize(fd int) (width int, height int, err error) {
	ws := &winsize{}
	_, _, errno := syscall.Syscall6(syscall.SYS_IOCTL, uintptr(fd), uintptr(syscall.TIOCGWINSZ), uintptr(unsafe.Pointer(ws)), 0, 0, 0)
	if errno != 0 {
		return 0, 0, errno
	}
	return int(ws.Col), int(ws.Row), nil
}
```

## File: `tui_linux.go`
```go
//go:build linux

package launchdock

import (
	"fmt"
	"os"
	"strings"
	"syscall"
	"unsafe"
)

type winsize struct {
	Row    uint16
	Col    uint16
	Xpixel uint16
	Ypixel uint16
}

// --- ANSI helpers ---

const (
	ansiReset     = "\033[0m"
	ansiBold      = "\033[1m"
	ansiDim       = "\033[2m"
	ansiCyan      = "\033[36m"
	ansiGreen     = "\033[32m"
	ansiYellow    = "\033[33m"
	ansiClearLine = "\033[2K"
	ansiHideCur   = "\033[?25l"
	ansiShowCur   = "\033[?25h"
)

// --- Raw terminal (no external deps, Linux) ---

type termios syscall.Termios

const (
	ioctlTCGETS     = 0x5401
	ioctlTCSETS     = 0x5402
	ioctlTIOCGWINSZ = 0x5413
)

func tcGet(fd int) (*termios, error) {
	var t termios
	_, _, errno := syscall.Syscall(syscall.SYS_IOCTL, uintptr(fd),
		uintptr(ioctlTCGETS), uintptr(unsafe.Pointer(&t)))
	if errno != 0 {
		return nil, errno
	}
	return &t, nil
}

func tcSet(fd int, t *termios) error {
	_, _, errno := syscall.Syscall(syscall.SYS_IOCTL, uintptr(fd),
		uintptr(ioctlTCSETS), uintptr(unsafe.Pointer(t)))
	if errno != 0 {
		return errno
	}
	return nil
}

func makeRaw(fd int) (*termios, error) {
	old, err := tcGet(fd)
	if err != nil {
		return nil, err
	}
	raw := *old
	raw.Iflag &^= syscall.IGNBRK | syscall.BRKINT | syscall.PARMRK | syscall.ISTRIP |
		syscall.INLCR | syscall.IGNCR | syscall.ICRNL | syscall.IXON
	raw.Oflag &^= syscall.OPOST
	raw.Lflag &^= syscall.ECHO | syscall.ECHONL | syscall.ICANON | syscall.ISIG | syscall.IEXTEN
	raw.Cflag &^= syscall.CSIZE | syscall.PARENB
	raw.Cflag |= syscall.CS8
	raw.Cc[syscall.VMIN] = 1
	raw.Cc[syscall.VTIME] = 0
	if err := tcSet(fd, &raw); err != nil {
		return nil, err
	}
	return old, nil
}

func restore(fd int, old *termios) {
	tcSet(fd, old)
}

// readKey reads a single keypress from stdin in raw mode.
func readKey(fd int) (byte, bool) {
	buf := make([]byte, 3)
	n, err := os.Stdin.Read(buf)
	if err != nil || n == 0 {
		return 0, false
	}
	if n == 3 && buf[0] == 0x1b && buf[1] == '[' {
		return buf[2], true
	}
	return buf[0], false
}

func getTerminalSize(fd int) (width int, height int, err error) {
	ws := &winsize{}
	_, _, errno := syscall.Syscall(syscall.SYS_IOCTL, uintptr(fd), uintptr(ioctlTIOCGWINSZ), uintptr(unsafe.Pointer(ws)))
	if errno != 0 {
		return 0, 0, errno
	}
	return int(ws.Col), int(ws.Row), nil
}

// --- Checkbox multi-select ---

type checkboxItem struct {
	label    string
	desc     string
	checked  bool
	disabled bool
}

func runCheckbox(title string, items []checkboxItem) []int {
	fd := int(os.Stdin.Fd())
	oldState, err := makeRaw(fd)
	if err != nil {
		var result []int
		for i, item := range items {
			if !item.disabled {
				result = append(result, i)
			}
		}
		return result
	}
	defer restore(fd, oldState)
	defer fmt.Print(ansiShowCur)
	fmt.Print(ansiHideCur)

	cursor := 0
	for cursor < len(items) && items[cursor].disabled {
		cursor++
	}
	if cursor >= len(items) {
		cursor = 0
	}

	render := func() {
		var sb strings.Builder
		sb.WriteString(fmt.Sprintf("\r%s%s%s %s(↑↓ move, space toggle, enter confirm, a all, q quit)%s\r\n",
			ansiBold, title, ansiReset, ansiDim, ansiReset))
		for i, item := range items {
			sb.WriteString("\r")
			if i == cursor {
				sb.WriteString(fmt.Sprintf("%s>%s ", ansiCyan, ansiReset))
			} else {
				sb.WriteString("  ")
			}
			if item.disabled {
				sb.WriteString(fmt.Sprintf("%s[ ] %-14s %s%s", ansiDim, item.label, item.desc, ansiReset))
			} else if item.checked {
				sb.WriteString(fmt.Sprintf("%s[x]%s %-14s %s", ansiGreen, ansiReset, item.label, item.desc))
			} else {
				sb.WriteString(fmt.Sprintf("[ ] %-14s %s", item.label, item.desc))
			}
			sb.WriteString("\r\n")
		}
		fmt.Print(sb.String())
	}

	clearRender := func() {
		lines := len(items) + 1
		for i := 0; i < lines; i++ {
			fmt.Printf("\033[A" + ansiClearLine)
		}
	}

	render()

	for {
		key, isArrow := readKey(fd)
		if isArrow {
			switch key {
			case 'A':
				for {
					cursor--
					if cursor < 0 {
						cursor = len(items) - 1
					}
					if !items[cursor].disabled {
						break
					}
				}
			case 'B':
				for {
					cursor++
					if cursor >= len(items) {
						cursor = 0
					}
					if !items[cursor].disabled {
						break
					}
				}
			}
		} else {
			switch key {
			case ' ':
				if !items[cursor].disabled {
					items[cursor].checked = !items[cursor].checked
				}
			case 'a':
				allChecked := true
				for _, item := range items {
					if !item.disabled && !item.checked {
						allChecked = false
						break
					}
				}
				for i := range items {
					if !items[i].disabled {
						items[i].checked = !allChecked
					}
				}
			case 13:
				clearRender()
				var result []int
				for i, item := range items {
					if item.checked {
						result = append(result, i)
					}
				}
				return result
			case 'q', 3:
				clearRender()
				return nil
			case 'k':
				for {
					cursor--
					if cursor < 0 {
						cursor = len(items) - 1
					}
					if !items[cursor].disabled {
						break
					}
				}
			case 'j':
				for {
					cursor++
					if cursor >= len(items) {
						cursor = 0
					}
					if !items[cursor].disabled {
						break
					}
				}
			}
		}
		clearRender()
		render()
	}
}

func runPicker(title string, options []string) int {
	fd := int(os.Stdin.Fd())
	oldState, err := makeRaw(fd)
	if err != nil {
		return 0
	}
	defer restore(fd, oldState)
	defer fmt.Print(ansiShowCur)
	fmt.Print(ansiHideCur)

	cursor := 0

	render := func() {
		var sb strings.Builder
		sb.WriteString(fmt.Sprintf("\r%s%s%s %s(↑↓ move, enter select, q quit)%s\r\n",
			ansiBold, title, ansiReset, ansiDim, ansiReset))
		for i, opt := range options {
			sb.WriteString("\r")
			if i == cursor {
				sb.WriteString(fmt.Sprintf("  %s> %s%s", ansiCyan, opt, ansiReset))
			} else {
				sb.WriteString(fmt.Sprintf("    %s", opt))
			}
			sb.WriteString("\r\n")
		}
		fmt.Print(sb.String())
	}

	clearRender := func() {
		lines := len(options) + 1
		for i := 0; i < lines; i++ {
			fmt.Printf("\033[A" + ansiClearLine)
		}
	}

	render()

	for {
		key, isArrow := readKey(fd)
		if isArrow {
			switch key {
			case 'A':
				cursor--
				if cursor < 0 {
					cursor = len(options) - 1
				}
			case 'B':
				cursor++
				if cursor >= len(options) {
					cursor = 0
				}
			}
		} else {
			switch key {
			case 13:
				clearRender()
				return cursor
			case 'q', 3:
				clearRender()
				return -1
			case 'k':
				cursor--
				if cursor < 0 {
					cursor = len(options) - 1
				}
			case 'j':
				cursor++
				if cursor >= len(options) {
					cursor = 0
				}
			}
		}
		clearRender()
		render()
	}
}

func runConfirm(prompt string) bool {
	fd := int(os.Stdin.Fd())
	oldState, err := makeRaw(fd)
	if err != nil {
		return true
	}
	defer restore(fd, oldState)

	fmt.Printf("\r%s%s%s %s[Y/n]%s ", ansiBold, prompt, ansiReset, ansiDim, ansiReset)

	for {
		key, isArrow := readKey(fd)
		if isArrow {
			continue
		}
		switch key {
		case 'y', 'Y', 13:
			fmt.Printf("%syes%s\r\n", ansiGreen, ansiReset)
			return true
		case 'n', 'N':
			fmt.Printf("%sno%s\r\n", ansiYellow, ansiReset)
			return false
		case 'q', 3:
			fmt.Printf("%sno%s\r\n", ansiYellow, ansiReset)
			return false
		}
	}
}

func isTerminal(fd int) bool {
	_, err := tcGet(fd)
	return err == nil
}
```

## File: `tui_windows.go`
```go
//go:build windows

package launchdock

const (
	ansiReset  = ""
	ansiBold   = ""
	ansiDim    = ""
	ansiCyan   = ""
	ansiGreen  = ""
	ansiYellow = ""
)

type checkboxItem struct {
	label    string
	desc     string
	checked  bool
	disabled bool
}

func isTerminal(fd int) bool {
	return false
}

func runCheckbox(title string, items []checkboxItem) []int {
	var out []int
	for i, item := range items {
		if item.checked && !item.disabled {
			out = append(out, i)
		}
	}
	return out
}

func runPicker(title string, options []string) int {
	if len(options) == 0 {
		return -1
	}
	return 0
}

func runConfirm(prompt string) bool {
	return true
}
```

## File: `cmd/launchdock/main.go`
```go
package main

import "github.com/nghiahoang/launchdock"

func main() {
	launchdock.Run()
}
```

## File: `internal/auth/auth_ui.go`
```go
package auth

import (
	"bytes"
	_ "embed"
	"html/template"
	"net/http"
)

//go:embed web/auth_success.html
var authSuccessHTML string

//go:embed web/auth_error.html
var authErrorHTML string

type authPageData struct {
	Provider string
	Title    string
	Message  string
	Detail   string
}

var (
	authSuccessTemplate = template.Must(template.New("auth_success").Parse(authSuccessHTML))
	authErrorTemplate   = template.Must(template.New("auth_error").Parse(authErrorHTML))
)

func writeAuthSuccess(w http.ResponseWriter, provider, title, message string) {
	writeAuthTemplate(w, http.StatusOK, authSuccessTemplate, authPageData{
		Provider: provider,
		Title:    title,
		Message:  message,
	})
}

func writeAuthError(w http.ResponseWriter, status int, provider, title, message, detail string) {
	writeAuthTemplate(w, status, authErrorTemplate, authPageData{
		Provider: provider,
		Title:    title,
		Message:  message,
		Detail:   detail,
	})
}

func writeAuthTemplate(w http.ResponseWriter, status int, tmpl *template.Template, data authPageData) {
	var buf bytes.Buffer
	if err := tmpl.Execute(&buf, data); err != nil {
		http.Error(w, data.Message, status)
		return
	}
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	w.WriteHeader(status)
	_, _ = w.Write(buf.Bytes())
}
```

## File: `internal/auth/claude_profile.go`
```go
package auth

import (
	"encoding/json"
	"os"
	"path/filepath"
	"sort"
	"strings"
	"time"
)

type ClaudeProfile struct {
	Email            string
	AccountID        string
	OrganizationID   string
	DisplayName      string
	OrganizationName string
	SubscriptionType string
}

func LoadClaudeProfile() ClaudeProfile {
	home, _ := os.UserHomeDir()
	if home == "" {
		return ClaudeProfile{}
	}
	patterns := []string{
		filepath.Join(home, ".claude", "backups", ".claude.json.backup.*"),
		filepath.Join(home, ".claude", "telemetry", "*.json"),
		filepath.Join(home, "Library", "Application Support", "Claude", "local-agent-mode-sessions", "*", "*", "local_*.json"),
		filepath.Join(home, "Library", "Application Support", "Claude", "local-agent-mode-sessions", "*", "*", "local_*", ".claude", ".claude.json"),
	}

	type candidate struct {
		path    string
		modTime time.Time
	}
	var files []candidate
	for _, pattern := range patterns {
		matches, _ := filepath.Glob(pattern)
		for _, match := range matches {
			if info, err := os.Stat(match); err == nil && !info.IsDir() {
				files = append(files, candidate{path: match, modTime: info.ModTime()})
			}
		}
	}
	sort.Slice(files, func(i, j int) bool { return files[i].modTime.After(files[j].modTime) })

	best := ClaudeProfile{}
	for _, file := range files {
		profile := parseClaudeProfileFile(file.path)
		if best.Email == "" && profile.Email != "" {
			best.Email = profile.Email
		}
		if best.AccountID == "" && profile.AccountID != "" {
			best.AccountID = profile.AccountID
		}
		if best.OrganizationID == "" && profile.OrganizationID != "" {
			best.OrganizationID = profile.OrganizationID
		}
		if best.DisplayName == "" && profile.DisplayName != "" {
			best.DisplayName = profile.DisplayName
		}
		if best.OrganizationName == "" && profile.OrganizationName != "" {
			best.OrganizationName = profile.OrganizationName
		}
		if best.SubscriptionType == "" && profile.SubscriptionType != "" {
			best.SubscriptionType = profile.SubscriptionType
		}
		if best.Email != "" && best.AccountID != "" {
			break
		}
	}
	return best
}

func parseClaudeProfileFile(path string) ClaudeProfile {
	data, err := os.ReadFile(path)
	if err != nil {
		return ClaudeProfile{}
	}
	values := map[string]string{}
	var payload any
	if err := json.Unmarshal(data, &payload); err == nil {
		collectProfileStrings(payload, values)
	} else {
		for _, line := range strings.Split(string(data), "\n") {
			line = strings.TrimSpace(line)
			if line == "" {
				continue
			}
			var item any
			if json.Unmarshal([]byte(line), &item) == nil {
				collectProfileStrings(item, values)
			}
		}
	}
	return ClaudeProfile{
		Email:            firstNonEmpty(values["emailaddress"], values["email"]),
		AccountID:        firstNonEmpty(values["account_uuid"], values["accountid"]),
		OrganizationID:   firstNonEmpty(values["organization_uuid"], values["organizationid"]),
		DisplayName:      firstNonEmpty(values["displayname"], values["accountname"]),
		OrganizationName: values["organizationname"],
		SubscriptionType: firstNonEmpty(values["subscriptiontype"], values["billingtype"], values["ratelimittier"]),
	}
}

func collectProfileStrings(v any, out map[string]string) {
	switch x := v.(type) {
	case map[string]any:
		for k, child := range x {
			key := strings.ToLower(k)
			if s, ok := child.(string); ok && s != "" {
				if _, exists := out[key]; !exists {
					out[key] = s
				}
			}
			collectProfileStrings(child, out)
		}
	case []any:
		for _, child := range x {
			collectProfileStrings(child, out)
		}
	}
}

func firstNonEmpty(values ...string) string {
	for _, v := range values {
		if v != "" {
			return v
		}
	}
	return ""
}
```

## File: `internal/auth/credentials.go`
```go
package auth

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io"
	"log/slog"
	"net/http"
	"net/url"
	"os"
	"os/exec"
	"path/filepath"
	"regexp"
	"strconv"
	"strings"
	"time"
)

type AuthType string

const (
	AuthOAuth  AuthType = "oauth"
	AuthAPIKey AuthType = "apikey"
)

type Credential struct {
	ID       string
	Provider string // "anthropic" | "openai"
	AuthType AuthType
	Label    string
	Source   string // "keychain:claude-code" | "file:~/.codex/auth.json" | "config:~/.config/launchdock/config.json"
	Kind     string // e.g. "codex_chatgpt", "openai_oauth"
	Managed  bool

	// OAuth fields
	AccessToken  string
	RefreshToken string
	AccountID    string // chatgpt-account-id for OpenAI OAuth
	Email        string
	ExpiresAt    time.Time

	// API key field
	APIKey string

	// Runtime state
	CooldownUntil time.Time
}

// Token returns the bearer token for this credential.
func (c *Credential) Token() string {
	if c.AuthType == AuthAPIKey {
		return c.APIKey
	}
	return c.AccessToken
}

// IsExpired checks if the credential's access token has expired.
func (c *Credential) IsExpired() bool {
	if c.AuthType == AuthAPIKey {
		return false
	}
	if c.ExpiresAt.IsZero() {
		return false
	}
	return time.Now().After(c.ExpiresAt.Add(-5 * time.Minute)) // 5 min buffer
}

// --- Load from macOS Keychain (Claude OAuth) ---

func LoadFromKeychain() ([]Credential, error) {
	profile := LoadClaudeProfile()
	// Claude Code stores OAuth tokens in macOS Keychain:
	//   "Claude Code-credentials"          — primary account
	//   "Claude Code-credentials-<hex>"    — additional accounts
	services := listClaudeKeychainServices()

	var creds []Credential
	for _, service := range services {
		cred, err := loadKeychainEntry(service, profile)
		if err != nil {
			slog.Debug("keychain entry not found", "service", service, "error", err)
			continue
		}
		creds = append(creds, *cred)
	}

	// Fallback: ~/.claude/.credentials.json
	if len(creds) == 0 {
		home, _ := os.UserHomeDir()
		if home != "" {
			credFile := filepath.Join(home, ".claude", ".credentials.json")
			if data, err := os.ReadFile(credFile); err == nil {
				if cred := parseClaudeCredentialJSON(data, "file:"+credFile, profile); cred != nil {
					creds = append(creds, *cred)
				}
			}
		}
	}

	return creds, nil
}

// listClaudeKeychainServices scans keychain for all Claude Code credential entries.
func listClaudeKeychainServices() []string {
	cmd := exec.Command("security", "dump-keychain")
	out, err := cmd.Output()
	if err != nil {
		return []string{"Claude Code-credentials"}
	}

	re := regexp.MustCompile(`"(Claude Code-credentials(?:-[0-9a-f]+)?)"`)
	matches := re.FindAllStringSubmatch(string(out), -1)

	seen := map[string]bool{}
	var services []string

	// Primary first
	const primary = "Claude Code-credentials"
	for _, m := range matches {
		svc := m[1]
		if !seen[svc] {
			seen[svc] = true
			if svc == primary {
				services = append([]string{primary}, services...)
			} else {
				services = append(services, svc)
			}
		}
	}

	if len(services) == 0 {
		return []string{primary}
	}
	return services
}

func loadKeychainEntry(service string, profile ClaudeProfile) (*Credential, error) {
	cmd := exec.Command("security", "find-generic-password",
		"-s", service,
		"-w", // password only
	)
	out, err := cmd.Output()
	if err != nil {
		return nil, fmt.Errorf("keychain lookup failed for %s: %w", service, err)
	}

	raw := strings.TrimSpace(string(out))

	// Parse the JSON credential — may be nested under "claudeAiOauth"
	var wrapper struct {
		ClaudeAiOauth *struct {
			AccessToken  string      `json:"accessToken"`
			RefreshToken string      `json:"refreshToken"`
			ExpiresAt    json.Number `json:"expiresAt"`
		} `json:"claudeAiOauth"`
		AccessToken  string      `json:"accessToken"`
		RefreshToken string      `json:"refreshToken"`
		ExpiresAt    json.Number `json:"expiresAt"`
	}
	if err := json.Unmarshal([]byte(raw), &wrapper); err != nil {
		return nil, fmt.Errorf("parse keychain JSON: %w", err)
	}

	accessToken := wrapper.AccessToken
	refreshToken := wrapper.RefreshToken
	expiresAtRaw := wrapper.ExpiresAt.String()
	if wrapper.ClaudeAiOauth != nil {
		accessToken = wrapper.ClaudeAiOauth.AccessToken
		refreshToken = wrapper.ClaudeAiOauth.RefreshToken
		expiresAtRaw = wrapper.ClaudeAiOauth.ExpiresAt.String()
	}

	if accessToken == "" {
		return nil, fmt.Errorf("no accessToken in keychain entry %s", service)
	}

	var expiresAt time.Time
	if expiresAtRaw != "" {
		if ms, err := strconv.ParseInt(expiresAtRaw, 10, 64); err == nil {
			expiresAt = time.UnixMilli(ms)
		} else if t, err := time.Parse(time.RFC3339, expiresAtRaw); err == nil {
			expiresAt = t
		}
	}

	return &Credential{
		Provider:     "anthropic",
		AuthType:     AuthOAuth,
		Label:        "Claude Keychain",
		Source:       "keychain:" + service,
		AccessToken:  accessToken,
		RefreshToken: refreshToken,
		AccountID:    profile.AccountID,
		Email:        profile.Email,
		ExpiresAt:    expiresAt,
	}, nil
}

// --- Load from file (Codex OAuth: ~/.codex/auth.json) ---

func LoadFromFile(path string) ([]Credential, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return nil, err
	}

	var auth struct {
		AuthMode string `json:"auth_mode"`
		Tokens   struct {
			IDToken      string `json:"id_token"`
			AccessToken  string `json:"access_token"`
			RefreshToken string `json:"refresh_token"`
			AccountID    string `json:"account_id"`
		} `json:"tokens"`
		LastRefresh string `json:"last_refresh"`
	}
	if err := json.Unmarshal(data, &auth); err != nil {
		return nil, fmt.Errorf("parse %s: %w", path, err)
	}

	if auth.Tokens.AccessToken == "" {
		return nil, fmt.Errorf("no access_token in %s", path)
	}

	// Decode JWT to get expiry
	expiresAt := extractJWTExpiry(auth.Tokens.AccessToken)

	return []Credential{{
		Provider:     "openai",
		AuthType:     AuthOAuth,
		Label:        "Codex OAuth (" + auth.AuthMode + ")",
		Source:       "file:" + path,
		Kind:         "codex_" + auth.AuthMode,
		AccessToken:  auth.Tokens.AccessToken,
		RefreshToken: auth.Tokens.RefreshToken,
		AccountID:    auth.Tokens.AccountID,
		Email:        extractOpenAIEmail(auth.Tokens.IDToken),
		ExpiresAt:    expiresAt,
	}}, nil
}

// --- Refresh ---

const (
	// OpenAI / Codex OAuth
	openAIOAuthEndpoint = "https://auth.openai.com/oauth/token"
	openAIClientID      = "app_EMoamEEZ73f0CkXaXp7hrann"

	// Claude OAuth (from Claude Code binary)
	claudeOAuthEndpoint = "https://platform.claude.com/v1/oauth/token"
	claudeClientID      = "9d1c250a-e61b-44d9-88ed-5944d1962f5e"
	claudeDefaultScopes = "user:profile user:inference user:sessions:claude_code user:mcp_servers user:file_upload"
)

// RefreshClaudeOAuth refreshes a Claude OAuth token using the discovered endpoint.
// Claude uses JSON body (not form-encoded) and requires a scope field.
func RefreshClaudeOAuth(refreshToken string) (accessToken, newRefresh string, expiresAt time.Time, err error) {
	body := map[string]string{
		"grant_type":    "refresh_token",
		"refresh_token": refreshToken,
		"client_id":     claudeClientID,
		"scope":         claudeDefaultScopes,
	}
	bodyBytes, _ := json.Marshal(body)

	req, err := http.NewRequest("POST", claudeOAuthEndpoint, bytes.NewReader(bodyBytes))
	if err != nil {
		return "", "", time.Time{}, fmt.Errorf("build refresh request: %w", err)
	}
	req.Header.Set("Content-Type", "application/json")

	resp, err := APIClient.Do(req)
	if err != nil {
		return "", "", time.Time{}, fmt.Errorf("refresh request: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		respBody, _ := io.ReadAll(resp.Body)
		return "", "", time.Time{}, fmt.Errorf("refresh failed: status %d body=%s", resp.StatusCode, string(respBody))
	}

	var result struct {
		AccessToken  string `json:"access_token"`
		RefreshToken string `json:"refresh_token"`
		ExpiresIn    int    `json:"expires_in"`
		Scope        string `json:"scope"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return "", "", time.Time{}, fmt.Errorf("parse refresh response: %w", err)
	}

	exp := time.Now().Add(time.Duration(result.ExpiresIn) * time.Second)
	nr := result.RefreshToken
	if nr == "" {
		nr = refreshToken
	}
	return result.AccessToken, nr, exp, nil
}

// RefreshOpenAIOAuth refreshes an OpenAI/Codex OAuth token (form-encoded).
func RefreshOpenAIOAuth(refreshToken string) (accessToken, newRefresh string, expiresAt time.Time, err error) {
	resp, err := http.PostForm(openAIOAuthEndpoint, url.Values{
		"grant_type":    {"refresh_token"},
		"refresh_token": {refreshToken},
		"client_id":     {openAIClientID},
	})
	if err != nil {
		return "", "", time.Time{}, fmt.Errorf("refresh request: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		respBody, _ := io.ReadAll(resp.Body)
		return "", "", time.Time{}, fmt.Errorf("refresh failed: status %d body=%s", resp.StatusCode, string(respBody))
	}

	var result struct {
		AccessToken  string `json:"access_token"`
		RefreshToken string `json:"refresh_token"`
		ExpiresIn    int    `json:"expires_in"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return "", "", time.Time{}, fmt.Errorf("parse refresh response: %w", err)
	}

	exp := time.Now().Add(time.Duration(result.ExpiresIn) * time.Second)
	nr := result.RefreshToken
	if nr == "" {
		nr = refreshToken
	}
	return result.AccessToken, nr, exp, nil
}

func RefreshViaCLI(command string) error {
	parts := strings.Fields(command)
	cmd := exec.Command(parts[0], parts[1:]...)
	cmd.Stdout = os.Stderr
	cmd.Stderr = os.Stderr
	return cmd.Run()
}

// --- Helpers ---

// parseClaudeCredentialJSON parses a ~/.claude/.credentials.json file.
func parseClaudeCredentialJSON(data []byte, source string, profile ClaudeProfile) *Credential {
	var wrapper struct {
		ClaudeAiOauth *struct {
			AccessToken  string      `json:"accessToken"`
			RefreshToken string      `json:"refreshToken"`
			ExpiresAt    json.Number `json:"expiresAt"`
		} `json:"claudeAiOauth"`
	}
	if err := json.Unmarshal(data, &wrapper); err != nil || wrapper.ClaudeAiOauth == nil {
		return nil
	}
	oauth := wrapper.ClaudeAiOauth
	if oauth.AccessToken == "" {
		return nil
	}
	var expiresAt time.Time
	if ms, err := strconv.ParseInt(oauth.ExpiresAt.String(), 10, 64); err == nil {
		expiresAt = time.UnixMilli(ms)
	}
	return &Credential{
		Provider:     "anthropic",
		AuthType:     AuthOAuth,
		Label:        "Claude Credentials File",
		Source:       source,
		AccessToken:  oauth.AccessToken,
		RefreshToken: oauth.RefreshToken,
		AccountID:    profile.AccountID,
		Email:        profile.Email,
		ExpiresAt:    expiresAt,
	}
}

func extractJWTExpiry(token string) time.Time {
	parts := strings.Split(token, ".")
	if len(parts) != 3 {
		return time.Time{}
	}
	decoded, err := base64.RawURLEncoding.DecodeString(parts[1])
	if err != nil {
		return time.Time{}
	}
	var claims struct {
		Exp json.Number `json:"exp"`
	}
	if err := json.Unmarshal(decoded, &claims); err != nil {
		return time.Time{}
	}
	sec, err := strconv.ParseInt(claims.Exp.String(), 10, 64)
	if err != nil {
		return time.Time{}
	}
	return time.Unix(sec, 0)
}

// LoadAllCredentials discovers all available credentials from known sources.
func LoadAllCredentials() []Credential {
	var all []Credential

	// 1. Claude OAuth from macOS Keychain
	if creds, err := LoadFromKeychain(); err == nil {
		all = append(all, creds...)
	}

	// 2. Codex OAuth from ~/.codex/auth.json
	home, _ := os.UserHomeDir()
	if home != "" {
		codexAuth := filepath.Join(home, ".codex", "auth.json")
		if creds, err := LoadFromFile(codexAuth); err == nil {
			all = append(all, creds...)
		}
	}

	// 3. Config file credentials (multi-account)
	configCreds := LoadFromConfig()
	all = append(all, configCreds...)

	return all
}
```

## File: `internal/auth/httpclient.go`
```go
package auth

import (
	"net"
	"net/http"
	"time"
)

var APIClient = &http.Client{
	Timeout: 120 * time.Second,
	Transport: &http.Transport{
		Proxy: http.ProxyFromEnvironment,
		DialContext: (&net.Dialer{
			Timeout:   30 * time.Second,
			KeepAlive: 30 * time.Second,
		}).DialContext,
		MaxIdleConns:        100,
		MaxIdleConnsPerHost: 20,
		IdleConnTimeout:     90 * time.Second,
		TLSHandshakeTimeout: 10 * time.Second,
	},
}
```

## File: `internal/auth/oauth.go`
```go
package auth

import (
	"bytes"
	"crypto/rand"
	"crypto/sha256"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io"
	"log/slog"
	"net"
	"net/http"
	"net/url"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
	"strings"
	"time"
)

// OAuthFlow implements the OAuth 2.0 Authorization Code + PKCE flow
// for adding Claude accounts to launchdock.

const (
	claudeAuthorizeURL = "https://claude.ai/oauth/authorize"
	openAIAuthorizeURL = "https://auth.openai.com/oauth/authorize"
	openAIDefaultPort  = 1455
)

// RunOAuthFlow opens a browser for the user to authorize, captures the callback,
// exchanges the code for tokens, and saves the credential.
func RunOAuthFlow(label string) (*Credential, error) {
	// Generate PKCE
	verifier := generateCodeVerifier()
	challenge := generateCodeChallenge(verifier)
	state := generateState()

	// Start local callback server
	listener, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		return nil, fmt.Errorf("start callback server: %w", err)
	}
	port := listener.Addr().(*net.TCPAddr).Port

	redirectURI := fmt.Sprintf("http://localhost:%d/callback", port)
	scopes := claudeDefaultScopes

	// Build authorize URL
	authorizeURL := fmt.Sprintf(
		"%s?code=true&client_id=%s&response_type=code&redirect_uri=%s&scope=%s&code_challenge=%s&code_challenge_method=S256&state=%s",
		claudeAuthorizeURL,
		claudeClientID,
		redirectURI,
		scopes,
		challenge,
		state,
	)

	// Channel to receive the auth code
	codeCh := make(chan string, 1)
	errCh := make(chan error, 1)

	mux := http.NewServeMux()
	mux.HandleFunc("/callback", func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Query().Get("state") != state {
			errCh <- fmt.Errorf("state mismatch")
			writeAuthError(w, http.StatusBadRequest, "Claude", "Sign-in could not be completed", "The callback state did not match this login request.", "state mismatch")
			return
		}
		if errMsg := r.URL.Query().Get("error"); errMsg != "" {
			errCh <- fmt.Errorf("auth error: %s - %s", errMsg, r.URL.Query().Get("error_description"))
			writeAuthError(w, http.StatusUnauthorized, "Claude", "Authentication failed", "Launchdock could not finish connecting your Claude account.", errMsg)
			return
		}
		code := r.URL.Query().Get("code")
		if code == "" {
			errCh <- fmt.Errorf("no code in callback")
			writeAuthError(w, http.StatusBadRequest, "Claude", "Authorization code missing", "Claude did not return an authorization code.", "missing code")
			return
		}
		codeCh <- code
		writeAuthSuccess(w, "Claude", "Connected to Launchdock", "Your Claude account is ready. Return to the terminal to continue.")
	})

	server := &http.Server{Handler: mux}
	go server.Serve(listener)
	defer server.Close()

	// Open browser
	fmt.Fprintf(os.Stderr, "\nOpening browser to authenticate...\n")
	fmt.Fprintf(os.Stderr, "If the browser doesn't open, visit:\n%s\n\n", authorizeURL)
	openBrowser(authorizeURL)

	// Wait for callback
	var code string
	select {
	case code = <-codeCh:
	case err := <-errCh:
		return nil, err
	case <-time.After(5 * time.Minute):
		return nil, fmt.Errorf("authentication timed out after 5 minutes")
	}

	slog.Info("received auth code, exchanging for tokens...")

	// Exchange code for tokens
	cred, err := exchangeCodeForTokens(code, verifier, state, redirectURI, label)
	if err != nil {
		return nil, fmt.Errorf("token exchange: %w", err)
	}

	// Save to config
	if err := SaveCredentialToConfig(cred); err != nil {
		slog.Warn("failed to save credential to config", "error", err)
	}

	return cred, nil
}

func RunOpenAIOAuthFlow(label string) (*Credential, error) {
	verifier := generateCodeVerifier()
	challenge := generateCodeChallenge(verifier)
	state := generateState()

	listener, err := net.Listen("tcp", fmt.Sprintf("127.0.0.1:%d", openAIDefaultPort))
	if err != nil {
		listener, err = net.Listen("tcp", "127.0.0.1:0")
		if err != nil {
			return nil, fmt.Errorf("start callback server: %w", err)
		}
	}
	port := listener.Addr().(*net.TCPAddr).Port
	redirectURI := fmt.Sprintf("http://localhost:%d/auth/callback", port)

	authorizeURL := fmt.Sprintf(
		"%s?response_type=code&client_id=%s&redirect_uri=%s&scope=%s&code_challenge=%s&code_challenge_method=S256&id_token_add_organizations=true&codex_cli_simplified_flow=true&state=%s",
		openAIAuthorizeURL,
		openAIClientID,
		redirectURI,
		"openid+profile+email+offline_access",
		challenge,
		state,
	)

	codeCh := make(chan string, 1)
	errCh := make(chan error, 1)
	mux := http.NewServeMux()
	mux.HandleFunc("/auth/callback", func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Query().Get("state") != state {
			errCh <- fmt.Errorf("state mismatch")
			writeAuthError(w, http.StatusBadRequest, "OpenAI", "Sign-in could not be completed", "The callback state did not match this login request.", "state mismatch")
			return
		}
		if errMsg := r.URL.Query().Get("error"); errMsg != "" {
			errCh <- fmt.Errorf("auth error: %s - %s", errMsg, r.URL.Query().Get("error_description"))
			writeAuthError(w, http.StatusUnauthorized, "OpenAI", "Authentication failed", "Launchdock could not finish connecting your OpenAI account.", errMsg)
			return
		}
		code := r.URL.Query().Get("code")
		if code == "" {
			errCh <- fmt.Errorf("no code in callback")
			writeAuthError(w, http.StatusBadRequest, "OpenAI", "Authorization code missing", "OpenAI did not return an authorization code.", "missing code")
			return
		}
		codeCh <- code
		http.Redirect(w, r, "/success", http.StatusFound)
	})
	mux.HandleFunc("/success", func(w http.ResponseWriter, r *http.Request) {
		writeAuthSuccess(w, "OpenAI", "Connected to Launchdock", "Your OpenAI account is ready. Return to the terminal to continue.")
	})

	server := &http.Server{Handler: mux}
	go server.Serve(listener)
	defer server.Close()

	fmt.Fprintf(os.Stderr, "\nOpening browser to authenticate with OpenAI...\n")
	fmt.Fprintf(os.Stderr, "If the browser doesn't open, visit:\n%s\n\n", authorizeURL)
	openBrowser(authorizeURL)

	var code string
	select {
	case code = <-codeCh:
	case err := <-errCh:
		return nil, err
	case <-time.After(5 * time.Minute):
		return nil, fmt.Errorf("authentication timed out after 5 minutes")
	}

	cred, err := exchangeOpenAICodeForTokens(code, verifier, redirectURI, label)
	if err != nil {
		return nil, fmt.Errorf("token exchange: %w", err)
	}
	if err := SaveCredentialToConfig(cred); err != nil {
		slog.Warn("failed to save credential to config", "error", err)
	}
	return cred, nil
}

func exchangeCodeForTokens(code, verifier, state, redirectURI, label string) (*Credential, error) {
	body := map[string]string{
		"grant_type":    "authorization_code",
		"code":          code,
		"redirect_uri":  redirectURI,
		"client_id":     claudeClientID,
		"code_verifier": verifier,
		"state":         state,
	}
	bodyBytes, _ := json.Marshal(body)

	req, err := http.NewRequest("POST", claudeOAuthEndpoint, bytes.NewReader(bodyBytes))
	if err != nil {
		return nil, err
	}
	req.Header.Set("Content-Type", "application/json")

	resp, err := APIClient.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		respBody, _ := io.ReadAll(resp.Body)
		return nil, fmt.Errorf("status %d: %s", resp.StatusCode, string(respBody))
	}

	var result struct {
		AccessToken  string `json:"access_token"`
		RefreshToken string `json:"refresh_token"`
		ExpiresIn    int    `json:"expires_in"`
		Scope        string `json:"scope"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return nil, fmt.Errorf("parse response: %w", err)
	}

	return &Credential{
		Provider:     "anthropic",
		AuthType:     AuthOAuth,
		Label:        label,
		Source:       "oauth:launchdock",
		AccessToken:  result.AccessToken,
		RefreshToken: result.RefreshToken,
		ExpiresAt:    time.Now().Add(time.Duration(result.ExpiresIn) * time.Second),
	}, nil
}

func exchangeOpenAICodeForTokens(code, verifier, redirectURI, label string) (*Credential, error) {
	body := fmt.Sprintf(
		"grant_type=authorization_code&code=%s&redirect_uri=%s&client_id=%s&code_verifier=%s",
		url.QueryEscape(code),
		url.QueryEscape(redirectURI),
		url.QueryEscape(openAIClientID),
		url.QueryEscape(verifier),
	)
	req, err := http.NewRequest("POST", openAIOAuthEndpoint, bytes.NewBufferString(body))
	if err != nil {
		return nil, err
	}
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")

	resp, err := APIClient.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()
	if resp.StatusCode != 200 {
		respBody, _ := io.ReadAll(resp.Body)
		return nil, fmt.Errorf("status %d: %s", resp.StatusCode, string(respBody))
	}

	var result struct {
		IDToken      string `json:"id_token"`
		AccessToken  string `json:"access_token"`
		RefreshToken string `json:"refresh_token"`
		ExpiresIn    int    `json:"expires_in"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return nil, fmt.Errorf("parse response: %w", err)
	}
	accountID := extractOpenAIAccountID(result.IDToken)
	email := extractOpenAIEmail(result.IDToken)
	return &Credential{
		Provider:     "openai",
		AuthType:     AuthOAuth,
		Label:        label,
		Source:       "oauth:launchdock",
		Kind:         "codex_chatgpt",
		AccessToken:  result.AccessToken,
		RefreshToken: result.RefreshToken,
		AccountID:    accountID,
		Email:        email,
		ExpiresAt:    time.Now().Add(time.Duration(result.ExpiresIn) * time.Second),
	}, nil
}

// --- Config file for multi-account persistence ---

type Config struct {
	Credentials  []ConfigCredential `json:"credentials"`
	AutoDiscover bool               `json:"auto_discover"`
}

type ConfigCredential struct {
	ID           string `json:"id,omitempty"`
	Label        string `json:"label"`
	Provider     string `json:"provider"`
	Kind         string `json:"kind,omitempty"`
	AccessToken  string `json:"access_token,omitempty"`
	ExpiresAt    string `json:"expires_at,omitempty"`
	RefreshToken string `json:"refresh_token,omitempty"`
	APIKey       string `json:"api_key,omitempty"`
	AccountID    string `json:"account_id,omitempty"`
	Email        string `json:"email,omitempty"`
	Disabled     bool   `json:"disabled,omitempty"`
}

func ConfigPath() string {
	home, _ := os.UserHomeDir()
	return filepath.Join(home, ".config", "launchdock", "config.json")
}

func LoadConfig() *Config {
	data, err := os.ReadFile(ConfigPath())
	if err != nil {
		return &Config{AutoDiscover: true}
	}
	var cfg Config
	if err := json.Unmarshal(data, &cfg); err != nil {
		return &Config{AutoDiscover: true}
	}
	for i := range cfg.Credentials {
		if cfg.Credentials[i].ID == "" {
			cfg.Credentials[i].ID = GenerateCredentialID()
		}
	}
	return &cfg
}

func SaveConfig(cfg *Config) error {
	dir := filepath.Dir(ConfigPath())
	if err := os.MkdirAll(dir, 0700); err != nil {
		return err
	}
	data, err := json.MarshalIndent(cfg, "", "  ")
	if err != nil {
		return err
	}
	return os.WriteFile(ConfigPath(), data, 0600)
}

func SaveCredentialToConfig(cred *Credential) error {
	cfg := LoadConfig()
	provider := normalizeProvider(cred.Provider)
	match := -1
	for i := range cfg.Credentials {
		cc := cfg.Credentials[i]
		if normalizeProvider(cc.Provider) != provider {
			continue
		}
		if cred.AccountID != "" && cc.AccountID != "" && cc.AccountID == cred.AccountID {
			match = i
			break
		}
		if match == -1 && cred.Email != "" && cc.Email != "" && strings.EqualFold(cc.Email, cred.Email) {
			match = i
		}
	}
	if match >= 0 {
		cfg.Credentials[match].Label = cred.Label
		cfg.Credentials[match].Provider = provider
		cfg.Credentials[match].Kind = cred.Kind
		cfg.Credentials[match].AccessToken = cred.AccessToken
		if !cred.ExpiresAt.IsZero() {
			cfg.Credentials[match].ExpiresAt = cred.ExpiresAt.Format(time.RFC3339)
		}
		cfg.Credentials[match].RefreshToken = cred.RefreshToken
		cfg.Credentials[match].APIKey = cred.APIKey
		cfg.Credentials[match].AccountID = cred.AccountID
		cfg.Credentials[match].Email = cred.Email
		cfg.Credentials[match].Disabled = false
		if cfg.Credentials[match].ID == "" {
			cfg.Credentials[match].ID = GenerateCredentialID()
		}
	} else {
		cfg.Credentials = append(cfg.Credentials, ConfigCredential{
			ID:           GenerateCredentialID(),
			Label:        cred.Label,
			Provider:     provider,
			Kind:         cred.Kind,
			AccessToken:  cred.AccessToken,
			ExpiresAt:    FormatExpiresAt(cred.ExpiresAt),
			RefreshToken: cred.RefreshToken,
			APIKey:       cred.APIKey,
			AccountID:    cred.AccountID,
			Email:        cred.Email,
		})
	}
	return SaveConfig(cfg)
}

func SaveAPIKeyToConfig(provider, label, apiKey string) error {
	provider = normalizeProvider(provider)
	if strings.TrimSpace(apiKey) == "" {
		return fmt.Errorf("api key is empty")
	}
	if label == "" {
		label = strings.ToUpper(provider) + " API key"
	}
	cfg := LoadConfig()
	cfg.Credentials = append(cfg.Credentials, ConfigCredential{
		ID:       GenerateCredentialID(),
		Label:    label,
		Provider: provider,
		APIKey:   apiKey,
	})
	return SaveConfig(cfg)
}

func GenerateCredentialID() string {
	return "cred_" + generateState()
}

func RemoveConfigCredential(id string) error {
	cfg := LoadConfig()
	var filtered []ConfigCredential
	removed := false
	for _, cc := range cfg.Credentials {
		if cc.ID == id {
			removed = true
			continue
		}
		filtered = append(filtered, cc)
	}
	if !removed {
		return fmt.Errorf("credential not found")
	}
	cfg.Credentials = filtered
	return SaveConfig(cfg)
}

func ToggleConfigCredentialDisabled(id string) error {
	cfg := LoadConfig()
	for i := range cfg.Credentials {
		if cfg.Credentials[i].ID == id {
			cfg.Credentials[i].Disabled = !cfg.Credentials[i].Disabled
			return SaveConfig(cfg)
		}
	}
	return fmt.Errorf("credential not found")
}

func SetConfigCredentialDisabled(id string, disabled bool) error {
	cfg := LoadConfig()
	for i := range cfg.Credentials {
		if cfg.Credentials[i].ID == id {
			cfg.Credentials[i].Disabled = disabled
			return SaveConfig(cfg)
		}
	}
	return fmt.Errorf("credential not found")
}

func PersistManagedCredentialState(id, refreshToken, accountID, email string) error {
	cfg := LoadConfig()
	for i := range cfg.Credentials {
		if cfg.Credentials[i].ID != id {
			continue
		}
		if refreshToken != "" {
			cfg.Credentials[i].RefreshToken = refreshToken
		}
		if accountID != "" {
			cfg.Credentials[i].AccountID = accountID
		}
		if email != "" {
			cfg.Credentials[i].Email = email
		}
		return SaveConfig(cfg)
	}
	return fmt.Errorf("managed credential not found")
}

// LoadFromConfig loads credentials from ~/.config/launchdock/config.json
func LoadFromConfig() []Credential {
	cfg := LoadConfig()
	var creds []Credential
	for _, cc := range cfg.Credentials {
		if cc.Disabled {
			continue
		}
		provider := normalizeProvider(cc.Provider)
		if cc.APIKey != "" {
			if provider == "anthropic" {
				continue
			}
			creds = append(creds, Credential{
				ID:       cc.ID,
				Provider: provider,
				AuthType: AuthAPIKey,
				Label:    cc.Label,
				Source:   "config:" + ConfigPath(),
				Kind:     cc.Kind,
				Managed:  true,
				Email:    cc.Email,
				APIKey:   cc.APIKey,
			})
		} else if cc.RefreshToken != "" {
			if cc.AccessToken != "" {
				exp := parseConfigExpiresAt(cc.ExpiresAt)
				cred := Credential{
					ID:           cc.ID,
					Provider:     provider,
					AuthType:     AuthOAuth,
					Label:        cc.Label,
					Source:       "config:" + ConfigPath(),
					Kind:         cc.Kind,
					Managed:      true,
					AccessToken:  cc.AccessToken,
					RefreshToken: cc.RefreshToken,
					AccountID:    cc.AccountID,
					Email:        cc.Email,
					ExpiresAt:    exp,
				}
				if !cred.IsExpired() {
					creds = append(creds, cred)
					continue
				}
				// Token is expired or near expiry; fall through to refresh path.
			}
			// Refresh only when needed.
			var at, rt string
			var exp time.Time
			var err error

			if provider == "anthropic" {
				at, rt, exp, err = RefreshClaudeOAuth(cc.RefreshToken)
			} else if provider == "openai" {
				at, rt, exp, err = RefreshOpenAIOAuth(cc.RefreshToken)
			}

			if err != nil {
				slog.Warn("config credential refresh failed", "label", cc.Label, "error", err)
				if provider == "openai" && cc.ID != "" && IsTerminalOpenAIRefreshError(err) {
					if derr := SetConfigCredentialDisabled(cc.ID, true); derr != nil {
						slog.Warn("disable stale OpenAI credential failed", "label", cc.Label, "id", cc.ID, "error", derr)
					} else {
						slog.Warn("disabled stale OpenAI credential", "label", cc.Label, "id", cc.ID)
					}
					continue
				}
				// Store with refresh token anyway — will retry later
				creds = append(creds, Credential{
					ID:           cc.ID,
					Provider:     provider,
					AuthType:     AuthOAuth,
					Label:        cc.Label,
					Source:       "config:" + ConfigPath(),
					Kind:         cc.Kind,
					Managed:      true,
					RefreshToken: cc.RefreshToken,
					AccountID:    cc.AccountID,
					Email:        cc.Email,
				})
			} else {
				creds = append(creds, Credential{
					ID:           cc.ID,
					Provider:     provider,
					AuthType:     AuthOAuth,
					Label:        cc.Label,
					Source:       "config:" + ConfigPath(),
					Kind:         cc.Kind,
					Managed:      true,
					AccessToken:  at,
					RefreshToken: rt,
					AccountID:    cc.AccountID,
					Email:        cc.Email,
					ExpiresAt:    exp,
				})
			}
		}
	}
	return creds
}

func normalizeProvider(provider string) string {
	switch strings.ToLower(strings.TrimSpace(provider)) {
	case "claude", "anthropic":
		return "anthropic"
	case "codex", "openai":
		return "openai"
	default:
		return strings.ToLower(strings.TrimSpace(provider))
	}
}

func IsTerminalOpenAIRefreshError(err error) bool {
	msg := strings.ToLower(err.Error())
	return strings.Contains(msg, "refresh_token_reused") ||
		strings.Contains(msg, "already been used to generate a new access token")
}

func parseConfigExpiresAt(v string) time.Time {
	if v == "" {
		return time.Time{}
	}
	t, err := time.Parse(time.RFC3339, v)
	if err != nil {
		return time.Time{}
	}
	return t
}

func FormatExpiresAt(t time.Time) string {
	if t.IsZero() {
		return ""
	}
	return t.Format(time.RFC3339)
}

// --- PKCE helpers ---

func generateCodeVerifier() string {
	b := make([]byte, 32)
	rand.Read(b)
	return base64.RawURLEncoding.EncodeToString(b)
}

func generateCodeChallenge(verifier string) string {
	h := sha256.Sum256([]byte(verifier))
	return base64.RawURLEncoding.EncodeToString(h[:])
}

func generateState() string {
	b := make([]byte, 16)
	rand.Read(b)
	return base64.RawURLEncoding.EncodeToString(b)
}

func openBrowser(url string) {
	var cmd *exec.Cmd
	switch runtime.GOOS {
	case "darwin":
		cmd = exec.Command("open", url)
	case "linux":
		cmd = exec.Command("xdg-open", url)
	default:
		cmd = exec.Command("open", url)
	}
	cmd.Start()
}

func extractOpenAIAccountID(idToken string) string {
	parts := strings.Split(idToken, ".")
	if len(parts) != 3 {
		return ""
	}
	decoded, err := base64.RawURLEncoding.DecodeString(parts[1])
	if err != nil {
		return ""
	}
	var claims struct {
		Auth map[string]any `json:"https://api.openai.com/auth"`
	}
	if err := json.Unmarshal(decoded, &claims); err != nil {
		return ""
	}
	if v, ok := claims.Auth["chatgpt_account_id"].(string); ok {
		return v
	}
	if v, ok := claims.Auth["account_id"].(string); ok {
		return v
	}
	return ""
}

func extractOpenAIEmail(idToken string) string {
	parts := strings.Split(idToken, ".")
	if len(parts) != 3 {
		return ""
	}
	decoded, err := base64.RawURLEncoding.DecodeString(parts[1])
	if err != nil {
		return ""
	}
	var claims struct {
		Email string `json:"email"`
	}
	if err := json.Unmarshal(decoded, &claims); err != nil {
		return ""
	}
	return claims.Email
}
```

## File: `internal/auth/web/auth_error.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{{.Title}}</title>
    <style>
      :root {
        --bg: #faf6f3;
        --panel: rgba(255, 255, 255, 0.9);
        --text: #241814;
        --muted: rgba(36, 24, 20, 0.72);
        --border: rgba(103, 48, 29, 0.16);
        --accent: #b4512d;
      }
      * { box-sizing: border-box; }
      body {
        margin: 0;
        min-height: 100vh;
        background:
          radial-gradient(circle at top right, rgba(180, 81, 45, 0.12), transparent 28%),
          radial-gradient(circle at bottom left, rgba(210, 124, 79, 0.15), transparent 24%),
          var(--bg);
        color: var(--text);
        font-family: Iowan Old Style, Charter, Georgia, serif;
      }
      .wrap {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 24px;
      }
      .card {
        width: min(620px, 100%);
        padding: 36px 32px;
        border: 1px solid var(--border);
        border-radius: 24px;
        background: var(--panel);
        box-shadow: 0 18px 60px rgba(46, 26, 20, 0.08);
      }
      .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 8px 14px;
        border-radius: 999px;
        border: 1px solid var(--border);
        color: var(--muted);
        font: 600 12px/1.2 ui-monospace, SFMono-Regular, Menlo, monospace;
        letter-spacing: 0.08em;
        text-transform: uppercase;
      }
      .dot {
        width: 9px;
        height: 9px;
        border-radius: 50%;
        background: var(--accent);
        box-shadow: 0 0 0 6px rgba(180, 81, 45, 0.12);
      }
      h1 {
        margin: 24px 0 10px;
        font-size: clamp(32px, 5vw, 46px);
        line-height: 1.08;
        font-weight: 500;
      }
      p {
        margin: 0 0 18px;
        color: var(--muted);
        font: 400 18px/1.6 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }
      .detail {
        padding: 14px 16px;
        border-radius: 14px;
        border: 1px solid var(--border);
        background: rgba(255, 255, 255, 0.8);
        color: var(--text);
        font: 500 14px/1.5 ui-monospace, SFMono-Regular, Menlo, monospace;
        overflow-wrap: anywhere;
      }
    </style>
  </head>
  <body>
    <div class="wrap">
      <div class="card">
        <div class="eyebrow"><span class="dot"></span>{{.Provider}}</div>
        <h1>{{.Title}}</h1>
        <p>{{.Message}}</p>
        {{if .Detail}}<div class="detail">{{.Detail}}</div>{{end}}
      </div>
    </div>
  </body>
</html>
```

## File: `internal/auth/web/auth_success.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{{.Title}}</title>
    <style>
      :root {
        --bg: #f5f7f4;
        --panel: rgba(255, 255, 255, 0.84);
        --text: #182019;
        --muted: rgba(24, 32, 25, 0.68);
        --border: rgba(24, 32, 25, 0.1);
        --accent: #1f6b4f;
      }
      * { box-sizing: border-box; }
      body {
        margin: 0;
        min-height: 100vh;
        background:
          radial-gradient(circle at top left, rgba(31, 107, 79, 0.12), transparent 28%),
          radial-gradient(circle at bottom right, rgba(86, 156, 116, 0.16), transparent 24%),
          var(--bg);
        color: var(--text);
        font-family: Iowan Old Style, Charter, Georgia, serif;
      }
      .wrap {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 24px;
      }
      .card {
        width: min(620px, 100%);
        padding: 36px 32px;
        border: 1px solid var(--border);
        border-radius: 24px;
        background: var(--panel);
        backdrop-filter: blur(10px);
        box-shadow: 0 18px 60px rgba(17, 24, 20, 0.08);
        text-align: center;
      }
      .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 8px 14px;
        border-radius: 999px;
        border: 1px solid var(--border);
        color: var(--muted);
        font: 600 12px/1.2 ui-monospace, SFMono-Regular, Menlo, monospace;
        letter-spacing: 0.08em;
        text-transform: uppercase;
      }
      .dot {
        width: 9px;
        height: 9px;
        border-radius: 50%;
        background: var(--accent);
        box-shadow: 0 0 0 6px rgba(31, 107, 79, 0.12);
      }
      h1 {
        margin: 24px 0 10px;
        font-size: clamp(34px, 6vw, 52px);
        line-height: 1.05;
        font-weight: 500;
      }
      p {
        margin: 0 auto;
        max-width: 460px;
        color: var(--muted);
        font: 400 18px/1.6 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }
    </style>
  </head>
  <body>
    <div class="wrap">
      <div class="card">
        <div class="eyebrow"><span class="dot"></span>{{.Provider}}</div>
        <h1>{{.Title}}</h1>
        <p>{{.Message}}</p>
      </div>
    </div>
  </body>
</html>
```

## File: `internal/httpapi/auth_retry.go`
```go
package httpapi

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"log/slog"
	"net/http"
	"strings"
	"time"

	authpkg "github.com/nghiahoang/launchdock/internal/auth"
	providerspkg "github.com/nghiahoang/launchdock/internal/providers"
)

func isAuthFailure(provider string, statusCode int, body []byte) bool {
	if statusCode != http.StatusUnauthorized && statusCode != http.StatusForbidden {
		return false
	}
	msg := strings.ToLower(authFailureMessage(provider, body))
	switch provider {
	case "anthropic":
		return strings.Contains(msg, "authentication") ||
			strings.Contains(msg, "api key") ||
			strings.Contains(msg, "oauth") ||
			strings.Contains(msg, "token") ||
			strings.Contains(msg, "unauthorized") ||
			strings.Contains(msg, "forbidden") ||
			strings.Contains(msg, "expired") ||
			strings.Contains(msg, "invalid")
	case "openai":
		return strings.Contains(msg, "auth") ||
			strings.Contains(msg, "token") ||
			strings.Contains(msg, "unauthorized") ||
			strings.Contains(msg, "forbidden") ||
			strings.Contains(msg, "expired") ||
			strings.Contains(msg, "invalid")
	default:
		return statusCode == http.StatusUnauthorized || statusCode == http.StatusForbidden
	}
}

func authFailureMessage(provider string, body []byte) string {
	switch provider {
	case "openai":
		var payload struct {
			Error struct {
				Message string `json:"message"`
				Code    string `json:"code"`
				Type    string `json:"type"`
			} `json:"error"`
			Detail struct {
				Code    string `json:"code"`
				Message string `json:"message"`
			} `json:"detail"`
		}
		if json.Unmarshal(body, &payload) == nil {
			return strings.TrimSpace(payload.Error.Message + " " + payload.Error.Code + " " + payload.Error.Type + " " + payload.Detail.Code + " " + payload.Detail.Message)
		}
	case "anthropic":
		var payload struct {
			Error struct {
				Message string `json:"message"`
				Type    string `json:"type"`
			} `json:"error"`
		}
		if json.Unmarshal(body, &payload) == nil {
			return strings.TrimSpace(payload.Error.Message + " " + payload.Error.Type)
		}
	}
	return string(body)
}

func doWithCredentialRetry(pool *providerspkg.Pool, providerName string, cred *authpkg.Credential, attempt func(*authpkg.Credential) (*http.Response, error)) (*http.Response, *authpkg.Credential, error) {
	return doWithCredentialRetryMatching(pool, providerName, cred, func(*authpkg.Credential) bool { return true }, attempt)
}

type retryState struct {
	refreshedSame bool
	fallbackTried bool
}

func doWithCredentialRetryMatching(pool *providerspkg.Pool, providerName string, cred *authpkg.Credential, match func(*authpkg.Credential) bool, attempt func(*authpkg.Credential) (*http.Response, error)) (*http.Response, *authpkg.Credential, error) {
	state := retryState{}

	for {
		resp, err := attempt(cred)
		if err != nil {
			return nil, cred, err
		}
		if resp.StatusCode == http.StatusOK {
			return resp, cred, nil
		}

		errBody, _ := io.ReadAll(resp.Body)
		resp.Body.Close()

		if isAuthFailure(providerName, resp.StatusCode, errBody) {
			if !state.refreshedSame && cred.AuthType == authpkg.AuthOAuth && cred.RefreshToken != "" {
				state.refreshedSame = true
				if err := pool.RefreshCredential(cred); err == nil {
					slog.Warn("auth failure recovered by refresh", "provider", providerName, "credential", cred.Label)
					continue
				}
			}
			nextCred, ok := pickFallbackCredential(pool, providerName, cred, match, &state, 45*time.Second, "auth failure")
			if ok {
				cred = nextCred
				continue
			}
			return rebuildErrorResponse(resp, errBody), cred, nil
		}

		if isRetryable(resp.StatusCode) {
			slog.Warn("retryable upstream error, trying next credential", "status", resp.StatusCode, "credential", cred.Label, "body", string(errBody))
			cooldown := 0 * time.Second
			switch resp.StatusCode {
			case 429:
				cooldown = 60 * time.Second
			case 529, 503:
				cooldown = 30 * time.Second
			}
			nextCred, ok := pickFallbackCredential(pool, providerName, cred, match, &state, cooldown, "retryable upstream error")
			if ok {
				cred = nextCred
				continue
			}
		}

		return rebuildErrorResponse(resp, errBody), cred, nil
	}
}

func pickFallbackCredential(pool *providerspkg.Pool, providerName string, cred *authpkg.Credential, match func(*authpkg.Credential) bool, state *retryState, cooldown time.Duration, reason string) (*authpkg.Credential, bool) {
	if state.fallbackTried {
		return nil, false
	}
	state.fallbackTried = true
	if cooldown > 0 {
		pool.Cooldown(cred, cooldown)
	}
	nextCred, err := pool.PickNextMatching(providerName, cred, match)
	if err != nil {
		return nil, false
	}
	slog.Warn("retrying with fallback credential", "provider", providerName, "reason", reason, "credential", cred.Label, "fallback", nextCred.Label)
	return nextCred, true
}

func ensureOKOrRetryMatching(pool *providerspkg.Pool, providerName string, cred *authpkg.Credential, match func(*authpkg.Credential) bool, attempt func(*authpkg.Credential) (*http.Response, error)) (*http.Response, *authpkg.Credential, error) {
	resp, nextCred, err := doWithCredentialRetryMatching(pool, providerName, cred, match, attempt)
	if err != nil {
		return nil, nextCred, err
	}
	if resp.StatusCode == http.StatusOK {
		return resp, nextCred, nil
	}
	body, _ := io.ReadAll(resp.Body)
	resp.Body.Close()
	return nil, nextCred, fmt.Errorf("upstream status %d: %s", resp.StatusCode, strings.TrimSpace(string(body)))
}

func rebuildErrorResponse(resp *http.Response, body []byte) *http.Response {
	return &http.Response{
		StatusCode: resp.StatusCode,
		Status:     resp.Status,
		Header:     resp.Header.Clone(),
		Body:       io.NopCloser(bytes.NewReader(body)),
	}
}

func ensureOKOrRetry(pool *providerspkg.Pool, providerName string, cred *authpkg.Credential, attempt func(*authpkg.Credential) (*http.Response, error)) (*http.Response, *authpkg.Credential, error) {
	resp, nextCred, err := doWithCredentialRetry(pool, providerName, cred, attempt)
	if err != nil {
		return nil, nextCred, err
	}
	if resp.StatusCode == http.StatusOK {
		return resp, nextCred, nil
	}
	body, _ := io.ReadAll(resp.Body)
	resp.Body.Close()
	return nil, nextCred, fmt.Errorf("upstream status %d: %s", resp.StatusCode, strings.TrimSpace(string(body)))
}
```

## File: `internal/httpapi/deps.go`
```go
package httpapi

import (
	"io"
	"net/http"

	authpkg "github.com/nghiahoang/launchdock/internal/auth"
	httpxpkg "github.com/nghiahoang/launchdock/internal/httpx"
	protocol "github.com/nghiahoang/launchdock/internal/protocol"
	providerspkg "github.com/nghiahoang/launchdock/internal/providers"
)

type Credential = authpkg.Credential

const AuthOAuth = authpkg.AuthOAuth

type Pool = providerspkg.Pool
type Provider = providerspkg.Provider
type OpenAIProvider = providerspkg.OpenAIProvider
type AnthropicProvider = providerspkg.AnthropicProvider

type ChatRequest = protocol.ChatRequest
type ChatMessage = protocol.ChatMessage
type ChatTool = protocol.ChatTool
type ChatToolCall = protocol.ChatToolCall
type ChatFunctionCall = protocol.ChatFunctionCall
type ChatStreamChunk = protocol.ChatStreamChunk
type ChatChoice = protocol.ChatChoice
type ChatResponse = protocol.ChatResponse
type ChatUsage = protocol.ChatUsage
type SSEWriter = protocol.SSEWriter
type SSEEvent = protocol.SSEEvent
type ClaudeResponse = protocol.ClaudeResponse
type ClaudeMessageDelta = protocol.ClaudeMessageDelta
type ClaudeContentBlockStart = protocol.ClaudeContentBlockStart
type ClaudeContentBlockDelta = protocol.ClaudeContentBlockDelta
type ClaudeMessageStart = protocol.ClaudeMessageStart
type ClaudeChatAdapter = protocol.ClaudeChatAdapter

var (
	StreamClient = httpxpkg.StreamClient
	APIClient    = httpxpkg.APIClient
)

func NewSSEWriter(w http.ResponseWriter) (*SSEWriter, bool) { return protocol.NewSSEWriter(w) }
func ReadSSE(r io.Reader, fn func(SSEEvent) error) error    { return protocol.ReadSSE(r, fn) }
func PrefixTools(body []byte, prefix string) ([]byte, error) {
	return providerspkg.PrefixTools(body, prefix)
}
func EnsureOAuthRequirements(body []byte) ([]byte, error) {
	return providerspkg.EnsureOAuthRequirements(body)
}
func PrepareAnthropicOAuthBody(body []byte, prefix string) ([]byte, error) {
	return providerspkg.PrepareOAuthBody(body, prefix)
}
func StripToolPrefix(data []byte, prefix string) []byte {
	return providerspkg.StripToolPrefix(data, prefix)
}
func ChatToResponsesRequest(body []byte) ([]byte, error) {
	return protocol.ChatToResponsesRequest(body)
}

type ResponsesToChatState = protocol.ResponsesToChatState

func NewResponsesToChatState() *protocol.ResponsesToChatState {
	return protocol.NewResponsesToChatState()
}
func ResponsesSSEToChatSSE(eventType, data string, model string, chatID string, created int64, state *ResponsesToChatState) string {
	return protocol.ResponsesSSEToChatSSE(eventType, data, model, chatID, created, state)
}
func ResponsesNonStreamToChat(body []byte, model string) ([]byte, error) {
	return protocol.ResponsesNonStreamToChat(body, model)
}
func ClaudeStopToChat(reason *string) string { return protocol.ClaudeStopToChat(reason) }
func ClaudeToChat(cr *ClaudeResponse, model string) *ChatResponse {
	return protocol.ClaudeToChat(cr, model)
}
func ChatToClaudeRequest(chat *ChatRequest) (*protocol.ClaudeRequest, error) {
	return protocol.ChatToClaudeRequest(chat)
}
func NewClaudeChatAdapter(model string, isOAuth bool) *protocol.ClaudeChatAdapter {
	return protocol.NewClaudeChatAdapter(model, isOAuth)
}
```

## File: `internal/httpapi/handle_chat.go`
```go
package httpapi

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"log/slog"
	"net/http"
	"strings"
	"time"

	authpkg "github.com/nghiahoang/launchdock/internal/auth"
	protocol "github.com/nghiahoang/launchdock/internal/protocol"
	providerspkg "github.com/nghiahoang/launchdock/internal/providers"
)

// HandleChatCompletions handles POST /v1/chat/completions
func HandleChatCompletions(pool *providerspkg.Pool, providers []providerspkg.Provider) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			httpError(w, http.StatusMethodNotAllowed, "method not allowed")
			return
		}

		// Read and parse request
		body, err := io.ReadAll(r.Body)
		if err != nil {
			httpError(w, http.StatusBadRequest, "read body: "+err.Error())
			return
		}

		var chatReq protocol.ChatRequest
		if err := json.Unmarshal(body, &chatReq); err != nil {
			httpError(w, http.StatusBadRequest, "parse request: "+err.Error())
			return
		}

		if strings.HasPrefix(strings.ToLower(chatReq.Model), "claude") {
			thinking, _ := json.Marshal(chatReq.Thinking)
			reasoning, _ := json.Marshal(chatReq.Reasoning)
			slog.Info("claude chat request",
				"model", chatReq.Model,
				"has_thinking", chatReq.Thinking != nil,
				"thinking", trimForLog(string(thinking), 400),
				"reasoning", trimForLog(string(reasoning), 400),
				"reasoning_effort", chatReq.ReasoningEffort,
			)
		}

		if chatReq.Model == "" {
			httpError(w, http.StatusBadRequest, "model is required")
			return
		}

		applyClaudeThinkingAlias(&chatReq)

		// Route to provider
		provider := providerspkg.RouteProvider(providers, chatReq.Model)
		if provider == nil {
			httpError(w, http.StatusBadRequest, fmt.Sprintf("no provider for model %q", chatReq.Model))
			return
		}

		// Pick credential
		cred, err := pool.Pick(provider.ProviderName())
		if err != nil {
			httpError(w, http.StatusServiceUnavailable, err.Error())
			return
		}

		slog.Info("routing request",
			"model", chatReq.Model,
			"provider", provider.ProviderName(),
			"credential", cred.Label,
			"stream", chatReq.Stream,
		)

		// OpenAI OAuth (Codex) → route through Responses API with translation
		if _, ok := provider.(*providerspkg.OpenAIProvider); ok && cred.AuthType == authpkg.AuthOAuth {
			handleChatViaResponsesAPI(w, r, &chatReq, body, provider.(*providerspkg.OpenAIProvider), pool, cred)
			return
		}

		// Translate request
		upstreamBody, urlPath, err := provider.TranslateRequest(&chatReq)
		if err != nil {
			httpError(w, http.StatusInternalServerError, "translate: "+err.Error())
			return
		}

		// Apply OAuth quirks for Anthropic
		if _, ok := provider.(*providerspkg.AnthropicProvider); ok && cred.AuthType == authpkg.AuthOAuth {
			upstreamBody, _ = providerspkg.PrepareOAuthBody(upstreamBody, "mcp_")
		}

		// Send with retry on retryable errors
		upResp, cred, err := sendWithRetry(r, provider, pool, cred, chatReq.Model, upstreamBody, urlPath)
		if err != nil {
			httpError(w, http.StatusBadGateway, "upstream: "+err.Error())
			return
		}
		defer upResp.Body.Close()

		// Handle errors (non-retryable at this point)
		if upResp.StatusCode != http.StatusOK {
			if provider.ProviderName() == "anthropic" {
				logAnthropicRequestSummary("chat.completions", upstreamBody)
			}
			handleUpstreamError(w, upResp, pool, cred)
			return
		}

		// Stream or non-stream response
		if chatReq.Stream {
			handleStreamResponse(w, upResp, provider, cred, chatReq.Model)
		} else {
			handleNonStreamResponse(w, upResp, provider, cred, chatReq.Model)
		}
	}
}

func applyClaudeThinkingAlias(chatReq *protocol.ChatRequest) {
	switch chatReq.Model {
	case "claude-opus-4-6-thinking":
		chatReq.Model = "claude-opus-4-6"
		if chatReq.Thinking == nil {
			chatReq.Thinking = map[string]any{"type": "enabled", "budget_tokens": 16000}
		}
	case "claude-sonnet-4-6-thinking":
		chatReq.Model = "claude-sonnet-4-6"
		if chatReq.Thinking == nil {
			chatReq.Thinking = map[string]any{"type": "enabled", "budget_tokens": 16000}
		}
	}
}

// sendWithRetry sends the upstream request, retrying with a different credential on retryable errors.
func sendWithRetry(r *http.Request, provider Provider, pool *Pool, cred *Credential, model string, body []byte, urlPath string) (*http.Response, *Credential, error) {
	return doWithCredentialRetry(pool, provider.ProviderName(), cred, func(current *Credential) (*http.Response, error) {
		upReq, err := http.NewRequestWithContext(r.Context(), "POST",
			provider.BaseURL()+urlPath, bytes.NewReader(body))
		if err != nil {
			return nil, err
		}

		if ap, ok := provider.(*AnthropicProvider); ok {
			ap.PrepareWithModel(upReq, current, model)
		} else {
			provider.Prepare(upReq, current)
		}

		resp, err := StreamClient.Do(upReq)
		if err != nil {
			return nil, err
		}
		return resp, nil
	})
}

func handleStreamResponse(w http.ResponseWriter, upResp *http.Response, provider Provider, cred *Credential, model string) {
	sse, ok := NewSSEWriter(w)
	if !ok {
		httpError(w, http.StatusInternalServerError, "streaming not supported")
		return
	}

	isAnthropic := provider.ProviderName() == "anthropic"

	if isAnthropic {
		relayClaudeSSEAsChat(sse, upResp.Body, model, cred)
	} else {
		// OpenAI — passthrough SSE
		ReadSSE(upResp.Body, func(ev SSEEvent) error {
			if ev.Data == "[DONE]" {
				sse.WriteDone()
				return nil
			}
			sse.WriteData(ev.Data)
			return nil
		})
	}
}

func relayClaudeSSEAsChat(sse *SSEWriter, body io.Reader, model string, cred *Credential) {
	adapter := NewClaudeChatAdapter(model, cred.AuthType == AuthOAuth)
	ReadSSE(body, func(ev SSEEvent) error {
		for _, chunk := range adapter.Consume(ev.Event, ev.Data) {
			sse.WriteJSON(chunk)
		}
		if ev.Event == "message_stop" {
			sse.WriteDone()
			return nil
		}
		var event struct {
			Type string `json:"type"`
		}
		if json.Unmarshal([]byte(ev.Data), &event) == nil && event.Type == "message_stop" {
			sse.WriteDone()
		}
		return nil
	})
}

func handleNonStreamResponse(w http.ResponseWriter, upResp *http.Response, provider Provider, cred *Credential, model string) {
	body, err := io.ReadAll(upResp.Body)
	if err != nil {
		httpError(w, http.StatusBadGateway, "read upstream: "+err.Error())
		return
	}

	if provider.ProviderName() == "anthropic" {
		var claudeResp ClaudeResponse
		if err := json.Unmarshal(body, &claudeResp); err != nil {
			httpError(w, http.StatusBadGateway, "parse claude response: "+err.Error())
			return
		}
		// Strip mcp_ prefix from tool names for OAuth
		if cred.AuthType == AuthOAuth {
			for i, c := range claudeResp.Content {
				if c.Type == "tool_use" {
					claudeResp.Content[i].Name = stripPrefix(c.Name, "mcp_")
				}
			}
		}
		chatResp := ClaudeToChat(&claudeResp, model)
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(chatResp)
	} else {
		// OpenAI — passthrough
		w.Header().Set("Content-Type", "application/json")
		w.Write(body)
	}
}

// isRetryable returns true if the upstream error warrants trying another credential.
func isRetryable(statusCode int) bool {
	return statusCode == 429 || statusCode == 500 || statusCode == 502 ||
		statusCode == 503 || statusCode == 529
}

func handleUpstreamError(w http.ResponseWriter, resp *http.Response, pool *Pool, cred *Credential) {
	body, _ := io.ReadAll(resp.Body)
	slog.Warn("upstream error",
		"status", resp.StatusCode,
		"credential", cred.Label,
		"body", trimForLog(string(body), 1200),
	)

	// Cooldown on rate limit or overload
	switch resp.StatusCode {
	case 429:
		pool.Cooldown(cred, 60*time.Second)
	case 529, 503:
		pool.Cooldown(cred, 30*time.Second)
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(resp.StatusCode)
	w.Write(body)
}

func logAnthropicRequestSummary(endpoint string, body []byte) {
	var req map[string]any
	if err := json.Unmarshal(body, &req); err != nil {
		slog.Warn("anthropic request summary unavailable", "endpoint", endpoint, "error", err)
		return
	}

	toolNames := []string{}
	if tools, ok := req["tools"].([]any); ok {
		for _, t := range tools {
			if tm, ok := t.(map[string]any); ok {
				if name, _ := tm["name"].(string); name != "" {
					toolNames = append(toolNames, name)
				}
			}
		}
	}

	lastRole := ""
	lastTypes := []string{}
	assistantToolCalls := []string{}
	if msgs, ok := req["messages"].([]any); ok && len(msgs) > 0 {
		if last, ok := msgs[len(msgs)-1].(map[string]any); ok {
			lastRole, _ = last["role"].(string)
			switch content := last["content"].(type) {
			case string:
				lastTypes = append(lastTypes, "text")
			case []any:
				for _, item := range content {
					if cm, ok := item.(map[string]any); ok {
						if typ, _ := cm["type"].(string); typ != "" {
							lastTypes = append(lastTypes, typ)
						}
					}
				}
			}
			if toolCalls, ok := last["tool_calls"].([]any); ok {
				for _, tc := range toolCalls {
					if tcm, ok := tc.(map[string]any); ok {
						if fn, ok := tcm["function"].(map[string]any); ok {
							if name, _ := fn["name"].(string); name != "" {
								assistantToolCalls = append(assistantToolCalls, name)
							}
						}
					}
				}
			}
		}
	}

	toolChoice, _ := json.Marshal(req["tool_choice"])
	thinking, _ := json.Marshal(req["thinking"])
	system, _ := json.Marshal(req["system"])

	slog.Warn("anthropic request summary",
		"endpoint", endpoint,
		"model", req["model"],
		"stream", req["stream"],
		"max_tokens", req["max_tokens"],
		"tool_names", toolNames,
		"tool_choice", string(toolChoice),
		"thinking", trimForLog(string(thinking), 400),
		"last_role", lastRole,
		"last_content_types", lastTypes,
		"last_tool_calls", assistantToolCalls,
		"system", trimForLog(string(system), 400),
	)
}

func trimForLog(s string, max int) string {
	if len(s) <= max {
		return s
	}
	if max <= 3 {
		return s[:max]
	}
	return s[:max-3] + "..."
}

func httpError(w http.ResponseWriter, code int, msg string) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(code)
	json.NewEncoder(w).Encode(map[string]any{
		"error": map[string]any{
			"message": msg,
			"type":    "error",
			"code":    code,
		},
	})
}

func stripPrefix(s, prefix string) string {
	if len(s) > len(prefix) && s[:len(prefix)] == prefix {
		return s[len(prefix):]
	}
	return s
}

// handleChatViaResponsesAPI translates Chat Completions → Responses API for OpenAI OAuth.
func handleChatViaResponsesAPI(w http.ResponseWriter, r *http.Request, chatReq *ChatRequest, body []byte, openai *OpenAIProvider, pool *Pool, cred *Credential) {
	// Translate Chat → Responses format
	respBody, err := ChatToResponsesRequest(body)
	if err != nil {
		httpError(w, http.StatusInternalServerError, "translate to responses: "+err.Error())
		return
	}
	upResp, cred, err := doWithCredentialRetry(pool, "openai", cred, func(current *Credential) (*http.Response, error) {
		upstreamURL := openai.ChatGPTBaseURL() + "/responses"
		upReq, err := http.NewRequestWithContext(r.Context(), "POST", upstreamURL, bytes.NewReader(respBody))
		if err != nil {
			return nil, err
		}
		openai.Prepare(upReq, current)
		return StreamClient.Do(upReq)
	})
	if err != nil {
		httpError(w, http.StatusBadGateway, "upstream: "+err.Error())
		return
	}
	defer upResp.Body.Close()

	if upResp.StatusCode != http.StatusOK {
		handleUpstreamError(w, upResp, pool, cred)
		return
	}

	// ChatGPT backend always streams — handle both client modes
	if chatReq.Stream {
		// Stream: translate Responses SSE → Chat SSE
		sse, ok := NewSSEWriter(w)
		if !ok {
			httpError(w, http.StatusInternalServerError, "streaming not supported")
			return
		}
		chatID := fmt.Sprintf("chatcmpl-%d", time.Now().UnixNano())
		created := time.Now().Unix()
		state := NewResponsesToChatState()

		ReadSSE(upResp.Body, func(ev SSEEvent) error {
			chunk := ResponsesSSEToChatSSE(ev.Event, ev.Data, chatReq.Model, chatID, created, state)
			if chunk != "" {
				sse.WriteRawJSON([]byte(chunk))
			}
			var obj map[string]any
			if json.Unmarshal([]byte(ev.Data), &obj) == nil {
				if t, _ := obj["type"].(string); t == "response.completed" || t == "response.done" {
					sse.WriteDone()
				}
			}
			return nil
		})
	} else {
		body, err := collectResponsesCompletedJSON(upResp.Body)
		if err != nil {
			httpError(w, http.StatusBadGateway, "collect responses: "+err.Error())
			return
		}
		chatBody, err := ResponsesNonStreamToChat(body, chatReq.Model)
		if err != nil {
			httpError(w, http.StatusBadGateway, "translate responses: "+err.Error())
			return
		}
		w.Header().Set("Content-Type", "application/json")
		w.Write(chatBody)
	}
}
```

## File: `internal/httpapi/handle_messages.go`
```go
package httpapi

import (
	"bytes"
	"encoding/json"
	"io"
	"log/slog"
	"net/http"
)

// HandleMessages handles POST /v1/messages (Claude Messages API passthrough)
// Clients that speak Claude format natively hit this endpoint.
// The mux adds credential auth + OAuth quirks, then forwards to Anthropic.
func HandleMessages(pool *Pool, anthropic *AnthropicProvider) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			httpError(w, http.StatusMethodNotAllowed, "method not allowed")
			return
		}

		body, err := io.ReadAll(r.Body)
		if err != nil {
			httpError(w, http.StatusBadRequest, "read body: "+err.Error())
			return
		}

		// Extract model for logging and header building
		var peek struct {
			Model  string `json:"model"`
			Stream bool   `json:"stream"`
		}
		json.Unmarshal(body, &peek)

		if peek.Model == "" {
			httpError(w, http.StatusBadRequest, "model is required")
			return
		}

		// Pick credential
		cred, err := pool.Pick("anthropic")
		if err != nil {
			httpError(w, http.StatusServiceUnavailable, err.Error())
			return
		}

		slog.Info("routing messages",
			"model", peek.Model,
			"credential", cred.Label,
			"stream", peek.Stream,
		)

		// Apply OAuth quirks if needed
		if cred.AuthType == AuthOAuth {
			body, _ = PrepareAnthropicOAuthBody(body, "mcp_")
		}

		upResp, cred, err := ensureOKOrRetry(pool, "anthropic", cred, func(current *Credential) (*http.Response, error) {
			upReq, err := http.NewRequestWithContext(r.Context(), "POST",
				anthropic.BaseURL()+"/v1/messages", bytes.NewReader(body))
			if err != nil {
				return nil, err
			}
			anthropic.PrepareWithModel(upReq, current, peek.Model)
			return StreamClient.Do(upReq)
		})
		if err != nil {
			httpError(w, http.StatusBadGateway, "upstream: "+err.Error())
			return
		}
		defer upResp.Body.Close()

		if upResp.StatusCode != http.StatusOK {
			logAnthropicRequestSummary("messages", body)
		}

		if peek.Stream {
			relayClaudeMessagesStream(w, upResp, cred)
		} else {
			relayClaudeMessagesNonStream(w, upResp, cred)
		}
	}
}

// relayClaudeMessagesStream forwards Claude SSE as-is, only stripping mcp_ prefix.
func relayClaudeMessagesStream(w http.ResponseWriter, upResp *http.Response, cred *Credential) {
	flusher, ok := w.(http.Flusher)
	if !ok {
		httpError(w, http.StatusInternalServerError, "streaming not supported")
		return
	}

	// Copy upstream headers
	for _, h := range []string{"Content-Type", "Cache-Control"} {
		if v := upResp.Header.Get(h); v != "" {
			w.Header().Set(h, v)
		}
	}
	w.Header().Set("Content-Type", "text/event-stream")
	w.Header().Set("Cache-Control", "no-cache")
	w.Header().Set("Connection", "keep-alive")
	w.WriteHeader(http.StatusOK)

	isOAuth := cred.AuthType == AuthOAuth

	ReadSSE(upResp.Body, func(ev SSEEvent) error {
		data := ev.Data
		// Strip mcp_ prefix from tool names in SSE data
		if isOAuth {
			data = string(StripToolPrefix([]byte(data), "mcp_"))
		}

		if ev.Event != "" {
			writeSSEMessage(w, ev.Event, data)
		} else {
			writeSSEMessage(w, "", data)
		}
		flusher.Flush()
		return nil
	})
}

// relayClaudeMessagesNonStream forwards the Claude JSON response, stripping mcp_ prefix.
func relayClaudeMessagesNonStream(w http.ResponseWriter, upResp *http.Response, cred *Credential) {
	body, err := io.ReadAll(upResp.Body)
	if err != nil {
		httpError(w, http.StatusBadGateway, "read upstream: "+err.Error())
		return
	}

	if cred.AuthType == AuthOAuth {
		body = StripToolPrefix(body, "mcp_")
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write(body)
}

func writeSSEMessage(w http.ResponseWriter, event, data string) {
	if event != "" {
		_, _ = w.Write([]byte("event: "))
		_, _ = w.Write([]byte(event))
		_, _ = w.Write([]byte("\n"))
	}
	_, _ = w.Write([]byte("data: "))
	_, _ = w.Write([]byte(data))
	_, _ = w.Write([]byte("\n\n"))
}
```

## File: `internal/httpapi/handle_meta.go`
```go
package httpapi

import (
	"encoding/json"
	"log/slog"
	"net/http"
	"sync"
	"time"
)

func HandleHealth(pool *Pool) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(map[string]any{
			"status":    "ok",
			"providers": pool.Providers(),
			"credentials": map[string]int{
				"anthropic": pool.Count("anthropic"),
				"openai":    pool.Count("openai"),
				"total":     pool.Count(""),
			},
		})
	}
}

// --- Models cache ---

var (
	modelCache     []map[string]any
	modelCacheMu   sync.RWMutex
	modelCacheTime time.Time
	modelCacheTTL  = 10 * time.Minute
)

func HandleModels(pool *Pool, anthropic *AnthropicProvider) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		models := getCachedModels(pool, anthropic)
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(map[string]any{
			"object": "list",
			"data":   models,
		})
	}
}

func ResetModelCache() {
	modelCacheMu.Lock()
	defer modelCacheMu.Unlock()
	modelCache = nil
	modelCacheTime = time.Time{}
}

func getCachedModels(pool *Pool, anthropic *AnthropicProvider) []map[string]any {
	modelCacheMu.RLock()
	if modelCache != nil && time.Since(modelCacheTime) < modelCacheTTL {
		defer modelCacheMu.RUnlock()
		return modelCache
	}
	modelCacheMu.RUnlock()

	models := fetchAllModels(pool, anthropic)

	modelCacheMu.Lock()
	modelCache = models
	modelCacheTime = time.Now()
	modelCacheMu.Unlock()

	return models
}

func fetchAllModels(pool *Pool, anthropic *AnthropicProvider) []map[string]any {
	var models []map[string]any

	// Anthropic — fetch from API
	if pool.Count("anthropic") > 0 {
		apiModels := fetchAnthropicModels(pool, anthropic)
		if len(apiModels) > 0 {
			models = append(models, apiModels...)
			models = append(models, anthropicThinkingAliasModels(apiModels)...)
		} else {
			// Fallback to hardcoded if API fails
			fallback := anthropicFallbackModels()
			models = append(models, fallback...)
			models = append(models, anthropicThinkingAliasModels(fallback)...)
		}
	}

	// OpenAI — hardcoded (Codex OAuth lacks api.model.read scope)
	if pool.Count("openai") > 0 {
		models = append(models, openAIModels()...)
	}

	return models
}

func FetchAllModels(pool *Pool, anthropic *AnthropicProvider) []map[string]any {
	return fetchAllModels(pool, anthropic)
}

func fetchAnthropicModels(pool *Pool, provider *AnthropicProvider) []map[string]any {
	cred, err := pool.Pick("anthropic")
	if err != nil {
		slog.Debug("no anthropic credential for models fetch", "error", err)
		return nil
	}

	req, err := http.NewRequest("GET", provider.BaseURL()+"/v1/models", nil)
	if err != nil {
		return nil
	}
	provider.PrepareWithModel(req, cred, "")

	resp, err := APIClient.Do(req)
	if err != nil {
		slog.Debug("anthropic models fetch failed", "error", err)
		return nil
	}
	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		slog.Debug("anthropic models fetch non-200", "status", resp.StatusCode)
		return nil
	}

	var result struct {
		Data []struct {
			ID          string `json:"id"`
			DisplayName string `json:"display_name"`
			CreatedAt   string `json:"created_at"`
		} `json:"data"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		slog.Debug("anthropic models parse failed", "error", err)
		return nil
	}

	var models []map[string]any
	for _, m := range result.Data {
		models = append(models, map[string]any{
			"id":       m.ID,
			"object":   "model",
			"created":  time.Now().Unix(),
			"owned_by": "anthropic",
		})
	}

	slog.Info("fetched anthropic models", "count", len(models))
	return models
}

func anthropicFallbackModels() []map[string]any {
	var models []map[string]any
	for _, m := range []string{
		"claude-opus-4-20250514",
		"claude-opus-4-1-20250805",
		"claude-sonnet-4-20250514",
		"claude-sonnet-4-1-20250514",
		"claude-haiku-3-5-20241022",
	} {
		models = append(models, map[string]any{
			"id":       m,
			"object":   "model",
			"created":  time.Now().Unix(),
			"owned_by": "anthropic",
		})
	}
	return models
}

func anthropicThinkingAliasModels(base []map[string]any) []map[string]any {
	var aliases []map[string]any
	for _, m := range base {
		id, _ := m["id"].(string)
		switch id {
		case "claude-opus-4-6", "claude-sonnet-4-6":
			aliases = append(aliases, map[string]any{
				"id":       id + "-thinking",
				"object":   "model",
				"created":  m["created"],
				"owned_by": "anthropic",
			})
		}
	}
	return aliases
}

const codexModelsURL = "https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/models.json"

func openAIModels() []map[string]any {
	// Try fetching from Codex repo
	if models := fetchCodexModels(); len(models) > 0 {
		return models
	}
	// Fallback hardcoded
	return openAIFallbackModels()
}

func fetchCodexModels() []map[string]any {
	resp, err := APIClient.Get(codexModelsURL)
	if err != nil {
		slog.Debug("codex models fetch failed", "error", err)
		return nil
	}
	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		return nil
	}

	var result struct {
		Models []struct {
			Slug          string `json:"slug"`
			DisplayName   string `json:"display_name"`
			Visibility    string `json:"visibility"`
			ContextWindow int    `json:"context_window"`
		} `json:"models"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		slog.Debug("codex models parse failed", "error", err)
		return nil
	}

	var models []map[string]any
	for _, m := range result.Models {
		if m.Visibility != "list" {
			continue
		}
		models = append(models, map[string]any{
			"id":       m.Slug,
			"object":   "model",
			"created":  time.Now().Unix(),
			"owned_by": "openai",
		})
	}

	slog.Info("fetched codex models", "count", len(models))
	return models
}

func openAIFallbackModels() []map[string]any {
	var models []map[string]any
	for _, m := range []string{
		"gpt-5.4",
		"gpt-5.4-mini",
		"gpt-5.3-codex",
		"o3-mini",
		"o4-mini",
	} {
		models = append(models, map[string]any{
			"id":       m,
			"object":   "model",
			"created":  time.Now().Unix(),
			"owned_by": "openai",
		})
	}
	return models
}
```

## File: `internal/httpapi/handle_responses.go`
```go
package httpapi

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"log/slog"
	"net/http"
	"strings"
	"time"
)

// HandleResponses handles POST /v1/responses (OpenAI Responses API passthrough)
// Codex CLI and other Responses API clients hit this endpoint.
// The mux adds credential auth, then forwards to OpenAI.
func HandleResponses(pool *Pool, openai *OpenAIProvider, anthropic *AnthropicProvider) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			httpError(w, http.StatusMethodNotAllowed, "method not allowed")
			return
		}

		body, err := io.ReadAll(r.Body)
		if err != nil {
			httpError(w, http.StatusBadRequest, "read body: "+err.Error())
			return
		}

		// Extract model for logging
		var peek struct {
			Model  string `json:"model"`
			Stream bool   `json:"stream"`
		}
		json.Unmarshal(body, &peek)

		if peek.Model == "" {
			httpError(w, http.StatusBadRequest, "model is required")
			return
		}

		if strings.HasPrefix(peek.Model, "claude") {
			handleClaudeResponses(w, r, body, &peek, pool, anthropic)
			return
		}

		credMatcher := func(c *Credential) bool {
			return c.Provider == "openai" && c.Kind == "codex_chatgpt"
		}

		// Pick credential compatible with ChatGPT Codex backend.
		cred, err := pool.PickMatching("openai", nil, credMatcher)
		if err != nil {
			httpError(w, http.StatusServiceUnavailable, err.Error())
			return
		}

		slog.Info("routing responses",
			"model", peek.Model,
			"credential", cred.Label,
			"stream", peek.Stream,
		)

		requestBody := body
		if cred.AuthType == AuthOAuth {
			requestBody = prepareResponsesOAuthBody(body, !peek.Stream)
		}

		upResp, cred, err := ensureOKOrRetryMatching(pool, "openai", cred, credMatcher, func(current *Credential) (*http.Response, error) {
			var upstreamURL string
			bodyToSend := requestBody
			if current.AuthType == AuthOAuth {
				upstreamURL = openai.ChatGPTBaseURL() + "/responses"
			} else {
				upstreamURL = openai.BaseURL() + "/v1/responses"
			}
			upReq, err := http.NewRequestWithContext(r.Context(), "POST",
				upstreamURL, bytes.NewReader(bodyToSend))
			if err != nil {
				return nil, err
			}

			openai.Prepare(upReq, current)

			for _, h := range []string{
				"x-codex-turn-state",
				"x-codex-turn-metadata",
				"x-codex-beta-features",
				"x-client-request-id",
				"OpenAI-Beta",
			} {
				if v := r.Header.Get(h); v != "" {
					upReq.Header.Set(h, v)
				}
			}

			client := APIClient
			if current.AuthType == AuthOAuth || peek.Stream {
				client = StreamClient
			}
			return client.Do(upReq)
		})
		if err != nil {
			httpError(w, http.StatusBadGateway, "upstream: "+err.Error())
			return
		}
		defer upResp.Body.Close()

		if peek.Stream {
			relayResponsesStream(w, upResp)
		} else {
			if cred.AuthType == AuthOAuth {
				relayResponsesCollectedNonStream(w, upResp)
			} else {
				relayResponsesNonStream(w, upResp)
			}
		}
	}
}

func handleClaudeResponses(w http.ResponseWriter, r *http.Request, body []byte, peek *struct {
	Model  string `json:"model"`
	Stream bool   `json:"stream"`
}, pool *Pool, anthropic *AnthropicProvider) {
	chatReq, err := responsesToChatRequest(body)
	if err != nil {
		httpError(w, http.StatusBadRequest, "translate responses: "+err.Error())
		return
	}
	applyClaudeThinkingAlias(chatReq)
	chatReq.Stream = true

	cred, err := pool.Pick("anthropic")
	if err != nil {
		httpError(w, http.StatusServiceUnavailable, err.Error())
		return
	}

	upstreamBody, _, err := anthropic.TranslateRequest(chatReq)
	if err != nil {
		httpError(w, http.StatusInternalServerError, "translate: "+err.Error())
		return
	}
	if cred.AuthType == AuthOAuth {
		upstreamBody, _ = PrepareAnthropicOAuthBody(upstreamBody, "mcp_")
	}

	upResp, cred, err := sendWithRetry(r, anthropic, pool, cred, chatReq.Model, upstreamBody, "/v1/messages")
	if err != nil {
		httpError(w, http.StatusBadGateway, "upstream: "+err.Error())
		return
	}
	defer upResp.Body.Close()
	if upResp.StatusCode != http.StatusOK {
		handleUpstreamError(w, upResp, pool, cred)
		return
	}

	if peek.Stream {
		relayClaudeResponsesStream(w, upResp, chatReq.Model)
		return
	}
	respObj, err := collectClaudeResponses(upResp.Body, chatReq.Model)
	if err != nil {
		httpError(w, http.StatusBadGateway, "collect responses: "+err.Error())
		return
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(respObj)
}

func responsesToChatRequest(body []byte) (*ChatRequest, error) {
	var req map[string]any
	if err := json.Unmarshal(body, &req); err != nil {
		return nil, err
	}
	chat := &ChatRequest{Model: asString(req["model"]), Stream: true}
	if inputStr, ok := req["input"].(string); ok && inputStr != "" {
		chat.Messages = append(chat.Messages, ChatMessage{Role: "user", Content: inputStr})
	}
	if input, ok := req["input"].([]any); ok {
		for _, item := range input {
			m, _ := item.(map[string]any)
			if m == nil {
				if s, ok := item.(string); ok && s != "" {
					chat.Messages = append(chat.Messages, ChatMessage{Role: "user", Content: s})
				}
				continue
			}
			role, _ := m["role"].(string)
			if role == "" {
				role = "user"
			}
			content := m["content"]
			if parts, ok := content.([]any); ok {
				var texts []string
				for _, p := range parts {
					pm, _ := p.(map[string]any)
					if pm == nil {
						continue
					}
					if t, _ := pm["type"].(string); t == "input_text" || t == "output_text" {
						if s, _ := pm["text"].(string); s != "" {
							texts = append(texts, s)
						}
					}
				}
				content = strings.Join(texts, "")
			}
			chat.Messages = append(chat.Messages, ChatMessage{Role: role, Content: content})
		}
	}
	if len(chat.Messages) == 0 {
		return nil, fmt.Errorf("messages: Input should be a valid list")
	}
	if tools, ok := req["tools"].([]any); ok {
		for _, item := range tools {
			m, _ := item.(map[string]any)
			if m == nil {
				continue
			}
			typ, _ := m["type"].(string)
			if typ != "function" {
				continue
			}
			tool := ChatTool{Type: "function"}
			if name, _ := m["name"].(string); name != "" {
				tool.Function.Name = name
			}
			if desc, _ := m["description"].(string); desc != "" {
				tool.Function.Description = desc
			}
			if params, ok := m["parameters"]; ok {
				if b, err := json.Marshal(params); err == nil {
					tool.Function.Parameters = b
				}
			}
			if tool.Function.Name != "" {
				chat.Tools = append(chat.Tools, tool)
			}
		}
	}
	if tc, ok := req["tool_choice"]; ok {
		chat.ToolChoice = tc
	}
	if instructions, _ := req["instructions"].(string); instructions != "" {
		chat.Messages = append([]ChatMessage{{Role: "system", Content: instructions}}, chat.Messages...)
	}
	return chat, nil
}

func relayClaudeResponsesStream(w http.ResponseWriter, upResp *http.Response, model string) {
	flusher, ok := w.(http.Flusher)
	if !ok {
		httpError(w, http.StatusInternalServerError, "streaming not supported")
		return
	}
	w.Header().Set("Content-Type", "text/event-stream")
	w.Header().Set("Cache-Control", "no-cache")
	w.Header().Set("Connection", "keep-alive")
	w.WriteHeader(http.StatusOK)

	state := newClaudeResponsesState(model)

	writeEvent := func(event string, payload map[string]any) {
		payload["sequence_number"] = state.sequence
		state.sequence++
		b, _ := json.Marshal(payload)
		writeSSEMessage(w, event, string(b))
		flusher.Flush()
	}

	writeEvent("response.created", map[string]any{"type": "response.created", "response": state.baseResponse("in_progress")})
	writeEvent("response.in_progress", map[string]any{"type": "response.in_progress", "response": state.baseResponse("in_progress")})

	ReadSSE(upResp.Body, func(ev SSEEvent) error {
		for _, out := range state.consumeEvent(ev) {
			writeEvent(out.event, out.payload)
		}
		return nil
	})
}

type claudeResponsesState struct {
	model            string
	respID           string
	created          int64
	sequence         int
	reasoningID      string
	messageID        string
	toolCallID       string
	toolCallName     string
	reasoningStarted bool
	messageStarted   bool
	toolStarted      bool
	reasoningText    strings.Builder
	outputText       strings.Builder
	toolArgs         strings.Builder
}

type responsesEventOut struct {
	event   string
	payload map[string]any
}

func newClaudeResponsesState(model string) *claudeResponsesState {
	return &claudeResponsesState{model: model, respID: fmt.Sprintf("resp_%d", time.Now().UnixNano()), created: time.Now().Unix(), reasoningID: fmt.Sprintf("rs_%d", time.Now().UnixNano()), messageID: fmt.Sprintf("msg_%d", time.Now().UnixNano())}
}

func (s *claudeResponsesState) baseResponse(status string) map[string]any {
	return map[string]any{"id": s.respID, "object": "response", "created_at": s.created, "status": status, "model": s.model, "output": []any{}}
}

func (s *claudeResponsesState) consumeEvent(ev SSEEvent) []responsesEventOut {
	var outs []responsesEventOut
	switch ev.Event {
	case "content_block_start":
		var cbs ClaudeContentBlockStart
		if json.Unmarshal([]byte(ev.Data), &cbs) != nil {
			return nil
		}
		if cbs.ContentBlock.Type == "tool_use" {
			s.toolStarted = true
			s.toolCallID = cbs.ContentBlock.ID
			s.toolCallName = stripPrefix(cbs.ContentBlock.Name, "mcp_")
			outs = append(outs, responsesEventOut{"response.output_item.added", map[string]any{"type": "response.output_item.added", "item": map[string]any{"id": s.toolCallID, "type": "function_call", "call_id": s.toolCallID, "name": s.toolCallName, "arguments": "", "status": "in_progress"}, "output_index": 0}})
		}
	case "content_block_delta":
		var cbd ClaudeContentBlockDelta
		if json.Unmarshal([]byte(ev.Data), &cbd) != nil {
			return nil
		}
		switch cbd.Delta.Type {
		case "thinking_delta":
			if cbd.Delta.Thinking == "" {
				return nil
			}
			if !s.reasoningStarted {
				s.reasoningStarted = true
				outs = append(outs,
					responsesEventOut{"response.output_item.added", map[string]any{"type": "response.output_item.added", "item": map[string]any{"id": s.reasoningID, "type": "reasoning", "summary": []any{}}, "output_index": 0}},
					responsesEventOut{"response.reasoning_summary_part.added", map[string]any{"type": "response.reasoning_summary_part.added", "item_id": s.reasoningID, "output_index": 0, "part": map[string]any{"type": "summary_text", "text": ""}, "summary_index": 0}},
				)
			}
			s.reasoningText.WriteString(cbd.Delta.Thinking)
			outs = append(outs, responsesEventOut{"response.reasoning_summary_text.delta", map[string]any{"type": "response.reasoning_summary_text.delta", "delta": cbd.Delta.Thinking, "item_id": s.reasoningID, "output_index": 0, "summary_index": 0}})
		case "text_delta":
			if cbd.Delta.Text == "" {
				return nil
			}
			if !s.messageStarted {
				s.messageStarted = true
				idx := 0
				if s.reasoningStarted {
					idx = 1
				}
				outs = append(outs,
					responsesEventOut{"response.output_item.added", map[string]any{"type": "response.output_item.added", "item": map[string]any{"id": s.messageID, "type": "message", "status": "in_progress", "content": []any{}, "phase": "final_answer", "role": "assistant"}, "output_index": idx}},
					responsesEventOut{"response.content_part.added", map[string]any{"type": "response.content_part.added", "content_index": 0, "item_id": s.messageID, "output_index": idx, "part": map[string]any{"type": "output_text", "annotations": []any{}, "logprobs": []any{}, "text": ""}}},
				)
			}
			s.outputText.WriteString(cbd.Delta.Text)
			idx := 0
			if s.reasoningStarted {
				idx = 1
			}
			outs = append(outs, responsesEventOut{"response.output_text.delta", map[string]any{"type": "response.output_text.delta", "content_index": 0, "delta": cbd.Delta.Text, "item_id": s.messageID, "logprobs": []any{}, "output_index": idx}})
		case "input_json_delta":
			if !s.toolStarted || cbd.Delta.PartialJSON == "" {
				return nil
			}
			s.toolArgs.WriteString(cbd.Delta.PartialJSON)
			outs = append(outs, responsesEventOut{"response.function_call_arguments.delta", map[string]any{"type": "response.function_call_arguments.delta", "delta": cbd.Delta.PartialJSON, "item_id": s.toolCallID, "output_index": 0}})
		}
	case "message_stop":
		if s.toolStarted {
			args := s.toolArgs.String()
			outs = append(outs, responsesEventOut{"response.function_call_arguments.done", map[string]any{"type": "response.function_call_arguments.done", "arguments": args, "item_id": s.toolCallID, "output_index": 0}})
			outs = append(outs, responsesEventOut{"response.output_item.done", map[string]any{"type": "response.output_item.done", "item": map[string]any{"id": s.toolCallID, "type": "function_call", "call_id": s.toolCallID, "name": s.toolCallName, "arguments": args, "status": "completed"}, "output_index": 0}})
		}
		if s.reasoningStarted {
			text := s.reasoningText.String()
			outs = append(outs,
				responsesEventOut{"response.reasoning_summary_text.done", map[string]any{"type": "response.reasoning_summary_text.done", "item_id": s.reasoningID, "output_index": 0, "summary_index": 0, "text": text}},
				responsesEventOut{"response.reasoning_summary_part.done", map[string]any{"type": "response.reasoning_summary_part.done", "item_id": s.reasoningID, "output_index": 0, "part": map[string]any{"type": "summary_text", "text": text}, "summary_index": 0}},
				responsesEventOut{"response.output_item.done", map[string]any{"type": "response.output_item.done", "item": map[string]any{"id": s.reasoningID, "type": "reasoning", "summary": []any{map[string]any{"type": "summary_text", "text": text}}}, "output_index": 0}},
			)
		}
		if s.messageStarted {
			idx := 0
			if s.reasoningStarted {
				idx = 1
			}
			text := s.outputText.String()
			outs = append(outs,
				responsesEventOut{"response.output_text.done", map[string]any{"type": "response.output_text.done", "content_index": 0, "item_id": s.messageID, "logprobs": []any{}, "output_index": idx, "text": text}},
				responsesEventOut{"response.content_part.done", map[string]any{"type": "response.content_part.done", "content_index": 0, "item_id": s.messageID, "output_index": idx, "part": map[string]any{"type": "output_text", "annotations": []any{}, "logprobs": []any{}, "text": text}}},
				responsesEventOut{"response.output_item.done", map[string]any{"type": "response.output_item.done", "item": map[string]any{"id": s.messageID, "type": "message", "status": "completed", "content": []any{map[string]any{"type": "output_text", "annotations": []any{}, "logprobs": []any{}, "text": text}}, "phase": "final_answer", "role": "assistant"}, "output_index": idx}},
			)
		}
		outs = append(outs, responsesEventOut{"response.completed", map[string]any{"type": "response.completed", "response": s.finalResponse()}})
	}
	return outs
}

func (s *claudeResponsesState) finalResponse() map[string]any {
	usage := map[string]any{"input_tokens": 0, "input_tokens_details": map[string]any{"cached_tokens": 0}, "output_tokens": 0, "output_tokens_details": map[string]any{"reasoning_tokens": 0}, "total_tokens": 0}
	output := buildClaudeResponseOutput(s.reasoningStarted, s.reasoningID, s.reasoningText.String(), s.messageStarted, s.messageID, s.outputText.String())
	if s.toolStarted {
		output = append(output, map[string]any{"id": s.toolCallID, "type": "function_call", "call_id": s.toolCallID, "name": s.toolCallName, "arguments": s.toolArgs.String(), "status": "completed"})
	}
	return map[string]any{"id": s.respID, "object": "response", "created_at": s.created, "status": "completed", "model": s.model, "output": output, "reasoning": map[string]any{"effort": "high", "summary": "detailed"}, "usage": usage}
}

func collectClaudeResponses(r io.Reader, model string) (map[string]any, error) {
	state := newClaudeResponsesState(model)
	err := ReadSSE(r, func(ev SSEEvent) error {
		state.consumeEvent(ev)
		return nil
	})
	if err != nil {
		return nil, err
	}
	return state.finalResponse(), nil
}

func buildClaudeResponseOutput(hasReasoning bool, reasoningID, reasoningText string, hasMessage bool, messageID, outputText string) []any {
	var out []any
	if hasReasoning {
		out = append(out, map[string]any{"id": reasoningID, "type": "reasoning", "summary": []any{map[string]any{"type": "summary_text", "text": reasoningText}}})
	}
	if hasMessage {
		out = append(out, map[string]any{"id": messageID, "type": "message", "status": "completed", "content": []any{map[string]any{"type": "output_text", "annotations": []any{}, "logprobs": []any{}, "text": outputText}}, "phase": "final_answer", "role": "assistant"})
	}
	return out
}

func asString(v any) string {
	s, _ := v.(string)
	return s
}

// relayResponsesStream forwards Responses API SSE as-is.
func relayResponsesStream(w http.ResponseWriter, upResp *http.Response) {
	flusher, ok := w.(http.Flusher)
	if !ok {
		httpError(w, http.StatusInternalServerError, "streaming not supported")
		return
	}

	// Copy response headers
	w.Header().Set("Content-Type", "text/event-stream")
	w.Header().Set("Cache-Control", "no-cache")
	w.Header().Set("Connection", "keep-alive")

	// Forward x-codex-turn-state from upstream response
	if v := upResp.Header.Get("x-codex-turn-state"); v != "" {
		w.Header().Set("x-codex-turn-state", v)
	}

	w.WriteHeader(http.StatusOK)

	// Passthrough SSE — no translation needed
	ReadSSE(upResp.Body, func(ev SSEEvent) error {
		if ev.Event != "" {
			writeSSEMessage(w, ev.Event, ev.Data)
		} else {
			writeSSEMessage(w, "", ev.Data)
		}
		flusher.Flush()
		return nil
	})
}

// relayResponsesNonStream forwards the JSON response as-is.
func relayResponsesNonStream(w http.ResponseWriter, upResp *http.Response) {
	body, err := io.ReadAll(upResp.Body)
	if err != nil {
		httpError(w, http.StatusBadGateway, "read upstream: "+err.Error())
		return
	}

	// Forward response headers
	w.Header().Set("Content-Type", "application/json")
	if v := upResp.Header.Get("x-codex-turn-state"); v != "" {
		w.Header().Set("x-codex-turn-state", v)
	}
	w.Write(body)
}

func relayResponsesCollectedNonStream(w http.ResponseWriter, upResp *http.Response) {
	body, err := collectResponsesCompletedJSON(upResp.Body)
	if err != nil {
		httpError(w, http.StatusBadGateway, err.Error())
		return
	}
	w.Header().Set("Content-Type", "application/json")
	if v := upResp.Header.Get("x-codex-turn-state"); v != "" {
		w.Header().Set("x-codex-turn-state", v)
	}
	w.Write(body)
}

func collectResponsesCompletedJSON(r io.Reader) ([]byte, error) {
	var finalResponse json.RawMessage
	err := ReadSSE(r, func(ev SSEEvent) error {
		var obj struct {
			Type     string          `json:"type"`
			Response json.RawMessage `json:"response"`
		}
		if json.Unmarshal([]byte(ev.Data), &obj) != nil {
			return nil
		}
		if obj.Type == "response.completed" || obj.Type == "response.done" {
			finalResponse = append(finalResponse[:0], obj.Response...)
		}
		return nil
	})
	if err != nil {
		return nil, err
	}
	if len(finalResponse) == 0 {
		return nil, fmt.Errorf("missing response.completed event")
	}
	return finalResponse, nil
}
```

## File: `internal/httpapi/request_rewrite.go`
```go
package httpapi

import "encoding/json"

func prepareResponsesOAuthBody(body []byte, forceStream bool) []byte {
	var req map[string]any
	if err := json.Unmarshal(body, &req); err != nil {
		return body
	}
	if _, ok := req["instructions"]; !ok {
		req["instructions"] = "You are a helpful assistant."
	}
	req["store"] = false
	if forceStream {
		req["stream"] = true
	}
	if _, ok := req["tool_choice"]; !ok {
		if tools, ok := req["tools"].([]any); ok && len(tools) > 0 {
			req["tool_choice"] = "auto"
			req["parallel_tool_calls"] = true
		}
	}
	input, ok := req["input"]
	if ok && input != nil {
		switch v := input.(type) {
		case string:
			req["input"] = []map[string]any{{
				"role": "user",
				"content": []map[string]any{{
					"type": "input_text",
					"text": v,
				}},
			}}
		case map[string]any:
			if _, hasRole := v["role"]; hasRole {
				req["input"] = []any{v}
			} else if text, _ := v["text"].(string); text != "" {
				req["input"] = []map[string]any{{
					"role": "user",
					"content": []map[string]any{{
						"type": "input_text",
						"text": text,
					}},
				}}
			}
		}
	}
	out, err := json.Marshal(req)
	if err != nil {
		return body
	}
	return out
}
```

## File: `internal/httpx/httpclient.go`
```go
package httpx

import (
	"net"
	"net/http"
	"time"
)

// Shared HTTP clients with connection pooling.
// Reuses TCP connections + TLS sessions across requests → saves ~100-200ms/req.

var (
	// For streaming requests (long timeout, keep-alive)
	StreamClient = &http.Client{
		Timeout: 10 * time.Minute,
		Transport: &http.Transport{
			MaxIdleConns:        20,
			MaxIdleConnsPerHost: 10,
			IdleConnTimeout:     120 * time.Second,
			TLSHandshakeTimeout: 10 * time.Second,
			DialContext: (&net.Dialer{
				Timeout:   10 * time.Second,
				KeepAlive: 30 * time.Second,
			}).DialContext,
			DisableCompression: true, // SSE should not be compressed
			ForceAttemptHTTP2:  true,
		},
	}

	// For non-streaming requests (shorter timeout, gzip ok)
	APIClient = &http.Client{
		Timeout: 5 * time.Minute,
		Transport: &http.Transport{
			MaxIdleConns:        20,
			MaxIdleConnsPerHost: 10,
			IdleConnTimeout:     120 * time.Second,
			TLSHandshakeTimeout: 10 * time.Second,
			DialContext: (&net.Dialer{
				Timeout:   10 * time.Second,
				KeepAlive: 30 * time.Second,
			}).DialContext,
			ForceAttemptHTTP2: true,
		},
	}
)
```

## File: `internal/protocol/adapter_claude_chat.go`
```go
package protocol

import (
	"encoding/json"
	"fmt"
	"strings"
	"time"
)

type ClaudeChatAdapter struct {
	chatID   string
	model    string
	created  int64
	isOAuth  bool
	toolCall *claudeToolCallState
}

type claudeToolCallState struct {
	id   string
	name string
	args string
	idx  int
}

func NewClaudeChatAdapter(model string, isOAuth bool) *ClaudeChatAdapter {
	return &ClaudeChatAdapter{
		chatID:  fmt.Sprintf("chatcmpl-%d", time.Now().UnixNano()),
		model:   model,
		created: time.Now().Unix(),
		isOAuth: isOAuth,
	}
}

func (a *ClaudeChatAdapter) Consume(eventType, data string) []ChatStreamChunk {
	var event struct {
		Type string `json:"type"`
	}
	if err := json.Unmarshal([]byte(data), &event); err != nil {
		return nil
	}
	if event.Type == "" {
		event.Type = eventType
	}

	switch event.Type {
	case "message_start":
		return []ChatStreamChunk{a.chunk(&ChatMessage{Role: "assistant"}, nil)}

	case "content_block_start":
		var cbs ClaudeContentBlockStart
		if json.Unmarshal([]byte(data), &cbs) != nil {
			return nil
		}
		if cbs.ContentBlock.Type != "tool_use" {
			return nil
		}
		name := cbs.ContentBlock.Name
		if a.isOAuth {
			name = strings.TrimPrefix(name, "mcp_")
		}
		a.toolCall = &claudeToolCallState{id: cbs.ContentBlock.ID, name: name, idx: 0}
		return []ChatStreamChunk{a.chunk(&ChatMessage{ToolCalls: []ChatToolCall{{
			Index: 0,
			ID:    a.toolCall.id,
			Type:  "function",
			Function: ChatFunctionCall{
				Name: name,
			},
		}}}, nil)}

	case "content_block_delta":
		var cbd ClaudeContentBlockDelta
		if json.Unmarshal([]byte(data), &cbd) != nil {
			return nil
		}
		switch cbd.Delta.Type {
		case "text_delta":
			if cbd.Delta.Text == "" {
				return nil
			}
			return []ChatStreamChunk{a.chunk(&ChatMessage{Content: cbd.Delta.Text}, nil)}
		case "thinking_delta":
			if cbd.Delta.Thinking == "" {
				return nil
			}
			return []ChatStreamChunk{a.chunk(&ChatMessage{ReasoningContent: cbd.Delta.Thinking}, nil)}
		case "input_json_delta":
			if a.toolCall == nil || cbd.Delta.PartialJSON == "" {
				return nil
			}
			a.toolCall.args += cbd.Delta.PartialJSON
		}
		return nil

	case "content_block_stop":
		if a.toolCall == nil || a.toolCall.args == "" {
			a.toolCall = nil
			return nil
		}
		chunk := a.chunk(&ChatMessage{ToolCalls: []ChatToolCall{{
			Index: 0,
			ID:    a.toolCall.id,
			Type:  "function",
			Function: ChatFunctionCall{
				Name:      a.toolCall.name,
				Arguments: a.toolCall.args,
			},
		}}}, nil)
		a.toolCall = nil
		return []ChatStreamChunk{chunk}

	case "message_delta":
		var md ClaudeMessageDelta
		if json.Unmarshal([]byte(data), &md) != nil {
			return nil
		}
		finish := ClaudeStopToChat(md.Delta.StopReason)
		chunk := a.chunk(&ChatMessage{}, &finish)
		if md.Usage != nil {
			chunk.Usage = &ChatUsage{
				PromptTokens:     md.Usage.InputTokens,
				CompletionTokens: md.Usage.OutputTokens,
				TotalTokens:      md.Usage.InputTokens + md.Usage.OutputTokens,
			}
		}
		return []ChatStreamChunk{chunk}
	}

	return nil
}

func (a *ClaudeChatAdapter) chunk(delta *ChatMessage, finish *string) ChatStreamChunk {
	return ChatStreamChunk{
		ID:      a.chatID,
		Object:  "chat.completion.chunk",
		Created: a.created,
		Model:   a.model,
		Choices: []ChatChoice{{Index: 0, Delta: delta, FinishReason: finish}},
	}
}
```

## File: `internal/protocol/adapter_responses.go`
```go
package protocol

import (
	"encoding/json"
	"fmt"
	"strings"
	"time"
)

// Chat Completions ↔ Responses API translation
// Based on ZipZhu/ResponseBridge and huggingface/responses.js patterns

// ChatToResponsesRequest translates a Chat Completions request to Responses API format.
func ChatToResponsesRequest(body []byte) ([]byte, error) {
	var chat map[string]any
	if err := json.Unmarshal(body, &chat); err != nil {
		return nil, err
	}

	resp := map[string]any{
		"model": chat["model"],
		"store": false,
	}

	// Convert messages → input + instructions
	messages, _ := chat["messages"].([]any)
	var input []any
	var instructions []string

	for _, m := range messages {
		msg, ok := m.(map[string]any)
		if !ok {
			continue
		}
		role, _ := msg["role"].(string)
		content := msg["content"]

		switch role {
		case "system", "developer":
			// System messages become instructions
			if text := contentToString(content); text != "" {
				instructions = append(instructions, text)
			}

		case "user":
			parts := contentToParts(content, "input_text")
			input = append(input, map[string]any{
				"role":    "user",
				"content": parts,
			})

		case "assistant":
			// Assistant messages with tool_calls
			toolCalls, _ := msg["tool_calls"].([]any)
			if len(toolCalls) > 0 {
				for _, tc := range toolCalls {
					tcMap, _ := tc.(map[string]any)
					fn, _ := tcMap["function"].(map[string]any)
					name, _ := fn["name"].(string)
					args, _ := fn["arguments"].(string)
					callID, _ := tcMap["id"].(string)
					input = append(input, map[string]any{
						"type":      "function_call",
						"name":      name,
						"arguments": args,
						"call_id":   callID,
					})
				}
			}
			// Text content
			text := contentToString(content)
			if text != "" {
				parts := contentToParts(content, "output_text")
				input = append(input, map[string]any{
					"role":    "assistant",
					"content": parts,
				})
			}

		case "tool":
			callID, _ := msg["tool_call_id"].(string)
			text := contentToString(content)
			input = append(input, map[string]any{
				"type":    "function_call_output",
				"call_id": callID,
				"output":  text,
			})
		}
	}

	resp["input"] = input

	if len(instructions) > 0 {
		resp["instructions"] = strings.Join(instructions, "\n\n")
	} else {
		resp["instructions"] = "You are a helpful assistant."
	}

	// ChatGPT backend requires stream=true always
	resp["stream"] = true

	// Passthrough common params (skip max_tokens — not supported by ChatGPT backend)
	for _, key := range []string{"temperature", "top_p"} {
		if v, ok := chat[key]; ok {
			resp[key] = v
		}
	}

	// Tools — Chat Completions tool shape differs from Responses API
	if tools, ok := chat["tools"].([]any); ok && len(tools) > 0 {
		resp["tools"] = chatToolsToResponsesTools(tools)
		resp["tool_choice"] = translateResponsesToolChoice(chat["tool_choice"])
		resp["parallel_tool_calls"] = true
	}

	// Service tier — only set if explicitly passed
	if tier, ok := chat["service_tier"]; ok {
		resp["service_tier"] = tier
	}

	// Reasoning — passthrough if present, or set defaults for capable models
	if reasoning, ok := chat["reasoning"]; ok {
		if rm, ok := reasoning.(map[string]any); ok {
			clone := map[string]any{}
			for k, v := range rm {
				clone[k] = v
			}
			if _, ok := clone["summary"]; !ok {
				clone["summary"] = "detailed"
			}
			resp["reasoning"] = clone
		} else {
			resp["reasoning"] = reasoning
		}
	} else if reasoning, ok := chat["reasoning_effort"]; ok {
		// OpenAI SDK sends reasoning_effort as string
		resp["reasoning"] = map[string]any{"effort": reasoning, "summary": "detailed"}
	}

	// Text verbosity — low for concise responses by default
	if text, ok := chat["text"]; ok {
		resp["text"] = text
	}
	if responseFormat, ok := chat["response_format"]; ok {
		applyChatResponseFormat(resp, responseFormat)
	}

	// Prompt cache key — conversation-level stable ID
	// Codex uses conversation_id (UUID per session) so server caches the full prefix
	// For Chat Completions clients: caller can pass prompt_cache_key explicitly,
	// otherwise not set (server won't cache — stateless by design)
	if cacheKey, ok := chat["prompt_cache_key"]; ok {
		resp["prompt_cache_key"] = cacheKey
	}

	// Previous response ID — chain responses for incremental context
	if prevID, ok := chat["previous_response_id"]; ok {
		resp["previous_response_id"] = prevID
	}

	return json.Marshal(resp)
}

func applyChatResponseFormat(resp map[string]any, responseFormat any) {
	rf, ok := responseFormat.(map[string]any)
	if !ok || rf == nil {
		return
	}
	rfType, _ := rf["type"].(string)
	if rfType == "" || rfType == "text" {
		return
	}
	text, _ := resp["text"].(map[string]any)
	if text == nil {
		text = map[string]any{}
	}
	switch rfType {
	case "json_object":
		text["format"] = map[string]any{"type": "json_object"}
	case "json_schema":
		js, _ := rf["json_schema"].(map[string]any)
		if js == nil {
			return
		}
		format := map[string]any{"type": "json_schema"}
		for _, key := range []string{"name", "schema", "description", "strict"} {
			if v, ok := js[key]; ok {
				format[key] = v
			}
		}
		if _, ok := format["schema"]; !ok {
			return
		}
		text["format"] = format
	default:
		return
	}
	resp["text"] = text
}

func chatToolsToResponsesTools(tools []any) []map[string]any {
	var out []map[string]any
	for _, item := range tools {
		tool, _ := item.(map[string]any)
		if tool == nil {
			continue
		}
		if toolType, _ := tool["type"].(string); toolType != "function" {
			continue
		}
		fn, _ := tool["function"].(map[string]any)
		if fn == nil {
			continue
		}
		name, _ := fn["name"].(string)
		if name == "" {
			continue
		}
		respTool := map[string]any{
			"type": "function",
			"name": name,
		}
		if desc, _ := fn["description"].(string); desc != "" {
			respTool["description"] = desc
		}
		if params, ok := fn["parameters"]; ok {
			respTool["parameters"] = params
		}
		out = append(out, respTool)
	}
	return out
}

func translateResponsesToolChoice(choice any) any {
	if choice == nil {
		return "auto"
	}
	switch v := choice.(type) {
	case string:
		return v
	case map[string]any:
		if toolType, _ := v["type"].(string); toolType == "function" {
			if fn, ok := v["function"].(map[string]any); ok {
				if name, _ := fn["name"].(string); name != "" {
					return map[string]any{"type": "function", "name": name}
				}
			}
		}
	}
	return "auto"
}

// contentToParts converts message content to Responses API content parts.
func contentToParts(content any, textType string) []map[string]any {
	switch v := content.(type) {
	case string:
		if v == "" {
			return []map[string]any{}
		}
		return []map[string]any{{"type": textType, "text": v}}
	case []any:
		var parts []map[string]any
		for _, item := range v {
			m, ok := item.(map[string]any)
			if !ok {
				continue
			}
			t, _ := m["type"].(string)
			switch t {
			case "text":
				text, _ := m["text"].(string)
				parts = append(parts, map[string]any{"type": textType, "text": text})
			case "image_url":
				// Pass through image URLs
				parts = append(parts, m)
			}
		}
		return parts
	default:
		return []map[string]any{}
	}
}

type ResponsesToolState struct {
	ID    string
	Name  string
	Type  string
	Index int
}

type ResponsesToChatState struct {
	IsFirst bool
	Tools   map[string]ResponsesToolState
}

func NewResponsesToChatState() *ResponsesToChatState {
	return &ResponsesToChatState{IsFirst: true, Tools: map[string]ResponsesToolState{}}
}

// ResponsesSSEToChatSSE translates a single Responses API SSE event to Chat Completions SSE chunk.
// Returns empty string if the event should be skipped.
func ResponsesSSEToChatSSE(eventType, data string, model string, chatID string, created int64, state *ResponsesToChatState) string {
	var obj map[string]any
	if err := json.Unmarshal([]byte(data), &obj); err != nil {
		return ""
	}

	typ, _ := obj["type"].(string)
	if typ == "" {
		typ = eventType
	}

	switch {
	case typ == "response.reasoning_summary_text.delta":
		delta, _ := obj["delta"].(string)
		if delta == "" {
			return ""
		}
		chunk := buildChatChunk(chatID, model, created, state.IsFirst, "", delta, nil, nil)
		state.IsFirst = false
		b, _ := json.Marshal(chunk)
		return string(b)

	case typ == "response.output_text.delta":
		delta, _ := obj["delta"].(string)
		if delta == "" {
			return ""
		}
		chunk := buildChatChunk(chatID, model, created, state.IsFirst, delta, "", nil, nil)
		state.IsFirst = false
		b, _ := json.Marshal(chunk)
		return string(b)

	case typ == "response.output_item.added":
		item, _ := obj["item"].(map[string]any)
		if item != nil && item["type"] == "function_call" {
			id, _ := item["id"].(string)
			name, _ := item["name"].(string)
			if id != "" {
				state.Tools[id] = ResponsesToolState{ID: id, Name: name, Type: "function", Index: 0}
				chunk := buildChatChunk(chatID, model, created, state.IsFirst, "", "", []ChatToolCall{{
					Index: 0,
					ID:    id,
					Type:  "function",
					Function: ChatFunctionCall{
						Name: name,
					},
				}}, nil)
				state.IsFirst = false
				b, _ := json.Marshal(chunk)
				return string(b)
			}
		}
		if state.IsFirst {
			chunk := buildChatChunk(chatID, model, created, true, "", "", nil, nil)
			state.IsFirst = false
			b, _ := json.Marshal(chunk)
			return string(b)
		}

	case typ == "response.function_call_arguments.delta":
		delta, _ := obj["delta"].(string)
		callID, _ := obj["item_id"].(string)
		if callID == "" {
			callID, _ = obj["call_id"].(string)
		}
		tool, ok := state.Tools[callID]
		var tc *ChatToolCall
		if ok {
			tc = &ChatToolCall{
				Index: tool.Index,
				ID:    tool.ID,
				Type:  tool.Type,
				Function: ChatFunctionCall{
					Name:      tool.Name,
					Arguments: delta,
				},
			}
		} else if delta != "" {
			tc = &ChatToolCall{Index: 0, Function: ChatFunctionCall{Arguments: delta}}
		}
		if tc != nil {
			chunk := buildChatChunk(chatID, model, created, state.IsFirst, "", "", []ChatToolCall{*tc}, nil)
			state.IsFirst = false
			b, _ := json.Marshal(chunk)
			return string(b)
		}

	case typ == "response.completed" || typ == "response.done":
		finish := "stop"
		// Check if it was a tool call
		if resp, ok := obj["response"].(map[string]any); ok {
			if output, ok := resp["output"].([]any); ok {
				for _, item := range output {
					if itemMap, ok := item.(map[string]any); ok {
						if itemMap["type"] == "function_call" {
							finish = "tool_calls"
							break
						}
					}
				}
			}
		}
		chunk := buildChatChunk(chatID, model, created, false, "", "", nil, &finish)
		// Add usage if available
		if resp, ok := obj["response"].(map[string]any); ok {
			if usage, ok := resp["usage"].(map[string]any); ok {
				inputTokens, _ := usage["input_tokens"].(float64)
				outputTokens, _ := usage["output_tokens"].(float64)
				chunk["usage"] = map[string]any{
					"prompt_tokens":     int(inputTokens),
					"completion_tokens": int(outputTokens),
					"total_tokens":      int(inputTokens + outputTokens),
				}
			}
		}
		b, _ := json.Marshal(chunk)
		return string(b)

	}

	return ""
}

// ResponsesNonStreamToChat translates a non-stream Responses API response to Chat Completions.
func ResponsesNonStreamToChat(body []byte, model string) ([]byte, error) {
	var resp map[string]any
	if err := json.Unmarshal(body, &resp); err != nil {
		return nil, err
	}

	var text string
	var reasoning string
	var toolCalls []ChatToolCall
	finishReason := "stop"

	output, _ := resp["output"].([]any)
	for _, item := range output {
		block, _ := item.(map[string]any)
		if block == nil {
			continue
		}

		switch block["type"] {
		case "reasoning":
			summary, _ := block["summary"].([]any)
			for _, part := range summary {
				p, _ := part.(map[string]any)
				if p == nil {
					continue
				}
				if s, _ := p["text"].(string); s != "" {
					reasoning += s
				}
			}
		case "message":
			content, _ := block["content"].([]any)
			for _, part := range content {
				p, _ := part.(map[string]any)
				if p == nil {
					continue
				}
				if t, _ := p["type"].(string); t == "output_text" {
					if s, _ := p["text"].(string); s != "" {
						text += s
					}
				}
			}
		case "function_call":
			name, _ := block["name"].(string)
			args, _ := block["arguments"].(string)
			callID, _ := block["call_id"].(string)
			toolCalls = append(toolCalls, ChatToolCall{
				ID:   callID,
				Type: "function",
				Function: ChatFunctionCall{
					Name:      name,
					Arguments: args,
				},
			})
			finishReason = "tool_calls"
		}
	}

	msg := ChatMessage{Role: "assistant"}
	if reasoning != "" {
		msg.ReasoningContent = reasoning
	}
	if text != "" {
		msg.Content = text
	}
	if len(toolCalls) > 0 {
		msg.ToolCalls = toolCalls
	}

	rid, _ := resp["id"].(string)
	usage := resp["usage"]

	chatResp := map[string]any{
		"id":      fmt.Sprintf("chatcmpl-%s", rid),
		"object":  "chat.completion",
		"created": time.Now().Unix(),
		"model":   model,
		"choices": []map[string]any{{
			"index":         0,
			"message":       msg,
			"finish_reason": finishReason,
		}},
	}

	if u, ok := usage.(map[string]any); ok {
		inputTokens, _ := u["input_tokens"].(float64)
		outputTokens, _ := u["output_tokens"].(float64)
		chatResp["usage"] = map[string]any{
			"prompt_tokens":     int(inputTokens),
			"completion_tokens": int(outputTokens),
			"total_tokens":      int(inputTokens + outputTokens),
		}
	}

	return json.Marshal(chatResp)
}

func buildChatChunk(id, model string, created int64, withRole bool, content string, reasoningContent string, toolCalls []ChatToolCall, finishReason *string) map[string]any {
	delta := map[string]any{}
	if withRole {
		delta["role"] = "assistant"
	}
	if content != "" {
		delta["content"] = content
	}
	if reasoningContent != "" {
		delta["reasoning_content"] = reasoningContent
	}
	if len(toolCalls) > 0 {
		delta["tool_calls"] = toolCalls
	}

	choice := map[string]any{
		"index":         0,
		"delta":         delta,
		"finish_reason": finishReason,
	}

	return map[string]any{
		"id":      id,
		"object":  "chat.completion.chunk",
		"created": created,
		"model":   model,
		"choices": []any{choice},
	}
}
```

## File: `internal/protocol/sse.go`
```go
package protocol

import (
	"bufio"
	"encoding/json"
	"io"
	"net/http"
	"strings"
)

// SSE helpers for reading upstream and writing downstream

// SSEWriter wraps an http.ResponseWriter for streaming SSE events.
type SSEWriter struct {
	w       http.ResponseWriter
	flusher http.Flusher
}

func NewSSEWriter(w http.ResponseWriter) (*SSEWriter, bool) {
	flusher, ok := w.(http.Flusher)
	if !ok {
		return nil, false
	}
	w.Header().Set("Content-Type", "text/event-stream")
	w.Header().Set("Cache-Control", "no-cache")
	w.Header().Set("Connection", "keep-alive")
	w.Header().Set("X-Accel-Buffering", "no")
	w.WriteHeader(http.StatusOK)
	return &SSEWriter{w: w, flusher: flusher}, true
}

func (s *SSEWriter) WriteData(data string) {
	s.writeDataBytes([]byte(data))
}

func (s *SSEWriter) WriteJSON(v any) error {
	b, err := json.Marshal(v)
	if err != nil {
		return err
	}
	s.WriteRawJSON(b)
	return nil
}

func (s *SSEWriter) WriteRawJSON(data []byte) {
	s.writeDataBytes(data)
}

func (s *SSEWriter) WriteDone() {
	_, _ = s.w.Write([]byte("data: [DONE]\n\n"))
	s.flusher.Flush()
}

func (s *SSEWriter) WriteEvent(event, data string) {
	_, _ = s.w.Write([]byte("event: "))
	_, _ = s.w.Write([]byte(event))
	_, _ = s.w.Write([]byte("\ndata: "))
	_, _ = s.w.Write([]byte(data))
	_, _ = s.w.Write([]byte("\n\n"))
	s.flusher.Flush()
}

func (s *SSEWriter) writeDataBytes(data []byte) {
	_, _ = s.w.Write([]byte("data: "))
	_, _ = s.w.Write(data)
	_, _ = s.w.Write([]byte("\n\n"))
	s.flusher.Flush()
}

// SSEReader reads SSE events from a stream.
// It yields (event_type, data) pairs.
type SSEEvent struct {
	Event string // event type (empty if not specified)
	Data  string // data payload
}

func ReadSSE(r io.Reader, fn func(SSEEvent) error) error {
	scanner := bufio.NewScanner(r)
	scanner.Buffer(make([]byte, 0, 64*1024), 1024*1024) // 1MB max line

	var event string
	var data strings.Builder

	for scanner.Scan() {
		line := scanner.Text()

		if line == "" {
			// Empty line = event boundary
			if data.Len() > 0 {
				d := data.String()
				if strings.HasSuffix(d, "\n") {
					d = d[:len(d)-1]
				}
				if err := fn(SSEEvent{Event: event, Data: d}); err != nil {
					return err
				}
				data.Reset()
				event = ""
			}
			continue
		}

		if strings.HasPrefix(line, "event: ") {
			event = line[7:]
		} else if strings.HasPrefix(line, "data: ") {
			data.WriteString(line[6:])
			data.WriteByte('\n')
		} else if line == "data:" {
			data.WriteByte('\n')
		}
		// Ignore comments (lines starting with :) and unknown fields
	}

	return scanner.Err()
}
```

## File: `internal/protocol/translate.go`
```go
package protocol

import (
	"encoding/json"
	"fmt"
	"regexp"
	"strings"
	"time"
)

// Chat ↔ Claude translation

const defaultMaxTokens = 8192

// ChatToClaudeRequest translates an OpenAI Chat Completions request to Claude Messages API.
func ChatToClaudeRequest(chat *ChatRequest) (*ClaudeRequest, error) {
	cr := &ClaudeRequest{
		Model:     chat.Model,
		Stream:    chat.Stream,
		MaxTokens: defaultMaxTokens,
	}

	if chat.MaxTokens != nil {
		cr.MaxTokens = *chat.MaxTokens
	}
	cr.Temperature = chat.Temperature
	cr.TopP = chat.TopP
	cr.Thinking = normalizeClaudeThinking(chat.Thinking, chat.ReasoningEffort)
	adjustClaudeMaxTokens(cr, chat.Thinking, chat.ReasoningEffort)

	// Extract system messages
	var systemParts []string
	var messages []ClaudeMessage

	for _, msg := range chat.Messages {
		switch msg.Role {
		case "system":
			text := contentToString(msg.Content)
			if text != "" {
				systemParts = append(systemParts, text)
			}

		case "user":
			cm, err := chatMsgToClaudeMsg(msg)
			if err != nil {
				return nil, err
			}
			messages = append(messages, cm)

		case "assistant":
			cm, err := assistantToClaudeMsg(msg)
			if err != nil {
				return nil, err
			}
			messages = append(messages, cm)

		case "tool":
			cm := toolResultToClaudeMsg(msg)
			messages = append(messages, cm)
		}
	}

	if len(systemParts) > 0 {
		cr.System = strings.Join(systemParts, "\n\n")
	}

	// Merge consecutive same-role messages (Claude requires alternating roles)
	cr.Messages = mergeConsecutiveMessages(messages)

	// Translate tools
	for _, t := range chat.Tools {
		cr.Tools = append(cr.Tools, ClaudeTool{
			Name:        t.Function.Name,
			Description: t.Function.Description,
			InputSchema: t.Function.Parameters,
		})
	}

	// Translate tool_choice
	if chat.ToolChoice != nil {
		cr.ToolChoice = translateToolChoice(chat.ToolChoice)
	}

	return cr, nil
}

func adjustClaudeMaxTokens(cr *ClaudeRequest, rawThinking any, reasoningEffort string) {
	budget := extractClaudeThinkingBudget(cr.Thinking)
	if budget <= 0 {
		budget = extractClaudeThinkingBudget(rawThinking)
	}
	if budget <= 0 {
		switch strings.ToLower(strings.TrimSpace(reasoningEffort)) {
		case "low":
			budget = 4096
		case "medium":
			budget = 16000
		case "high":
			budget = 32000
		}
	}
	if budget <= 0 {
		return
	}
	if cr.MaxTokens <= budget {
		cr.MaxTokens = budget + 1024
	}
}

func extractClaudeThinkingBudget(thinking any) int {
	m, ok := thinking.(map[string]any)
	if !ok {
		return 0
	}
	if budget, ok := asInt(m["budget_tokens"]); ok && budget > 0 {
		return budget
	}
	if budget, ok := asInt(m["budgetTokens"]); ok && budget > 0 {
		return budget
	}
	if enabled, ok := m["enabled"].(map[string]any); ok {
		if budget, ok := asInt(enabled["budget_tokens"]); ok && budget > 0 {
			return budget
		}
		if budget, ok := asInt(enabled["budgetTokens"]); ok && budget > 0 {
			return budget
		}
	}
	return 0
}

func normalizeClaudeThinking(thinking any, reasoningEffort string) any {
	if m, ok := thinking.(map[string]any); ok {
		clone := map[string]any{}
		for k, v := range m {
			clone[k] = v
		}
		if enabled, ok := clone["enabled"].(map[string]any); ok {
			if _, ok := clone["type"]; !ok {
				clone["type"] = "enabled"
			}
			if _, ok := clone["budget_tokens"]; !ok {
				if v, ok := enabled["budget_tokens"]; ok {
					clone["budget_tokens"] = v
				} else if v, ok := enabled["budgetTokens"]; ok {
					clone["budget_tokens"] = v
				}
			}
			delete(clone, "enabled")
		}
		if _, ok := clone["budget_tokens"]; !ok {
			if v, ok := clone["budgetTokens"]; ok {
				clone["budget_tokens"] = v
				delete(clone, "budgetTokens")
			}
		}
		if _, ok := clone["type"]; !ok && clone["budget_tokens"] != nil {
			clone["type"] = "enabled"
		}
		if clone["budget_tokens"] != nil || clone["type"] != nil {
			return clone
		}
	}

	switch strings.ToLower(strings.TrimSpace(reasoningEffort)) {
	case "low":
		return map[string]any{"type": "enabled", "budget_tokens": 4096}
	case "medium":
		return map[string]any{"type": "enabled", "budget_tokens": 16000}
	case "high":
		return map[string]any{"type": "enabled", "budget_tokens": 32000}
	default:
		return thinking
	}
}

func asInt(v any) (int, bool) {
	switch x := v.(type) {
	case int:
		return x, true
	case int64:
		return int(x), true
	case float64:
		return int(x), true
	case json.Number:
		i, err := x.Int64()
		if err == nil {
			return int(i), true
		}
	case string:
		if i, err := json.Number(x).Int64(); err == nil {
			return int(i), true
		}
	}
	return 0, false
}

func chatMsgToClaudeMsg(msg ChatMessage) (ClaudeMessage, error) {
	content, err := toClaudeContent(msg.Content)
	if err != nil {
		return ClaudeMessage{}, err
	}
	return ClaudeMessage{Role: "user", Content: content}, nil
}

func assistantToClaudeMsg(msg ChatMessage) (ClaudeMessage, error) {
	var parts []ClaudeContent

	// Text content
	text := contentToString(msg.Content)
	if text != "" {
		parts = append(parts, ClaudeContent{Type: "text", Text: text})
	}

	// Tool calls
	for _, tc := range msg.ToolCalls {
		parts = append(parts, ClaudeContent{
			Type:  "tool_use",
			ID:    sanitizeToolCallID(tc.ID),
			Name:  tc.Function.Name,
			Input: json.RawMessage(tc.Function.Arguments),
		})
	}

	if len(parts) == 0 {
		// Claude rejects empty assistant messages
		parts = append(parts, ClaudeContent{Type: "text", Text: "."})
	}

	return ClaudeMessage{Role: "assistant", Content: parts}, nil
}

func toolResultToClaudeMsg(msg ChatMessage) ClaudeMessage {
	content := contentToString(msg.Content)
	return ClaudeMessage{
		Role: "user",
		Content: []ClaudeContent{{
			Type:      "tool_result",
			ToolUseID: sanitizeToolCallID(msg.ToolCallID),
			Content:   content,
		}},
	}
}

// --- Response translation ---

// ClaudeToChat translates a non-streaming Claude response to Chat Completions format.
func ClaudeToChat(cr *ClaudeResponse, model string) *ChatResponse {
	msg := &ChatMessage{Role: "assistant"}

	var textParts []string
	var toolCalls []ChatToolCall

	for _, c := range cr.Content {
		switch c.Type {
		case "text":
			textParts = append(textParts, c.Text)
		case "tool_use":
			toolCalls = append(toolCalls, ChatToolCall{
				ID:   c.ID,
				Type: "function",
				Function: ChatFunctionCall{
					Name:      c.Name,
					Arguments: string(c.Input),
				},
			})
		}
	}

	if len(textParts) > 0 {
		text := strings.Join(textParts, "")
		msg.Content = text
	}
	if len(toolCalls) > 0 {
		msg.ToolCalls = toolCalls
	}

	finishReason := claudeStopToChat(cr.StopReason)

	return &ChatResponse{
		ID:      "chatcmpl-" + cr.ID,
		Object:  "chat.completion",
		Created: time.Now().Unix(),
		Model:   model,
		Choices: []ChatChoice{{
			Index:        0,
			Message:      msg,
			FinishReason: &finishReason,
		}},
		Usage: &ChatUsage{
			PromptTokens:     cr.Usage.InputTokens + cr.Usage.CacheReadInputTokens + cr.Usage.CacheCreationInputTokens,
			CompletionTokens: cr.Usage.OutputTokens,
			TotalTokens:      cr.Usage.InputTokens + cr.Usage.CacheReadInputTokens + cr.Usage.CacheCreationInputTokens + cr.Usage.OutputTokens,
			PromptTokensDetails: func() *PromptTokensDetails {
				if cr.Usage.CacheReadInputTokens > 0 {
					return &PromptTokensDetails{CachedTokens: cr.Usage.CacheReadInputTokens}
				}
				return nil
			}(),
		},
	}
}

func claudeStopToChat(reason *string) string {
	if reason == nil {
		return "stop"
	}
	switch *reason {
	case "end_turn", "stop_sequence":
		return "stop"
	case "max_tokens":
		return "length"
	case "tool_use":
		return "tool_calls"
	default:
		return "stop"
	}
}

func ClaudeStopToChat(reason *string) string {
	return claudeStopToChat(reason)
}

// --- Helpers ---

func contentToString(content any) string {
	switch v := content.(type) {
	case string:
		return v
	case []any:
		var parts []string
		for _, item := range v {
			if m, ok := item.(map[string]any); ok {
				if t, _ := m["type"].(string); t == "text" {
					if text, _ := m["text"].(string); text != "" {
						parts = append(parts, text)
					}
				}
			}
		}
		return strings.Join(parts, "")
	default:
		if b, err := json.Marshal(content); err == nil {
			return string(b)
		}
		return fmt.Sprintf("%v", content)
	}
}

func toClaudeContent(content any) (any, error) {
	switch v := content.(type) {
	case string:
		if v == "" {
			return []ClaudeContent{{Type: "text", Text: "."}}, nil
		}
		return v, nil
	case []any:
		var parts []ClaudeContent
		for _, item := range v {
			m, ok := item.(map[string]any)
			if !ok {
				continue
			}
			switch m["type"] {
			case "text":
				text, _ := m["text"].(string)
				if text != "" {
					parts = append(parts, ClaudeContent{Type: "text", Text: text})
				}
			case "image_url":
				if iu, ok := m["image_url"].(map[string]any); ok {
					url, _ := iu["url"].(string)
					if strings.HasPrefix(url, "data:") {
						// data:image/png;base64,xxx
						mt, data := parseDataURI(url)
						parts = append(parts, ClaudeContent{
							Type: "image",
							Source: &ClaudeImageSource{
								Type:      "base64",
								MediaType: mt,
								Data:      data,
							},
						})
					}
				}
			}
		}
		if len(parts) == 0 {
			return []ClaudeContent{{Type: "text", Text: "."}}, nil
		}
		return parts, nil
	default:
		return content, nil
	}
}

func parseDataURI(uri string) (mediaType, data string) {
	// data:image/png;base64,xxxx
	after, _ := strings.CutPrefix(uri, "data:")
	parts := strings.SplitN(after, ",", 2)
	if len(parts) != 2 {
		return "application/octet-stream", ""
	}
	meta := parts[0] // image/png;base64
	mt, _, _ := strings.Cut(meta, ";")
	return mt, parts[1]
}

var validToolCallID = regexp.MustCompile(`[^a-zA-Z0-9_-]`)

func sanitizeToolCallID(id string) string {
	return validToolCallID.ReplaceAllString(id, "_")
}

func mergeConsecutiveMessages(msgs []ClaudeMessage) []ClaudeMessage {
	if len(msgs) == 0 {
		return msgs
	}
	var result []ClaudeMessage
	result = append(result, msgs[0])

	for i := 1; i < len(msgs); i++ {
		last := &result[len(result)-1]
		if last.Role == msgs[i].Role {
			// Merge content arrays
			lastContent := toContentSlice(last.Content)
			newContent := toContentSlice(msgs[i].Content)
			last.Content = append(lastContent, newContent...)
		} else {
			result = append(result, msgs[i])
		}
	}
	return result
}

func toContentSlice(content any) []ClaudeContent {
	switch v := content.(type) {
	case []ClaudeContent:
		return v
	case string:
		return []ClaudeContent{{Type: "text", Text: v}}
	default:
		// Try JSON round-trip
		b, _ := json.Marshal(content)
		var parts []ClaudeContent
		if json.Unmarshal(b, &parts) == nil {
			return parts
		}
		return []ClaudeContent{{Type: "text", Text: fmt.Sprintf("%v", content)}}
	}
}

func translateToolChoice(tc any) any {
	switch v := tc.(type) {
	case string:
		switch v {
		case "none":
			return map[string]string{"type": "none"}
		case "auto":
			return map[string]string{"type": "auto"}
		case "required":
			return map[string]string{"type": "any"}
		default:
			return map[string]string{"type": "auto"}
		}
	case map[string]any:
		if fn, ok := v["function"].(map[string]any); ok {
			if name, ok := fn["name"].(string); ok {
				return map[string]any{"type": "tool", "name": name}
			}
		}
	}
	return nil
}
```

## File: `internal/protocol/types_chat.go`
```go
package protocol

import "encoding/json"

// OpenAI Chat Completions wire types — client-facing lingua franca

type ChatRequest struct {
	Model          string        `json:"model"`
	Messages       []ChatMessage `json:"messages"`
	Stream         bool          `json:"stream,omitempty"`
	MaxTokens      *int          `json:"max_tokens,omitempty"`
	Temperature    *float64      `json:"temperature,omitempty"`
	TopP           *float64      `json:"top_p,omitempty"`
	Tools          []ChatTool    `json:"tools,omitempty"`
	ToolChoice     any           `json:"tool_choice,omitempty"`
	Stop           any           `json:"stop,omitempty"`
	ResponseFormat any           `json:"response_format,omitempty"`
	Text           any           `json:"text,omitempty"`

	// Extended thinking (non-standard, passed through to Claude)
	Thinking        any    `json:"thinking,omitempty"`
	Reasoning       any    `json:"reasoning,omitempty"`
	ReasoningEffort string `json:"reasoning_effort,omitempty"`
}

type ChatMessage struct {
	Role             string         `json:"role,omitempty"`
	Content          any            `json:"content,omitempty"` // string or []ChatContentPart
	ReasoningContent string         `json:"reasoning_content,omitempty"`
	Name             *string        `json:"name,omitempty"`
	ToolCalls        []ChatToolCall `json:"tool_calls,omitempty"`
	ToolCallID       string         `json:"tool_call_id,omitempty"`
}

type ChatContentPart struct {
	Type     string        `json:"type"`
	Text     string        `json:"text,omitempty"`
	ImageURL *ChatImageURL `json:"image_url,omitempty"`
}

type ChatImageURL struct {
	URL    string `json:"url"`
	Detail string `json:"detail,omitempty"`
}

type ChatTool struct {
	Type     string       `json:"type"`
	Function ChatFunction `json:"function"`
}

type ChatFunction struct {
	Name        string          `json:"name"`
	Description string          `json:"description,omitempty"`
	Parameters  json.RawMessage `json:"parameters,omitempty"`
}

type ChatToolCall struct {
	Index    int              `json:"index"`
	ID       string           `json:"id,omitempty"`
	Type     string           `json:"type,omitempty"`
	Function ChatFunctionCall `json:"function"`
}

type ChatFunctionCall struct {
	Name      string `json:"name,omitempty"`
	Arguments string `json:"arguments,omitempty"`
}

// --- Response types ---

type ChatResponse struct {
	ID      string       `json:"id"`
	Object  string       `json:"object"`
	Created int64        `json:"created"`
	Model   string       `json:"model"`
	Choices []ChatChoice `json:"choices"`
	Usage   *ChatUsage   `json:"usage,omitempty"`
}

type ChatChoice struct {
	Index        int          `json:"index"`
	Message      *ChatMessage `json:"message,omitempty"`
	Delta        *ChatMessage `json:"delta,omitempty"`
	FinishReason *string      `json:"finish_reason"`
}

type ChatUsage struct {
	PromptTokens        int                  `json:"prompt_tokens"`
	CompletionTokens    int                  `json:"completion_tokens"`
	TotalTokens         int                  `json:"total_tokens"`
	PromptTokensDetails *PromptTokensDetails `json:"prompt_tokens_details,omitempty"`
}

type PromptTokensDetails struct {
	CachedTokens int `json:"cached_tokens,omitempty"`
}

// --- SSE chunk ---

type ChatStreamChunk struct {
	ID      string       `json:"id"`
	Object  string       `json:"object"`
	Created int64        `json:"created"`
	Model   string       `json:"model"`
	Choices []ChatChoice `json:"choices"`
	Usage   *ChatUsage   `json:"usage,omitempty"`
}
```

## File: `internal/protocol/types_claude.go`
```go
package protocol

import "encoding/json"

// Claude Messages API wire types

type ClaudeRequest struct {
	Model     string          `json:"model"`
	Messages  []ClaudeMessage `json:"messages"`
	System    any             `json:"system,omitempty"` // string or []ClaudeContent
	Stream    bool            `json:"stream,omitempty"`
	MaxTokens int             `json:"max_tokens"`
	Metadata  *ClaudeMetadata `json:"metadata,omitempty"`

	Temperature *float64     `json:"temperature,omitempty"`
	TopP        *float64     `json:"top_p,omitempty"`
	TopK        *int         `json:"top_k,omitempty"`
	Tools       []ClaudeTool `json:"tools,omitempty"`
	ToolChoice  any          `json:"tool_choice,omitempty"`
	StopSeqs    []string     `json:"stop_sequences,omitempty"`
	Thinking    any          `json:"thinking,omitempty"`
}

type ClaudeMetadata struct {
	UserID string `json:"user_id,omitempty"`
}

type ClaudeMessage struct {
	Role    string `json:"role"`
	Content any    `json:"content"` // string or []ClaudeContent
}

type ClaudeContent struct {
	Type string `json:"type"`

	// text
	Text string `json:"text,omitempty"`

	// image
	Source *ClaudeImageSource `json:"source,omitempty"`

	// tool_use
	ID    string          `json:"id,omitempty"`
	Name  string          `json:"name,omitempty"`
	Input json.RawMessage `json:"input,omitempty"`

	// tool_result
	ToolUseID string `json:"tool_use_id,omitempty"`
	Content   any    `json:"content,omitempty"` // string or []ClaudeContent (nested)
	IsError   bool   `json:"is_error,omitempty"`
}

type ClaudeImageSource struct {
	Type      string `json:"type"`       // "base64"
	MediaType string `json:"media_type"` // "image/png"
	Data      string `json:"data"`
}

type ClaudeTool struct {
	Name        string          `json:"name"`
	Description string          `json:"description,omitempty"`
	InputSchema json.RawMessage `json:"input_schema"`
}

// --- Response types ---

type ClaudeResponse struct {
	ID           string          `json:"id"`
	Type         string          `json:"type"`
	Role         string          `json:"role"`
	Content      []ClaudeContent `json:"content"`
	Model        string          `json:"model"`
	StopReason   *string         `json:"stop_reason"`
	StopSequence *string         `json:"stop_sequence"`
	Usage        ClaudeUsage     `json:"usage"`
}

type ClaudeUsage struct {
	InputTokens              int `json:"input_tokens"`
	OutputTokens             int `json:"output_tokens"`
	CacheCreationInputTokens int `json:"cache_creation_input_tokens,omitempty"`
	CacheReadInputTokens     int `json:"cache_read_input_tokens,omitempty"`
}

// --- SSE event types ---

type ClaudeSSEEvent struct {
	Type string          `json:"type"`
	Raw  json.RawMessage `json:"-"` // full event data
}

type ClaudeMessageStart struct {
	Type    string         `json:"type"`
	Message ClaudeResponse `json:"message"`
}

type ClaudeContentBlockStart struct {
	Type         string        `json:"type"`
	Index        int           `json:"index"`
	ContentBlock ClaudeContent `json:"content_block"`
}

type ClaudeContentBlockDelta struct {
	Type  string      `json:"type"`
	Index int         `json:"index"`
	Delta ClaudeDelta `json:"delta"`
}

type ClaudeDelta struct {
	Type        string `json:"type"`
	Text        string `json:"text,omitempty"`         // text_delta
	PartialJSON string `json:"partial_json,omitempty"` // input_json_delta
	Thinking    string `json:"thinking,omitempty"`     // thinking_delta
}

type ClaudeMessageDelta struct {
	Type  string              `json:"type"`
	Delta ClaudeMessageDeltaD `json:"delta"`
	Usage *ClaudeUsage        `json:"usage,omitempty"`
}

type ClaudeMessageDeltaD struct {
	StopReason   *string `json:"stop_reason"`
	StopSequence *string `json:"stop_sequence"`
}
```

## File: `internal/providers/anthropic.go`
```go
package providers

import (
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"

	authpkg "github.com/nghiahoang/launchdock/internal/auth"
	protocol "github.com/nghiahoang/launchdock/internal/protocol"
)

// AnthropicProvider handles Claude API communication.
// OAuth mode matches Claude Code v2.1.81 binary fingerprint exactly.
type AnthropicProvider struct{}

const cliVersion = "2.1.81"

func (p *AnthropicProvider) Match(model string) bool {
	return strings.HasPrefix(strings.ToLower(model), "claude")
}

func (p *AnthropicProvider) ProviderName() string { return "anthropic" }
func (p *AnthropicProvider) BaseURL() string      { return "https://api.anthropic.com" }

func (p *AnthropicProvider) Prepare(req *http.Request, cred *authpkg.Credential) {
	p.PrepareWithModel(req, cred, "")
}

func (p *AnthropicProvider) PrepareWithModel(req *http.Request, cred *authpkg.Credential, model string) {
	switch cred.AuthType {
	case authpkg.AuthOAuth:
		req.Header.Set("Authorization", "Bearer "+cred.AccessToken)
		applyOAuthHeaders(req, model)
	case authpkg.AuthAPIKey:
		req.Header.Set("x-api-key", cred.APIKey)
	}
	req.Header.Set("anthropic-version", "2023-06-01")
	req.Header.Set("Content-Type", "application/json")
}

func (p *AnthropicProvider) TranslateRequest(chatReq *protocol.ChatRequest) ([]byte, string, error) {
	claudeReq, err := protocol.ChatToClaudeRequest(chatReq)
	if err != nil {
		return nil, "", err
	}
	body, err := json.Marshal(claudeReq)
	if err != nil {
		return nil, "", err
	}
	return body, "/v1/messages", nil
}

// --- OAuth headers — match Claude Code v2.1.81 exactly ---

// buildBetas replicates hPq/oN from Claude Code binary.
// Logic: model-dependent beta selection.
func buildBetas(model string) []string {
	m := strings.ToLower(model)
	isHaiku := strings.Contains(m, "haiku")

	betas := []string{}

	// claude-code identity beta (all non-haiku models)
	if !isHaiku {
		betas = append(betas, "claude-code-20250219")
	}

	// OAuth required
	betas = append(betas, "oauth-2025-04-20")

	// Interleaved thinking (non-haiku, non-claude-3)
	if !isHaiku && !strings.Contains(m, "claude-3-") {
		betas = append(betas, "interleaved-thinking-2025-05-14")
	}

	// Prompt caching
	betas = append(betas, "prompt-caching-scope-2026-01-05")

	return betas
}

// computeCCH replicates PL6/w2q from Claude Code binary.
// Hash = sha256(salt + chars_at_positions_4_7_20_of_first_user_message + version)[:5]
func computeCCH(firstUserContent string) string {
	const salt = "59cf53e54c78"
	chars := ""
	positions := []int{4, 7, 20}
	for _, pos := range positions {
		if pos < len(firstUserContent) {
			chars += string(firstUserContent[pos])
		} else {
			chars += "0"
		}
	}
	input := salt + chars + cliVersion
	h := sha256.Sum256([]byte(input))
	return hex.EncodeToString(h[:])[:5]
}

func applyOAuthHeaders(req *http.Request, model string) {
	// Beta headers — dynamic per model
	betas := buildBetas(model)
	req.Header.Set("anthropic-beta", strings.Join(betas, ","))

	// User-Agent — exact match Claude Code v2.1.81
	req.Header.Set("User-Agent", "claude-cli/"+cliVersion+" (external, cli)")
	req.Header.Set("Anthropic-Dangerous-Direct-Browser-Access", "true")

	// x-app header
	req.Header.Set("x-app", "cli")
}

// PrefixTools adds "mcp_" prefix to all tool names in the request body.
// Required for Claude OAuth accounts.
func PrefixTools(body []byte, prefix string) ([]byte, error) {
	var req map[string]any
	if err := json.Unmarshal(body, &req); err != nil {
		return body, err
	}
	transformToolNames(req, prefix, false)
	return json.Marshal(req)
}

// PrepareOAuthBody applies Claude OAuth request rewrites in a single pass.
func PrepareOAuthBody(body []byte, prefix string) ([]byte, error) {
	var req map[string]any
	if err := json.Unmarshal(body, &req); err != nil {
		return body, err
	}
	transformToolNames(req, prefix, false)
	ensureOAuthRequirementsMap(req)
	return json.Marshal(req)
}

func transformToolNames(req map[string]any, prefix string, strip bool) {
	// Prefix tool definitions
	if tools, ok := req["tools"].([]any); ok {
		for _, t := range tools {
			if tm, ok := t.(map[string]any); ok {
				if name, ok := tm["name"].(string); ok {
					tm["name"] = maybeTransformToolName(name, prefix, strip)
				}
			}
		}
	}

	// Prefix tool_use blocks in messages
	if msgs, ok := req["messages"].([]any); ok {
		for _, m := range msgs {
			mm, ok := m.(map[string]any)
			if !ok {
				continue
			}
			content, ok := mm["content"].([]any)
			if !ok {
				continue
			}
			for _, c := range content {
				cm, ok := c.(map[string]any)
				if !ok {
					continue
				}
				if cm["type"] == "tool_use" {
					if name, ok := cm["name"].(string); ok {
						cm["name"] = maybeTransformToolName(name, prefix, strip)
					}
				}
			}

			// Prefix assistant tool_calls in OpenAI-style chat payloads before translation.
			if toolCalls, ok := mm["tool_calls"].([]any); ok {
				for _, tc := range toolCalls {
					tcm, ok := tc.(map[string]any)
					if !ok {
						continue
					}
					fn, ok := tcm["function"].(map[string]any)
					if !ok {
						continue
					}
					if name, ok := fn["name"].(string); ok {
						fn["name"] = maybeTransformToolName(name, prefix, strip)
					}
				}
			}
		}
	}

	// Prefix explicit tool_choice
	if tc, ok := req["tool_choice"].(map[string]any); ok {
		if tc["type"] == "tool" {
			if name, ok := tc["name"].(string); ok {
				tc["name"] = maybeTransformToolName(name, prefix, strip)
			}
		}
	}
}

func maybeTransformToolName(name, prefix string, strip bool) string {
	if strip {
		return strings.TrimPrefix(name, prefix)
	}
	if !strings.HasPrefix(name, prefix) {
		return prefix + name
	}
	return name
}

// StripToolPrefix removes prefix from tool names in response data.
func StripToolPrefix(data []byte, prefix string) []byte {
	return []byte(strings.ReplaceAll(string(data), fmt.Sprintf(`"name":"%s`, prefix), `"name":"`))
}

// ensureOAuthRequirements ensures the request has system prompt identity
// and at least one tool (required by Claude OAuth).
func EnsureOAuthRequirements(body []byte) ([]byte, error) {
	var req map[string]any
	if err := json.Unmarshal(body, &req); err != nil {
		return body, err
	}
	ensureOAuthRequirementsMap(req)
	return json.Marshal(req)
}

func ensureOAuthRequirementsMap(req map[string]any) {
	// System prompt — exact string from Claude Code binary
	const identity = "You are Claude Code, Anthropic's official CLI for Claude."

	// Check if system already contains identity
	hasIdentity := false
	switch s := req["system"].(type) {
	case string:
		hasIdentity = strings.Contains(s, identity)
	case []any:
		for _, item := range s {
			if m, ok := item.(map[string]any); ok {
				if text, ok := m["text"].(string); ok && strings.Contains(text, identity) {
					hasIdentity = true
					break
				}
			}
		}
	}

	if !hasIdentity {
		billingLine := fmt.Sprintf("x-anthropic-billing-header: cc_version=%s; cc_entrypoint=cli; cch=%s;", cliVersion, computeCCH(firstUserText(req)))
		// Prepend identity as first system block (array format like Claude Code does)
		// Add cache_control on system prompt for prompt caching
		existing := req["system"]
		var systemBlocks []map[string]any
		systemBlocks = append(systemBlocks, map[string]any{
			"type":          "text",
			"text":          billingLine,
			"cache_control": map[string]any{"type": "ephemeral", "ttl": "1h"},
		})
		systemBlocks = append(systemBlocks, map[string]any{
			"type":          "text",
			"text":          identity,
			"cache_control": map[string]any{"type": "ephemeral", "ttl": "1h"},
		})

		switch s := existing.(type) {
		case string:
			if s != "" {
				systemBlocks = append(systemBlocks, map[string]any{"type": "text", "text": s})
			}
		case []any:
			for _, item := range s {
				if m, ok := item.(map[string]any); ok {
					text, _ := m["text"].(string)
					typ, _ := m["type"].(string)
					if typ == "" {
						typ = "text"
					}
					systemBlocks = append(systemBlocks, map[string]any{"type": typ, "text": text})
				}
			}
		}
		req["system"] = systemBlocks
	}

	// Add cache_control on last user message for prompt caching
	if msgs, ok := req["messages"].([]any); ok && len(msgs) > 0 {
		// Find last user message
		for i := len(msgs) - 1; i >= 0; i-- {
			msg, ok := msgs[i].(map[string]any)
			if !ok || msg["role"] != "user" {
				continue
			}
			// Add cache_control to last content block of last user message
			switch c := msg["content"].(type) {
			case string:
				msg["content"] = []map[string]any{{
					"type":          "text",
					"text":          c,
					"cache_control": map[string]any{"type": "ephemeral", "ttl": "1h"},
				}}
			case []any:
				if len(c) > 0 {
					if last, ok := c[len(c)-1].(map[string]any); ok {
						last["cache_control"] = map[string]any{"type": "ephemeral", "ttl": "1h"}
					}
				}
			}
			break
		}
	}

	// Ensure at least one tool exists (OAuth requires tools)
	tools, _ := req["tools"].([]any)
	if len(tools) == 0 {
		req["tools"] = []map[string]any{{
			"name":        "mcp_noop",
			"description": "No-op placeholder tool",
			"input_schema": map[string]any{
				"type":       "object",
				"properties": map[string]any{},
			},
		}}
	}
}

func firstUserText(req map[string]any) string {
	msgs, _ := req["messages"].([]any)
	for _, item := range msgs {
		msg, _ := item.(map[string]any)
		if msg == nil || msg["role"] != "user" {
			continue
		}
		switch c := msg["content"].(type) {
		case string:
			return c
		case []any:
			for _, part := range c {
				pm, _ := part.(map[string]any)
				if pm == nil {
					continue
				}
				if pm["type"] == "text" {
					if text, _ := pm["text"].(string); text != "" {
						return text
					}
				}
			}
		}
	}
	return ""
}

// InjectSystemPrompt prepends a system prompt to the Claude request.
func InjectSystemPrompt(body []byte, prompt string) ([]byte, error) {
	if prompt == "" {
		return body, nil
	}
	var req map[string]any
	if err := json.Unmarshal(body, &req); err != nil {
		return body, err
	}
	existing, _ := req["system"].(string)
	if existing != "" {
		req["system"] = prompt + "\n\n" + existing
	} else {
		req["system"] = prompt
	}
	return json.Marshal(req)
}
```

## File: `internal/providers/openai.go`
```go
package providers

import (
	"encoding/json"
	"net/http"
	"strings"

	authpkg "github.com/nghiahoang/launchdock/internal/auth"
	protocol "github.com/nghiahoang/launchdock/internal/protocol"
)

// OpenAIProvider handles OpenAI API communication (mostly passthrough).
type OpenAIProvider struct{}

func (p *OpenAIProvider) Match(model string) bool {
	m := strings.ToLower(model)
	return strings.HasPrefix(m, "gpt-") ||
		strings.HasPrefix(m, "o1") ||
		strings.HasPrefix(m, "o3") ||
		strings.HasPrefix(m, "o4") ||
		strings.HasPrefix(m, "chatgpt")
}

func (p *OpenAIProvider) ProviderName() string { return "openai" }

// BaseURL returns the API base URL.
// For OAuth (ChatGPT) auth, Codex uses chatgpt.com/backend-api/codex, not api.openai.com.
func (p *OpenAIProvider) BaseURL() string { return "https://api.openai.com" }

// ChatGPTBaseURL returns the ChatGPT backend URL used by Codex OAuth.
func (p *OpenAIProvider) ChatGPTBaseURL() string {
	return "https://chatgpt.com/backend-api/codex"
}

func (p *OpenAIProvider) Prepare(req *http.Request, cred *authpkg.Credential) {
	switch cred.AuthType {
	case authpkg.AuthOAuth:
		req.Header.Set("Authorization", "Bearer "+cred.AccessToken)
		if cred.AccountID != "" {
			req.Header.Set("chatgpt-account-id", cred.AccountID)
		}
	case authpkg.AuthAPIKey:
		req.Header.Set("Authorization", "Bearer "+cred.APIKey)
	}
	req.Header.Set("Content-Type", "application/json")
}

func (p *OpenAIProvider) TranslateRequest(chatReq *protocol.ChatRequest) ([]byte, string, error) {
	// OpenAI Chat Completions is passthrough — no translation needed.
	// We re-encode to ensure clean JSON.
	body, err := json.Marshal(chatReq)
	return body, "/v1/chat/completions", err
}
```

## File: `internal/providers/pool.go`
```go
package providers

import (
	"fmt"
	"log/slog"
	"sync"
	"time"

	authpkg "github.com/nghiahoang/launchdock/internal/auth"
)

// Pool manages credentials with round-robin selection and cooldown.
type Pool struct {
	mu           sync.Mutex
	creds        []authpkg.Credential
	cursor       int
	refreshMu    sync.Mutex
	refreshLocks map[string]*sync.Mutex
}

func NewPool(creds []authpkg.Credential) *Pool {
	return &Pool{creds: creds, refreshLocks: make(map[string]*sync.Mutex)}
}

// Pick selects the next available credential for the given provider.
// Skips credentials that are cooled down or expired (and can't refresh).
func (p *Pool) Pick(provider string) (*authpkg.Credential, error) {
	return p.PickMatching(provider, nil, func(*authpkg.Credential) bool { return true })
}

func (p *Pool) PickMatching(provider string, exclude *authpkg.Credential, match func(*authpkg.Credential) bool) (*authpkg.Credential, error) {
	n := len(p.creds)
	if n == 0 {
		return nil, fmt.Errorf("no credentials available")
	}
	for _, idx := range p.pickCandidateIndices(provider, exclude) {
		c := &p.creds[idx]
		if match != nil && !match(c) {
			continue
		}
		if p.needsRefresh(c) {
			if err := p.refresh(c); err != nil {
				slog.Warn("credential refresh failed", "label", c.Label, "error", err)
				continue
			}
		}
		p.mu.Lock()
		p.cursor = (idx + 1) % n
		p.mu.Unlock()
		return c, nil
	}
	return nil, fmt.Errorf("no available credential for provider %q", provider)
}

// PickNext selects the next credential after a failed attempt (for retry).
func (p *Pool) PickNext(provider string, exclude *authpkg.Credential) (*authpkg.Credential, error) {
	return p.PickNextMatching(provider, exclude, func(*authpkg.Credential) bool { return true })
}

func (p *Pool) PickNextMatching(provider string, exclude *authpkg.Credential, match func(*authpkg.Credential) bool) (*authpkg.Credential, error) {
	for _, idx := range p.pickCandidateIndices(provider, exclude) {
		c := &p.creds[idx]
		if match != nil && !match(c) {
			continue
		}
		if p.needsRefresh(c) {
			if err := p.refresh(c); err != nil {
				slog.Warn("fallback credential refresh failed", "label", c.Label, "error", err)
				continue
			}
		}
		p.mu.Lock()
		p.cursor = (idx + 1) % len(p.creds)
		p.mu.Unlock()
		return c, nil
	}
	return nil, fmt.Errorf("no fallback credential for provider %q", provider)
}

// Cooldown marks a credential as temporarily unavailable.
func (p *Pool) Cooldown(c *authpkg.Credential, d time.Duration) {
	if !p.hasAlternativeCredential(c.Provider, c) {
		slog.Info("skipping credential cooldown; no alternative available", "label", c.Label, "provider", c.Provider)
		return
	}
	p.mu.Lock()
	defer p.mu.Unlock()
	c.CooldownUntil = time.Now().Add(d)
	slog.Info("credential cooldown", "label", c.Label, "duration", d)
}

// Count returns total credentials (optionally filtered by provider).
func (p *Pool) Count(provider string) int {
	p.mu.Lock()
	defer p.mu.Unlock()
	if provider == "" {
		return len(p.creds)
	}
	n := 0
	for _, c := range p.creds {
		if c.Provider == provider {
			n++
		}
	}
	return n
}

// Providers returns unique provider names.
func (p *Pool) Providers() []string {
	p.mu.Lock()
	defer p.mu.Unlock()
	seen := map[string]bool{}
	var result []string
	for _, c := range p.creds {
		if !seen[c.Provider] {
			seen[c.Provider] = true
			result = append(result, c.Provider)
		}
	}
	return result
}

func (p *Pool) pickCandidateIndices(provider string, exclude *authpkg.Credential) []int {
	p.mu.Lock()
	defer p.mu.Unlock()
	n := len(p.creds)
	now := time.Now()
	start := p.cursor
	var result []int
	for i := 0; i < n; i++ {
		idx := (start + i) % n
		c := &p.creds[idx]
		if c.Provider != provider || c == exclude {
			continue
		}
		if now.Before(c.CooldownUntil) {
			slog.Debug("credential on cooldown", "label", c.Label, "until", c.CooldownUntil)
			continue
		}
		result = append(result, idx)
	}
	return result
}

func (p *Pool) needsRefresh(c *authpkg.Credential) bool {
	if c.AuthType != authpkg.AuthOAuth || c.RefreshToken == "" || c.ExpiresAt.IsZero() {
		return false
	}
	return time.Until(c.ExpiresAt) <= 5*time.Minute
}

func (p *Pool) hasAlternativeCredential(provider string, current *authpkg.Credential) bool {
	p.mu.Lock()
	defer p.mu.Unlock()
	for i := range p.creds {
		c := &p.creds[i]
		if c.Provider == provider && c != current {
			return true
		}
	}
	return false
}

func (p *Pool) lockForCredential(c *authpkg.Credential) *sync.Mutex {
	key := c.Provider + ":" + c.Source + ":" + c.Label
	if c.ID != "" {
		key = c.ID
	}
	p.refreshMu.Lock()
	defer p.refreshMu.Unlock()
	if lock, ok := p.refreshLocks[key]; ok {
		return lock
	}
	lock := &sync.Mutex{}
	p.refreshLocks[key] = lock
	return lock
}

// refresh runs outside the main pool lock to avoid blocking all requests.
func (p *Pool) refresh(c *authpkg.Credential) error {
	lock := p.lockForCredential(c)
	lock.Lock()
	defer lock.Unlock()

	p.mu.Lock()
	if time.Now().Before(c.CooldownUntil) {
		until := c.CooldownUntil
		p.mu.Unlock()
		return fmt.Errorf("credential on cooldown until %s", until.Format(time.RFC3339))
	}
	if !p.needsRefresh(c) {
		p.mu.Unlock()
		return nil
	}
	provider := c.Provider
	authType := c.AuthType
	refreshToken := c.RefreshToken
	label := c.Label
	managedID := c.ID
	managed := c.Managed
	p.mu.Unlock()

	switch {
	case provider == "openai" && authType == authpkg.AuthOAuth && refreshToken != "":
		at, rt, exp, err := authpkg.RefreshOpenAIOAuth(refreshToken)
		if err != nil {
			if managed && managedID != "" && authpkg.IsTerminalOpenAIRefreshError(err) {
				if derr := authpkg.SetConfigCredentialDisabled(managedID, true); derr != nil {
					slog.Warn("disable stale OpenAI credential failed", "label", label, "id", managedID, "error", derr)
				} else {
					slog.Warn("disabled stale OpenAI credential", "label", label, "id", managedID)
				}
			}
			p.Cooldown(c, 45*time.Second)
			return err
		}
		p.mu.Lock()
		c.AccessToken = at
		c.RefreshToken = rt
		c.ExpiresAt = exp
		p.mu.Unlock()
		if managed && managedID != "" {
			if err := authpkg.PersistManagedCredentialState(managedID, rt, c.AccountID, c.Email); err != nil {
				slog.Warn("persist managed OpenAI token failed", "label", label, "error", err)
			}
		}
		slog.Info("refreshed OpenAI OAuth token", "label", label, "expires", exp)
		return nil

	case provider == "anthropic" && authType == authpkg.AuthOAuth && refreshToken != "":
		at, rt, exp, err := authpkg.RefreshClaudeOAuth(refreshToken)
		if err != nil {
			p.Cooldown(c, 45*time.Second)
			// Fallback: try CLI refresh
			slog.Warn("direct OAuth refresh failed, trying CLI fallback", "error", err)
			if cliErr := authpkg.RefreshViaCLI("claude -p . --model haiku --text hi"); cliErr != nil {
				return fmt.Errorf("claude refresh failed (direct: %w, cli: %v)", err, cliErr)
			}
			creds, kerr := authpkg.LoadFromKeychain()
			if kerr != nil || len(creds) == 0 {
				return fmt.Errorf("re-read keychain after CLI refresh: %w", kerr)
			}
			p.mu.Lock()
			c.AccessToken = creds[0].AccessToken
			c.RefreshToken = creds[0].RefreshToken
			c.ExpiresAt = creds[0].ExpiresAt
			p.mu.Unlock()
			if managed && managedID != "" {
				if err := authpkg.PersistManagedCredentialState(managedID, creds[0].RefreshToken, c.AccountID, c.Email); err != nil {
					slog.Warn("persist managed Claude token failed", "label", label, "error", err)
				}
			}
			slog.Info("refreshed Claude OAuth token via CLI", "label", label)
			return nil
		}
		p.mu.Lock()
		c.AccessToken = at
		c.RefreshToken = rt
		c.ExpiresAt = exp
		p.mu.Unlock()
		if managed && managedID != "" {
			if err := authpkg.PersistManagedCredentialState(managedID, rt, c.AccountID, c.Email); err != nil {
				slog.Warn("persist managed Claude token failed", "label", label, "error", err)
			}
		}
		slog.Info("refreshed Claude OAuth token directly", "label", label, "expires", exp)
		return nil

	default:
		return fmt.Errorf("cannot refresh credential type %s/%s", c.Provider, c.AuthType)
	}
}

func (p *Pool) RefreshCredential(c *authpkg.Credential) error {
	return p.refresh(c)
}
```

## File: `internal/providers/provider.go`
```go
package providers

import (
	"net/http"
	"strings"

	authpkg "github.com/nghiahoang/launchdock/internal/auth"
	protocol "github.com/nghiahoang/launchdock/internal/protocol"
)

// Provider handles upstream communication for a specific backend.
type Provider interface {
	// Match returns true if this provider handles the given model name.
	Match(model string) bool

	// Prepare adds auth headers and provider-specific modifications to the upstream request.
	Prepare(req *http.Request, cred *authpkg.Credential)

	// ProviderName returns the credential provider name (e.g. "anthropic", "openai").
	ProviderName() string

	// BaseURL returns the API base URL.
	BaseURL() string

	// TranslateRequest converts a ChatRequest into the provider's native request body.
	// Returns the body bytes and target URL path.
	TranslateRequest(chatReq *protocol.ChatRequest) (body []byte, path string, err error)
}

// RouteProvider selects the appropriate provider based on model name.
func RouteProvider(providers []Provider, model string) Provider {
	for _, p := range providers {
		if p.Match(model) {
			return p
		}
	}
	return nil
}

// ModelToProvider maps model name prefix to provider name.
func ModelToProvider(model string) string {
	m := strings.ToLower(model)
	switch {
	case strings.HasPrefix(m, "claude"):
		return "anthropic"
	case strings.HasPrefix(m, "gpt-"),
		strings.HasPrefix(m, "o1"),
		strings.HasPrefix(m, "o3"),
		strings.HasPrefix(m, "o4"),
		strings.HasPrefix(m, "chatgpt"):
		return "openai"
	case strings.HasPrefix(m, "gemini"):
		return "gemini"
	default:
		return "anthropic" // default to anthropic
	}
}
```

## File: `internal/runtime/daemon.go`
```go
package runtime

import (
	"fmt"
	"net/http"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"time"
)

func daemonDir() string {
	home, _ := os.UserHomeDir()
	return filepath.Join(home, ".launchdock")
}

func daemonPIDPath() string {
	return filepath.Join(daemonDir(), "launchdock.pid")
}

func daemonLogPath() string {
	return filepath.Join(daemonDir(), "launchdock.log")
}

func isServerHealthy(rawURL string) bool {
	client := &http.Client{Timeout: 800 * time.Millisecond}
	resp, err := client.Get(rawURL + "/health")
	if err != nil {
		return false
	}
	defer resp.Body.Close()
	return resp.StatusCode == http.StatusOK
}

func readDaemonPID() (int, error) {
	data, err := os.ReadFile(daemonPIDPath())
	if err != nil {
		return 0, err
	}
	pid, err := strconv.Atoi(strings.TrimSpace(string(data)))
	if err != nil {
		return 0, err
	}
	return pid, nil
}

func writeDaemonPID(pid int) error {
	if err := os.MkdirAll(daemonDir(), 0755); err != nil {
		return err
	}
	return os.WriteFile(daemonPIDPath(), []byte(strconv.Itoa(pid)), 0644)
}

func removeDaemonPID() {
	_ = os.Remove(daemonPIDPath())
}

func processAlive(pid int) bool {
	if pid <= 0 {
		return false
	}
	proc, err := os.FindProcess(pid)
	if err != nil {
		return false
	}
	return signalProcess0(proc) == nil
}

func EnsureServerRunning(rawURL string) error {
	if isServerHealthy(rawURL) {
		return nil
	}
	if pid, err := readDaemonPID(); err == nil {
		if processAlive(pid) {
			return waitForHealthy(rawURL, 5*time.Second)
		}
		removeDaemonPID()
	}
	if err := startBackgroundServer(); err != nil {
		return err
	}
	return waitForHealthy(rawURL, 10*time.Second)
}

func waitForHealthy(rawURL string, timeout time.Duration) error {
	deadline := time.Now().Add(timeout)
	for time.Now().Before(deadline) {
		if isServerHealthy(rawURL) {
			return nil
		}
		time.Sleep(200 * time.Millisecond)
	}
	return fmt.Errorf("server did not become healthy at %s", rawURL)
}

func StopServer() error {
	pid, err := readDaemonPID()
	if err != nil {
		return fmt.Errorf("no running daemon")
	}
	proc, err := os.FindProcess(pid)
	if err != nil {
		removeDaemonPID()
		return fmt.Errorf("stale pid file")
	}
	if err := terminateProcess(proc); err != nil {
		removeDaemonPID()
		return err
	}
	deadline := time.Now().Add(5 * time.Second)
	for time.Now().Before(deadline) {
		if !processAlive(pid) {
			removeDaemonPID()
			return nil
		}
		time.Sleep(150 * time.Millisecond)
	}
	return fmt.Errorf("process %d did not stop", pid)
}

func DaemonStatus(rawURL string) (string, int) {
	pid, err := readDaemonPID()
	if err != nil {
		if isServerHealthy(rawURL) {
			return "running (unmanaged)", 0
		}
		return "stopped", 0
	}
	if !processAlive(pid) {
		removeDaemonPID()
		if isServerHealthy(rawURL) {
			return "running (unmanaged)", 0
		}
		return "stopped", 0
	}
	if isServerHealthy(rawURL) {
		return "running", pid
	}
	return "starting", pid
}

func DaemonLogPath() string { return daemonLogPath() }
```

## File: `internal/runtime/daemon_unix.go`
```go
//go:build darwin || linux

package runtime

import (
	"os"
	"os/exec"
	"syscall"
)

func startBackgroundServer() error {
	bin, err := resolveDaemonBinary()
	if err != nil {
		return err
	}
	if err := os.MkdirAll(daemonDir(), 0755); err != nil {
		return err
	}
	logf, err := os.OpenFile(daemonLogPath(), os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		return err
	}
	cmd := exec.Command(bin, "serve")
	cmd.Env = os.Environ()
	cmd.Stdout = logf
	cmd.Stderr = logf
	cmd.Stdin = nil
	cmd.SysProcAttr = &syscall.SysProcAttr{Setsid: true}
	if err := cmd.Start(); err != nil {
		_ = logf.Close()
		return err
	}
	if err := writeDaemonPID(cmd.Process.Pid); err != nil {
		return err
	}
	return logf.Close()
}

func resolveDaemonBinary() (string, error) {
	if path, err := exec.LookPath("launchdock"); err == nil {
		return path, nil
	}
	return os.Executable()
}
```

## File: `internal/runtime/daemon_windows.go`
```go
//go:build windows

package runtime

import (
	"os"
	"os/exec"
	"syscall"
)

func startBackgroundServer() error {
	bin, err := resolveDaemonBinary()
	if err != nil {
		return err
	}
	if err := os.MkdirAll(daemonDir(), 0755); err != nil {
		return err
	}
	logf, err := os.OpenFile(daemonLogPath(), os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		return err
	}
	cmd := exec.Command(bin, "serve")
	cmd.Env = os.Environ()
	cmd.Stdout = logf
	cmd.Stderr = logf
	cmd.SysProcAttr = &syscall.SysProcAttr{CreationFlags: 0x00000008}
	if err := cmd.Start(); err != nil {
		_ = logf.Close()
		return err
	}
	if err := writeDaemonPID(cmd.Process.Pid); err != nil {
		return err
	}
	return logf.Close()
}

func resolveDaemonBinary() (string, error) {
	if path, err := exec.LookPath("launchdock"); err == nil {
		return path, nil
	}
	return os.Executable()
}
```

## File: `internal/runtime/process_unix.go`
```go
//go:build darwin || linux

package runtime

import (
	"os"
	"syscall"
)

func signalProcess0(proc *os.Process) error {
	return proc.Signal(syscall.Signal(0))
}

func terminateProcess(proc *os.Process) error {
	return proc.Signal(syscall.SIGTERM)
}
```

## File: `internal/runtime/process_windows.go`
```go
//go:build windows

package runtime

import (
	"os"
	"syscall"
)

func signalProcess0(proc *os.Process) error {
	return proc.Signal(syscall.Signal(0))
}

func terminateProcess(proc *os.Process) error {
	return proc.Kill()
}
```

## File: `web/auth_error.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{{.Title}}</title>
    <style>
      :root {
        --bg: #faf6f3;
        --panel: rgba(255, 255, 255, 0.9);
        --text: #241814;
        --muted: rgba(36, 24, 20, 0.72);
        --border: rgba(103, 48, 29, 0.16);
        --accent: #b4512d;
      }
      * { box-sizing: border-box; }
      body {
        margin: 0;
        min-height: 100vh;
        background:
          radial-gradient(circle at top right, rgba(180, 81, 45, 0.12), transparent 28%),
          radial-gradient(circle at bottom left, rgba(210, 124, 79, 0.15), transparent 24%),
          var(--bg);
        color: var(--text);
        font-family: Iowan Old Style, Charter, Georgia, serif;
      }
      .wrap {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 24px;
      }
      .card {
        width: min(620px, 100%);
        padding: 36px 32px;
        border: 1px solid var(--border);
        border-radius: 24px;
        background: var(--panel);
        box-shadow: 0 18px 60px rgba(46, 26, 20, 0.08);
      }
      .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 8px 14px;
        border-radius: 999px;
        border: 1px solid var(--border);
        color: var(--muted);
        font: 600 12px/1.2 ui-monospace, SFMono-Regular, Menlo, monospace;
        letter-spacing: 0.08em;
        text-transform: uppercase;
      }
      .dot {
        width: 9px;
        height: 9px;
        border-radius: 50%;
        background: var(--accent);
        box-shadow: 0 0 0 6px rgba(180, 81, 45, 0.12);
      }
      h1 {
        margin: 24px 0 10px;
        font-size: clamp(32px, 5vw, 46px);
        line-height: 1.08;
        font-weight: 500;
      }
      p {
        margin: 0 0 18px;
        color: var(--muted);
        font: 400 18px/1.6 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }
      .detail {
        padding: 14px 16px;
        border-radius: 14px;
        border: 1px solid var(--border);
        background: rgba(255, 255, 255, 0.8);
        color: var(--text);
        font: 500 14px/1.5 ui-monospace, SFMono-Regular, Menlo, monospace;
        overflow-wrap: anywhere;
      }
    </style>
  </head>
  <body>
    <div class="wrap">
      <div class="card">
        <div class="eyebrow"><span class="dot"></span>{{.Provider}}</div>
        <h1>{{.Title}}</h1>
        <p>{{.Message}}</p>
        {{if .Detail}}<div class="detail">{{.Detail}}</div>{{end}}
      </div>
    </div>
  </body>
</html>
```

## File: `web/auth_success.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{{.Title}}</title>
    <style>
      :root {
        --bg: #f5f7f4;
        --panel: rgba(255, 255, 255, 0.84);
        --text: #182019;
        --muted: rgba(24, 32, 25, 0.68);
        --border: rgba(24, 32, 25, 0.1);
        --accent: #1f6b4f;
      }
      * { box-sizing: border-box; }
      body {
        margin: 0;
        min-height: 100vh;
        background:
          radial-gradient(circle at top left, rgba(31, 107, 79, 0.12), transparent 28%),
          radial-gradient(circle at bottom right, rgba(86, 156, 116, 0.16), transparent 24%),
          var(--bg);
        color: var(--text);
        font-family: Iowan Old Style, Charter, Georgia, serif;
      }
      .wrap {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 24px;
      }
      .card {
        width: min(620px, 100%);
        padding: 36px 32px;
        border: 1px solid var(--border);
        border-radius: 24px;
        background: var(--panel);
        backdrop-filter: blur(10px);
        box-shadow: 0 18px 60px rgba(17, 24, 20, 0.08);
        text-align: center;
      }
      .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 8px 14px;
        border-radius: 999px;
        border: 1px solid var(--border);
        color: var(--muted);
        font: 600 12px/1.2 ui-monospace, SFMono-Regular, Menlo, monospace;
        letter-spacing: 0.08em;
        text-transform: uppercase;
      }
      .dot {
        width: 9px;
        height: 9px;
        border-radius: 50%;
        background: var(--accent);
        box-shadow: 0 0 0 6px rgba(31, 107, 79, 0.12);
      }
      h1 {
        margin: 24px 0 10px;
        font-size: clamp(34px, 6vw, 52px);
        line-height: 1.05;
        font-weight: 500;
      }
      p {
        margin: 0 auto;
        max-width: 460px;
        color: var(--muted);
        font: 400 18px/1.6 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }
    </style>
  </head>
  <body>
    <div class="wrap">
      <div class="card">
        <div class="eyebrow"><span class="dot"></span>{{.Provider}}</div>
        <h1>{{.Title}}</h1>
        <p>{{.Message}}</p>
      </div>
    </div>
  </body>
</html>
```

