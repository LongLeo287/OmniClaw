#!/usr/bin/env node

const fs = require("fs");
const path = require("path");
const childProcess = require("child_process");

const WORKSPACE_MARKERS = [
  "brain/rules/_DIR_IDENTITY.md",
  "ecosystem/_REGIONAL_MAP.md",
];

const REQUIRED_FILES = [
  "brain/rules/_DIR_IDENTITY.md",
  "ecosystem/_REGIONAL_MAP.md",
  "ecosystem/bridges/docker-compose.yml",
  "core/scripts/tool_loader.py",
  "core/scripts/skill_assimilator.py",
  "core/scripts/generate_ecosystem_root_map.py",
  "core/docs/usage_guides/activation_guide.md",
];

function exists(target) {
  try {
    fs.accessSync(target, fs.constants.F_OK);
    return true;
  } catch {
    return false;
  }
}

function hasWorkspaceMarkers(rootDir) {
  return WORKSPACE_MARKERS.every((relativePath) =>
    exists(path.join(rootDir, relativePath)),
  );
}

function findWorkspaceRoot(startDir) {
  let currentDir = path.resolve(startDir);

  while (true) {
    if (hasWorkspaceMarkers(currentDir)) {
      return currentDir;
    }

    const parentDir = path.dirname(currentDir);
    if (parentDir === currentDir) {
      return null;
    }

    currentDir = parentDir;
  }
}

function getWorkspaceRoot() {
  const explicitRoot = process.env.OMNICLAW_ROOT
    ? path.resolve(process.env.OMNICLAW_ROOT)
    : null;

  if (explicitRoot && hasWorkspaceMarkers(explicitRoot)) {
    return explicitRoot;
  }

  return findWorkspaceRoot(process.cwd()) || explicitRoot;
}

function getExternalRoots(workspaceRoot) {
  const siblingRoot = workspaceRoot ? path.dirname(workspaceRoot) : process.cwd();

  return {
    OMNICLAW_ROOT: workspaceRoot || "(unresolved)",
    OMNICLAW_REMOTE_ROOT:
      process.env.OMNICLAW_REMOTE_ROOT || path.join(siblingRoot, "OmniClaw REMOTE"),
    OMNICLAW_UI_ROOT:
      process.env.OMNICLAW_UI_ROOT || path.join(siblingRoot, "OmniClaw UI"),
    OMNICLAW_MODELS_ROOT:
      process.env.OMNICLAW_MODELS_ROOT || path.join(siblingRoot, "OmniClaw_Models"),
  };
}

function commandExists(command) {
  const probe = process.platform === "win32" ? "where" : "which";
  const result = childProcess.spawnSync(probe, [command], {
    stdio: "ignore",
    shell: false,
  });
  return result.status === 0;
}

function printHelp() {
  console.log("OmniClaw bootstrap CLI");
  console.log("");
  console.log("Usage:");
  console.log("  omniclaw help");
  console.log("  omniclaw doctor");
  console.log("  omniclaw paths");
  console.log("");
  console.log("Notes:");
  console.log("  Run inside an OmniClaw clone, or set OMNICLAW_ROOT first.");
  console.log("  OmniClaw REMOTE and OmniClaw UI are optional external projects.");
}

function printPaths() {
  const workspaceRoot = getWorkspaceRoot();
  const roots = getExternalRoots(workspaceRoot);

  console.log("Resolved OmniClaw paths");
  console.log("");
  Object.entries(roots).forEach(([key, value]) => {
    console.log(`${key}: ${value}`);
  });
}

function runDoctor() {
  const workspaceRoot = getWorkspaceRoot();

  if (!workspaceRoot || !hasWorkspaceMarkers(workspaceRoot)) {
    console.error("Workspace root not found.");
    console.error("Run this inside an OmniClaw clone, or set OMNICLAW_ROOT.");
    process.exitCode = 1;
    return;
  }

  let failed = false;

  console.log(`Workspace root: ${workspaceRoot}`);
  console.log("");
  console.log("Required files");

  REQUIRED_FILES.forEach((relativePath) => {
    const filePath = path.join(workspaceRoot, relativePath);
    const ok = exists(filePath);
    console.log(`${ok ? "OK " : "ERR"} ${relativePath}`);
    if (!ok) {
      failed = true;
    }
  });

  console.log("");
  console.log("Runtime checks");

  const runtimeChecks = [
    ["git", commandExists("git"), true],
    ["node", commandExists("node"), true],
    ["python", commandExists("python") || commandExists("py"), true],
    ["docker", commandExists("docker"), false],
  ];

  runtimeChecks.forEach(([name, ok, required]) => {
    const label = ok ? "OK " : required ? "ERR" : "WARN";
    const suffix = required ? "" : " (optional)";
    console.log(`${label} ${name}${suffix}`);
    if (!ok && required) {
      failed = true;
    }
  });

  console.log("");
  console.log("External roots");
  const roots = getExternalRoots(workspaceRoot);
  Object.entries(roots).forEach(([key, value]) => {
    const configured = process.env[key] ? "env" : "default";
    console.log(`OK  ${key}: ${value} [${configured}]`);
  });

  if (failed) {
    console.error("");
    console.error("Doctor found blocking issues.");
    process.exitCode = 1;
    return;
  }

  console.log("");
  console.log("Doctor completed without blocking issues.");
}

function main() {
  const command = (process.argv[2] || "help").toLowerCase();

  switch (command) {
    case "help":
    case "--help":
    case "-h":
      printHelp();
      break;
    case "paths":
      printPaths();
      break;
    case "doctor":
      runDoctor();
      break;
    default:
      console.error(`Unknown command: ${command}`);
      console.error("Run `omniclaw help` for usage.");
      process.exitCode = 1;
  }
}

main();
