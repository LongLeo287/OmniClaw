import { unlinkSync, writeFileSync } from "node:fs";
import { addLogEntry, loadLogs, saveLogs } from "./packages/core/src/logger";

/**
 * Reproduces the issues.
 */
async function repro() {
	const testFile = "./test-repro.csv";

	// 1. Create a CSV with rows missing id and created-at
	const initialCSV = "name,problem\nOld Task,Old Problem\n";
	writeFileSync(testFile, initialCSV);

	console.log("Initial file content:");
	console.log(initialCSV);

	// 2. Load logs
	let entries = await loadLogs(testFile);
	console.log(`Loaded ${entries.length} entries.`);

	// 3. Add a new entry
	entries = addLogEntry(entries, {
		name: "New Task",
		problem: "New Problem",
	});
	console.log(`After adding, total entries: ${entries.length}`);

	// 4. Save logs
	await saveLogs(testFile, entries);

	// 5. Read file back
	const finalCSV = await Bun.file(testFile).text();
	console.log("Final file content:");
	console.log(finalCSV);

	unlinkSync(testFile);
}

repro();
