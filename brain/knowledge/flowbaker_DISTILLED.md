---
id: flowbaker
type: knowledge
owner: OA_Triage
---
# flowbaker
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<img src="assets/head.png" alt="Flowbaker Executor" width="100%">

Workflow automation executor that runs on your machine. It connects to the Flowbaker platform to execute workflows with various integrations like Discord, GitHub, Gmail, and more.
<div align="center">

  [![Go Version](https://img.shields.io/badge/go-1.25.0-blue.svg?style=flat-square)](https://golang.org/)
  [![Community](https://img.shields.io/discord/1369035097394647162?style=flat-square&label=discord)](https://discord.gg/wDxHFkcbhD)

</div>

## Quick Start

### Installation

Download the latest binary from [releases](https://github.com/flowbaker/flowbaker/releases) or build from source:

```bash
git clone https://github.com/flowbaker/flowbaker.git
cd flowbaker
go build -o flowbaker cmd/main.go
```

### Setup

Start the executor and follow the setup prompts:

```bash
./flowbaker start
```

The setup will guide you through:
- Creating an executor ID
- Connecting to your Flowbaker workspace
- Generating secure authentication keys

Once setup is complete, the executor will run workflows assigned to it from your Flowbaker dashboard.

## Commands

- `flowbaker start` - Start the executor (auto-setup on first run)
- `flowbaker status` - Check executor status
- `flowbaker reset` - Reset configuration
- `flowbaker workspaces` - Manage workspace connections

## Building from Source

```bash
go build -o flowbaker cmd/main.go
```

Requirements: Go 1.25+

## Community

- [Discord](https://discord.gg/wDxHFkcbhD) - Get help and discuss
- [GitHub Issues](https://github.com/flowbaker/flowbaker/issues) - Report bugs or request features

## License

Apache 2.0

## Star History

<a href="https://www.star-history.com/#flowbaker/flowbaker&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=flowbaker/flowbaker&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=flowbaker/flowbaker&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=flowbaker/flowbaker&type=date&legend=top-left" />
 </picture>
</a>

```

### File: cmd\main.go
```go
package main

import (
	"os"

	"github.com/flowbaker/flowbaker/cmd/cli"
	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
)

func main() {
	log.Logger = log.Output(zerolog.ConsoleWriter{Out: os.Stderr})

	cli.Execute()
}

```

### File: cmd\cli\reset.go
```go
package cli

import (
	"context"
	"fmt"
	"os"

	"github.com/flowbaker/flowbaker/internal/initialization"
	"github.com/rs/zerolog/log"
	"github.com/spf13/cobra"
)

func NewResetCommand(executorContainer *initialization.ExecutorContainer) *cobra.Command {
	cmd := &cobra.Command{
		Use:   "reset",
		Short: "Reset configuration and start fresh",
		Long:  `Reset the executor configuration and start fresh. This will remove all existing configuration and require you to set up the executor again.`,
		RunE: func(cmd *cobra.Command, args []string) error {
			return runReset(executorContainer)
		},
	}

	return cmd
}

func runReset(executorContainer *initialization.ExecutorContainer) error {
	configManager := executorContainer.GetConfigManager()

	if err := configManager.ResetConfig(context.Background()); err != nil {
		log.Fatal().Err(err).Msg("Failed to reset configuration")
		return err
	}

	fmt.Println("✅ Configuration reset successfully")
	fmt.Printf("Run '%s start' to begin setup\n", os.Args[0])
	return nil
}

```

### File: cmd\cli\root.go
```go
package cli

import (
	"fmt"
	"os"

	"github.com/flowbaker/flowbaker/internal/initialization"
	"github.com/spf13/cobra"
)

func NewRootCommand() *cobra.Command {
	rootCmd := &cobra.Command{
		Use:   "flowbaker",
		Short: "Flowbaker Executor CLI",
		Long: `Flowbaker Executor is a workflow automation engine that connects to the Flowbaker platform
to execute workflows and manage integrations.`,
		SilenceUsage:  true,
		SilenceErrors: true,
	}

	rootCmd.PersistentFlags().Bool("debug", false, "Enable debug logging")
	rootCmd.PersistentFlags().String("api-url", "", "Override API URL")

	executorContainer, err := initialization.NewExecutorContainer()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Failed to initialize executor container: %v\n", err)
		os.Exit(1)
	}

	rootCmd.AddCommand(NewStartCommand(executorContainer))
	rootCmd.AddCommand(NewResetCommand(executorContainer))
	rootCmd.AddCommand(NewStatusCommand(executorContainer))
	rootCmd.AddCommand(NewWorkspacesCommand(executorContainer))

	return rootCmd
}

// Execute runs the root command
func Execute() {
	if err := NewRootCommand().Execute(); err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}
}

```

### File: cmd\cli\start.go
```go
package cli

import (
	"context"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/flowbaker/flowbaker/internal/controllers"
	"github.com/flowbaker/flowbaker/internal/initialization"
	"github.com/flowbaker/flowbaker/internal/middlewares"
	"github.com/flowbaker/flowbaker/internal/server"
	"github.com/flowbaker/flowbaker/internal/version"
	"github.com/flowbaker/flowbaker/pkg/clients/flowbaker"
	"github.com/gofiber/fiber/v3"
	"github.com/gofiber/fiber/v3/middleware/cors"
	"github.com/gofiber/fiber/v3/middleware/logger"
	"github.com/rs/zerolog/log"
	"github.com/spf13/cobra"
)

func NewStartCommand(executorContainer *initialization.ExecutorContainer) *cobra.Command {
	cmd := &cobra.Command{
		Use:   "start",
		Short: "Start the executor (auto-setup if needed)",
		Long:  `Start the executor service. If this is the first time running, it will automatically guide you through the setup process.`,
		RunE: func(cmd *cobra.Command, args []string) error {
			return runStart(executorContainer)
		},
	}

	return cmd
}

func runStart(executorContainer *initialization.ExecutorContainer) error {
	ctx := context.Background()
	configManager := executorContainer.GetConfigManager()
	workspaceRegistrationManager := executorContainer.GetWorkspaceRegistrationManager()

	if !configManager.IsSetupComplete(ctx) {
		// Start HTTP server with health check endpoint before registration
		// so the API can verify connectivity during the registration process
		ctx, cancel := context.WithCancel(ctx)

		app := startHealthCheckServer(ctx, executorContainer)

		if err := initialization.RunFirstTimeSetup(ctx, initialization.RunFirstTimeSetupParams{
			ConfigManager:       configManager,
			RegistrationManager: workspaceRegistrationManager,
		}); err != nil {
			log.Fatal().Err(err).Msg("Failed to complete setup")
		}

		// Gracefully shutdown the health check server
		cancel() // Cancel the server's context first
		shutdownCtx, shutdownCancel := context.WithTimeout(context.Background(), 5*time.Second)
		defer shutdownCancel()

		if err := app.ShutdownWithContext(shutdownCtx); err != nil {
			log.Error().Err(err).Msg("Failed to shutdown health check server gracefully")
		}
	}

	return runExecutor(executorContainer)
}

func runExecutor(executorContainer *initialization.ExecutorContainer) error {
	ctx, cancel := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
	defer cancel()

	log.Info().Msg("Starting executor service")

	configManager := executorContainer.GetConfigManager()
	config, err := configManager.GetConfig(ctx)
	if err != nil || config.ExecutorID == "" || !config.SetupComplete {
		log.Fatal().Msg("No configuration found. Run 'start' to set up.")
	}

	log.Info().
		Str("executor_id", config.ExecutorID).
		Str("api_base_url", config.APIBaseURL).
		Msg("Executor configuration loaded")

	flowbakerClient := flowbaker.NewClient(
		flowbaker.WithBaseURL(config.APIBaseURL),
		flowbaker.WithExecutorID(config.ExecutorID),
		flowbaker.WithEd25519PrivateKey(config.Ed25519PrivateKey),
	)

	log.Info().Msg("Flowbaker client with signature-based auth ready")

	deps, err := executorContainer.BuildExecutorDependencies(context.Background(), initialization.ExecutorDependencyConfig{
		FlowbakerClient: flowbakerClient,
		ExecutorID:      config.ExecutorID,
		Config:          config,
	})
	if err != nil {
		log.Fatal().Err(err).Msg("Failed to build executor dependencies")
	}

	var keyProvider middlewares.WorkspaceAPIKeyProvider
	if config.SkipWorkspaceAssignments || config.StaticAPISignaturePublicKey != "" {
		keyProvider = nil
	} else {
		if len(config.WorkspaceAssignments) == 0 {
			log.Fatal().Msg("No workspace API keys found in config")
		}
		keyProvider = middlewares.NewConfigAPIKeyProvider(config)
	}

	server := server.NewHTTPServer(context.Background(), server.HTTPServerDependencies{
		Config:             config,
		ExecutorController: deps.ExecutorController,
		KeyProvider:        keyProvider,
	})

	shutdownChan := make(chan os.Signal, 1)
	signal.Notify(shutdownChan, syscall.SIGINT, syscall.SIGTERM)

	if err := server.Listen(":8081", fiber.ListenConfig{
		GracefulContext:       ctx,
		DisableStartupMessage: true,
	}); err != nil {
		log.Error().Err(err).Msg("HTTP server failed")
	}

	log.Info().Msg("Executor service stopped")
	return nil
}

// startHealthCheckServer starts a minimal HTTP server with only the health check endpoint
// This is used during the initial setup phase to allow API connectivity verification
func startHealthCheckServer(ctx context.Context, executorContainer *initialization.ExecutorContainer) *fiber.App {
	workspaceRegistrationManager := executorContainer.GetWorkspaceRegistrationManager()

	// Create a minimal executor controller for registration
	executorController := &controllers.ExecutorController{}
	executorController = controllers.NewExecutorController(controllers.ExecutorControllerDependencies{
		WorkspaceRegistrationManager: workspaceRegistrationManager,
	})

	app := fiber.New(fiber.Config{
		AppName: "flowbaker-executor-setup",
	})

	app.Use(cors.New())
	app.Use(logger.New())

	app.Get("/health", func(c fiber.Ctx) error {
		return c.Status(fiber.StatusOK).JSON(fiber.Map{
			"status":     "healthy",
			"service":    "flowbaker-executor",
			"version":    version.GetVersion(),
			"timestamp":  time.Now().UTC().Format(time.RFC3339),
			"setup_mode": true,
		})
	})

	workspaces := app.Group("/workspaces")
	workspaces.Post("/", executorController.RegisterWorkspace)

	go func() {
		if err := app.Listen(":8081", fiber.ListenConfig{
			GracefulContext:       ctx,
			DisableStartupMessage: true,
		}); err != nil {
			log.Error().Err(err).Msg("Health check server failed to start")
		}
	}()

	return app
}

```

### File: cmd\cli\status.go
```go
package cli

import (
	"context"
	"fmt"
	"os"
	"strings"

	"github.com/flowbaker/flowbaker/internal/initialization"
	"github.com/rs/zerolog/log"
	"github.com/spf13/cobra"
)

func NewStatusCommand(executorContainer *initialization.ExecutorContainer) *cobra.Command {
	cmd := &cobra.Command{
		Use:   "status",
		Short: "Show current executor status",
		Long:  `Display the current status of the executor including configuration details and workspace assignments.`,
		RunE: func(cmd *cobra.Command, args []string) error {
			return runStatus(executorContainer)
		},
	}

	return cmd
}

func runStatus(executorContainer *initialization.ExecutorContainer) error {
	configManager := executorContainer.GetConfigManager()

	if configManager.IsSetupComplete(context.Background()) {
		config, err := configManager.GetConfig(context.Background())
		if err != nil {
			log.Fatal().Err(err).Msg("Failed to load configuration")
			return err
		}

		workspaceNames := make([]string, len(config.WorkspaceAssignments))

		for i, assignment := range config.WorkspaceAssignments {
			workspaceNames[i] = assignment.WorkspaceName
		}

		fmt.Println("✅ Executor is set up and ready")
		fmt.Printf("   Executor ID: %s\n", config.ExecutorID)
		fmt.Printf("   Workspaces (%d): %s\n", len(config.WorkspaceAssignments), strings.Join(workspaceNames, ", "))
		fmt.Printf("   API URL: %s\n", config.APIBaseURL)
		lastConnected := config.GetLastConnectedTime()
		if !lastConnected.IsZero() {
			fmt.Printf("   Last connected: %s\n", lastConnected.Format("2006-01-02 15:04:05"))
		}
	} else {
		fmt.Println("❌ Executor is not set up")
		fmt.Printf("Run '%s start' to begin setup\n", os.Args[0])
	}

	return nil
}

```

### File: cmd\cli\workspaces.go
```go
package cli

import (
	"context"
	"fmt"
	"os"

	"github.com/flowbaker/flowbaker/internal/initialization"
	"github.com/flowbaker/flowbaker/internal/managers"
	"github.com/flowbaker/flowbaker/pkg/clients/flowbaker"
	"github.com/rs/zerolog/log"
	"github.com/spf13/cobra"
)

func NewWorkspacesCommand(executorContainer *initialization.ExecutorContainer) *cobra.Command {
	cmd := &cobra.Command{
		Use:   "workspaces",
		Short: "Manage workspace assignments",
		Long:  `Manage workspace assignments for the executor. View, add, or remove workspace assignments.`,
	}

	cmd.AddCommand(NewWorkspacesListCommand(executorContainer))

	return cmd
}

func NewWorkspacesListCommand(executorContainer *initialization.ExecutorContainer) *cobra.Command {
	cmd := &cobra.Command{
		Use:   "list",
		Short: "List all assigned workspaces",
		Long:  `List all workspaces that this executor is assigned to, showing workspace names and details.`,
		RunE: func(cmd *cobra.Command, args []string) error {
			return runWorkspacesList(executorContainer)
		},
	}

	return cmd
}

func runWorkspacesList(executorContainer *initialization.ExecutorContainer) error {
	configManager := executorContainer.GetConfigManager()

	if !configManager.IsSetupComplete(context.Background()) {
		fmt.Println("❌ Executor is not set up. Run 'start' to begin setup.")
		os.Exit(1)
	}

	config, err := configManager.GetConfig(context.Background())
	if err != nil {
		log.Fatal().Err(err).Msg("Failed to load configuration")
		return err
	}

	fmt.Println("📋 Assigned Workspaces:")
	if len(config.WorkspaceAssignments) == 0 {
		fmt.Println("   No workspaces assigned")
		return nil
	}

	flowbakerClient := flowbaker.NewClient(
		flowbaker.WithBaseURL(config.APIBaseURL),
		flowbaker.WithExecutorID(config.ExecutorID),
		flowbaker.WithEd25519PrivateKey(config.Ed25519PrivateKey),
	)

	workspaceManager := managers.NewExecutorWorkspaceManager(managers.ExecutorWorkspaceManagerDependencies{
		FlowbakerClient: flowbakerClient,
	})

	ctx := context.Background()
	workspaces, err := workspaceManager.GetWorkspaces(ctx)
	if err != nil {
		log.Fatal().Err(err).Msg("Failed to fetch workspace details")
		return err
	}

	for i, workspace := range workspaces {
		fmt.Printf("   %d. %s (%s)\n", i+1, workspace.Name, workspace.Slug)
	}
	fmt.Printf("\nTotal: %d workspace(s)\n", len(workspaces))

	return nil
}

```

### File: internal\auth\api_signature.go
```go
package auth

import (
	"crypto/ed25519"
	"crypto/sha256"
	"encoding/base64"
	"fmt"
	"strconv"
	"time"
)

// APIRequestSigner signs API requests for executor authentication
type APIRequestSigner struct {
	privateKey ed25519.PrivateKey
}

// NewAPIRequestSigner creates a new request signer
func NewAPIRequestSigner(privateKeyBase64 string) (*APIRequestSigner, error) {
	privateKeyBytes, err := base64.StdEncoding.DecodeString(privateKeyBase64)
	if err != nil {
		return nil, fmt.Errorf("failed to decode private key: %w", err)
	}

	if len(privateKeyBytes) != ed25519.PrivateKeySize {
		return nil, fmt.Errorf("invalid private key size: expected %d, got %d", ed25519.PrivateKeySize, len(privateKeyBytes))
	}

	return &APIRequestSigner{
		privateKey: ed25519.PrivateKey(privateKeyBytes),
	}, nil
}

// SignRequest creates signature headers for an API request
func (s *APIRequestSigner) SignRequest(method, path string, body []byte) (map[string]string, error) {
	timestamp := time.Now().Unix()
	timestampStr := strconv.FormatInt(timestamp, 10)

	// Create body hash
	bodyHash := sha256.Sum256(body)
	bodyHashStr := fmt.Sprintf("sha256:%x", bodyHash)

	// Create canonical request
	canonicalRequest := fmt.Sprintf("%s\n%s\n\n%s\n%s", method, path, timestampStr, bodyHashStr)

	// Sign the canonical request
	signature := ed25519.Sign(s.privateKey, []byte(canonicalRequest))
	signatureB64 := base64.StdEncoding.EncodeToString(signature)

	return map[string]string{
		"X-API-Signature": fmt.Sprintf("ed25519=%s", signatureB64),
		"X-API-Timestamp": timestampStr,
	}, nil
}

// APISignatureVerifier verifies API request signatures
type APISignatureVerifier struct {
	publicKey ed25519.PublicKey
}

// NewAPISignatureVerifier creates a new signature verifier
func NewAPISignatureVerifier(publicKeyBase64 string) (*APISignatureVerifier, error) {
	publicKeyBytes, err := base64.StdEncoding.DecodeString(publicKeyBase64)
	if err != nil {
		return nil, fmt.Errorf("failed to decode public key: %w", err)
	}

	if len(publicKeyBytes) != ed25519.PublicKeySize {
		return nil, fmt.Errorf("invalid public key size: expected %d, got %d", ed25519.PublicKeySize, len(publicKeyBytes))
	}

	return &APISignatureVerifier{
		publicKey: ed25519.PublicKey(publicKeyBytes),
	}, nil
}

// VerifyRequest verifies the signature of an API request
func (v *APISignatureVerifier) VerifyRequest(method, path, signatureHeader, timestampHeader string, body []byte) error {
	// Parse signature header
	if len(signatureHeader) < 9 || signatureHeader[:8] != "ed25519=" {
		return fmt.Errorf("invalid signature format")
	}
	signatureB64 := signatureHeader[8:]

	signature, err := base64.StdEncoding.DecodeString(signatureB64)
	if err != nil {
		return fmt.Errorf("failed to decode signature: %w", err)
	}

	// Parse timestamp
	timestamp, err := strconv.ParseInt(timestampHeader, 10, 64)
	if err != nil {
		return fmt.Errorf("invalid timestamp: %w", err)
	}

	// Check timestamp window (5 minutes)
	now := time.Now().Unix()
	timeDiff := now - timestamp
	if timeDiff < 0 {
		timeDiff = -timeDiff
	}
	if timeDiff > 300 { // 5 minutes
		return fmt.Errorf("timestamp outside allowed window")
	}

	// Create body hash
	bodyHash := sha256.Sum256(body)
	bodyHashStr := fmt.Sprintf("sha256:%x", bodyHash)

	// Create canonical request
	canonicalRequest := fmt.Sprintf("%s\n%s\n\n%s\n%s", method, path, timestampHeader, bodyHashStr)

	// Verify signature
	if !ed25519.Verify(v.publicKey, []byte(canonicalRequest), signature) {
		return fmt.Errorf("signature verification failed")
	}

	return nil
}

```

### File: internal\controllers\executor_controller.go
```go
package controllers

import (
	"encoding/json"

	executortypes "github.com/flowbaker/flowbaker/pkg/clients/flowbaker-executor"

	"github.com/flowbaker/flowbaker/pkg/domain/executor"
	"github.com/flowbaker/flowbaker/pkg/domain/mappers"

	"github.com/flowbaker/flowbaker/pkg/domain"

	"github.com/gofiber/fiber/v3"
	"github.com/rs/zerolog/log"
)

// ExecutorController handles API-initiated requests to executor services
// This controller is used when the API needs to send commands to executors
type ExecutorController struct {
	executorService              executor.WorkflowExecutorService
	workspaceRegistrationManager domain.WorkspaceRegistrationManager
}

type ExecutorControllerDependencies struct {
	WorkflowExecutorService      executor.WorkflowExecutorService
	WorkspaceRegistrationManager domain.WorkspaceRegistrationManager
}

func NewExecutorController(deps ExecutorControllerDependencies) *ExecutorController {
	return &ExecutorController{
		executorService:              deps.WorkflowExecutorService,
		workspaceRegistrationManager: deps.WorkspaceRegistrationManager,
	}
}

func (c *ExecutorController) RegisterWorkspace(ctx fiber.Ctx) error {
	log.Info().Msg("Registering workspace")

	var req executortypes.RegisterWorkspaceRequest

	if err := ctx.Bind().Body(&req); err != nil {
		return fiber.NewError(fiber.StatusBadRequest, "Invalid request body")
	}

	p := domain.RegisterWorkspaceParams{
		ExecutorID: req.ExecutorID,
		Passcode:   req.Passcode,
		Assignment: domain.WorkspaceAssignment{
			WorkspaceID:   req.Assignment.WorkspaceID,
			WorkspaceName: req.Assignment.WorkspaceName,
			WorkspaceSlug: req.Assignment.WorkspaceSlug,
			APIPublicKey:  req.Assignment.APIPublicKey,
		},
	}

	err := c.workspaceRegistrationManager.TryRegisterWorkspace(ctx.RequestCtx(), p)
	if err != nil {
		log.Error().Err(err).Msg("Failed to register workspace")
		return fiber.NewError(fiber.StatusInternalServerError, "Failed to register workspace")
	}

	return ctx.JSON(executortypes.RegisterWorkspaceResponse{
		Success: true,
	})
}

// StartExecution handles the start of a workflow execution
func (c *ExecutorController) StartExecution(ctx fiber.Ctx) error {
	workspaceID := ctx.Params("workspaceID")
	if workspaceID == "" {
		return fiber.NewError(fiber.StatusBadRequest, "Workspace ID is required")
	}

	var req executortypes.StartExecutionRequest

	if err := ctx.Bind().Body(&req); err != nil {
		return fiber.NewError(fiber.StatusBadRequest, "Invalid request body")
	}

	isTestingWorkflow := req.WorkflowType == executortypes.WorkflowTypeTesting

	if isTestingWorkflow {
		req.Workflow = &req.TestingWorkflow.Workflow
	}

	p := executor.ExecuteParams{
		ExecutionID:       req.ExecutionID,
		Workflow:          mappers.ExecutorWorkflowToDomain(req.Workflow),
		EventName:         req.EventName,
		PayloadJSON:       string(req.PayloadJSON),
		EnableEvents:      req.EnableEvents,
		IsTestingWorkflow: isTestingWorkflow,
	}

	if isTestingWorkflow {
		p.UserID = req.UserID
	}

	result, err := c.executorService.Execute(ctx.RequestCtx(), p)
	if err != nil {
		return fiber.NewError(fiber.StatusInternalServerError, "Failed to execute workflow")
	}

	response := executortypes.ExecutionResult{
		Payload:    result.Payload,
		Headers:    result.Headers,
		StatusCode: result.StatusCode,
	}

	return ctx.JSON(response)
}

func (c *ExecutorController) RerunNode(ctx fiber.Ctx) error {
	workspaceID := ctx.Params("workspaceID")
	if workspaceID == "" {
		return fiber.NewError(fiber.StatusBadRequest, "Workspace ID is required")
	}

	var req executortypes.RerunNodeRequest

	if err := ctx.Bind().Body(&req); err != nil {
		return fiber.NewError(fiber.StatusBadRequest, "Invalid request body")
	}

	result, err := c.executorService.RerunNode(ctx.RequestCtx(), executor.RerunNodeParams{
		ExecutionID:        req.ExecutionID,
		WorkspaceID:        workspaceID,
		NodeID:             req.NodeID,
		NodeExecutionEntry: mappers.FlowbakerNodeExecutionEntryToDomain(req.NodeExecutionEntry),
		Workflow:           mappers.ExecutorWorkflowToDomain(&req.Workflow),
	})
	if err != nil {
		log.Error().Err(err).Msg("Failed to rerun node")
		return fiber.NewError(fiber.StatusInternalServerError, "Failed to rerun node")
	}

	return ctx.JSON(executortypes.RerunNodeResponse{
		Payload: result.Payload,
	})
}

func (c *ExecutorController) RunNode(ctx fiber.Ctx) error {
	workspaceID := ctx.Params("workspaceID")
	if workspaceID == "" {
		return fiber.NewError(fiber.StatusBadRequest, "Workspace ID is required")
	}

	var req executortypes.RunNodeRequest
	if err := ctx.Bind().Body(&req); err != nil {
		return fiber.NewError(fiber.StatusBadRequest, "Invalid request body")
	}

	itemsByInputIndex := map[int][]domain.Item{}
	for idx, raw := range req.ItemsByInputIndex {
		var items []domain.Item
		if err := json.Unmarshal(raw, &items); err != nil {
			return fiber.NewError(fiber.StatusBadRequest, "Invalid items format")
		}
		itemsByInputIndex[idx] = items
	}

	result, err := c.executorService.RunNode(ctx.RequestCtx(), executor.RunNodeParams{
		ExecutionID:       req.ExecutionID,
		NodeID:            req.NodeID,
		Workflow:          mappers.ExecutorWorkflowToDomain(&req.Workflow),
		ItemsByInputIndex: itemsByInputIndex,
		WorkspaceID:       workspaceID,
	})
	if err != nil {
		log.Error().Err(err).Msg("Failed to run node")
		return fiber.NewError(fiber.StatusInternalServerError, "Failed to run node")
	}

	return ctx.JSON(executortypes.RunNodeResponse{
		Results: result.Results,
	})
}

func (c *ExecutorController) StopExecution(ctx fiber.Ctx) error {
	executionID := ctx.Params("executionID")
	if executionID == "" {
		return fiber.NewError(fiber.StatusBadRequest, "Execution ID is required")
	}

	// it should return success no matter what
	err := c.executorService.Stop(ctx.RequestCtx(), executionID)
	if err != nil {
		return ctx.JSON(executortypes.StopExecutionResponse{
			Success: true,
		})
	}

	return ctx.JSON(executortypes.StopExecutionResponse{
		Success: true,
	})
}

// HandlePollingEvent handles a polling event request from the API
func (c *ExecutorController) HandlePollingEvent(ctx fiber.Ctx) error {
	workspaceID := ctx.Params("workspaceID")
	if workspaceID == "" {
		return fiber.NewError(fiber.StatusBadRequest, "Workspace ID is required")
	}

	var req executortypes.PollingEventRequest

	if err := ctx.Bind().Body(&req); err != nil {
		return fiber.NewError(fiber.StatusBadRequest, "Invalid request body")
	}

	// Convert executor types to domain types
	pollingEvent := domain.PollingEvent{
		IntegrationType: domain.IntegrationType(req.IntegrationType),
		Trigger:         mappers.ExecutorWorkflowNodeToDomain(req.Trigger),
		Workflow:        mappers.ExecutorWorkflowToDomain(&req.Workflow),
		UserID:          req.UserID,
		WorkflowType:    mappers.ExecutorWorkflowTypeToDomain(req.WorkflowType),
		WorkspaceID:     workspaceID,
	}

	// Call the executor service to handle the polling event
	result, err := c.executorService.HandlePollingEvent(ctx.RequestCtx(), pollingEvent)
	if err != nil {
		log.Error().Err(err).Msg("Failed to handle polling event")
		return fiber.NewError(fiber.StatusInternalServerError, "Failed to handle polling event")
	}

	response := executortypes.PollingEventResponse{
		LastModifiedData: result.LastModifiedData,
	}

	return ctx.JSON(response)
}

// TestConnection handles connection testing requests from the API
func (c *ExecutorController) TestConnection(ctx fiber.Ctx) error {
	workspaceID := ctx.Params("workspaceID")
	if workspaceID == "" {
		return fiber.NewError(fiber.StatusBadRequest, "Workspace ID is required")
	}

	var req executortypes.ConnectionTestRequest

	if err := ctx.Bind().Body(&req); err != nil {
		return fiber.NewError(fiber.StatusBadRequest, "Invalid request body")
	}

	log.Info().
		Str("integration_type", string(req.IntegrationType)).
		Str("credential_id", req.CredentialID).
		Str("workspace_id", workspaceID).
		Msg("Testing connection")

	// Call the executor service to test the connection
	success, err := c.executorService.TestConnection(ctx.RequestCtx(), executor.TestConnectionParams{
		IntegrationType: domain.IntegrationType(req.IntegrationType),
		CredentialID:    req.CredentialID,
		WorkspaceID:     workspaceID,
		Payload:         req.Payload,
	})
	if err != nil {
		log.Error().Err(err).Msg("Failed to test connection")
		return ctx.JSON(executortypes.ConnectionTestResponse{
			Success: false,
			Error:   err.Error(),
		})
	}

	return ctx.JSON(executortypes.ConnectionTestResponse{
		Success: success,
	})
}

func (c *ExecutorController) PeekData(ctx fiber.Ctx) error {
	workspaceID := ctx.Params("workspaceID")
	if workspaceID == "" {
		return fiber.NewError(fiber.StatusBadRequest, "Workspace ID is required")
	}

	var req executortypes.PeekDataRequest

	if err := ctx.Bind().Body(&req); err != nil {
		return fiber.NewError(fiber.StatusBadRequest, "Invalid request body")
	}

	var pagination domain.PaginationParams
	if req.Pagination != nil {
		pagination = *req.Pagination
	}

	result, err := c.executorService.PeekData(ctx.RequestCtx(), executor.PeekDataParams{
		IntegrationType: domain.IntegrationType(req.IntegrationType),
		CredentialID:    req.CredentialID,
		WorkspaceID:     workspaceID,
		UserID:          req.UserID,
		PeekableType:    req.PeekableType,
		Cursor:          req.Cursor,
		Pagination:      pagination,
		PayloadJSON:     req.PayloadJSON,
	})
	if err != nil {
		log.Error().Err(err).Msg("Failed to peek data")

		ctx.Status(fiber.StatusInternalServerError)

		return ctx.JSON(executortypes.PeekDataResponse{
			Success: false,
			Error:   err.Error(),
		})
	}

	return ctx.JSON(executortypes.PeekDataResponse{
		Success:    true,
		Result:     mappers.DomainPeekResultItemsToExecutor(result.Result),
		Pagination: result.Pagination,
	})
}

func (c *ExecutorController) UnregisterWorkspace(ctx fiber.Ctx) error {
	workspaceID := ctx.Params("workspaceID")
	if workspaceID == "" {
		return fiber.NewError(fiber.StatusBadRequest, "Workspace ID is required")
	}

	err := c.workspaceRegistrationManager.UnregisterWorkspace(ctx.RequestCtx(), workspaceID)
	if err != nil {
		log.Error().Err(err).Msg("Failed to unregister workspace")
		return fiber.NewError(fiber.StatusInternalServerError, "Failed to unregister workspace")
	}

	return ctx.JSON(executortypes.UnregisterWorkspaceResponse{
		Success: true,
	})
}

```

### File: internal\version\version.go
```go
package version

import (
	"fmt"
	"runtime"
	"runtime/debug"
)

var (
	// Version is the semantic version (set by ldflags during build)
	Version = "dev"
	
	// GitCommit is the git commit hash (set by ldflags during build)
	GitCommit = ""
	
	// BuildDate is the build date (set by ldflags during build)
	BuildDate = ""
	
	// BuildUser is the user who built the binary (set by ldflags during build)
	BuildUser = ""
)

// Info represents version and build information
type Info struct {
	Version   string `json:"version"`
	GitCommit string `json:"git_commit,omitempty"`
	BuildDate string `json:"build_date,omitempty"`
	BuildUser string `json:"build_user,omitempty"`
	GoVersion string `json:"go_version"`
	Platform  string `json:"platform"`
}

// Get returns the version information
func Get() Info {
	return Info{
		Version:   getVersion(),
		GitCommit: GitCommit,
		BuildDate: BuildDate,
		BuildUser: BuildUser,
		GoVersion: runtime.Version(),
		Platform:  fmt.Sprintf("%s/%s", runtime.GOOS, runtime.GOARCH),
	}
}

// GetVersion returns the version string
func GetVersion() string {
	return getVersion()
}

// getVersion returns the version, falling back to build info if ldflags version is not set
func getVersion() string {
	if Version != "" && Version != "dev" {
		return Version
	}
	
	// Fallback to build info
	if info, ok := debug.ReadBuildInfo(); ok {
		if info.Main.Version != "(devel)" && info.Main.Version != "" {
			return info.Main.Version
		}
	}
	
	return "dev"
}

// GetShortVersion returns a short version string
func GetShortVersion() string {
	version := getVersion()
	if GitCommit != "" && len(GitCommit) >= 7 {
		return fmt.Sprintf("%s-%s", version, GitCommit[:7])
	}
	return version
}
```

### File: pkg\integrations\chat\schema.go
```go
package chat

import (
	"github.com/flowbaker/flowbaker/pkg/domain"
)

const (
	IntegrationTriggerType_ChatMessageReceived domain.IntegrationTriggerEventType = "chat_message_received"
)

var (
	Schema = schema

	schema domain.Integration = domain.Integration{
		ID:          domain.IntegrationType_ChatTrigger,
		Name:        "Chat Trigger",
		Description: "Trigger workflows from chat messages",
		Triggers: []domain.IntegrationTrigger{
			{
				ID:          "chat_message_received",
				Name:        "Chat Message Received",
				EventType:   IntegrationTriggerType_ChatMessageReceived,
				Description: "Triggered when a chat message is received",
				HandlesByContext: map[domain.ActionUsageContext]domain.ContextHandles{
					domain.UsageContextWorkflow: {
						Output: []domain.NodeHandle{
							{
								Type:         domain.NodeHandleTypeDefault,
								Position:     domain.NodeHandlePositionBottom,
								Text:         "Agent",
								UsageContext: domain.UsageContextWorkflow,
								AllowedIntegrations: []domain.IntegrationType{
									domain.IntegrationType_AIAgent,
								},
							},
						},
					},
				},
			},
		},
	}
)

```

### File: pkg\integrations\gemini\schema.go
```go
package gemini

import (
	"github.com/flowbaker/flowbaker/pkg/domain"
)

var (
	GeminiSchema = domain.Integration{
		ID:          domain.IntegrationType_Gemini,
		Name:        "Google Gemini",
		Description: "Use Google's Gemini AI models to generate content and analyze text.",
		CredentialProperties: []domain.NodeProperty{
			{
				Key:         "api_key",
				Name:        "API Key",
				Description: "The Google AI API key for authentication",
				Required:    true,
				Type:        domain.NodePropertyType_String,
			},
		},
		Actions: []domain.IntegrationAction{
			{
				ID:          "ai_agent_chat",
				Name:        "AI Agent Chat",
				ActionType:  "ai_agent_chat",
				Description: "Use Gemini for AI agent conversation",
				SupportedContexts: []domain.ActionUsageContext{
					domain.UsageContextLLMProvider,
				},
				Properties: []domain.NodeProperty{
					{
						Key:         "model",
						Name:        "Model",
						Description: "The Gemini model to use",
						Required:    true,
						Type:        domain.NodePropertyType_String,
						Options:     modelOptions,
					},
					{
						Key:         "temperature",
						Name:        "Temperature",
						Description: "Controls randomness in the output. Higher values make output more random",
						Required:    false,
						Type:        domain.NodePropertyType_Number,
						Advanced:    true,
						NumberOpts: &domain.NumberPropertyOptions{
							Min:  0,
							Max:  2,
							Step: 0.1,
						},
					},
					{
						Key:         "max_tokens",
						Name:        "Max Tokens",
						Description: "The maximum number of tokens to generate",
						Required:    false,
						Type:        domain.NodePropertyType_Integer,
					},
					{
						Key:         "top_p",
						Name:        "Top P",
						Description: "The top P value to use for nucleus sampling",
						Required:    false,
						Type:        domain.NodePropertyType_Number,
						Advanced:    true,
						NumberOpts: &domain.NumberPropertyOptions{
							Min:  0,
							Max:  1,
							Step: 0.01,
						},
					},
					{
						Key:         "top_k",
						Name:        "Top K",
						Description: "Only sample from the top K options for each subsequent token",
						Required:    false,
						Type:        domain.NodePropertyType_Integer,
						Advanced:    true,
					},
				},
			},
		},
		Triggers: []domain.IntegrationTrigger{},
	}
)

var modelOptions = []domain.NodePropertyOption{
	// Gemini 3 models (Preview)
	{Label: "Gemini 3 Pro (Preview)", Value: "gemini-3-pro-preview"},
	{Label: "Gemini 3 Flash (Preview)", Value: "gemini-3-flash-preview"},

	// Gemini 2.5 models (Stable)
	{Label: "Gemini 2.5 Pro", Value: "gemini-2.5-pro"},
	{Label: "Gemini 2.5 Flash", Value: "gemini-2.5-flash"},
	{Label: "Gemini 2.5 Flash Lite", Value: "gemini-2.5-flash-lite"},

	// Gemini 2.0 models
	{Label: "Gemini 2.0 Flash", Value: "gemini-2.0-flash"},
	{Label: "Gemini 2.0 Flash Lite", Value: "gemini-2.0-flash-lite"},
}

```

### File: pkg\integrations\github\github_connection_tester.go
```go
package githubintegration

import (
	"context"
	"fmt"
	"net/http"

	"github.com/flowbaker/flowbaker/internal/managers"

	"github.com/flowbaker/flowbaker/pkg/domain"

	"github.com/google/go-github/v57/github"
	"github.com/rs/zerolog/log"
	"golang.org/x/oauth2"
)

type GitHubConnectionTester struct {
	credentialGetter domain.CredentialGetter[domain.OAuthAccountSensitiveData]
}

func NewGitHubConnectionTester(deps domain.IntegrationDeps) domain.IntegrationConnectionTester {
	return &GitHubConnectionTester{
		credentialGetter: managers.NewExecutorCredentialGetter[domain.OAuthAccountSensitiveData](deps.ExecutorCredentialManager),
	}
}

func (c *GitHubConnectionTester) TestConnection(ctx context.Context, params domain.TestConnectionParams) (bool, error) {
	// GitHub uses OAuth credentials, so we need to get the OAuth account
	// using the credential ID (the service will handle the OAuth account lookup)
	if params.Credential.Type != domain.CredentialTypeOAuth && params.Credential.Type != domain.CredentialTypeOAuthWithParams {
		log.Error().Str("credential_type", string(params.Credential.Type)).Msg("Invalid credential type for GitHub - OAuth required")
		return false, fmt.Errorf("invalid credential type %s - GitHub requires OAuth authentication", params.Credential.Type)
	}

	// Get the OAuth account using the credential ID (not the OAuth account ID)
	oauthAccount, err := c.credentialGetter.GetDecryptedCredential(ctx, params.Credential.ID)
	if err != nil {
		log.Error().Err(err).Str("credential_id", params.Credential.ID).Msg("Failed to get decrypted GitHub OAuth credential")
		return false, fmt.Errorf("failed to get decrypted GitHub OAuth credential: %w", err)
	}

	// Create OAuth2 token source using the OAuth account structure
	ts := oauth2.StaticTokenSource(
		&oauth2.Token{AccessToken: oauthAccount.AccessToken},
	)
	tc := oauth2.NewClient(ctx, ts)

	// Create GitHub client
	client := github.NewClient(tc)

	// Test the connection by getting the authenticated user
	user, response, err := client.Users.Get(ctx, "")
	if err != nil {
		log.Error().Err(err).Msg("Failed to get authenticated user from GitHub")
		return false, fmt.Errorf("failed to authenticate with GitHub: %w", err)
	}

	// Check if response status is OK
	if response.StatusCode != http.StatusOK {
		log.Error().Int("status_code", response.StatusCode).Msg("GitHub API returned non-OK status")
		return false, fmt.Errorf("GitHub API returned status %d", response.StatusCode)
	}

	// Log successful connection
	if user.Login != nil {
		log.Info().Str("user", *user.Login).Msg("Successfully connected to GitHub")
	} else {
		log.Info().Msg("Successfully connected to GitHub")
	}

	return true, nil
}

```

### File: pkg\integrations\github\github_integration.go
```go
package githubintegration

import (
	"context"
	"encoding/json"
	"fmt"
	"strconv"
	"strings"
	"time"

	"github.com/flowbaker/flowbaker/internal/managers"

	"github.com/flowbaker/flowbaker/pkg/domain"

	"github.com/google/go-github/v57/github" // Assuming a recent version, adjust if necessary
	"golang.org/x/oauth2"
)

const (
	// File Actions
	GithubActionType_CreateFile domain.IntegrationActionType = "create_file"
	GithubActionType_DeleteFile domain.IntegrationActionType = "delete_file"
	GithubActionType_EditFile   domain.IntegrationActionType = "edit_file"
	GithubActionType_GetFile    domain.IntegrationActionType = "get_file"
	GithubActionType_ListFiles  domain.IntegrationActionType = "list_files"

	// Organization Actions
	GithubActionType_OrgGetRepositories domain.IntegrationActionType = "org_get_repositories"

	// Release Actions
	GithubActionType_CreateRelease domain.IntegrationActionType = "create_release"
	GithubActionType_DeleteRelease domain.IntegrationActionType = "delete_release"
	GithubActionType_GetRelease    domain.IntegrationActionType = "get_release"
	GithubActionType_ListReleases  domain.IntegrationActionType = "list_releases"
	GithubActionType_UpdateRelease domain.IntegrationActionType = "update_release"

	// Repository Actions
	GithubActionType_GetRepository           domain.IntegrationActionType = "get_repository"
	GithubActionType_GetRepositoryIssues     domain.IntegrationActionType = "get_repository_issues"
	GithubActionType_GetRepositoryLicense    domain.IntegrationActionType = "get_repository_license"
	GithubActionType_GetRepositoryProfile    domain.IntegrationActionType = "get_repository_profile"
	GithubActionType_GetRepositoryPRs        domain.IntegrationActionType = "get_repository_prs"
	GithubActionType_ListPopularPaths        domain.IntegrationActionType = "list_popular_paths"
	GithubActionType_ListRepositoryReferrers domain.IntegrationActionType = "list_repository_referrers"

	// Review Actions
	GithubActionType_CreateReview domain.IntegrationActionType = "create_review"
	GithubActionType_GetReview    domain.IntegrationActionType = "get_review"
	GithubActionType_ListReviews  domain.IntegrationActionType = "list_reviews"
	GithubActionType_UpdateReview domain.IntegrationActionType = "update_review"

	// User Actions
	GithubActionType_UserGetRepositories domain.IntegrationActionType = "user_get_repositories"
	GithubActionType_UserInvite          domain.IntegrationActionType = "user_invite"

	// Issue Actions
	GithubActionType_CreateIssue        domain.IntegrationActionType = "create_issue"
	GithubActionType_CreateIssueComment domain.IntegrationActionType = "create_issue_comment"
	GithubActionType_EditIssue          domain.IntegrationActionType = "edit_issue"
	GithubActionType_GetIssue           domain.IntegrationActionType = "get_issue"
	GithubActionType_LockIssue          domain.IntegrationActionType = "lock_issue"

	// Peekable Types
	GithubPeekable_Repositories domain.IntegrationPeekableType = "repositories"
	GithubPeekable_Users        domain.IntegrationPeekableType = "users"
	GithubPeekable_Branches     domain.IntegrationPeekableType = "branches"
)

type GithubIntegrationCreator struct {
	binder           domain.IntegrationParameterBinder
	credentialGetter domain.CredentialGetter[domain.OAuthAccountSensitiveData]
	// Add other necessary services like routeService, oauthAccountRepo if needed for GitHub
}

func NewGithubIntegrationCreator(deps domain.IntegrationDeps) domain.IntegrationCreator {
	return &GithubIntegrationCreator{
		binder:           deps.ParameterBinder,
		credentialGetter: managers.NewExecutorCredentialGetter[domain.OAuthAccountSensitiveData](deps.ExecutorCredentialManager),
	}
}

func (c *GithubIntegrationCreator) CreateIntegration(ctx context.Context, p domain.CreateIntegrationParams) (domain.IntegrationExecutor, error) {
	return NewGithubIntegration(ctx, GithubIntegrationDependencies{
		CredentialID:     p.CredentialID,
		ParameterBinder:  c.binder,
		CredentialGetter: c.credentialGetter,
	})
}

type GithubIntegration struct {
	githubClient *github.Client

	binder           domain.IntegrationParameterBinder
	credentialGetter domain.CredentialGetter[domain.OAuthAccountSensitiveData]

	actionManager *domain.IntegrationActionManager

	peekFuncs map[domain.IntegrationPeekableType]func(ctx context.Context, params domain.PeekParams) (domain.PeekResult, error)
}

type GithubIntegrationDependencies struct {
	CredentialID string

	ParameterBinder  domain.IntegrationParameterBinder
	CredentialGetter domain.CredentialGetter[domain.OAuthAccountSensitiveData]
}

func NewGithubIntegration(ctx context.Context, deps GithubIntegrationDependencies) (*GithubIntegration, error) {
	integration := &GithubIntegration{
		binder:           deps.ParameterBinder,
		credentialGetter: deps.CredentialGetter,
	}

	actionManager := domain.NewIntegrationActionManager().
		AddPerItem(GithubActionType_CreateFile, integration.CreateFile).
		AddPerItem(GithubActionType_DeleteFile, integration.DeleteFile).
		AddPerItem(GithubActionType_EditFile, integration.EditFile).
		AddPerItem(GithubActionType_GetFile, integration.GetFile).
		AddPerItemMulti(GithubActionType_ListFiles, integration.ListFiles).
		AddPerItemMulti(GithubActionType_OrgGetRepositories, integration.OrgGetRepositories).
		AddPerItemMulti(GithubActionType_ListReleases, integration.ListReleases).
		AddPerItemMulti(GithubActionType_GetRepositoryIssues, integration.GetRepositoryIssues).
		AddPerItemMulti(GithubActionType_GetRepositoryPRs, integration.GetRepositoryPRs).
		AddPerItemMulti(GithubActionType_ListPopularPaths, integration.ListPopularPaths).
		AddPerItemMulti(GithubActionType_ListRepositoryReferrers, integration.ListRepositoryReferrers).
		AddPerItemMulti(GithubActionType_UserGetRepositories, integration.UserGetRepositories).
		AddPerItemMulti(GithubActionType_ListReviews, integration.ListReviews).
		AddPerItem(GithubActionType_CreateRelease, integration.CreateRelease).
		AddPerItem(GithubActionType_DeleteRelease, integration.DeleteRelease).
		AddPerItem(GithubActionType_GetRelease, integration.GetRelease).
		AddPerItem(GithubActionType_UpdateRelease, integration.UpdateRelease).
		AddPerItem(GithubActionType_GetRepository, integration.GetRepository).
		AddPerItem(GithubActionType_GetRepositoryLicense, integration.GetRepositoryLicense).
		AddPerItem(GithubActionType_GetRepositoryProfile, integration.GetRepositoryProfile).
		AddPerItem(GithubActionType_CreateReview, integration.CreateReview).
		AddPerItem(GithubActionType_GetReview, integration.GetReview).
		AddPerItem(GithubActionType_UpdateReview, integration.UpdateReview).
		AddPerItem(GithubActionType_UserInvite, integration.UserInvite).
		AddPerItem(GithubActionType_CreateIssue, integration.CreateIssue).
		AddPerItem(GithubActionType_CreateIssueComment, integration.CreateIssueComment).
		AddPerItem(GithubActionType_EditIssue, integration.EditIssue).
		AddPerItem(GithubActionType_GetIssue, integration.GetIssue).
		AddPerItem(GithubActionType_LockIssue, integration.LockIssue)

	peekFuncs := map[domain.IntegrationPeekableType]func(ctx context.Context, p domain.PeekParams) (domain.PeekResult, error){
		GithubPeekable_Repositories: integration.PeekRepositories,
		GithubPeekable_Users:        integration.PeekUsers,
		GithubPeekable_Branches:     integration.PeekBranches,
	}

	integration.actionManager = actionManager
	integration.peekFuncs = peekFuncs

	if deps.CredentialID == "" {
		return nil, fmt.Errorf("credential ID is required for GitHub integration")
	}

	oauthAccount, err := deps.CredentialGetter.GetDecryptedCredential(ctx, deps.CredentialID)
	if err != nil {
		return nil, fmt.Errorf("failed to get decrypted GitHub OAuth credential: %w", err)
	}

	ts := oauth2.StaticTokenSource(
		&oauth2.Token{AccessToken: oauthAccount.AccessToken},
	)
	tc := oauth2.NewClient(context.Background(), ts)
	integration.githubClient = github.NewClient(tc)

	return integration, nil
}

func (i *GithubIntegration) Execute(ctx context.Context, params domain.IntegrationInput) (domain.IntegrationOutput, error) {
	return i.actionManager.Run(ctx, params.ActionType, params)
}

func (i *GithubIntegration) parseOwnerRepo(ctx context.Context, repoID string) (string, string, error) {
	ownerRepo := strings.Split(repoID, "/")
	if len(ownerRepo) == 2 {
		return ownerRepo[0], ownerRepo[1], nil
	} else if len(ownerRepo) == 1 {
		user, _, err := i.githubClient.Users.Get(ctx, "")
		if err != nil || user.Login == nil {
			return "", "", fmt.Errorf("repository_id must be in 'owner/repo' format or an owner must be determinable: %v", err)
		}
		return *user.Login, repoID, nil
	} else {
		return "", "", fmt.Errorf("invalid repository_id format: %s", repoID)
	}
}

func (i *GithubIntegration) Peek(ctx context.Context, params domain.PeekParams) (domain.PeekResult, error) {
	peekFunc, ok := i.peekFuncs[params.PeekableType]
	if !ok {
		return domain.PeekResult{}, fmt.Errorf("peek function %s not found for GitHub integration", params.PeekableType)
	}
	return peekFunc(ctx, params)
}

func (i *GithubIntegration) CreateFile(ctx context.Context, input domain.IntegrationInput, item domain.Item) (domain.Item, error) {
	params := CreateFileParams{}
	if err := i.binder.BindToStruct(ctx, item, &params, input.IntegrationParams.Settings); err != nil {
		return nil, fmt.Errorf("failed to bind parameters: %w", err)
	}

	owner, repoName, err := i.parseOwnerRepo(ctx, params.Owner)
	if err != nil {
		return nil, err
	}

	contentBytes := []byte(params.Content)

	opts := &github.RepositoryContentFileOptions{
		Message: &params.Message,
		Content: contentBytes,
		Branch:  params.Branch,
	}

	content, _, err := i.githubClient.Repositories.CreateFile(ctx, owner, repoName, params.Path, opts)
	if err != nil {
		return nil, fmt.Errorf("failed to create file %s in %s/%s: %w", params.Path, owner, repoName, err)
	}

	return content, nil
}

func (i *GithubIntegration) DeleteFile(ctx context.Context, input domain.IntegrationInput, item domain.Item) (domain.Item, error) {
	params := DeleteFileParams{}
	if err := i.binder.BindToStruct(ctx, item, &params, input.IntegrationParams.Settings); err != nil {
		return nil, fmt.Errorf("failed to bind parameters: %w", err)
	}

	owner, repoName, err := i.parseOwnerRepo(ctx, params.Owner)
	if err != nil {
		return nil, err
	}

	if params.Path == "" {
		return nil, fmt.Errorf("path is required to delete a file")
	}
	if params.Message == "" {
		return nil, fmt.Errorf("message (commit message) is required to delete a file")
	}
	if params.SHA == "" {
		return nil, fmt.Errorf("sha is required to delete a file")
	}

	opts := &github.RepositoryContentFileOptions{
		Message: &params.Message,
		SHA:     &params.SHA,
		Branch:  params.Branch,
	}

	resp, _, err := i.githubClient.Repositories.DeleteFile(ctx, owner, repoName, params.Path, opts)
	if err != nil {
		return nil, fmt.Errorf("failed to delete file %s in %s/%s: %w", params.Path, owner, repoName, err)
	}

	return resp, nil
}

func (i *GithubIntegration) EditFile(ctx context.Context, input domain.IntegrationInput, item domain.Item) (domain.Item, error) {
	params := CreateFileParams{}
	if err := i.binder.BindToStruct(ctx, item, &params, input.IntegrationParams.Settings); err != nil {
		return nil, fmt.Errorf("failed to bind parameters: %w", err)
	}

	owner, repoName, err := i.parseOwnerRepo(ctx, params.Owner)
	if err != nil {
		return nil, err
	}

	if params.Path == "" {
		return nil, fmt.Errorf("path is required to update a file")
	}
	if params.Message == "" {
		return nil, fmt.Errorf("message (commit message) is required to update a file")
	}
	if params.Content == "" {
		return nil, fmt.Errorf("content is required to update a file")
	}
	if params.SHA == nil || *params.SHA == "" {
		return nil, fmt.Errorf("SHA is required to update file %s in %s/%s", params.Path, owner, repoName)
	}

	// Content is now plain text, convert directly to bytes for the GitHub library.
	contentBytes := []byte(params.Content)

	opts := &github.RepositoryContentFileOptions{
		Message: &params.Message,
		Content: contentBytes,
		SHA:     params.SHA, // SHA is required for update
		Branch:  params.Branch,
	}

	content, _, err := i.githubClient.Repositories.UpdateFile(ctx, owner, repoName, params.Path, opts)
	if err != nil {
		return nil, fmt.Errorf("failed to update file %s in %s/%s: %w", params.Path, owner, repoName, err)
	}

	return content, nil
}

func (i *GithubIntegration) GetFile(ctx context.Context, input domain.IntegrationInput, item domain.Item) (domain.Item, error) {
	params := GetFileParams{}
	if err := i.binder.BindToStruct(ctx, item, &params, input.IntegrationParams.Settings); err != nil {
		return nil, fmt.Errorf("failed to bind parameters: %w", err)
	}

	owner, repoName, err := i.parseOwnerRepo(ctx, params.Owner)
	if err != nil {
		return nil, err
	}
	if params.Path == "" {
		return nil, fmt.Errorf("path is required to get a file")
	}

	var opts *github.RepositoryContentGetOptions
	if params.Ref != nil && *params.Ref != "" {
		opts = &github.RepositoryContentGetOptions{Ref: *params.Ref}
	}

	fileContent, _, _, err := i.githubClient.Repositories.GetContents(ctx, owner, repoName, params.Path, opts)
	if err != nil {
		return nil, fmt.Errorf("failed to get file %s from %s/%s: %w", params.Path, owner, repoName, err)
	}
	if fileContent == nil {
		return nil, fmt.Errorf("path %s in %s/%s is a directory or does not exist as a file", params.Path, owner, repoName)
	}

	return fileContent, nil
}

func (i *GithubIntegration) ListFiles(ctx context.Context, input domain.IntegrationInput, item domain.Item) ([]domain.Item, error) {
	params := ListFilesParams{}
	if err := i.binder.BindToStruct(ctx, item, &params, input.IntegrationParams.Settings); err != nil {
		return nil, fmt.Errorf("failed to bind parameters: %w", err)
	}

	owner, repoName, err := i.parseOwnerRepo(ctx, params.Owner)
	if err != nil {
		return nil, err
	}

	var opts *github.RepositoryContentGetOptions
	if params.Ref != nil && *params.Ref != "" {
		opts = &github.RepositoryContentGetOptions{Ref: *params.Ref}
	}

	_, dirContents, _, err := i.githubClient.Repositories.GetContents(ctx, owner, repoName, params.Path, opts)
	if err != nil {
		return nil, fmt.Errorf("failed to list files/directories at path '%s' in %s/%s: %w", params.Path, owner, repoName, err)
	}

	items := make([]domain.Item, 0)

	for _, dirContent := range dirContents {
		items = append(items, dirContent)
	}

	return items, nil
}

func (i *GithubIntegration) OrgGetRepositories(ctx context.Context, input domain.IntegrationInput, item domain.Item) ([]domain.Item, error) {
	params := OrgGetRepositoriesParams{}
	if err := i.binder.BindToStruct(ctx, item, &params, input.IntegrationParams.Settings); err != nil {
		return nil, fmt.Errorf("failed to bind parameters: %w", err)
	}

	if params.Org == "" {
		return nil, fmt.Errorf("organization name (org) is required")
	}

	limit := 30
	if params.Limit != nil && *params.Limit > 0 && *params.Limit <= 100 {
		limit = *params.Limit
	}

	p
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
