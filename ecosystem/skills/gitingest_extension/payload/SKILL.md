---
owner: Dept 1
forged_at: 2026-04-08T13:47:36.659700
status: active_forge
---

# gitingest Extension

## Overview
This extension provides a Flask API to fetch and process data from a specified Git repository. It supports specifying the repository URL and branch.

## Usage
1. Ensure you have the necessary dependencies installed.
2. Set up environment variables for your Git token and repository path.
3. Run the application and make POST requests to `/api/v1/gitingest` with JSON data containing `repo_url` and optionally `branch`.