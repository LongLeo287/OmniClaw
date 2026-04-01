#!/usr/bin/env node
const { execSync } = require('child_process');
const path = require('path');

const args = process.argv.slice(2);
if (args.length > 1) {
    console.warn(`⚠️ [Warning] Extra argument: "${args.slice(1).join(' ')}" - will be ignored.`);
}
const command = args[0] || 'start';

const rootDir = path.resolve(__dirname, '..');
const setupPath = path.join(rootDir, 'setup.ps1');

if (command === 'setup' || command === 'start') {
    console.log("🚀 [OmniClaw] Loading System Controller (Kernel)...");
    try {
        const { execFileSync } = require('child_process');
        execFileSync('powershell', ['-ExecutionPolicy', 'Bypass', '-File', setupPath], { stdio: 'inherit', cwd: rootDir });
    } catch (e) {
        console.error("❌ [OmniClaw] Execution interrupted or errored.");
        console.error(`Chi tiết lỗi: ${e.message}`);
        process.exit(1);
    }
} else {
    console.log(`Invalid command: omniclaw ${command}`);
    console.log(`Please use: omniclaw (Start dashboard) omniclaw (Start dashboard)`);
}
