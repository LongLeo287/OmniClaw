# Knowledge Dump for antigravity-switcher

## File: README.md
```
# Antigravity Switcher

A native macOS menu bar application to easily switch between **Antigravity** accounts.

## Features

- **Backup Accounts**: Save the current state of your Antigravity app (database) as a backup.
- **Switch Accounts**: Seamlessly switch between saved accounts. The Antigravity app stays open during the switch!
- **Manage Accounts**: Remove old or unused account backups directly from the menu.
- **Native Experience**: Runs quietly in your menu bar.

## Requirements

- macOS 13.0+
- Swift 5.9+

## Building

To build the application, run the provided build script:

```bash
./build.sh
```

The application will be built to: `build/AntigravityMenuBar.app`

## Installation

1. Build the app using the command above.
2. Drag `build/AntigravityMenuBar.app` to your `Applications` folder.
3. Launch the app. It will appear in your menu bar with a "person" icon.

```

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_antigravity-switcher_152026



================================================
FILE: README.md
================================================
# Antigravity Switcher

A native macOS menu bar application to easily switch between **Antigravity** accounts.

## Features

- **Backup Accounts**: Save the current state of your Antigravity app (database) as a backup.
- **Switch Accounts**: Seamlessly switch between saved accounts. The Antigravity app stays open during the switch!
- **Manage Accounts**: Remove old or unused account backups directly from the menu.
- **Native Experience**: Runs quietly in your menu bar.

## Requirements

- macOS 13.0+
- Swift 5.9+

## Building

To build the application, run the provided build script:

```bash
./build.sh
```

The application will be built to: `build/AntigravityMenuBar.app`

## Installation

1. Build the app using the command above.
2. Drag `build/AntigravityMenuBar.app` to your `Applications` folder.
3. Launch the app. It will appear in your menu bar with a "person" icon.

```

## File: .github\workflows\build.yml
```
name: Build MacOS App

on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]

jobs:
  build:
    name: Build and Package
    runs-on: macos-14
    
    permissions:
      contents: write

    steps:
    - name: Checkout
      uses: actions/checkout@v4
      with:
        fetch-depth: '0'

    - name: Make build script executable
      run: chmod +x build.sh
      
    - name: Build App
      run: ./build.sh

    - name: Zip Application
      run: |
        cd build
        zip -r AntigravityMenuBar.zip AntigravityMenuBar.app

    - name: Bump version and push tag
      id: tag_version
      if: github.event_name == 'push' && github.ref == 'refs/heads/master'
      uses: mathieudutour/github-tag-action@v6.2
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}

    - name: Create Release
      if: github.event_name == 'push' && github.ref == 'refs/heads/master'
      uses: softprops/action-gh-release@v2
      with:
        tag_name: ${{ steps.tag_version.outputs.new_tag }}
        name: Release ${{ steps.tag_version.outputs.new_tag }}
        body: ${{ steps.tag_version.outputs.changelog }}
        files: build/AntigravityMenuBar.zip
      
    - name: Upload Artifact
      uses: actions/upload-artifact@v4
      with:
        name: AntigravityMenuBar
        path: build/AntigravityMenuBar.zip
        if-no-files-found: error

```

