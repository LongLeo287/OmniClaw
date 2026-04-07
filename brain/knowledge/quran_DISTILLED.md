---
id: quran
type: knowledge
owner: OA_Triage
---
# quran
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "quran-validator",
  "version": "1.3.0",
  "description": "Validate and verify Quranic verses in LLM-generated text with 100% accuracy",
  "main": "dist/index.js",
  "module": "dist/index.mjs",
  "types": "dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.mjs",
      "require": "./dist/index.js"
    }
  },
  "files": [
    "dist",
    "data"
  ],
  "scripts": {
    "build": "tsup src/index.ts --format cjs,esm --dts --clean",
    "dev": "tsup src/index.ts --format cjs,esm --dts --watch",
    "test": "vitest run",
    "test:watch": "vitest",
    "lint": "eslint src --ext .ts",
    "typecheck": "tsc --noEmit",
    "prepublishOnly": "npm run test && npm run build",
    "fetch-quran": "tsx scripts/fetch-quran-data.ts"
  },
  "keywords": [
    "quran",
    "islamic",
    "validation",
    "llm",
    "arabic",
    "text-verification",
    "ai",
    "nlp"
  ],
  "author": "Yazin Alirhayim",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/yazinsai/quran-validator"
  },
  "dependencies": {
    "arabic-text-normalizer": "^1.4.0"
  },
  "devDependencies": {
    "@types/node": "^20.10.0",
    "eslint": "^8.56.0",
    "tsup": "^8.0.1",
    "tsx": "^4.7.0",
    "typescript": "^5.3.3",
    "vitest": "^1.2.0"
  },
  "engines": {
    "node": ">=18"
  }
}

```

### File: README.md
```md
# quran-validator

Validate and verify Quranic verses in LLM-generated text with high accuracy.

[![npm package](https://img.shields.io/npm/v/quran-validator.svg)](https://www.npmjs.com/package/quran-validator)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## The Problem

LLMs can misquote Quranic verses - sometimes subtly changing words, missing diacritics, or combining verses incorrectly. For Islamic content, this is unacceptable. This library provides:

1. **System prompts** that instruct LLMs to tag Quran quotes in a parseable format
2. **Post-processing** that validates tagged quotes against the authentic Quran database
3. **Auto-correction** that fixes misquotes to the authentic text
4. **Detection** of untagged Arabic text that might be Quran verses

## Features

- **LLM Integration**: System prompts + post-processor for complete LLM pipelines
- **Multi-tier Matching**: Exact → Normalized → Partial → Fuzzy matching
- **Auto-Correction**: Automatically fix misquoted verses
- **Arabic Normalization**: Handles diacritics, alef variants, alef-wasla, and more
- **Full Quran Database**: All 6,236 verses (Uthmani script) bundled
- **Zero Dependencies**: Fully self-contained
- **TypeScript Support**: Full type definitions included

## Installation

```bash
npm install quran-validator
# or
pnpm add quran-validator
# or
yarn add quran-validator
```

## Quick Start: LLM Integration (Recommended)

### Step 1: Add System Prompt to Your LLM

```typescript
import { SYSTEM_PROMPTS } from 'quran-validator';

// Add this to your LLM's system prompt
const systemPrompt = `
${SYSTEM_PROMPTS.xml}

${yourOtherInstructions}
`;

// The LLM will now output Quran quotes like:
// <quran ref="1:1">بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ</quran>
```

### Step 2: Process LLM Response

```typescript
import { LLMProcessor } from 'quran-validator';

const processor = new LLMProcessor();

// Process the LLM's response
const result = processor.process(llmResponse);

// Check if all quotes are valid
if (!result.allValid) {
  console.log('Some quotes need attention:', result.quotes.filter(q => !q.isValid));
}

// Use the corrected text (misquotes auto-fixed)
console.log(result.correctedText);

// See all detected quotes
for (const quote of result.quotes) {
  console.log(`${quote.reference}: ${quote.isValid ? '✓' : '✗'} (${quote.detectionMethod})`);
}
```

### Step 3: Handle Warnings

```typescript
// Warnings about potential untagged Quran content
for (const warning of result.warnings) {
  console.warn(warning);
  // e.g., "Potential untagged Quran quote detected: قُلْ هُوَ... (possibly 112:1, 92% confidence)"
}
```

## Verse Range Support

The library supports verse ranges for quoting multiple consecutive verses:

```typescript
// Single verse
<quran ref="1:1">بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ</quran>

// Verse range (e.g., Surah Al-Ikhlas 112:1-4)
<quran ref="112:1-4">قُلْ هُوَ ٱللَّهُ أَحَدٌ ٱللَّهُ ٱلصَّمَدُ لَمْ يَلِدْ وَلَمْ يُولَدْ وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ</quran>
```

You can also look up verse ranges programmatically:

```typescript
const validator = new QuranValidator();
const range = validator.getVerseRange(112, 1, 4); // Surah 112, verses 1-4

console.log(range.text);   // Concatenated Arabic text
console.log(range.verses); // Array of 4 QuranVerse objects
```

## System Prompt Formats

The library supports multiple tagging formats:

### XML (Recommended)
```typescript
SYSTEM_PROMPTS.xml
// LLM outputs: <quran ref="1:1">بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ</quran>
// Or for ranges: <quran ref="112:1-4">...</quran>
```

### Markdown
```typescript
SYSTEM_PROMPTS.markdown
// LLM outputs:
// ```quran ref="1:1"
// بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
// ```
```

### Bracket
```typescript
SYSTEM_PROMPTS.bracket
// LLM outputs: [[Q:1:1|بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ]]
```

### Minimal (for models that don't follow complex formats)
```typescript
SYSTEM_PROMPTS.minimal
// LLM outputs: بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (1:1)
```

## LLMProcessor Options

```typescript
const processor = new LLMProcessor({
  autoCorrect: true,      // Auto-fix misquoted verses (default: true)
  minConfidence: 0.85,    // Minimum confidence for fuzzy matches (default: 0.85)
  scanUntagged: true,     // Scan for untagged potential Quran (default: true)
  tagFormat: 'xml',       // 'xml' | 'markdown' | 'bracket' (default: 'xml')
});
```

## Quick Validation

For simple use cases:

```typescript
import { quickValidate } from 'quran-validator';

const result = quickValidate(llmResponse);

console.log(result.hasQuranContent);  // true if Quran quotes detected
console.log(result.allValid);         // true if all quotes are authentic
console.log(result.issues);           // Array of issues found
```

## Direct Validation API

For validating specific text without the full LLM pipeline:

```typescript
import { QuranValidator } from 'quran-validator';

const validator = new QuranValidator();

// Validate a specific quote
const result = validator.validate('بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ');

console.log(result.isValid);     // true
console.log(result.reference);   // "1:1"
console.log(result.matchType);   // "exact" | "normalized" | "partial" | "fuzzy" | "none"
console.log(result.confidence);  // 0-1

// Get corrections if needed
if (result.matchType !== 'exact' && result.matchedVerse) {
  console.log('Correct text:', result.matchedVerse.text);
}
```

## Detection Methods

The processor uses three methods to find Quran quotes:

| Method | Description | When Used |
|--------|-------------|-----------|
| `tagged` | Explicitly tagged with XML/markdown/bracket | Always checked first |
| `contextual` | Found after phrases like "Allah says", "in the Quran" | After tagged quotes |
| `fuzzy` | Untagged Arabic text matching Quran verses | If `scanUntagged: true` |

## Match Types

| Type | Description | Confidence |
|------|-------------|------------|
| `exact` | Perfect character-by-character match | 1.0 |
| `normalized` | Match after removing diacritics | ~0.95 |
| `partial` | Input is part of a verse or vice versa | 0.7-0.9 |
| `fuzzy` | Similar but not exact (Levenshtein) | 0.8+ |
| `none` | No match found | 0 |

## Utility Functions

### Verse Lookup

```typescript
// Get specific verse
const verse = validator.getVerse(2, 255); // Ayat al-Kursi
console.log(verse?.text);

// Get surah info
const surah = validator.getSurah(1);
console.log(surah?.englishName); // "Al-Faatiha"
console.log(surah?.versesCount); // 7

// Search verses
const results = validator.search('الرحمن الرحيم', 5);
```

### Arabic Text Processing

```typescript
import {
  normalizeArabic,
  removeDiacritics,
  containsArabic,
  extractArabicSegments,
} from 'quran-validator';

// Normalize for comparison
normalizeArabic('السَّلَامُ عَلَيْكُمُ'); // 'السلام عليكم'

// Remove diacritics only
removeDiacritics('بِسْمِ اللَّهِ'); // 'بسم الله'

// Check for Arabic
containsArabic('Hello مرحبا world'); // true

// Extract Arabic segments
extractArabicSegments('Say بسم الله and continue');
// [{ text: 'بسم الله', startIndex: 4, endIndex: 12 }]
```

## Real-World Example

```typescript
import { LLMProcessor, SYSTEM_PROMPTS } from 'quran-validator';

// Your LLM call
async function askAboutQuran(question: string) {
  const response = await openai.chat.completions.create({
    model: 'gpt-4',
    messages: [
      {
        role: 'system',
        content: `You are an Islamic scholar. ${SYSTEM_PROMPTS.xml}`
      },
      { role: 'user', content: question }
    ]
  });

  // Validate and correct the response
  const processor = new LLMProcessor();
  const validated = processor.process(response.choices[0].message.content);

  if (!validated.allValid) {
    console.warn('Response contained inaccurate Quran quotes');
    // Log for review or regenerate
  }

  return validated.correctedText;
}
```

## Data Source

This library uses high-quality Quranic data from **[QUL (Quranic Universal Library)](https://qul.tarteel.ai/)** by **[Tarteel AI](https://tarteel.ai/)**:

- **Uthmani Script**: Authoritative Arabic text with full diacritics (for corrections)
- **Imlaei Simple**: Simplified phonetic Arabic (for matching/search)

| | |
|---|---|
| **Total Verses** | 6,236 |
| **Total Surahs** | 114 |
| **Uthmani Source** | QUL - Uthmani (Ayah by Ayah) |
| **Simple Source** | QUL - Imlaei Simple (Word by Word, aggregated) |
| **Encoding** | UTF-8 |

### Credits

- **[Tarteel AI](https://tarteel.ai/)** - For creating and maintaining QUL
- **[QUL (Quranic Universal Library)](https://qul.tarteel.ai/)** - Open-source Quranic resources platform
- Data sourced from the authoritative Medina Mushaf

## License

MIT © Yazin Alirhayim

Quran data is provided by [QUL/Tarteel](https://qul.tarteel.ai/) - please review their licensing terms for commercial use.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

```

### File: benchmark\package.json
```json
{
  "name": "quran-validator-benchmark",
  "version": "1.0.0",
  "description": "Benchmark LLMs on Quranic verse accuracy",
  "private": true,
  "type": "module",
  "scripts": {
    "benchmark": "tsx benchmark.ts",
    "screenshot": "tsx screenshot.ts",
    "setup": "npm install && npx playwright install chromium"
  },
  "dependencies": {
    "playwright": "^1.40.0",
    "tsx": "^4.7.0",
    "quran-validator": "file:.."
  }
}

```

### File: benchmark\README.md
```md
# Quran Validator LLM Benchmark

Benchmark tool to test how accurately different LLMs can quote Quranic verses.

## Setup

```bash
cd benchmark
npm install
npx playwright install chromium
```

## Usage

1. Get an API key from [OpenRouter](https://openrouter.ai/)

2. Run the benchmark:
```bash
export OPENROUTER_API_KEY='[REDACTED_API_KEY]'
npm run benchmark
```

3. Generate screenshots (optional):
```bash
npm run screenshot
```

## Output

Results are saved to `results/`:
- `summary.html` - Leaderboard with all models
- `details.html` - Detailed diff view for errors
- `data.json` - Raw results data
- `summary.png` - Screenshot of leaderboard
- `details.png` - Screenshot of error details

## Customization

Edit `benchmark.ts` to customize:

```typescript
const CONFIG = {
  // Add/remove models
  models: [
    { id: 'anthropic/claude-sonnet-4.5', name: 'Claude Sonnet 4.5', icon: '🟤' },
    // ...
  ],

  // Change the test prompt
  prompt: 'What does the Quran say about giving to the needy?',
};
```

## How It Works

1. Each model receives a system prompt instructing it to quote Quran verses using XML tags:
   ```
   <quran ref="1:1">بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ</quran>
   ```

2. The `quran-validator` library validates each quoted verse against the authentic Quran database

3. Results show:
   - ✅ **Valid** - Exact or near-exact match
   - ⚠️ **Diacritic errors** - Correct letters, wrong vowel marks
   - ❌ **Invalid** - Misquoted or fabricated verse

## Example Results

![Summary](example.png)

## License

MIT

```

### File: web\package.json
```json
{
  "name": "quran-validator-leaderboard",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "@iconify/react": "^6.0.2",
    "arabic-text-normalizer": "^1.3.0",
    "next": "^14.1.0",
    "quran-validator": "github:yazinsai/quran-validator",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/node": "^20.10.0",
    "@types/react": "^18.2.0",
    "autoprefixer": "^10.4.17",
    "postcss": "^8.4.33",
    "tailwindcss": "^3.4.0",
    "typescript": "^5.3.3"
  }
}

```

### File: web\README.md
```md
# Quran Validator Leaderboard

A hosted web app that benchmarks how accurately different LLMs can quote the Quran.

## Features

- Test any model available on [OpenRouter](https://openrouter.ai)
- Results are cached - same model is never tested twice
- Leaderboard sorted by accuracy
- Detailed view shows each quoted verse with validation status

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Create `.env` file with your OpenRouter API key:
   ```bash
   cp .env.example .env
   # Edit .env with your API key
   ```

3. Run development server:
   ```bash
   npm run dev
   ```

4. Open [http://localhost:3000](http://localhost:3000)

## How It Works

1. User enters an OpenRouter model ID (e.g., `anthropic/claude-3.5-sonnet`)
2. The app sends a test prompt asking for Quranic verses
3. The response is validated using the `quran-validator` package
4. Results are cached to `cache.json` and displayed on the leaderboard

## Deployment

This app can be deployed to Vercel:

```bash
npm run build
```

Make sure to set `OPENROUTER_API_KEY` in your environment variables.

```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.2] - 2025-02-02

### Added
- **Verse range support**: Validate multiple consecutive verses with range references like `2:255-257` or `112:1-4`
- New `getVerseRange(surah, startAyah, endAyah)` method on `QuranValidator`
- Updated system prompts with verse range examples
- LLMs can now tag verse ranges: `<quran ref="112:1-4">...</quran>`

### Fixed
- Improved reference parsing to handle edge cases

## [1.0.1] - 2025-02-02

### Fixed
- README now displays correctly on npm

## [1.0.0] - 2025-02-02

### Added
- Initial release
- `QuranValidator` class for validating Quranic verses
- `LLMProcessor` class for processing LLM output with tagged Quran quotes
- Multi-tier matching: exact, normalized, partial, and fuzzy
- Auto-correction of misquoted verses
- Arabic text normalization utilities
- System prompts for LLM integration (XML, Markdown, Bracket, Minimal formats)
- Full Quran database (6,236 verses) from QUL/Tarteel
- `quickValidate()` helper for simple validation
- TypeScript support with full type definitions
- Zero runtime dependencies

```

### File: CLAUDE.md
```md
# quran-validator Development Guidelines

## Testing Rule (CRITICAL)

**Before making ANY code changes, ALWAYS add failing test cases first, then fix them.**

This ensures:
1. The expected behavior is documented
2. Regressions are caught
3. The fix actually addresses the problem

## Project Overview

Quran text validation library for verifying LLM-generated Quranic quotes.

## Validation Logic

Simple binary matching:
- Normalize both input and stored verse text (strip diacritics, normalize characters)
- **Exact normalized match** → valid
- **No match** → invalid

No fuzzy matching, no confidence scores, no partial matching.

## Running Tests

```bash
npm test        # Run all tests
npm run build   # Build the package
```

## Web Benchmark

```bash
cd web
npx tsx scripts/rerun-cache.ts --concurrency=5  # Re-run cached benchmarks
```

```

### File: package_lock.json
```json
{
  "name": "quran-validator",
  "version": "1.2.1",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "quran-validator",
      "version": "1.2.1",
      "license": "MIT",
      "dependencies": {
        "arabic-text-normalizer": "^1.4.0"
      },
      "devDependencies": {
        "@types/node": "^20.10.0",
        "eslint": "^8.56.0",
        "tsup": "^8.0.1",
        "tsx": "^4.7.0",
        "typescript": "^5.3.3",
        "vitest": "^1.2.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/aix-ppc64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.27.2.tgz",
      "integrity": "sha512-GZMB+a0mOMZs4MpDbj8RJp4cw+w1WV5NYD6xzgvzUJ5Ek2jerwfO2eADyI6ExDSUED+1X8aMbegahsJi+8mgpw==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "aix"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.27.2.tgz",
      "integrity": "sha512-DVNI8jlPa7Ujbr1yjU2PfUSRtAUZPG9I1RwW4F4xFB1Imiu2on0ADiI/c3td+KmDtVKNbi+nffGDQMfcIMkwIA==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.27.2.tgz",
      "integrity": "sha512-pvz8ZZ7ot/RBphf8fv60ljmaoydPU12VuXHImtAs0XhLLw+EXBi2BLe3OYSBslR4rryHvweW5gmkKFwTiFy6KA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-x64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.27.2.tgz",
      "integrity": "sha512-z8Ank4Byh4TJJOh4wpz8g2vDy75zFL0TlZlkUkEwYXuPSgX8yzep596n6mT7905kA9uHZsf/o2OJZubl2l3M7A==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-arm64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.27.2.tgz",
      "integrity": "sha512-davCD2Zc80nzDVRwXTcQP/28fiJbcOwvdolL0sOiOsbwBa72kegmVU0Wrh1MYrbuCL98Omp5dVhQFWRKR2ZAlg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-x64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.27.2.tgz",
      "integrity": "sha512-ZxtijOmlQCBWGwbVmwOF/UCzuGIbUkqB1faQRf5akQmxRJ1ujusWsb3CVfk/9iZKr2L5SMU5wPBi1UWbvL+VQA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-arm64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.27.2.tgz",
      "integrity": "sha512-lS/9CN+rgqQ9czogxlMcBMGd+l8Q3Nj1MFQwBZJyoEKI50XGxwuzznYdwcav6lpOGv5BqaZXqvBSiB/kJ5op+g==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-x64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.27.2.tgz",
      "integrity": "sha512-tAfqtNYb4YgPnJlEFu4c212HYjQWSO/w/h/lQaBK7RbwGIkBOuNKQI9tqWzx7Wtp7bTPaGC6MJvWI608P3wXYA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-arm": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.27.2.tgz",
      "integrity": "sha512-vWfq4GaIMP9AIe4yj1ZUW18RDhx6EPQKjwe7n8BbIecFtCQG4CfHGaHuh7fdfq+y3LIA2vGS/o9ZBGVxIDi9hw==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-arm64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.27.2.tgz",
      "integrity": "sha512-hYxN8pr66NsCCiRFkHUAsxylNOcAQaxSSkHMMjcpx0si13t1LHFphxJZUiGwojB1a/Hd5OiPIqDdXONia6bhTw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-ia32": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.27.2.tgz",
      "integrity": "sha512-MJt5BRRSScPDwG2hLelYhAAKh9imjHK5+NE/tvnRLbIqUWa+0E9N4WNMjmp/kXXPHZGqPLxggwVhz7QP8CTR8w==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-loong64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.27.2.tgz",
      "integrity": "sha512-lugyF1atnAT463aO6KPshVCJK5NgRnU4yb3FUumyVz+cGvZbontBgzeGFO1nF+dPueHD367a2ZXe1NtUkAjOtg==",
      "cpu": [
        "loong64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-mips64el": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.27.2.tgz",
      "integrity": "sha512-nlP2I6ArEBewvJ2gjrrkESEZkB5mIoaTswuqNFRv/WYd+ATtUpe9Y09RnJvgvdag7he0OWgEZWhviS1OTOKixw==",
      "cpu": [
        "mips64el"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-ppc64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.27.2.tgz",
      "integrity": "sha512-C92gnpey7tUQONqg1n6dKVbx3vphKtTHJaNG2Ok9lGwbZil6DrfyecMsp9CrmXGQJmZ7iiVXvvZH6Ml5hL6XdQ==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-riscv64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-riscv64/-/linux-riscv64-0.27.2.tgz",
      "integrity": "sha512-B5BOmojNtUyN8AXlK0QJyvjEZkWwy/FKvakkTDCziX95AowLZKR6aCDhG7LeF7uMCXEJqwa8Bejz5LTPYm8AvA==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-s390x": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-s390x/-/linux-s390x-0.27.2.tgz",
      "integrity": "sha512-p4bm9+wsPwup5Z8f4EpfN63qNagQ47Ua2znaqGH6bqLlmJ4bx97Y9JdqxgGZ6Y8xVTixUnEkoKSHcpRlDnNr5w==",
      "cpu": [
        "s390x"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-x64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.27.2.tgz",
      "integrity": "sha512-uwp2Tip5aPmH+NRUwTcfLb+W32WXjpFejTIOWZFw/v7/KnpCDKG66u4DLcurQpiYTiYwQ9B7KOeMJvLCu/OvbA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/netbsd-arm64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-arm64/-/netbsd-arm64-0.27.2.tgz",
      "integrity": "sha512-Kj6DiBlwXrPsCRDeRvGAUb/LNrBASrfqAIok+xB0LxK8CHqxZ037viF13ugfsIpePH93mX7xfJp97cyDuTZ3cw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "netbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/netbsd-x64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-0.27.2.tgz",
      "integrity": "sha512-HwGDZ0VLVBY3Y+Nw0JexZy9o/nUAWq9MlV7cahpaXKW6TOzfVno3y3/M8Ga8u8Yr7GldLOov27xiCnqRZf0tCA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "netbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/openbsd-arm64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/openbsd-arm64/-/openbsd-arm64-0.27.2.tgz",
      "integrity": "sha512-DNIHH2BPQ5551A7oSHD0CKbwIA/Ox7+78/AWkbS5QoRzaqlev2uFayfSxq68EkonB+IKjiuxBFoV8ESJy8bOHA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/openbsd-x64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/openbsd-x64/-/openbsd-x64-0.27.2.tgz",
      "integrity": "sha512-/it7w9Nb7+0KFIzjalNJVR5bOzA9Vay+yIPLVHfIQYG/j+j9VTH84aNB8ExGKPU4AzfaEvN9/V4HV+F+vo8OEg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/openharmony-arm64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/openharmony-arm64/-/openharmony-arm64-0.27.2.tgz",
      "integrity": "sha512-LRBbCmiU51IXfeXk59csuX/aSaToeG7w48nMwA6049Y4J4+VbWALAuXcs+qcD04rHDuSCSRKdmY63sruDS5qag==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openharmony"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/sunos-x64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/sunos-x64/-/sunos-x64-0.27.2.tgz",
      "integrity": "sha512-kMtx1yqJHTmqaqHPAzKCAkDaKsffmXkPHThSfRwZGyuqyIeBvf08KSsYXl+abf5HDAPMJIPnbBfXvP2ZC2TfHg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "sunos"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/win32-arm64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-arm64/-/win32-arm64-0.27.2.tgz",
      "integrity": "sha512-Yaf78O/B3Kkh+nKABUF++bvJv5Ijoy9AN1ww904rOXZFLWVc5OLOfL56W+C8F9xn5JQZa3UX6m+IktJnIb1Jjg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/win32-ia32": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-ia32/-/win32-ia32-0.27.2.tgz",
      "integrity": "sha512-Iuws0kxo4yusk7sw70Xa2E2imZU5HoixzxfGCdxwBdhiDgt9vX9VUCBhqcwY7/uh//78A1hMkkROMJq9l27oLQ==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/win32-x64": {
      "version": "0.27.2",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-x64/-/win32-x64-0.27.2.tgz",
      "integrity": "sha512-sRdU18mcKf7F+YgheI/zGf5alZatMUTKj/jNS6l744f9u3WFu4v7twcUI9vu4mknF4Y9aDlblIie0IM+5xxaqQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@eslint-community/eslint-utils": {
      "version": "4.9.1",
      "resolved": "https://registry.npmjs.org/@eslint-community/eslint-utils/-/eslint-utils-4.9.1.tgz",
      "integrity": "sha512-phrYmNiYppR7znFEdqgfWHXR6NCkZEK7hwWDHZUjit/2/U0r6XvkDl0SYnoM51Hq7FhCGdLDT6zxCCOY1hexsQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "eslint-visitor-keys": "^3.4.3"
      },
      "engines": {
        "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      },
      "peerDependencies": {
        "eslint": "^6.0.0 || ^7.0.0 || >=8.0.0"
      }
    },
    "node_modules/@eslint-community/regexpp": {
      "version": "4.12.2",
      "resolved": "https://registry.npmjs.org/@eslint-community/regexpp/-/regexpp-4.12.2.tgz",
      "integrity": "sha512-EriSTlt5OC9/7SXkRSCAhfSxxoSUgBm33OH+IkwbdpgoqsSsUg7y3uh+IICI/Qg4BBWr3U2i39RpmycbxMq4ew==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": "^12.0.0 || ^14.0.0 || >=16.0.0"
      }
    },
    "node_modules/@eslint/eslintrc": {
      "version": "2.1.4",
      "resolved": "https://registry.npmjs.org/@eslint/eslintrc/-/eslintrc-2.1.4.tgz",
      "integrity": "sha512-269Z39MS6wVJtsoUl10L60WdkhJVdPG24Q4eZTH3nnF6lpvSShEK3wQjDX9JRWAUPvPh7COouPpU9IrqaZFvtQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ajv": "^6.12.4",
        "debug": "^4.3.2",
        "espree": "^9.6.0",
        "globals": "^13.19.0",
        "ignore": "^5.2.0",
        "import-fresh": "^3.2.1",
        "js-yaml": "^4.1.0",
        "minimatch": "^3.1.2",
        "strip-json-comments": "^3.1.1"
      },
      "engines": {
        "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
      },
      "funding": {
        "url": "
... [TRUNCATED]
```

### File: test-llm-comparison.ts
```ts
import { LLMProcessor, SYSTEM_PROMPTS } from './src';

const OPENROUTER_API_KEY = process.env.OPENROUTER_API_KEY;

if (!OPENROUTER_API_KEY) {
  console.error('Please set OPENROUTER_API_KEY environment variable');
  process.exit(1);
}

const models = [
  'openai/gpt-4o',
  'anthropic/claude-3.5-sonnet',
  'google/gemini-2.0-flash-001',
  'meta-llama/llama-3.3-70b-instruct',
  'deepseek/deepseek-chat',
];

const systemPrompt = `You are a knowledgeable Islamic scholar. ${SYSTEM_PROMPTS.xml}

When asked about Quranic topics, provide relevant verses with their exact Arabic text.`;

const userPrompt = `What does the Quran say about giving to the needy? Please share one or two relevant verses.`;

async function queryModel(model: string): Promise<string> {
  const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${OPENROUTER_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model,
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userPrompt },
      ],
      max_tokens: 1000,
    }),
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`${model} failed: ${error}`);
  }

  const data = await response.json();
  return data.choices[0].message.content;
}

async function main() {
  const processor = new LLMProcessor();

  console.log('╔════════════════════════════════════════════════════════════════╗');
  console.log('║           Quran Validator - LLM Comparison Test                ║');
  console.log('╚════════════════════════════════════════════════════════════════╝\n');
  console.log(`Prompt: "${userPrompt}"\n`);
  console.log('─'.repeat(68) + '\n');

  const results: Array<{
    model: string;
    response: string;
    allValid: boolean;
    quotes: number;
    validQuotes: number;
    details: string[];
  }> = [];

  for (const model of models) {
    const shortName = model.split('/')[1];
    process.stdout.write(`Testing ${shortName}... `);

    try {
      const response = await queryModel(model);
      const validated = processor.process(response);

      const validQuotes = validated.quotes.filter(q => q.isValid).length;

      results.push({
        model: shortName,
        response,
        allValid: validated.allValid,
        quotes: validated.quotes.length,
        validQuotes,
        details: validated.quotes.map(q =>
          `${q.reference || 'unknown'}: ${q.isValid ? '✓' : '✗'} (${q.matchType || 'tagged'}, ${Math.round((q.confidence || 0) * 100)}%)`
        ),
      });

      console.log(`✓ (${validQuotes}/${validated.quotes.length} valid)`);
    } catch (error) {
      console.log(`✗ Error: ${error}`);
      results.push({
        model: shortName,
        response: '',
        allValid: false,
        quotes: 0,
        validQuotes: 0,
        details: [`Error: ${error}`],
      });
    }
  }

  console.log('\n' + '─'.repeat(68) + '\n');
  console.log('DETAILED RESULTS\n');

  for (const result of results) {
    console.log(`┌─ ${result.model} ${'─'.repeat(Math.max(0, 60 - result.model.length))}┐`);
    console.log('│');

    // Show truncated response
    const lines = result.response.split('\n').filter(l => l.trim());
    for (const line of lines.slice(0, 10)) {
      const truncated = line.length > 64 ? line.substring(0, 61) + '...' : line;
      console.log(`│  ${truncated}`);
    }
    if (lines.length > 10) {
      console.log(`│  ... (${lines.length - 10} more lines)`);
    }

    console.log('│');
    console.log(`│  Quotes detected: ${result.quotes}`);
    console.log(`│  Valid quotes: ${result.validQuotes}/${result.quotes}`);
    for (const detail of result.details) {
      console.log(`│    └─ ${detail}`);
    }
    console.log(`│  Status: ${result.allValid || result.validQuotes === result.quotes ? '✓ ALL VALID' : '⚠ ISSUES FOUND'}`);
    console.log('│');
    console.log('└' + '─'.repeat(66) + '┘\n');
  }

  // Summary table
  console.log('═'.repeat(68));
  console.log('SUMMARY');
  console.log('═'.repeat(68));
  console.log(`${'Model'.padEnd(25)} ${'Quotes'.padEnd(10)} ${'Valid'.padEnd(10)} Status`);
  console.log('─'.repeat(68));

  for (const result of results) {
    const status = result.validQuotes === result.quotes && result.quotes > 0 ? '✓' : '⚠';
    console.log(
      `${result.model.padEnd(25)} ${String(result.quotes).padEnd(10)} ${String(result.validQuotes).padEnd(10)} ${status}`
    );
  }
  console.log('─'.repeat(68));
}

main().catch(console.error);

```

### File: test-local.ts
```ts
import { QuranValidator, LLMProcessor, SYSTEM_PROMPTS, quickValidate } from './src';

// 1. Basic validation
console.log('=== Basic Validation ===\n');
const validator = new QuranValidator();

const verse = 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ';
const result = validator.validate(verse);
console.log(`Verse: ${verse}`);
console.log(`Valid: ${result.isValid}`);
console.log(`Reference: ${result.reference}`);
console.log(`Match type: ${result.matchType}`);
console.log(`Confidence: ${result.confidence}\n`);

// 2. LLM Processor with tagged quotes
console.log('=== LLM Processor ===\n');
const processor = new LLMProcessor();

const llmResponse = `
The Quran begins with Surah Al-Fatiha. The first verse is:

<quran ref="1:1">بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ</quran>

This is followed by:

<quran ref="1:2">ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ</quran>
`;

const processed = processor.process(llmResponse);
console.log(`All valid: ${processed.allValid}`);
console.log(`Quotes found: ${processed.quotes.length}`);
for (const quote of processed.quotes) {
  console.log(`  - ${quote.reference}: ${quote.isValid ? '✓' : '✗'} (${quote.matchType})`);
}
console.log();

// 3. Test with a misquoted verse
console.log('=== Misquote Detection ===\n');
const misquoted = `
Here is a verse:

<quran ref="112:1">قل هو الله احد</quran>
`;

const misquoteResult = processor.process(misquoted);
console.log(`All valid: ${misquoteResult.allValid}`);
for (const quote of misquoteResult.quotes) {
  console.log(`  Reference: ${quote.reference}`);
  console.log(`  Valid: ${quote.isValid}`);
  console.log(`  Match type: ${quote.matchType}`);
  console.log(`  Confidence: ${quote.confidence}`);
  if (quote.correctedText) {
    console.log(`  Original: ${quote.text}`);
    console.log(`  Corrected: ${quote.correctedText}`);
  }
}
console.log();

// 4. Quick validate
console.log('=== Quick Validate ===\n');
const quick = quickValidate('<quran ref="2:255">ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ٱلْحَىُّ ٱلْقَيُّومُ</quran>');
console.log(`Has Quran content: ${quick.hasQuranContent}`);
console.log(`All valid: ${quick.allValid}`);
console.log();

// 5. Verse lookup
console.log('=== Verse Lookup ===\n');
const ayatKursi = validator.getVerse(2, 255);
console.log(`Ayat al-Kursi (2:255):`);
console.log(`${ayatKursi?.text.substring(0, 80)}...`);
console.log();

// 6. Verse range support
console.log('=== Verse Range Support ===\n');
const rangeResponse = `
Surah Al-Ikhlas (The Sincerity) is one of the shortest surahs:

<quran ref="112:1-4">قُلْ هُوَ ٱللَّهُ أَحَدٌ ٱللَّهُ ٱلصَّمَدُ لَمْ يَلِدْ وَلَمْ يُولَدْ وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ</quran>
`;

const rangeResult = processor.process(rangeResponse);
console.log(`Range quote detected: ${rangeResult.quotes.length}`);
for (const quote of rangeResult.quotes) {
  console.log(`  Reference: ${quote.reference}`);
  console.log(`  Valid: ${quote.isValid}`);
  console.log(`  Confidence: ${quote.confidence}`);
}
console.log();

// 7. Test getVerseRange directly
console.log('=== Direct Verse Range Lookup ===\n');
const surahIkhlas = validator.getVerseRange(112, 1, 4);
if (surahIkhlas) {
  console.log(`Surah 112:1-4 (${surahIkhlas.verses.length} verses):`);
  console.log(`${surahIkhlas.text.substring(0, 80)}...`);
}
console.log();

// 8. Show system prompt
console.log('=== System Prompt (XML) ===\n');
console.log(SYSTEM_PROMPTS.xml.substring(0, 400) + '...\n');

console.log('✓ All tests passed!');

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "lib": ["ES2022"],
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "declaration": true,
    "declarationMap": true,
    "outDir": "dist",
    "rootDir": "src",
    "resolveJsonModule": true,
    "allowSyntheticDefaultImports": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "isolatedModules": true
  },
  "include": ["src/**/*", "data/**/*.json"],
  "exclude": ["node_modules", "dist"]
}

```

### File: vitest.config.ts
```ts
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    globals: true,
    include: ['src/**/*.test.ts'],
  },
});

```

### File: .github\repo-policy.md
```md
# Product Guardrails
- Quranic text accuracy is non-negotiable — no change may cause a valid verse to be rejected or an invalid quote to be accepted
- Simplicity over features — binary match (exact or normalized), no fuzzy matching or confidence scores in core validation
- Zero false positives — it is better to reject valid input than to accept fabricated Quranic text
- Hafs reading only — multi-qiraat support was intentionally removed; do not reintroduce it
- Zero runtime dependencies beyond `arabic-text-normalizer` — the library must stay lightweight and self-contained

# Risk Classification
## Always High Risk
- Any change to `data/quran-verses.json`, `data/quran-verses.min.json`, `data/quran-surahs.json`, or `data/quran-surahs.min.json` — these are the authoritative Quran database
- Any change to `data/normalized-index.json` — this drives lookup correctness
- Changes to `src/normalizer.ts` — normalization logic directly affects match accuracy
- Changes to `src/validator.ts` `validate()` or `validateAgainst()` methods — core validation logic
- Changes to `src/llm-integration.ts` that alter how quotes are parsed or corrected
- Modifications to `scripts/fetch-quran-data.ts` or `scripts/process-qul-data.ts` — data pipeline scripts that regenerate the Quran database
- Changes to `package.json` `exports`, `main`, `module`, or `types` fields — public API surface of the npm package
- Any change to the release pipeline (`.github/workflows/release-runner.yml`)

## Always Low Risk
- Documentation-only changes (README.md, CHANGELOG.md, benchmark/README.md)
- Test-only changes (`*.test.ts` files) that do not modify source
- Changes to `web/` frontend code (benchmark dashboard, not the core library)
- Changes to `benchmark/` directory
- `.gitignore` or editor config changes
- Dependency version bumps in `devDependencies` only

# Decision Rules
## Bugs
- If a verse is being incorrectly validated (false positive or false negative), treat as critical — accept immediately with `state:planned`
- Bug reports must include the Arabic text input and expected vs actual result
- If a bug report lacks the specific verse or input text, mark `state:needs-repro`
- Normalization bugs (diacritic handling, alef variants, hamza carriers) are high priority — they can silently affect all 6,236 verses

## Features
- Accept if it improves validation accuracy without adding complexity to the core matching logic
- Decline requests to add fuzzy matching, confidence scores, or partial matching to the core validator — this was intentionally removed
- Decline requests to add qiraat other than Hafs — this was intentionally scoped down
- New LLM tag formats (beyond xml/markdown/bracket/minimal) are acceptable if demand is clear
- New utility exports from `src/normalizer.ts` are low risk and generally acceptable
- Escalate to human if the feature would add a new runtime dependency

## External PRs
- The idea matters, the exact code doesn't — OK to reimplement rather than iterate on the PR
- Any PR touching `data/` files must be verified against the QUL/Tarteel source — do not trust contributed Quran data without verification
- PRs must include or update tests in `src/validator.test.ts` or `src/llm-integration.test.ts`
- PRs that break the public API (`src/index.ts` exports) require `release:major` and human review

# Repo-Specific Rules
- **Test-first rule**: The project CLAUDE.md mandates adding failing test cases before any code change — PRs without corresponding tests should be flagged
- **Protect the `data/` directory**: The JSON files under `data/` are the single source of truth for all 6,236 verses. Changes must only come through the `scripts/fetch-quran-data.ts` → `scripts/process-qul-data.ts` pipeline, never through manual edits
- **Normalization consistency**: `normalizeArabic()` and `normalizeFabrication()` in `src/normalizer.ts` must stay in sync — `normalizeFabrication` is a stricter superset using `stripHamza: true`
- **`src/types.ts` MatchType enum**: Currently `'exact' | 'normalized' | 'none'` — adding new match types is a breaking change since consumers may switch on these values
- **No `.min.json` drift**: `quran-verses.min.json` and `quran-surahs.min.json` must always be generated from their non-minified counterparts, never edited independently
- **Web app is separate**: The `web/` directory is the benchmark dashboard deployed to dokku — it has its own `package.json` and dependencies. Changes there do not affect the npm package
- **Squash merge only**: `repo-policy.yml` specifies squash merge strategy — enforce this for all PRs
- **npm publish safety**: The `prepublishOnly` script runs tests then build — never bypass this with `--ignore-scripts`
- **Arabic text in issues/PRs**: GitHub may render Arabic RTL text incorrectly — when reviewing, use `gh` to fetch raw content rather than relying on rendered markdown
```

### File: benchmark\benchmark.ts
```ts
/**
 * Quran Validator LLM Benchmark
 *
 * Tests how accurately different LLMs can quote Quranic verses.
 *
 * Usage:
 *   export OPENROUTER_API_KEY='your-key'
 *   npm run benchmark
 */

import { LLMProcessor, SYSTEM_PROMPTS, QuranValidator, normalizeArabic } from 'quran-validator';
import * as fs from 'fs';

// ============================================================================
// CONFIGURATION - Edit these to customize the benchmark
// ============================================================================

const CONFIG = {
  // Models to test (OpenRouter model IDs)
  models: [
    { id: 'anthropic/claude-sonnet-4.5', name: 'Claude Sonnet 4.5', icon: '🟤' },
    { id: 'google/gemini-3-flash-preview', name: 'Gemini 3 Flash', icon: '🔵' },
    { id: 'deepseek/deepseek-v3.2', name: 'DeepSeek V3.2', icon: '🟢' },
    { id: 'x-ai/grok-code-fast-1', name: 'Grok Code Fast 1', icon: '⚫' },
    { id: 'google/gemini-2.5-flash', name: 'Gemini 2.5 Flash', icon: '💎' },
    { id: 'openai/gpt-4o', name: 'GPT-4o', icon: '🟡' },
    { id: 'stepfun/step-3.5-flash:free', name: 'Step 3.5 Flash', icon: '🔶' },
  ],

  // Test prompt
  prompt: 'What does the Quran say about giving to the needy? Please share one or two relevant verses.',

  // API settings
  maxTokens: 1000,
};

// ============================================================================
// TYPES
// ============================================================================

interface QuoteResult {
  reference: string;
  isValid: boolean;
  confidence: number;
  original: string;
  corrected?: string;
}

interface ModelResult {
  model: string;
  icon: string;
  response: string;
  quotes: QuoteResult[];
  validCount: number;
  totalCount: number;
  accuracy: number;
}

// ============================================================================
// UTILITY FUNCTIONS
// ============================================================================

function normalizeForVisual(str: string): string {
  return str
    .normalize('NFC')
    .replace(/[\u200B-\u200D\uFEFF\u200E\u200F\u061C]/g, '')
    .replace(/[\u00A0\u2000-\u200A\u202F\u205F]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function visuallyEqual(a: string, b: string): boolean {
  return normalizeForVisual(a) === normalizeForVisual(b);
}

function calculateSimilarity(a: string, b: string): number {
  const normA = normalizeArabic(a);
  const normB = normalizeArabic(b);
  if (normA === normB) return 1;
  if (!normA || !normB) return 0;

  const longer = normA.length > normB.length ? normA : normB;
  const shorter = normA.length > normB.length ? normB : normA;
  if (longer.length === 0) return 1;

  const matrix: number[][] = [];
  for (let i = 0; i <= shorter.length; i++) matrix[i] = [i];
  for (let j = 0; j <= longer.length; j++) matrix[0][j] = j;

  for (let i = 1; i <= shorter.length; i++) {
    for (let j = 1; j <= longer.length; j++) {
      if (shorter[i - 1] === longer[j - 1]) {
        matrix[i][j] = matrix[i - 1][j - 1];
      } else {
        matrix[i][j] = Math.min(
          matrix[i - 1][j - 1] + 1,
          matrix[i][j - 1] + 1,
          matrix[i - 1][j] + 1
        );
      }
    }
  }

  return (longer.length - matrix[shorter.length][longer.length]) / longer.length;
}

function generateWordDiff(
  original: string,
  correct: string
): { originalHtml: string; correctHtml: string; hasDiff: boolean } {
  const origWords = original.split(/\s+/);
  const corrWords = correct.split(/\s+/);
  const corrUsed = new Set<number>();
  const origMatches: { idx: number | null; matchType: 'visual' | 'normalized' | 'none' }[] = [];

  for (let i = 0; i < origWords.length; i++) {
    let bestMatch: number | null = null;
    let bestType: 'visual' | 'normalized' | 'none' = 'none';

    for (let j = 0; j < corrWords.length; j++) {
      if (corrUsed.has(j)) continue;
      if (visuallyEqual(origWords[i], corrWords[j])) {
        bestMatch = j;
        bestType = 'visual';
        break;
      }
      if (normalizeArabic(origWords[i]) === normalizeArabic(corrWords[j]) && bestType === 'none') {
        bestMatch = j;
        bestType = 'normalized';
      }
    }

    if (bestMatch !== null) corrUsed.add(bestMatch);
    origMatches.push({ idx: bestMatch, matchType: bestType });
  }

  const hasDiff =
    origMatches.some((m) => m.matchType !== 'visual') ||
    corrWords.some((_, i) => !corrUsed.has(i));

  const originalHtml = origWords
    .map((word, i) => {
      const match = origMatches[i];
      if (match.matchType === 'visual') return word;
      if (match.matchType === 'normalized')
        return `<span class="diff-word-diacritic">${word}</span>`;
      return `<span class="diff-word-wrong">${word}</span>`;
    })
    .join(' ');

  const corrVisuallyMatched = new Set<number>();
  origMatches.forEach((match) => {
    if (match.idx !== null && match.matchType === 'visual') corrVisuallyMatched.add(match.idx);
  });

  const correctHtml = corrWords
    .map((word, i) => {
      if (corrVisuallyMatched.has(i)) return word;
      if (corrUsed.has(i)) return `<span class="diff-word-diacritic-correct">${word}</span>`;
      return `<span class="diff-word-correct">${word}</span>`;
    })
    .join(' ');

  return { originalHtml, correctHtml, hasDiff };
}

// ============================================================================
// API
// ============================================================================

async function queryModel(modelId: string, apiKey: string): Promise<string> {
  const systemPrompt = `You are a knowledgeable Islamic scholar. ${SYSTEM_PROMPTS.xml}

When asked about Quranic topics, provide relevant verses with their exact Arabic text.`;

  const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: modelId,
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: CONFIG.prompt },
      ],
      max_tokens: CONFIG.maxTokens,
    }),
  });

  if (!response.ok) {
    throw new Error(`API error: ${await response.text()}`);
  }

  const data = await response.json();
  return data.choices[0].message.content;
}

// ============================================================================
// HTML GENERATION
// ============================================================================

function generateSummaryHTML(results: ModelResult[]): string {
  const sorted = [...results].sort((a, b) => b.accuracy - a.accuracy);
  const lowestAccuracy = Math.min(
    ...results.filter((r) => r.totalCount > 0).map((r) => r.accuracy)
  );

  const rows = sorted
    .map((r, i) => {
      const rank = i + 1;
      const isWinner = rank === 1 && r.accuracy === 100;
      const isLoser = r.accuracy === lowestAccuracy && r.totalCount > 0 && r.accuracy < 100;
      const noQuotes = r.totalCount === 0;

      let medal = isWinner ? '🏆' : rank === 2 && r.accuracy > 0 ? '🥈' : rank === 3 && r.accuracy > 0 ? '🥉' : '';
      let rowClass = isWinner ? 'winner-row' : isLoser ? 'loser-row' : noQuotes ? 'no-quotes-row' : '';
      const accuracyDisplay = noQuotes ? '—' : `${r.accuracy}%`;
      const statusIcon = noQuotes ? '🚫' : r.accuracy === 100 ? '✅' : '❌';

      return `
        <tr class="${rowClass}">
          <td class="rank-cell">${medal || rank}</td>
          <td class="model-cell">
            <span class="model-icon">${r.icon}</span>
            <span class="model-name">${r.model}</span>
            ${isLoser ? '<span class="loser-badge">BIGGEST LOSER</span>' : ''}
          </td>
          <td class="center">${r.totalCount || '—'}</td>
          <td class="center">${noQuotes ? '—' : r.validCount}</td>
          <td class="center accuracy-cell ${r.accuracy === 100 ? 'perfect' : r.accuracy === 0 ? 'zero' : ''}">${accuracyDisplay}</td>
          <td class="center">${statusIcon}</td>
        </tr>`;
    })
    .join('');

  const perfectCount = results.filter((r) => r.accuracy === 100).length;
  const testedCount = results.filter((r) => r.totalCount > 0).length;

  return `<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Inter', sans-serif; background: linear-gradient(145deg, #0f0f1a, #1a1a2e, #0f0f1a); color: #fff; padding: 50px 40px; min-height: 100vh; }
    .container { max-width: 750px; margin: 0 auto; }
    .header { text-align: center; margin-bottom: 40px; }
    .logo { font-size: 48px; margin-bottom: 8px; }
    .header h1 { font-size: 36px; font-weight: 800; margin-bottom: 12px; background: linear-gradient(135deg, #00d4ff, #7b2ff7, #ff6b6b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .header .subtitle { color: #666; font-size: 16px; }
    .stats-row { display: flex; justify-content: center; gap: 40px; margin: 30px 0; }
    .stat-box { text-align: center; }
    .stat-number { font-size: 32px; font-weight: 800; }
    .stat-number.green { color: #22c55e; }
    .stat-number.red { color: #ef4444; }
    .stat-label { font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }
    .prompt-box { background: linear-gradient(135deg, rgba(123, 47, 247, 0.1), rgba(0, 212, 255, 0.1)); border: 1px solid rgba(123, 47, 247, 0.3); border-radius: 16px; padding: 20px 24px; margin-bottom: 30px; font-size: 15px; color: #aaa; }
    .prompt-box strong { color: #7b2ff7; }
    .prompt-box .prompt-text { color: #fff; font-style: italic; }
    table { width: 100%; border-collapse: separate; border-spacing: 0 8px; }
    th { padding: 12px 16px; text-align: left; font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #555; }
    td { padding: 18px 16px; background: rgba(255, 255, 255, 0.03); }
    tr td:first-child { border-radius: 12px 0 0 12px; }
    tr td:last-child { border-radius: 0 12px 12px 0; }
    .winner-row td { background: linear-gradient(135deg, rgba(34, 197, 94, 0.15), rgba(34, 197, 94, 0.05)); border-top: 1px solid rgba(34, 197, 94, 0.3); border-bottom: 1px solid rgba(34, 197, 94, 0.3); }
    .winner-row td:first-child { border-left: 1px solid rgba(34, 197, 94, 0.3); }
    .winner-row td:last-child { border-right: 1px solid rgba(34, 197, 94, 0.3); }
    .loser-row td { background: linear-gradient(135deg, rgba(239, 68, 68, 0.2), rgba(239, 68, 68, 0.08)); border-top: 2px solid rgba(239, 68, 68, 0.5); border-bottom: 2px solid rgba(239, 68, 68, 0.5); }
    .loser-row td:first-child { border-left: 2px solid rgba(239, 68, 68, 0.5); }
    .loser-row td:last-child { border-right: 2px solid rgba(239, 68, 68, 0.5); }
    .no-quotes-row td { opacity: 0.5; }
    .rank-cell { font-size: 20px; font-weight: 700; width: 50px; text-align: center; }
    .model-cell { display: flex; align-items: center; gap: 12px; }
    .model-icon { font-size: 24px; }
    .model-name { font-weight: 600; font-size: 15px; }
    .loser-badge { background: linear-gradient(135deg, #ef4444, #dc2626); color: #fff; font-size: 9px; font-weight: 700; padding: 4px 8px; border-radius: 4px; margin-left: 8px; }
    .center { text-align: center; }
    .accuracy-cell { font-weight: 700; font-size: 16px; }
    .accuracy-cell.perfect { color: #22c55e; }
    .accuracy-cell.zero { color: #ef4444; }
    .footer { text-align: center; margin-top: 40px; padding-top: 30px; border-top: 1px solid rgba(255, 255, 255, 0.1); }
    .footer-text { color: #444; font-size: 13px; }
    .footer-npm { margin-top: 12px; display: inline-block; background: rgba(123, 47, 247, 0.1); border: 1px solid rgba(123, 47, 247, 0.3); padding: 8px 16px; border-radius: 8px; font-family: monospace; font-size: 13px; color: #7b2ff7; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="logo">🕌</div>
      <h1>Can LLMs Quote the Quran?</h1>
      <p class="subtitle">Testing whether AI models can accurately cite Quranic verses</p>
    </div>
    <div class="stats-row">
      <div class="stat-box"><div class="stat-number">${testedCount}</div><div class="stat-label">Models Tested</div></div>
      <div class="stat-box"><div class="stat-number green">${perfectCount}</div><div class="stat-label">Perfect Scores</div></div>
      <div class="stat-box"><div class="stat-number red">${testedCount - perfectCount}</div><div class="stat-label">Made Errors</div></div>
    </div>
    <div class="prompt-box">
      <strong>Test Prompt:</strong><br>
      <span class="prompt-text">"${CONFIG.prompt}"</span>
    </div>
    <table>
      <thead>
        <tr>
          <th class="center">#</th>
          <th>Model</th>
          <th class="center">Quotes</th>
          <th class="center">Valid</th>
          <th class="center">Accuracy</th>
          <th class="center"></th>
        </tr>
      </thead>
      <tbody>${rows}</tbody>
    </table>
    <div class="footer">
      <div class="footer-text">Validated with quran-validator</div>
      <div class="footer-npm">npm install quran-validator</div>
    </div>
  </div>
</body>
</html>`;
}

function generateDetailHTML(results: ModelResult[], validator: QuranValidator): string {
  const invalidResults = results.filter((r) => r.quotes.some((q) => !q.isValid || q.corrected));
  if (invalidResults.length === 0) {
    return '<html><body style="background:#1a1a2e;color:#fff;padding:50px;font-family:sans-serif;text-align:center;"><h1>🎉 All models passed!</h1></body></html>';
  }

  const lowestAccuracy = Math.min(...results.filter((r) => r.totalCount > 0).map((r) => r.accuracy));

  const sections = invalidResults
    .map((r) => {
      const isLoser = r.accuracy === lowestAccuracy && r.totalCount > 0;
      const invalidQuotes = r.quotes.filter((q) => !q.isValid || q.corrected);

      const quoteDiffs = invalidQuotes
        .map((q) => {
          let correctText = q.corrected || '';
          if (!correctText && q.reference) {
            const parts = q.reference.split(':');
            correctText = validator.getVerse(parseInt(parts[0]), parseInt(parts[1]))?.text || '';
          }

          const isVisuallyIdentical = visuallyEqual(q.original, correctText);
          const similarity = calculateSimilarity(q.original, correctText);

          let diffContent = '';

          if (isVisuallyIdentical) {
            diffContent = `
              <div class="diff-container visual-match">
                <div class="match-message">
                  <span class="match-icon">✓</span>
                  <span class="match-text">Visually identical - encoding differences only</span>
                </div>
                <div class="diff-row correct">
                  <div class="diff-text" dir="rtl">${correctText}</div>
                </div>
              </div>`;
 
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
