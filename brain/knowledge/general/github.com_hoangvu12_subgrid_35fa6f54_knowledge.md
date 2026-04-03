---
id: github.com-hoangvu12-subgrid-35fa6f54-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:07.499778
---

# KNOWLEDGE EXTRACT: github.com_hoangvu12_subgrid_35fa6f54
> **Extracted on:** 2026-04-01 11:12:15
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521310/github.com_hoangvu12_subgrid_35fa6f54

---

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 hoangvu12

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
# SubGrid

A simple tool to visualize your subscription costs. See where your money goes each month through an interactive treemap.

## What it does

- Track your subscriptions (Netflix, Spotify, etc.)
- View costs as a proportional grid so you can see which services eat up your budget
- Import subscriptions from bank statements (CSV)
- Export your visualization as an image
- Supports 38+ currencies

## How to use

Serve the files with any static server:

```
npx serve .
```

or

```
python -m http.server
```

Your data stays in your browser's local storage.

## Stack

Plain HTML, CSS, and JavaScript. Uses Tailwind CSS for styling.

## License

MIT
```

## File: `index.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Subscription Cost Visualizer - See Where Your Money Goes</title>
    <meta
      name="description"
      content="Visualize your subscription costs with an interactive grid. See the true proportion of your monthly spending at a glance."
    />
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://code.iconify.design/3/3.1.1/iconify.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/modern-screenshot@4.6.7/dist/index.js"></script>
    <link
      href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap"
      rel="stylesheet"
    />
    <script>
      tailwind.config = {
        theme: {
          extend: {
            fontFamily: {
              sans: ['"Plus Jakarta Sans"', "sans-serif"],
            },
            colors: {
              brand: {
                purple: "#E5DEFF",
                yellow: "#FFF4C3",
                orange: "#FFDCC2",
                cyan: "#C6F6F6",
                dark: "#0f172a",
              },
            },
            boxShadow: {
              soft: "0 4px 20px -2px rgba(0, 0, 0, 0.05)",
              card: "0 0 0 1px rgba(0,0,0,0.03), 0 2px 8px rgba(0,0,0,0.04)",
              glow: "0 0 20px rgba(99, 102, 241, 0.5)",
            },
            animation: {
              "fade-in": "fadeIn 0.3s ease-out forwards",
              "slide-up": "slideUp 0.4s ease-out forwards",
            },
            keyframes: {
              fadeIn: {
                "0%": { opacity: "0" },
                "100%": { opacity: "1" },
              },
              slideUp: {
                "0%": { opacity: "0", transform: "translateY(20px)" },
                "100%": { opacity: "1", transform: "translateY(0)" },
              },
            },
          },
        },
      };
    </script>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body
    class="flex min-h-screen flex-col bg-[#F8F9FB] font-sans text-slate-800 selection:bg-indigo-100 selection:text-indigo-900"
  >
    <header
      class="mx-auto w-full max-w-2xl px-4 pb-3 pt-6 sm:px-6 sm:pb-4 sm:pt-8"
    >
      <div class="mb-3 flex justify-end sm:mb-4">
        <div
          class="text-xs font-bold uppercase tracking-widest text-slate-400"
          id="step-indicator"
        >
          Step 1 of 3
        </div>
      </div>
      <div class="h-2 w-full overflow-hidden rounded-full bg-slate-200">
        <div
          id="progress-bar"
          class="h-full w-1/3 rounded-full bg-indigo-600 transition-all duration-500 ease-out"
        ></div>
      </div>
    </header>

    <main
      class="relative mx-auto w-full max-w-2xl flex-grow px-4 pb-24 sm:px-6 sm:pb-12"
    >
      <div id="step-1" class="step-panel active">
        <div
          id="empty-state"
          class="group mb-4 flex cursor-pointer flex-col items-center justify-center rounded-3xl border-2 border-dashed border-slate-200 bg-white p-8 text-center transition-all hover:border-indigo-300 hover:bg-slate-50"
          onclick="openModal()"
        >
          <div
            class="mb-4 flex h-16 w-16 items-center justify-center rounded-full bg-indigo-50 text-indigo-600 transition-transform group-hover:scale-110"
          >
            <span class="iconify h-8 w-8" data-icon="ph:plus-bold"></span>
          </div>
          <h3 class="text-lg font-bold text-slate-900">
            Add first subscription
          </h3>
          <p class="mt-1 text-sm text-slate-400">Netflix, Spotify, Gym, etc.</p>
        </div>

        <div id="sub-list-container" class="mb-4 hidden space-y-3"></div>

        <div id="presets-section" class="mb-6">
          <div class="mb-3 flex items-center justify-between">
            <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400">Quick Add</h4>
            <button onclick="openPresetsBrowser()" class="text-xs font-semibold text-indigo-600 hover:text-indigo-700 flex items-center gap-1">
              Browse all
              <span class="iconify h-3.5 w-3.5" data-icon="ph:caret-right-bold"></span>
            </button>
          </div>
          <div class="grid grid-cols-4 gap-2 sm:grid-cols-6" id="presets-grid"></div>
        </div>

        <div id="import-section" class="mb-24 space-y-3">
          <div class="mb-3">
            <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400">Import</h4>
          </div>
          <button
            onclick="openBankImport()"
            class="flex w-full cursor-pointer flex-col items-center justify-center gap-1 rounded-xl border-2 border-dashed border-slate-200 bg-white py-4 transition-all hover:border-indigo-300 hover:bg-slate-50 active:scale-[0.99]"
          >
            <div class="flex items-center gap-2 text-sm font-semibold text-slate-500">
              <span class="iconify h-5 w-5" data-icon="ph:bank-bold"></span>
              Import from bank statement
            </div>
            <span class="text-xs text-slate-400">CSV file from your bank</span>
          </button>
          <label
            class="flex cursor-pointer flex-col items-center justify-center gap-1 rounded-xl border-2 border-dashed border-slate-200 bg-white py-4 transition-all hover:border-indigo-300 hover:bg-slate-50 active:scale-[0.99]"
          >
            <div class="flex items-center gap-2 text-sm font-semibold text-slate-500">
              <span class="iconify h-5 w-5" data-icon="ph:upload-simple-bold"></span>
              Restore from SubGrid backup
            </div>
            <span class="text-xs text-slate-400">Previously exported .json file</span>
            <input type="file" accept=".json" onchange="importData(event)" class="hidden" />
          </label>
        </div>

        <div
          class="pointer-events-none fixed bottom-0 left-0 z-10 w-full bg-gradient-to-t from-[#F8F9FB] via-[#F8F9FB] to-transparent px-4 pb-4 pt-6 sm:bottom-6 sm:bg-none sm:px-6 sm:pb-0 sm:pt-0"
        >
          <div class="mx-auto flex max-w-2xl items-center justify-between">
            <div class="flex items-center gap-2">
              <button
                onclick="openSettings()"
                class="pointer-events-auto flex h-12 w-12 items-center justify-center rounded-xl bg-white text-slate-400 shadow-lg shadow-slate-900/10 transition-all hover:text-slate-600 active:scale-95 sm:h-14 sm:w-14 sm:rounded-2xl"
                title="Settings"
              >
                <span class="iconify h-5 w-5 sm:h-6 sm:w-6" data-icon="ph:gear-bold"></span>
              </button>
              <button
                onclick="clearAllSubs()"
                id="clear-btn"
                class="pointer-events-auto hidden items-center gap-1.5 rounded-full bg-white py-3 pl-4 pr-5 text-sm font-bold text-slate-400 shadow-lg shadow-slate-900/10 transition-all hover:text-red-500 active:scale-95 sm:py-3.5 sm:pl-5 sm:pr-6"
              >
                <span class="iconify h-4 w-4" data-icon="ph:trash-bold"></span>
                Clear All
              </button>
            </div>
            <button
              onclick="goToStep(2)"
              id="next-btn-1"
              disabled
              class="pointer-events-auto flex cursor-not-allowed items-center gap-2 rounded-full bg-slate-900 py-3 pl-5 pr-4 text-sm font-bold text-white opacity-50 shadow-xl shadow-slate-900/20 transition-all hover:scale-105 active:scale-95 sm:py-3.5 sm:pl-6 sm:pr-5 sm:text-base"
            >
              Generate Grid
              <span
                class="iconify h-5 w-5"
                data-icon="ph:arrow-right-bold"
              ></span>
            </button>
          </div>
        </div>
      </div>

      <div id="step-2" class="step-panel">
        <!-- View Toggle -->
        <div class="mb-3 flex justify-center">
          <div class="inline-flex rounded-xl bg-slate-100 p-1">
            <button
              id="view-treemap"
              onclick="setView('treemap')"
              class="flex items-center gap-1.5 rounded-lg px-3 py-1.5 text-xs font-bold transition-all bg-slate-900 text-white"
            >
              <span class="iconify h-4 w-4" data-icon="ph:grid-four-bold"></span>
              Grid
            </button>
            <button
              id="view-beeswarm"
              onclick="setView('beeswarm')"
              class="flex items-center gap-1.5 rounded-lg px-3 py-1.5 text-xs font-bold transition-all bg-white text-slate-600"
            >
              <span class="iconify h-4 w-4" data-icon="ph:dots-six-bold"></span>
              Swarm
            </button>
            <button
              id="view-circlepack"
              onclick="setView('circlepack')"
              class="flex items-center gap-1.5 rounded-lg px-3 py-1.5 text-xs font-bold transition-all bg-white text-slate-600"
            >
              <span class="iconify h-4 w-4" data-icon="ph:circles-three-bold"></span>
              Bubbles
            </button>
          </div>
        </div>

        <div
          id="export-container"
          class="relative overflow-hidden rounded-2xl border border-slate-100 bg-white p-3 shadow-card sm:rounded-[2.5rem] sm:p-5"
          style="font-family: 'Plus Jakarta Sans', system-ui, sans-serif"
        >
          <div
            id="bento-grid"
            class="treemap-container mb-4 bg-slate-50 sm:mb-6"
          ></div>
          <div
            id="beeswarm-container"
            class="treemap-container mb-4 bg-slate-50 sm:mb-6 hidden relative"
          ></div>
          <div
            id="circlepack-container"
            class="treemap-container mb-4 bg-slate-50 sm:mb-6 hidden relative"
          ></div>

          <div
            class="flex items-center justify-between rounded-xl border border-slate-100 bg-slate-50 p-3 sm:rounded-2xl sm:p-4"
          >
            <div>
              <div
                class="text-[10px] font-bold uppercase tracking-widest text-slate-400 whitespace-nowrap sm:text-xs"
              >
                Total / Month
              </div>
              <div
                class="text-xl font-black text-slate-900 whitespace-nowrap sm:text-2xl"
                id="step-2-total"
              >
                $0.00
              </div>
            </div>
            <div class="text-right">
              <div
                class="text-[10px] font-bold uppercase tracking-widest text-slate-400 whitespace-nowrap sm:text-xs"
              >
                Yearly Projection
              </div>
              <div
                class="text-sm font-bold text-indigo-600 whitespace-nowrap sm:text-base"
                id="step-2-yearly"
              >
                $0.00
              </div>
            </div>
          </div>
        </div>

        <div
          class="pointer-events-none fixed bottom-0 left-0 z-10 w-full bg-gradient-to-t from-[#F8F9FB] via-[#F8F9FB] to-transparent px-4 pb-4 pt-6 sm:bottom-6 sm:bg-none sm:px-6 sm:pb-0 sm:pt-0"
        >
          <div
            class="mx-auto flex max-w-2xl flex-col gap-2 sm:flex-row sm:items-center sm:gap-3"
          >
            <div class="flex gap-2 sm:contents">
              <button
                onclick="openSettings()"
                class="pointer-events-auto flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-white text-slate-400 shadow-lg shadow-slate-900/10 transition-all hover:text-slate-600 active:scale-95 sm:rounded-2xl sm:h-14 sm:w-14"
                title="Settings"
              >
                <span class="iconify h-5 w-5 sm:h-6 sm:w-6" data-icon="ph:gear-bold"></span>
              </button>
              <button
                onclick="goToStep(1)"
                class="pointer-events-auto flex-1 rounded-xl py-3 font-bold text-slate-500 bg-white shadow-lg shadow-slate-900/10 transition-colors hover:bg-slate-100 sm:rounded-2xl sm:py-4"
              >
                Back
              </button>
              <button
                onclick="exportAsImage()"
                class="pointer-events-auto flex flex-1 items-center justify-center gap-2 rounded-xl border-2 border-slate-200 bg-white py-3 font-bold text-slate-700 shadow-lg shadow-slate-900/10 transition-all hover:border-slate-300 hover:bg-slate-50 active:scale-95 sm:rounded-2xl sm:py-4"
              >
                <span
                  class="iconify h-5 w-5"
                  data-icon="ph:download-bold"
                ></span>
                Export
              </button>
            </div>
          </div>
        </div>
      </div>

    </main>

    <div
      id="modal-backdrop"
      class="fixed inset-0 z-50 hidden bg-slate-900/30 opacity-0 backdrop-blur-sm transition-opacity duration-300"
      aria-hidden="true"
    ></div>
    <div
      id="modal-panel"
      class="pointer-events-none fixed inset-0 z-50 flex hidden items-end justify-center sm:items-center sm:p-4"
    >
      <div
        class="pointer-events-auto flex max-h-[90vh] w-full translate-y-full transform flex-col overflow-hidden rounded-t-3xl bg-white opacity-0 shadow-2xl transition-all duration-300 sm:max-w-lg sm:translate-y-10 sm:scale-95 sm:rounded-3xl"
      >
        <div
          class="flex shrink-0 items-center justify-between border-b border-slate-100 bg-slate-50/80 p-5 backdrop-blur"
        >
          <h3 class="text-lg font-bold text-slate-900" id="modal-title">
            Add Subscription
          </h3>
          <button
            onclick="closeModal()"
            class="rounded-full bg-slate-100 p-2 text-slate-400 transition-colors hover:text-slate-600"
          >
            <span class="iconify h-5 w-5" data-icon="ph:x-bold"></span>
          </button>
        </div>

        <form
          id="sub-form"
          onsubmit="handleFormSubmit(event)"
          class="space-y-5 overflow-y-auto bg-white p-6"
        >
          <input type="hidden" id="entry-id" />

          <div>
            <label
              class="mb-2 block text-xs font-bold uppercase tracking-wider text-slate-500"
              >Website (Optional)</label
            >
            <div class="flex gap-3">
              <input
                type="text"
                id="url"
                placeholder="netflix.com"
                oninput="updateFavicon(this.value)"
                class="block w-full flex-1 rounded-xl border border-slate-200 bg-slate-50 p-3 text-base font-semibold text-slate-900 placeholder:text-slate-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100"
              />
              <div
                id="favicon-preview"
                class="flex h-12 w-12 shrink-0 items-center justify-center overflow-hidden rounded-xl border border-slate-200 bg-slate-100"
              >
                <span
                  class="iconify h-5 w-5 text-slate-300"
                  data-icon="ph:globe-simple"
                ></span>
              </div>
            </div>
          </div>

          <div>
            <label
              class="mb-2 block text-xs font-bold uppercase tracking-wider text-slate-500"
              >Service Name</label
            >
            <input
              type="text"
              id="name"
              required
              placeholder="e.g. Netflix"
              class="block w-full rounded-xl border border-slate-200 bg-slate-50 p-3 text-base font-semibold text-slate-900 placeholder:text-slate-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100"
            />
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <label
                class="mb-2 block text-xs font-bold uppercase tracking-wider text-slate-500"
                >Price</label
              >
              <input
                type="number"
                id="price"
                required
                step="0.01"
                placeholder="0.00"
                class="block w-full rounded-xl border border-slate-200 bg-slate-50 p-3 text-base font-semibold text-slate-900 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100"
              />
            </div>
            <div>
              <label
                class="mb-2 block text-xs font-bold uppercase tracking-wider text-slate-500"
                >Currency</label
              >
              <div class="relative">
                <select
                  id="sub-currency"
                  class="block w-full appearance-none rounded-xl border border-slate-200 bg-slate-50 p-3 text-base font-semibold text-slate-900 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100"
                ></select>
                <span
                  class="iconify pointer-events-none absolute right-3 top-1/2 h-4 w-4 -translate-y-1/2 text-slate-400"
                  data-icon="ph:caret-down-bold"
                ></span>
              </div>
            </div>
          </div>

          <div>
            <label
              class="mb-2 block text-xs font-bold uppercase tracking-wider text-slate-500"
              >Cycle</label
            >
            <select
              id="cycle"
              class="block w-full appearance-none rounded-xl border border-slate-200 bg-slate-50 p-3 text-base font-semibold text-slate-900 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100"
            >
              <option value="Monthly">Monthly</option>
              <option value="Yearly">Yearly</option>
              <option value="Weekly">Weekly</option>
            </select>
          </div>
          <input type="hidden" id="date" value="" />

          <div>
            <label
              class="mb-2 block text-xs font-bold uppercase tracking-wider text-slate-500"
              >Color</label
            >
            <div class="grid grid-cols-6 gap-2" id="color-selector"></div>
            <input type="hidden" id="selected-color" value="" />
          </div>

          <button
            type="submit"
            class="w-full rounded-xl bg-slate-900 py-4 font-bold text-white shadow-lg shadow-slate-900/20 transition-all hover:bg-slate-800 active:scale-95"
          >
            Save Item
          </button>
        </form>
      </div>
    </div>

    <div
      id="settings-backdrop"
      class="fixed inset-0 z-50 hidden bg-slate-900/30 opacity-0 backdrop-blur-sm transition-opacity duration-300"
      aria-hidden="true"
    ></div>
    <div
      id="settings-panel"
      class="pointer-events-none fixed inset-0 z-50 flex hidden items-end justify-center sm:items-center sm:p-4"
    >
      <div
        class="pointer-events-auto flex max-h-[85vh] w-full translate-y-full transform flex-col overflow-hidden rounded-t-3xl bg-white opacity-0 shadow-2xl transition-all duration-300 sm:max-w-md sm:translate-y-10 sm:scale-95 sm:rounded-3xl"
      >
        <div
          class="flex shrink-0 items-center justify-between border-b border-slate-100 bg-slate-50/80 p-5 backdrop-blur"
        >
          <h3 class="text-lg font-bold text-slate-900">Settings</h3>
          <button
            onclick="closeSettings()"
            class="rounded-full bg-slate-100 p-2 text-slate-400 transition-colors hover:text-slate-600"
          >
            <span class="iconify h-5 w-5" data-icon="ph:x-bold"></span>
          </button>
        </div>

        <div class="overflow-y-auto bg-white p-6 space-y-6">
          <div>
            <label
              class="mb-3 block text-xs font-bold uppercase tracking-wider text-slate-500"
              >Currency</label
            >
            <div class="relative">
              <select
                id="currency-selector"
                class="block w-full appearance-none rounded-xl border border-slate-200 bg-slate-50 p-4 text-base font-semibold text-slate-900 focus:border-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-100"
              ></select>
              <span
                class="iconify pointer-events-none absolute right-4 top-1/2 h-5 w-5 -translate-y-1/2 text-slate-400"
                data-icon="ph:caret-down-bold"
              ></span>
            </div>
            <p class="mt-2 text-xs text-slate-400">
              All prices will be converted using approximate exchange rates
            </p>
          </div>

          <div class="border-t border-slate-100 pt-6">
            <label class="mb-3 block text-xs font-bold uppercase tracking-wider text-slate-500">
              Import & Export
            </label>
            <p class="mb-4 text-xs text-slate-400">
              Backup your subscriptions or transfer them to another device
            </p>
            <div class="flex gap-3">
              <button
                onclick="exportData()"
                class="flex flex-1 items-center justify-center gap-2 rounded-xl border-2 border-slate-200 bg-white py-3 font-semibold text-slate-700 transition-all hover:border-slate-300 hover:bg-slate-50 active:scale-95"
              >
                <span class="iconify h-5 w-5" data-icon="ph:download-simple-bold"></span>
                Export
              </button>
              <label
                class="flex flex-1 cursor-pointer items-center justify-center gap-2 rounded-xl border-2 border-slate-200 bg-white py-3 font-semibold text-slate-700 transition-all hover:border-slate-300 hover:bg-slate-50 active:scale-95"
              >
                <span class="iconify h-5 w-5" data-icon="ph:upload-simple-bold"></span>
                Import
                <input type="file" accept=".json" onchange="importData(event)" class="hidden" />
              </label>
            </div>
          </div>

        </div>
      </div>
    </div>

    <div
      id="presets-backdrop"
      class="fixed inset-0 z-50 hidden bg-slate-900/30 opacity-0 backdrop-blur-sm transition-opacity duration-300"
      aria-hidden="true"
    ></div>
    <div
      id="presets-panel"
      class="pointer-events-none fixed inset-0 z-50 flex hidden items-end justify-center sm:items-center sm:p-4"
    >
      <div
        class="pointer-events-auto flex max-h-[90vh] w-full translate-y-full transform flex-col overflow-hidden rounded-t-3xl bg-white opacity-0 shadow-2xl transition-all duration-300 sm:max-w-lg sm:translate-y-10 sm:scale-95 sm:rounded-3xl"
      >
        <div
          class="flex shrink-0 items-center justify-between border-b border-slate-100 bg-slate-50/80 p-5 backdrop-blur"
        >
          <h3 class="text-lg font-bold text-slate-900">Browse Subscriptions</h3>
          <button
            onclick="closePresetsBrowser()"
            class="rounded-full bg-slate-100 p-2 text-slate-400 transition-colors hover:text-slate-600"
          >
            <span class="iconify h-5 w-5" data-icon="ph:x-bold"></span>
          </button>
        </div>

        <div class="border-b border-slate-100 bg-white px-5 py-3">
          <div class="relative">
            <span class="iconify absolute left-3 top-1/2 h-5 w-5 -translate-y-1/2 text-slate-400" data-icon="ph:magnifying-glass"></span>
            <input
              type="text"
              id="presets-search"
              placeholder="Search subscriptions..."
              oninput="filterPresets(this.value)"
              class="w-full rounded-xl border border-slate-200 bg-slate-50 py-2.5 pl-10 pr-4 text-sm font-medium text-slate-900 placeholder:text-slate-400 focus:border-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-100"
            />
          </div>
          <div class="mt-3 flex flex-wrap gap-1.5" id="category-filters"></div>
        </div>

        <div class="overflow-y-auto bg-white p-5" id="presets-browser-list" style="max-height: 50vh;"></div>
      </div>
    </div>

    <div
      id="bank-import-backdrop"
      class="fixed inset-0 z-50 hidden bg-slate-900/30 opacity-0 backdrop-blur-sm transition-opacity duration-300"
      aria-hidden="true"
    ></div>
    <div
      id="bank-import-panel"
      class="pointer-events-none fixed inset-0 z-50 flex hidden items-end justify-center sm:items-center sm:p-4"
    >
      <div
        class="pointer-events-auto flex max-h-[90vh] w-full translate-y-full transform flex-col overflow-hidden rounded-t-3xl bg-white opacity-0 shadow-2xl transition-all duration-300 sm:max-w-lg sm:translate-y-10 sm:scale-95 sm:rounded-3xl"
      >
        <div
          class="flex shrink-0 items-center justify-between border-b border-slate-100 bg-slate-50/80 p-5 backdrop-blur"
        >
          <h3 class="text-lg font-bold text-slate-900" id="bank-import-title">Import Bank Statement</h3>
          <button
            onclick="closeBankImport()"
            class="rounded-full bg-slate-100 p-2 text-slate-400 transition-colors hover:text-slate-600"
          >
            <span class="iconify h-5 w-5" data-icon="ph:x-bold"></span>
          </button>
        </div>

        <div class="overflow-y-auto bg-white p-5" style="max-height: 70vh;">
          <!-- Step 1: Upload -->
          <div id="bank-step-1">
            <p class="mb-4 text-sm text-slate-600">
              Upload a CSV file exported from your bank. We'll detect recurring transactions that might be subscriptions.
            </p>
            <label
              class="flex cursor-pointer flex-col items-center justify-center gap-2 rounded-xl border-2 border-dashed border-slate-300 bg-slate-50 py-8 transition-all hover:border-indigo-400 hover:bg-indigo-50"
            >
              <span class="iconify h-10 w-10 text-slate-400" data-icon="ph:file-csv"></span>
              <span class="text-sm font-semibold text-slate-600">Choose CSV file</span>
              <span class="text-xs text-slate-400">or drag and drop</span>
              <input type="file" accept=".csv" onchange="handleBankCSV(event)" class="hidden" id="bank-csv-input" />
            </label>
          </div>

          <!-- Step 2: Map Columns -->
          <div id="bank-step-2" class="hidden">
            <p class="mb-4 text-sm text-slate-600">
              We found <span id="csv-row-count" class="font-semibold">0</span> transactions. Map the columns:
            </p>
            <div class="space-y-4">
              <div>
                <label class="mb-1.5 block text-xs font-bold uppercase tracking-wider text-slate-500">Date Column</label>
                <select id="map-date" class="w-full rounded-xl border border-slate-200 bg-slate-50 p-3 text-sm font-medium"></select>
              </div>
              <div>
                <label class="mb-1.5 block text-xs font-bold uppercase tracking-wider text-slate-500">Description / Payee Column</label>
                <select id="map-description" class="w-full rounded-xl border border-slate-200 bg-slate-50 p-3 text-sm font-medium"></select>
              </div>
              <div>
                <label class="mb-1.5 block text-xs font-bold uppercase tracking-wider text-slate-500">Amount Column</label>
                <select id="map-amount" class="w-full rounded-xl border border-slate-200 bg-slate-50 p-3 text-sm font-medium"></select>
              </div>
            </div>
            <div class="mt-4 rounded-xl bg-slate-50 p-3">
              <div class="mb-2 text-xs font-bold uppercase tracking-wider text-slate-400">Preview</div>
              <div id="csv-preview" class="space-y-1 text-xs text-slate-600"></div>
            </div>
            <button
              onclick="detectRecurring()"
              class="mt-4 w-full rounded-xl bg-slate-900 py-3 font-bold text-white transition-all hover:bg-slate-800 active:scale-[0.98]"
            >
              Find Subscriptions
            </button>
          </div>

          <!-- Step 3: Review Detected -->
          <div id="bank-step-3" class="hidden">
            <p class="mb-4 text-sm text-slate-600">
              Found <span id="detected-count" class="font-semibold">0</span> potential subscriptions. Select which ones to add:
            </p>
            <div id="detected-list" class="space-y-2"></div>
            <div id="no-detected" class="hidden py-8 text-center">
              <span class="iconify mx-auto h-12 w-12 text-slate-300" data-icon="ph:magnifying-glass"></span>
              <p class="mt-2 text-sm text-slate-500">No recurring transactions found</p>
              <p class="text-xs text-slate-400">Try browsing other transactions below</p>
            </div>

            <div class="mt-5 border-t border-slate-100 pt-4">
              <button
                onclick="toggleOtherTransactions()"
                class="flex w-full items-center justify-between text-left"
                id="other-transactions-toggle"
              >
                <div>
                  <div class="text-xs font-bold uppercase tracking-wider text-slate-400">Didn't find something?</div>
                  <div class="text-xs text-slate-500">Browse <span id="other-count">0</span> other transactions</div>
                </div>
                <span class="iconify h-5 w-5 text-slate-400 transition-transform" data-icon="ph:caret-down-bold" id="other-caret"></span>
              </button>
              <div id="other-transactions" class="mt-3 hidden">
                <input
                  type="text"
                  placeholder="Search transactions..."
                  oninput="filterOtherTransactions(this.value)"
                  class="mb-3 w-full rounded-lg border border-slate-200 bg-slate-50 px-3 py-2 text-sm placeholder:text-slate-400 focus:border-indigo-500 focus:outline-none"
                />
                <div id="other-list" class="max-h-48 space-y-1.5 overflow-y-auto"></div>
              </div>
            </div>

            <button
              onclick="addSelectedSubscriptions()"
              id="add-selected-btn"
              class="mt-4 w-full rounded-xl bg-indigo-600 py-3 font-bold text-white transition-all hover:bg-indigo-700 active:scale-[0.98]"
            >
              Add Selected
            </button>
          </div>
        </div>
      </div>
    </div>
    <a href="https://www.exchangerate-api.com">Rates By Exchange Rate API</a>


    <script src="js/presets.js"></script>
    <script src="js/storage.js"></script>
    <script src="js/rates.js"></script>
    <script src="js/app.js"></script>
    <script src="js/treemap.js"></script>
    <script src="js/beeswarm.js"></script>
    <script src="js/circlepack.js"></script>
    <script src="js/modals.js"></script>
    <script src="js/bank-import.js"></script>
  </body>
</html>
```

## File: `styles.css`
```css
/* custom scrollbar - webkit only but whatever */
::-webkit-scrollbar { width: 6px }
::-webkit-scrollbar-track { background: transparent }
::-webkit-scrollbar-thumb {
  background-color: #cbd5e1;
  border-radius: 20px;
}

/* hide number input spinners */
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.iconify {
  display: inline-block;
  vertical-align: middle;
}

/* step wizard panels */
.step-panel { display: none }
.step-panel.active {
  display: flex;
  flex-direction: column;
  justify-content: center;
  min-height: calc(100vh - 200px);
  animation: fadeIn .4s ease-out;
}

.bento-grid-container { grid-auto-flow: dense }

/* treemap grid thing */
.treemap-container {
  position: relative;
  width: 100%;
  aspect-ratio: 4/3;
  border-radius: 1.5rem;
  overflow: hidden;
}

.treemap-cell {
  position: absolute;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-sizing: border-box;
  overflow: hidden;
  cursor: pointer;
  transition: z-index 0s;
  will-change: transform; /* helps with hover perf */
}
.treemap-cell:hover { z-index: 50 }

.treemap-cell-inner {
  position: absolute;
  inset: 3px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow: hidden;
  transition: transform .1s ease-out, box-shadow .2s ease;
}

.treemap-cell:hover .treemap-cell-inner {
  box-shadow: 0 20px 40px -10px rgba(0,0,0,.15);
  transform: scale(1.02);
}

.treemap-cell-name {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* tiny cells get centered content */
.treemap-cell.tiny .treemap-cell-inner {
  padding: 6px;
  justify-content: center;
  align-items: center;
}

/* beeswarm plot */
.beeswarm-dot {
  transition: transform 0.2s ease, z-index 0s;
  will-change: transform;
  -webkit-tap-highlight-color: transparent;
}

.beeswarm-dot:hover,
.beeswarm-dot.active {
  z-index: 100;
}

/* Show tooltip on tap for mobile */
.beeswarm-dot.active .beeswarm-tooltip {
  opacity: 1;
}

/* Prevent dots from being too small on mobile */
@media (max-width: 500px) {
  .beeswarm-dot > div:first-child {
    border-width: 1.5px;
  }
}

/* Circle pack bubbles */
.circlepack-bubble {
  transition: transform 0.2s ease, z-index 0s;
  will-change: transform;
  -webkit-tap-highlight-color: transparent;
}

.circlepack-bubble:hover,
.circlepack-bubble.active {
  z-index: 100;
}

.circlepack-bubble.active .circlepack-tooltip {
  opacity: 1;
}
```

## File: `wrangler.jsonc`
```
{
  "name": "subgrid",
  "pages_build_output_dir": ".",
  "compatibility_date": "2025-12-12"
}
```

## File: `js/app.js`
```javascript
let subs = [];
let step = 1;
let selectedCurrency = "USD";
let currentView = "treemap";

window.currencies = {
  USD: { symbol: "$", name: "US Dollar", rate: 1 },
  EUR: { symbol: "€", name: "Euro", rate: 0.92 },
  GBP: { symbol: "£", name: "British Pound", rate: 0.79 },
  JPY: { symbol: "¥", name: "Japanese Yen", rate: 149.5 },
  CNY: { symbol: "¥", name: "Chinese Yuan", rate: 7.24 },
  KRW: { symbol: "₩", name: "South Korean Won", rate: 1320 },
  INR: { symbol: "₹", name: "Indian Rupee", rate: 83.12 },
  CAD: { symbol: "C$", name: "Canadian Dollar", rate: 1.36 },
  AUD: { symbol: "A$", name: "Australian Dollar", rate: 1.53 },
  CHF: { symbol: "CHF", name: "Swiss Franc", rate: 0.88 },
  HKD: { symbol: "HK$", name: "Hong Kong Dollar", rate: 7.82 },
  SGD: { symbol: "S$", name: "Singapore Dollar", rate: 1.34 },
  SEK: { symbol: "kr", name: "Swedish Krona", rate: 10.42 },
  NOK: { symbol: "kr", name: "Norwegian Krone", rate: 10.85 },
  DKK: { symbol: "kr", name: "Danish Krone", rate: 6.87 },
  NZD: { symbol: "NZ$", name: "New Zealand Dollar", rate: 1.64 },
  MXN: { symbol: "MX$", name: "Mexican Peso", rate: 17.15 },
  BRL: { symbol: "R$", name: "Brazilian Real", rate: 4.97 },
  ZAR: { symbol: "R", name: "South African Rand", rate: 18.65 },
  RUB: { symbol: "₽", name: "Russian Ruble", rate: 92.5 },
  TRY: { symbol: "₺", name: "Turkish Lira", rate: 29.2 },
  PLN: { symbol: "zł", name: "Polish Zloty", rate: 3.98 },
  THB: { symbol: "฿", name: "Thai Baht", rate: 35.2 },
  IDR: { symbol: "Rp", name: "Indonesian Rupiah", rate: 15650 },
  MYR: { symbol: "RM", name: "Malaysian Ringgit", rate: 4.72 },
  PHP: { symbol: "₱", name: "Philippine Peso", rate: 55.8 },
  VND: { symbol: "₫", name: "Vietnamese Dong", rate: 24500 },
  TWD: { symbol: "NT$", name: "Taiwan Dollar", rate: 31.5 },
  AED: { symbol: "د.إ", name: "UAE Dirham", rate: 3.67 },
  SAR: { symbol: "﷼", name: "Saudi Riyal", rate: 3.75 },
  ILS: { symbol: "₪", name: "Israeli Shekel", rate: 3.68 },
  CZK: { symbol: "Kč", name: "Czech Koruna", rate: 22.8 },
  HUF: { symbol: "Ft", name: "Hungarian Forint", rate: 356 },
  RON: { symbol: "lei", name: "Romanian Leu", rate: 4.57 },
  BGN: { symbol: "лв", name: "Bulgarian Lev", rate: 1.8 },
  HRK: { symbol: "kn", name: "Croatian Kuna", rate: 6.93 },
  CLP: { symbol: "CLP$", name: "Chilean Peso", rate: 880 },
  COP: { symbol: "COL$", name: "Colombian Peso", rate: 3950 },
  ARS: { symbol: "ARS$", name: "Argentine Peso", rate: 365 },
  PEN: { symbol: "S/", name: "Peruvian Sol", rate: 3.72 },
  EGP: { symbol: "E£", name: "Egyptian Pound", rate: 30.9 },
  NGN: { symbol: "₦", name: "Nigerian Naira", rate: 785 },
  KES: { symbol: "KSh", name: "Kenyan Shilling", rate: 153 },
  PKR: { symbol: "₨", name: "Pakistani Rupee", rate: 278 },
  BDT: { symbol: "৳", name: "Bangladeshi Taka", rate: 110 },
  UAH: { symbol: "₴", name: "Ukrainian Hryvnia", rate: 37.5 },
};

// tailwind color palette - bg is the lighter shade, accent for gradients
const colors = [
  { id: "purple", bg: "#FAF5FF", accent: "#E9D5FF" },
  { id: "blue", bg: "#EFF6FF", accent: "#BFDBFE" },
  { id: "cyan", bg: "#ECFEFF", accent: "#A5F3FC" },
  { id: "green", bg: "#F0FDF4", accent: "#BBF7D0" },
  { id: "yellow", bg: "#FEFCE8", accent: "#FEF08A" },
  { id: "orange", bg: "#FFF7ED", accent: "#FED7AA" },
  { id: "pink", bg: "#FDF2F8", accent: "#FBCFE8" },
  { id: "rose", bg: "#FFF1F2", accent: "#FECDD3" },
  { id: "slate", bg: "#F8FAFC", accent: "#E2E8F0" },
  { id: "indigo", bg: "#EEF2FF", accent: "#C7D2FE" },
  { id: "teal", bg: "#F0FDFA", accent: "#99F6E4" },
  { id: "amber", bg: "#FFFBEB", accent: "#FDE68A" },
];

const randColor = () => colors[Math.floor(Math.random() * colors.length)];

function getColor(colorId) {
  const found = colors.find(c => c.id === colorId);
  return found ? found : randColor();
}

const currencyLocales = {
  USD: "en-US", EUR: "de-DE", GBP: "en-GB", JPY: "ja-JP", CNY: "zh-CN",
  KRW: "ko-KR", INR: "en-IN", CAD: "en-CA", AUD: "en-AU", CHF: "de-CH",
  HKD: "zh-HK", SGD: "en-SG", SEK: "sv-SE", NOK: "nb-NO", DKK: "da-DK",
  NZD: "en-NZ", MXN: "es-MX", BRL: "pt-BR", ZAR: "en-ZA", RUB: "ru-RU",
  TRY: "tr-TR", PLN: "pl-PL", THB: "th-TH", IDR: "id-ID", MYR: "ms-MY",
  PHP: "en-PH", VND: "vi-VN", TWD: "zh-TW", AED: "ar-AE", SAR: "ar-SA",
  ILS: "he-IL", CZK: "cs-CZ", HUF: "hu-HU", RON: "ro-RO", BGN: "bg-BG",
  HRK: "hr-HR", CLP: "es-CL", COP: "es-CO", ARS: "es-AR", PEN: "es-PE",
  EGP: "ar-EG", NGN: "en-NG", KES: "en-KE", PKR: "en-PK", BDT: "bn-BD",
  UAH: "uk-UA"
};

function convertToBase(amount, fromCurrency) {
  const from = currencies[fromCurrency] || currencies.USD;
  const to = currencies[selectedCurrency];
  const usdAmount = amount / from.rate;
  return usdAmount * to.rate;
}

function formatNum(amount, decimals, currencyCode) {
  const locale = currencyLocales[currencyCode] || "en-US";
  return amount.toLocaleString(locale, {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals
  });
}

function formatCurrency(baseAmount, decimals = 2) {
  const curr = currencies[selectedCurrency];
  const dec = curr.rate > 100 ? 0 : decimals;
  return curr.symbol + formatNum(baseAmount, dec, selectedCurrency);
}

function formatCurrencyShort(baseAmount) {
  const curr = currencies[selectedCurrency];
  if (baseAmount >= 1_000_000) return curr.symbol + (baseAmount / 1_000_000).toFixed(1) + "M";
  if (baseAmount >= 10_000) return curr.symbol + (baseAmount / 1_000).toFixed(0) + "k";
  if (curr.rate > 100) return curr.symbol + formatNum(Math.round(baseAmount), 0, selectedCurrency);
  return curr.symbol + formatNum(baseAmount, 0, selectedCurrency);
}

function formatOriginalPrice(sub) {
  const code = sub.currency || selectedCurrency || "USD";
  const curr = currencies[code] || currencies.USD;
  const dec = curr.rate > 100 ? 0 : 2;
  return curr.symbol + formatNum(sub.price, dec, code);
}

function formatOriginalMonthly(sub) {
  const code = sub.currency || selectedCurrency || "USD";
  const curr = currencies[code] || currencies.USD;
  let monthly = sub.price;
  if (sub.cycle === "Yearly") monthly = sub.price / 12;
  if (sub.cycle === "Weekly") monthly = sub.price * 4.33;
  const dec = curr.rate > 100 ? 0 : 2;
  return curr.symbol + formatNum(monthly, dec, code);
}

function formatOriginalMonthlyShort(sub) {
  const code = sub.currency || selectedCurrency || "USD";
  const curr = currencies[code] || currencies.USD;
  let monthly = sub.price;
  if (sub.cycle === "Yearly") monthly = sub.price / 12;
  if (sub.cycle === "Weekly") monthly = sub.price * 4.33;
  if (monthly >= 1_000_000) return curr.symbol + (monthly / 1_000_000).toFixed(1) + "M";
  if (monthly >= 10_000) return curr.symbol + (monthly / 1_000).toFixed(0) + "k";
  if (curr.rate > 100) return curr.symbol + formatNum(Math.round(monthly), 0, code);
  return curr.symbol + formatNum(monthly, 0, code);
}

function formatOriginalYearlyShort(sub) {
  const code = sub.currency || selectedCurrency || "USD";
  const curr = currencies[code] || currencies.USD;
  let yearly = sub.price * 12;
  if (sub.cycle === "Yearly") yearly = sub.price;
  if (sub.cycle === "Weekly") yearly = sub.price * 52;
  if (yearly >= 1_000_000) return curr.symbol + (yearly / 1_000_000).toFixed(1) + "M";
  if (yearly >= 10_000) return curr.symbol + (yearly / 1_000).toFixed(0) + "k";
  if (curr.rate > 100) return curr.symbol + formatNum(Math.round(yearly), 0, code);
  return curr.symbol + formatNum(yearly, 0, code);
}

function toMonthly(sub) {
  const subCurrency = sub.currency || selectedCurrency || "USD";
  let monthly = sub.price;
  if (sub.cycle === "Yearly") monthly = sub.price / 12;
  if (sub.cycle === "Weekly") monthly = sub.price * 4.33;
  return convertToBase(monthly, subCurrency);
}

function iconHtml(sub, className) {
  if (!sub.url) {
    return '<span class="iconify ' + className + ' text-slate-400 shrink-0" data-icon="ph:cube-bold"></span>';
  }

  const domain = sub.url.replace(/^(https?:\/\/)?(www\.)?/, "").split("/")[0];

  // logo.dev is pretty good at finding logos, free tier is enough for this
  const logoUrl = "https://img.logo.dev/" + domain + "?token=pk_KuI_oR-IQ1-fqpAfz3FPEw&size=100&retina=true&format=png";
  return '<img src="' + logoUrl + '" class="' + className + ' object-contain rounded-lg shrink-0" crossorigin="anonymous">';
}

function goToStep(stepNum) {
  document.querySelectorAll(".step-panel").forEach(panel => panel.classList.remove("active"));
  document.getElementById("step-" + stepNum).classList.add("active");

  const progressBar = document.getElementById("progress-bar");
  const indicator = document.getElementById("step-indicator");

  // tailwind doesn't support dynamic class names so we gotta hardcode these
  // tried using style.width but the transition didn't look as smooth
  const barClasses = "h-full bg-indigo-600 transition-all duration-500 ease-out rounded-full";
  if (stepNum === 1) {
    progressBar.className = barClasses + " w-1/2";
  } else {
    progressBar.className = barClasses + " w-full";
    setView(currentView);
  }

  indicator.innerText = "Step " + stepNum + " of 2";
  step = stepNum;
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function setView(view) {
  currentView = view;

  // Update button styles
  const views = ["treemap", "beeswarm", "circlepack"];
  const activeClass = "bg-slate-900 text-white";
  const inactiveClass = "bg-white text-slate-600";

  views.forEach(v => {
    const btn = document.getElementById("view-" + v);
    if (btn) {
      btn.classList.remove(...activeClass.split(" "), ...inactiveClass.split(" "));
      if (v === view) {
        btn.classList.add(...activeClass.split(" "));
      } else {
        btn.classList.add(...inactiveClass.split(" "));
      }
    }
  });

  // Toggle containers
  const treemapContainer = document.getElementById("bento-grid");
  const beeswarmContainer = document.getElementById("beeswarm-container");
  const circlepackContainer = document.getElementById("circlepack-container");

  treemapContainer.classList.add("hidden");
  beeswarmContainer.classList.add("hidden");
  circlepackContainer.classList.add("hidden");

  if (view === "treemap") {
    treemapContainer.classList.remove("hidden");
    renderGrid();
  } else if (view === "beeswarm") {
    beeswarmContainer.classList.remove("hidden");
    renderBeeswarm();
  } else if (view === "circlepack") {
    circlepackContainer.classList.remove("hidden");
    renderCirclePack();
  }
}

function renderList() {
  const listContainer = document.getElementById("sub-list-container");
  const emptyState = document.getElementById("empty-state");
  const nextBtn = document.getElementById("next-btn-1");
  const clearBtn = document.getElementById("clear-btn");

  if (subs.length === 0) {
    listContainer.classList.add("hidden");
    emptyState.classList.remove("hidden");
    nextBtn.disabled = true;
    nextBtn.classList.add("opacity-50", "cursor-not-allowed");
    clearBtn.classList.add("hidden");
    clearBtn.classList.remove("flex");
    return;
  }

  emptyState.classList.add("hidden");
  listContainer.classList.remove("hidden");
  nextBtn.disabled = false;
  nextBtn.classList.remove("opacity-50", "cursor-not-allowed");
  clearBtn.classList.remove("hidden");
  clearBtn.classList.add("flex");

  let html = "";
  for (let i = 0; i < subs.length; i++) {
    const sub = subs[i];
    const color = getColor(sub.color);

    html += '<div class="flex items-center justify-between p-4 bg-white border border-slate-100 rounded-2xl shadow-sm">';
    html += '<div class="flex items-center gap-3 flex-1 min-w-0 cursor-pointer" onclick="editSub(\'' + sub.id + '\')">';
    html += '<div class="w-1 h-10 rounded-full shrink-0" style="background: linear-gradient(180deg, ' + color.bg + ' 0%, ' + color.accent + ' 100%);"></div>';
    html += iconHtml(sub, "w-10 h-10");
    html += '<div class="min-w-0">';
    html += '<div class="font-bold text-slate-900 truncate">' + sub.name + '</div>';
    html += '<div class="text-xs text-slate-500">' + formatOriginalPrice(sub) + ' / ' + sub.cycle + '</div>';
    html += '</div></div>';
    html += '<div class="flex items-center gap-1">';
    html += '<button onclick="editSub(\'' + sub.id + '\')" class="text-slate-300 hover:text-indigo-500 p-2"><span class="iconify" data-icon="ph:pencil-simple-bold"></span></button>';
    html += '<button onclick="removeSub(\'' + sub.id + '\')" class="text-slate-300 hover:text-red-500 p-2"><span class="iconify" data-icon="ph:trash-bold"></span></button>';
    html += '</div></div>';
  }

  html += '<button onclick="openModal()" class="w-full py-4 rounded-2xl border-2 border-dashed border-slate-200 text-slate-400 font-bold hover:border-indigo-300 hover:text-indigo-600 hover:bg-white transition-all flex items-center justify-center gap-2">';
  html += '<span class="iconify w-5 h-5" data-icon="ph:plus-bold"></span> Add Another</button>';

  listContainer.innerHTML = html;
}


function renderPresets() {
  const grid = document.getElementById("presets-grid");
  if (!grid) return;

  // full list is overwhelming, just show common ones here
  const popular = presets.filter(p => p.popular);

  let html = "";
  for (let i = 0; i < popular.length; i++) {
    const preset = popular[i];
    const presetIndex = presets.indexOf(preset);
    const logo = "https://img.logo.dev/" + preset.domain + "?token=pk_KuI_oR-IQ1-fqpAfz3FPEw&size=100&retina=true&format=png";

    html += '<button onclick="openModalWithPreset(' + presetIndex + ')" ';
    html += 'class="flex flex-col items-center gap-1.5 rounded-xl border border-slate-100 bg-white p-2.5 shadow-sm transition-all hover:border-indigo-200 hover:shadow-md active:scale-95 sm:p-3">';
    html += '<img src="' + logo + '" class="h-8 w-8 rounded-lg object-contain sm:h-10 sm:w-10" crossorigin="anonymous" alt="' + preset.name + '">';
    html += '<span class="text-[10px] font-semibold text-slate-600 truncate w-full text-center sm:text-xs">' + preset.name + '</span>';
    html += '</button>';
  }
  grid.innerHTML = html;
}

function removeSub(subId) {
  subs = subs.filter(s => s.id !== subId);
  save();
}

function clearAllSubs() {
  if (!confirm("Delete all subscriptions?")) return;
  subs = [];
  save();
}

function editSub(subId) {
  const sub = subs.find(s => s.id === subId);
  if (!sub) return;

  document.getElementById("entry-id").value = sub.id;
  document.getElementById("name").value = sub.name;
  document.getElementById("price").value = sub.price;
  document.getElementById("sub-currency").value = sub.currency || selectedCurrency;
  document.getElementById("cycle").value = sub.cycle;
  document.getElementById("url").value = sub.url || "";

  updateFavicon(sub.url || "");
  pickColor(sub.color || randColor().id);

  document.getElementById("modal-title").innerText = "Edit Subscription";
  document.querySelector("#sub-form button[type='submit']").innerText = "Save Changes";

  showModal();
}

function initColorPicker() {
  const container = document.getElementById("color-selector");
  let html = "";
  for (const color of colors) {
    html += '<div onclick="pickColor(\'' + color.id + '\')" ';
    html += 'class="color-option cursor-pointer rounded-lg h-10 border-2 border-transparent transition-all hover:scale-105" ';
    html += 'data-val="' + color.id + '" ';
    html += 'style="background:linear-gradient(135deg,' + color.bg + ' 0%,' + color.accent + ' 100%)"></div>';
  }
  container.innerHTML = html;
}

function pickColor(colorId) {
  document.getElementById("selected-color").value = colorId;

  const options = document.querySelectorAll(".color-option");
  for (const opt of options) {
    if (opt.dataset.val === colorId) {
      opt.classList.add("ring-2", "ring-indigo-500", "ring-offset-2");
    } else {
      opt.classList.remove("ring-2", "ring-indigo-500", "ring-offset-2");
    }
  }
}

// debounce the favicon preview so we're not hammering the api on every keystroke
let faviconDebounce = null;

function updateFavicon(urlInput) {
  clearTimeout(faviconDebounce);

  faviconDebounce = setTimeout(function() {
    const preview = document.getElementById("favicon-preview");

    if (!urlInput) {
      preview.innerHTML = '<span class="iconify text-slate-300 w-5 h-5" data-icon="ph:globe-simple"></span>';
      return;
    }

    const domain = urlInput.replace(/^(https?:\/\/)?(www\.)?/, "").split("/")[0];

    // only fetch if domain looks legit (at least has a tld)
    if (domain.length > 3) {
      const logoUrl = "https://img.logo.dev/" + domain + "?token=pk_KuI_oR-IQ1-fqpAfz3FPEw&size=100&retina=true&format=png";
      preview.innerHTML = '<img src="' + logoUrl + '" class="w-full h-full object-cover" crossorigin="anonymous">';
    }
  }, 400);
}

function initCurrencySelector() {
  const dropdown = document.getElementById("currency-selector");
  if (!dropdown) return;

  let html = "";
  const currencyCodes = Object.keys(currencies);

  for (let i = 0; i < currencyCodes.length; i++) {
    const code = currencyCodes[i];
    const curr = currencies[code];
    const selected = (code === selectedCurrency) ? " selected" : "";
    html += '<option value="' + code + '"' + selected + '>' + curr.symbol + ' ' + code + ' - ' + curr.name + '</option>';
  }

  dropdown.innerHTML = html;
  dropdown.addEventListener("change", function(e) {
    saveCurrency(e.target.value);
  });
}

function initFormCurrencySelector() {
  const dropdown = document.getElementById("sub-currency");
  if (!dropdown) return;

  let html = "";
  const currencyCodes = Object.keys(currencies);

  for (let i = 0; i < currencyCodes.length; i++) {
    const code = currencyCodes[i];
    const curr = currencies[code];
    html += '<option value="' + code + '">' + curr.symbol + ' ' + code + '</option>';
  }

  dropdown.innerHTML = html;
  dropdown.value = selectedCurrency;
}

function handleFormSubmit(evt) {
  evt.preventDefault();

  const existingId = document.getElementById("entry-id").value;

  const subData = {
    id: existingId || Date.now().toString(),
    name: document.getElementById("name").value,
    price: parseFloat(document.getElementById("price").value),
    currency: document.getElementById("sub-currency").value,
    cycle: document.getElementById("cycle").value,
    url: document.getElementById("url").value,
    color: document.getElementById("selected-color").value || randColor().id,
    date: document.getElementById("date").value || ""
  };

  if (existingId) {
    const index = subs.findIndex(s => s.id === existingId);
    if (index !== -1) {
      subs[index] = subData;
    }
  } else {
    subs.push(subData);
  }

  save();
  hideModal();
}

document.addEventListener("DOMContentLoaded", async () => {
  await window.initRates();
  load();
  loadCurrency();
  initColorPicker();
  initCurrencySelector();
  initFormCurrencySelector();
  renderPresets();
  renderList();
  document.getElementById("date").value = new Date().toISOString().split("T")[0];
});
```

## File: `js/bank-import.js`
```javascript
let csvData = [];
let csvHeaders = [];
let detectedSubs = [];
let otherTransactions = [];
let otherExpanded = false;

// cache these so we're not querying the dom every time
const bankBackdrop = document.getElementById("bank-import-backdrop");
const bankPanel = document.getElementById("bank-import-panel");
const bankInner = bankPanel ? bankPanel.querySelector("div") : null;

function openBankImport() {
  document.getElementById("bank-step-1").classList.remove("hidden");
  document.getElementById("bank-step-2").classList.add("hidden");
  document.getElementById("bank-step-3").classList.add("hidden");
  document.getElementById("bank-csv-input").value = "";

  csvData = [];
  csvHeaders = [];
  detectedSubs = [];
  otherTransactions = [];
  otherExpanded = false;

  if (bankBackdrop) bankBackdrop.classList.remove("hidden");
  if (bankPanel) bankPanel.classList.remove("hidden");

  // rAF needed or the transition won't trigger
  requestAnimationFrame(function() {
    if (bankBackdrop) bankBackdrop.classList.remove("opacity-0");
    if (bankInner) {
      bankInner.classList.remove("translate-y-full", "sm:scale-95", "opacity-0");
      bankInner.classList.add("translate-y-0", "sm:translate-y-0", "sm:scale-100", "opacity-100");
    }
  });
}

function closeBankImport() {
  if (bankBackdrop) bankBackdrop.classList.add("opacity-0");

  if (bankInner) {
    bankInner.classList.remove("translate-y-0", "sm:translate-y-0", "sm:scale-100", "opacity-100");
    bankInner.classList.add("translate-y-full", "sm:scale-95", "opacity-0");
  }

  setTimeout(function() {
    if (bankBackdrop) bankBackdrop.classList.add("hidden");
    if (bankPanel) bankPanel.classList.add("hidden");
  }, 300);
}

// basic csv parser that handles quoted fields
// not perfect but works for most bank exports
function parseCSV(text) {
  const lines = text.trim().split(/\r?\n/);
  if (lines.length < 2) {
    return { headers: [], rows: [] };
  }

  function parseLine(line) {
    const fields = [];
    let current = "";
    let insideQuotes = false;

    for (let i = 0; i < line.length; i++) {
      const ch = line[i];

      if (ch === '"') {
        insideQuotes = !insideQuotes;
      } else if (ch === "," && !insideQuotes) {
        fields.push(current.trim());
        current = "";
      } else {
        current += ch;
      }
    }
    fields.push(current.trim());
    return fields;
  }

  const headers = parseLine(lines[0]);

  const rows = [];
  for (let i = 1; i < lines.length; i++) {
    const row = parseLine(lines[i]);
    const hasData = row.some(cell => cell !== "");
    if (hasData) rows.push(row);
  }

  return { headers: headers, rows: rows };
}

function handleBankCSV(event) {
  const file = event.target.files && event.target.files[0];
  if (!file) return;

  const reader = new FileReader();

  reader.onload = function(e) {
    const parsed = parseCSV(e.target.result);
    const headers = parsed.headers;
    const rows = parsed.rows;

    if (headers.length < 3 || rows.length < 1) {
      alert("Invalid CSV file. Make sure it has headers and transaction data.");
      return;
    }

    csvHeaders = headers;
    csvData = rows;

    let optionsHtml = "";
    for (let i = 0; i < headers.length; i++) {
      optionsHtml += '<option value="' + i + '">' + headers[i] + '</option>';
    }

    const dateSelect = document.getElementById("map-date");
    const descSelect = document.getElementById("map-description");
    const amountSelect = document.getElementById("map-amount");

    dateSelect.innerHTML = optionsHtml;
    descSelect.innerHTML = optionsHtml;
    amountSelect.innerHTML = optionsHtml;

    // try to auto-detect which columns are which
    // this works for most bank exports but user can fix if wrong
    const lowerHeaders = headers.map(h => h.toLowerCase());

    let dateIdx = -1;
    let descIdx = -1;
    let amountIdx = -1;

    for (let i = 0; i < lowerHeaders.length; i++) {
      const h = lowerHeaders[i];
      if (dateIdx < 0 && (h.includes("date") || h.includes("posted") || h.includes("time"))) {
        dateIdx = i;
      }
      if (descIdx < 0 && (h.includes("description") || h.includes("payee") || h.includes("merchant") || h.includes("name") || h.includes("memo") || h.includes("details"))) {
        descIdx = i;
      }
      if (amountIdx < 0 && (h.includes("amount") || h.includes("debit") || h.includes("withdrawal") || h.includes("charge") || h.includes("payment"))) {
        amountIdx = i;
      }
    }

    if (dateIdx >= 0) dateSelect.value = dateIdx;
    if (descIdx >= 0) descSelect.value = descIdx;
    if (amountIdx >= 0) amountSelect.value = amountIdx;

    updateCSVPreview();

    dateSelect.onchange = updateCSVPreview;
    descSelect.onchange = updateCSVPreview;
    amountSelect.onchange = updateCSVPreview;

    document.getElementById("csv-row-count").textContent = rows.length;
    document.getElementById("bank-step-1").classList.add("hidden");
    document.getElementById("bank-step-2").classList.remove("hidden");
  };

  reader.readAsText(file);
}

function updateCSVPreview() {
  const dateCol = parseInt(document.getElementById("map-date").value);
  const descCol = parseInt(document.getElementById("map-description").value);
  const amtCol = parseInt(document.getElementById("map-amount").value);

  const previewEl = document.getElementById("csv-preview");

  let html = "";
  const sampleRows = csvData.slice(0, 3);

  for (let i = 0; i < sampleRows.length; i++) {
    const row = sampleRows[i];
    html += '<div class="flex justify-between py-1 border-b border-slate-100 last:border-0">';
    html += '<span class="text-slate-400 w-20 shrink-0">' + (row[dateCol] || "-") + '</span>';
    html += '<span class="flex-1 truncate px-2">' + (row[descCol] || "-") + '</span>';
    html += '<span class="text-slate-900 font-medium">' + (row[amtCol] || "-") + '</span>';
    html += '</div>';
  }

  previewEl.innerHTML = html;
}

function detectRecurring() {
  const dateCol = parseInt(document.getElementById("map-date").value);
  const descCol = parseInt(document.getElementById("map-description").value);
  const amtCol = parseInt(document.getElementById("map-amount").value);

  const transactions = [];
  for (let i = 0; i < csvData.length; i++) {
    const row = csvData[i];
    const rawAmt = row[amtCol] ? row[amtCol].replace(/[^0-9.-]/g, "") : "0";
    const amount = Math.abs(parseFloat(rawAmt));
    const date = new Date(row[dateCol]);
    const desc = row[descCol] ? row[descCol].trim() : "";

    if (!desc || isNaN(amount) || amount <= 0 || isNaN(date.getTime())) continue;

    transactions.push({ date: date, description: desc, amount: amount });
  }

  // normalize merchant names to group similar transactions together
  // eg "NETFLIX.COM" and "NETFLIX INC" should match
  function normalizeDesc(str) {
    return str
      .toUpperCase()
      .replace(/[^A-Z0-9\s]/g, " ")
      .replace(/\s+/g, " ")
      .replace(/\b(INC|LLC|LTD|CORP|CO|PAYMENT|PURCHASE|POS|ACH|DEBIT)\b/g, "")
      .trim()
      .split(" ")
      .slice(0, 3) // just take first 3 words
      .join(" ");
  }

  const groups = {};
  for (let i = 0; i < transactions.length; i++) {
    const txn = transactions[i];
    const key = normalizeDesc(txn.description);
    if (!key) continue;

    if (!groups[key]) {
      groups[key] = { txns: [], names: new Set() };
    }
    groups[key].txns.push(txn);
    groups[key].names.add(txn.description);
  }

  const recurring = [];
  const groupKeys = Object.keys(groups);

  for (let g = 0; g < groupKeys.length; g++) {
    const key = groupKeys[g];
    const group = groups[key];

    // need at least 2 occurrences to detect a pattern
    if (group.txns.length < 2) continue;

    group.txns.sort(function(a, b) { return a.date - b.date; });

    let totalDays = 0;
    for (let i = 1; i < group.txns.length; i++) {
      const daysBetween = Math.round((group.txns[i].date - group.txns[i-1].date) / (1000 * 60 * 60 * 24));
      totalDays += daysBetween;
    }
    const avgDays = totalDays / (group.txns.length - 1);

    // ranges are fuzzy to account for weekends and billing day variations
    let cycle = null;
    if (avgDays >= 6 && avgDays <= 8) cycle = "Weekly";
    else if (avgDays >= 13 && avgDays <= 16) cycle = "Biweekly";
    else if (avgDays >= 25 && avgDays <= 35) cycle = "Monthly";
    else if (avgDays >= 85 && avgDays <= 100) cycle = "Quarterly";
    else if (avgDays >= 355 && avgDays <= 375) cycle = "Yearly";

    if (!cycle) continue;

    // subscriptions have fixed prices, so check amounts are within 20%
    let totalAmount = 0;
    for (let i = 0; i < group.txns.length; i++) {
      totalAmount += group.txns[i].amount;
    }
    const avgAmt = totalAmount / group.txns.length;

    let isConsistent = true;
    for (let i = 0; i < group.txns.length; i++) {
      const variance = Math.abs(group.txns[i].amount - avgAmt) / avgAmt;
      if (variance >= 0.2) {
        isConsistent = false;
        break;
      }
    }
    if (!isConsistent) continue;

    const nameCount = {};
    for (const name of group.names) {
      nameCount[name] = (nameCount[name] || 0) + 1;
    }
    let bestName = "";
    let bestCount = 0;
    for (const name in nameCount) {
      if (nameCount[name] > bestCount) {
        bestCount = nameCount[name];
        bestName = name;
      }
    }

    recurring.push({
      name: bestName,
      price: Math.round(avgAmt * 100) / 100,
      cycle: (cycle === "Biweekly" || cycle === "Quarterly") ? "Monthly" : cycle,
      count: group.txns.length,
      selected: true
    });
  }

  recurring.sort(function(a, b) {
    if (b.count !== a.count) return b.count - a.count;
    return b.price - a.price;
  });

  const detectedNames = new Set();
  for (let i = 0; i < recurring.length; i++) {
    detectedNames.add(recurring[i].name.toUpperCase());
  }

  const otherMap = {};
  for (let i = 0; i < transactions.length; i++) {
    const txn = transactions[i];
    if (detectedNames.has(txn.description.toUpperCase())) continue;

    if (!otherMap[txn.description]) {
      otherMap[txn.description] = { name: txn.description, price: txn.amount, count: 0 };
    }
    otherMap[txn.description].count++;
    otherMap[txn.description].price = txn.amount;
  }

  // $500+ is probably not a subscription
  const otherList = [];
  for (const key in otherMap) {
    const item = otherMap[key];
    if (item.price > 0 && item.price < 500) {
      otherList.push(item);
    }
  }
  otherList.sort(function(a, b) {
    if (b.count !== a.count) return b.count - a.count;
    return a.name.localeCompare(b.name);
  });

  detectedSubs = recurring;
  otherTransactions = otherList;
  otherExpanded = false;

  renderDetectedList();
  renderOtherTransactions();

  document.getElementById("bank-step-2").classList.add("hidden");
  document.getElementById("bank-step-3").classList.remove("hidden");
}

function renderDetectedList() {
  const listEl = document.getElementById("detected-list");
  const noResultsEl = document.getElementById("no-detected");
  const addBtn = document.getElementById("add-selected-btn");

  document.getElementById("detected-count").textContent = detectedSubs.length;

  if (detectedSubs.length === 0) {
    listEl.classList.add("hidden");
    noResultsEl.classList.remove("hidden");
    addBtn.classList.add("hidden");
    return;
  }

  listEl.classList.remove("hidden");
  noResultsEl.classList.add("hidden");
  addBtn.classList.remove("hidden");

  let html = "";
  for (let i = 0; i < detectedSubs.length; i++) {
    const sub = detectedSubs[i];
    const ringClass = sub.selected ? " ring-2 ring-indigo-500" : "";
    const checked = sub.selected ? " checked" : "";

    html += '<label class="flex items-center gap-3 rounded-xl border border-slate-100 bg-white p-3 cursor-pointer hover:bg-slate-50 transition-colors' + ringClass + '">';
    html += '<input type="checkbox"' + checked + ' onchange="toggleDetectedSub(' + i + ')" class="h-5 w-5 rounded border-slate-300 text-indigo-600 focus:ring-indigo-500">';
    html += '<div class="flex-1 min-w-0">';
    html += '<div class="font-semibold text-slate-900 text-sm truncate">' + sub.name + '</div>';
    html += '<div class="text-xs text-slate-500">' + sub.cycle + ' · Found ' + sub.count + 'x</div>';
    html += '</div>';
    html += '<div class="text-sm font-bold text-slate-900">$' + sub.price.toFixed(2) + '</div>';
    html += '</label>';
  }

  listEl.innerHTML = html;
  updateAddButtonText();
}

function toggleDetectedSub(idx) {
  detectedSubs[idx].selected = !detectedSubs[idx].selected;
  renderDetectedList();
}

function toggleOtherTransactions() {
  otherExpanded = !otherExpanded;

  var container = document.getElementById("other-transactions");
  var caret = document.getElementById("other-caret");

  if (otherExpanded) {
    container.classList.remove("hidden");
    caret.style.transform = "rotate(180deg)";
  } else {
    container.classList.add("hidden");
    caret.style.transform = "";
  }
}

function renderOtherTransactions(searchFilter) {
  const listEl = document.getElementById("other-list");
  document.getElementById("other-count").textContent = otherTransactions.length;

  let filtered = otherTransactions;
  if (searchFilter && searchFilter.length > 0) {
    const q = searchFilter.toLowerCase();
    filtered = otherTransactions.filter(function(t) {
      return t.name.toLowerCase().includes(q);
    });
  }

  if (filtered.length === 0) {
    listEl.innerHTML = '<div class="text-xs text-slate-400 text-center py-3">No transactions found</div>';
    return;
  }

  // rendering 100+ buttons gets sluggish
  let html = "";
  const limit = Math.min(filtered.length, 50);

  for (let i = 0; i < limit; i++) {
    const txn = filtered[i];
    const origIdx = otherTransactions.indexOf(txn);

    html += '<button onclick="addFromOther(' + origIdx + ')" class="flex w-full items-center justify-between rounded-lg border border-slate-100 bg-white px-3 py-2 text-left text-sm transition-all hover:border-indigo-200 hover:bg-indigo-50">';
    html += '<div class="flex-1 min-w-0">';
    html += '<div class="font-medium text-slate-700 truncate">' + txn.name + '</div>';
    html += '<div class="text-xs text-slate-400">' + txn.count + 'x in statement</div>';
    html += '</div>';
    html += '<div class="flex items-center gap-2">';
    html += '<span class="font-semibold text-slate-900">$' + txn.price.toFixed(2) + '</span>';
    html += '<span class="iconify h-4 w-4 text-slate-400" data-icon="ph:plus-circle-bold"></span>';
    html += '</div></button>';
  }

  listEl.innerHTML = html;
}

function filterOtherTransactions(q) {
  renderOtherTransactions(q);
}

function addFromOther(idx) {
  const txn = otherTransactions[idx];
  if (!txn) return;

  detectedSubs.push({
    name: txn.name,
    price: txn.price,
    cycle: "Monthly", // default to monthly, user can change later
    count: txn.count,
    selected: true
  });

  otherTransactions.splice(idx, 1);
  renderDetectedList();
  renderOtherTransactions();
}

function updateAddButtonText() {
  let selectedCount = 0;
  for (let i = 0; i < detectedSubs.length; i++) {
    if (detectedSubs[i].selected) selectedCount++;
  }

  const btn = document.getElementById("add-selected-btn");

  if (selectedCount > 0) {
    const plural = selectedCount > 1 ? "s" : "";
    btn.textContent = "Add " + selectedCount + " Subscription" + plural;
    btn.disabled = false;
    btn.classList.remove("opacity-50", "cursor-not-allowed");
  } else {
    btn.textContent = "Add Selected";
    btn.disabled = true;
    btn.classList.add("opacity-50", "cursor-not-allowed");
  }
}

function addSelectedSubscriptions() {
  const toAdd = detectedSubs.filter(function(s) { return s.selected; });
  if (toAdd.length === 0) return;

  for (let i = 0; i < toAdd.length; i++) {
    const sub = toAdd[i];
    subs.push({
      id: Date.now().toString() + Math.random().toString(36).slice(2),
      name: cleanSubscriptionName(sub.name),
      price: sub.price,
      currency: selectedCurrency,
      cycle: sub.cycle,
      url: "",
      color: randColor().id
    });
  }

  save();
  closeBankImport();

  const plural = toAdd.length > 1 ? "s" : "";
  alert("Added " + toAdd.length + " subscription" + plural + "!");
}

// bank names are ugly like "NETFLIX.COM*PURCHASE" so clean them up
function cleanSubscriptionName(rawName) {
  let name = rawName
    .replace(/\*+/g, " ")
    .replace(/\s+/g, " ")
    .replace(/\b(PURCHASE|POS|ACH|DEBIT|RECURRING|PAYMENT)\b/gi, "")
    .trim();

  const words = name.split(" ");
  for (let i = 0; i < words.length; i++) {
    if (words[i].length > 0) {
      words[i] = words[i].charAt(0).toUpperCase() + words[i].slice(1).toLowerCase();
    }
  }

  return words.join(" ").substring(0, 30);
}
```

## File: `js/beeswarm.js`
```javascript
// dots go on x-axis by value, then get pushed up/down to avoid overlap

class Beeswarm {
  constructor(width, height, padding = 20, isMobile = false) {
    this.width = width;
    this.height = height;
    this.padding = padding;
    this.centerY = height / 2;
    this.isMobile = isMobile;
  }

  layout(items) {
    if (!items.length) return [];

    // process cheap items first - they cluster on the left and this
    // gives a more balanced distribution when we push dots up/down
    const sorted = [...items].sort((a, b) => a.cost - b.cost);

    const costs = sorted.map(d => d.cost);
    const minCost = Math.min(...costs);
    const maxCost = Math.max(...costs);

    // fewer pixels to work with on mobile, so smaller dots
    const maxRadius = this.isMobile ? 28 : 45;
    const minRadius = this.isMobile ? 16 : 22;
    const spacing = this.isMobile ? 2.8 : 2.2;

    const baseRadius = Math.min(
      maxRadius,
      Math.max(minRadius, (this.width - this.padding * 2) / (items.length * spacing))
    );

    const xScale = (cost) => {
      if (maxCost === minCost) return this.width / 2;
      const ratio = (cost - minCost) / (maxCost - minCost);
      return this.padding + baseRadius + ratio * (this.width - this.padding * 2 - baseRadius * 2);
    };

    const placed = [];

    const positioned = sorted.map(item => {
      const x = xScale(item.cost);
      const y = this._findYPosition(x, baseRadius, placed);

      const result = { ...item, x, y, radius: baseRadius };
      placed.push(result);
      return result;
    });

    return this._normalizeY(positioned);
  }

  _findYPosition(x, radius, placed) {
    // start center, then zigzag up/down until we find a free spot
    let y = this.centerY;
    let offset = 0;
    let direction = 1;
    const step = radius * 0.8;

    while (this._hasCollision(x, y, radius, placed)) {
      offset += step;
      y = this.centerY + offset * direction;
      direction *= -1;

      if (offset > this.height) break; // shouldn't happen but just in case
    }

    return y;
  }

  _hasCollision(x, y, radius, placed) {
    // 1.8x radius means small gap between circles, looks cleaner
    const minDistance = radius * 1.8;

    for (const item of placed) {
      const dx = x - item.x;
      const dy = y - item.y;
      if (Math.sqrt(dx * dx + dy * dy) < minDistance) {
        return true;
      }
    }
    return false;
  }

  _normalizeY(items) {
    if (!items.length) return items;

    // the zigzag placement can make the swarm off-center or overflow
    // so we scale and recenter everything to fit nicely
    const ys = items.map(d => d.y);
    const minY = Math.min(...ys);
    const maxY = Math.max(...ys);
    const rangeY = maxY - minY;

    const availableHeight = this.height - this.padding * 2;
    const scale = rangeY > 0 ? Math.min(1, availableHeight / rangeY) : 1;
    const centerCurrent = (minY + maxY) / 2;

    return items.map(item => ({
      ...item,
      y: this.centerY + (item.y - centerCurrent) * scale,
    }));
  }
}

function renderBeeswarm() {
  const container = document.getElementById("beeswarm-container");
  if (!container || !subs.length) {
    if (container) {
      container.innerHTML = `
        <div class="flex items-center justify-center h-full text-slate-400">
          <p>Add subscriptions to see the beeswarm plot</p>
        </div>
      `;
    }
    return;
  }

  const rect = container.getBoundingClientRect();
  const width = rect.width || 800;
  const height = rect.height || 600;
  const isMobile = width < 500;
  const padding = isMobile ? 20 : 40;

  const items = subs.map(sub => ({ ...sub, cost: toMonthly(sub) }));
  const beeswarm = new Beeswarm(width, height, padding, isMobile);
  const positioned = beeswarm.layout(items);

  const costs = positioned.map(d => d.cost);
  const minCost = Math.min(...costs);
  const maxCost = Math.max(...costs);

  let html = `
    <div class="absolute left-4 right-4 sm:left-10 sm:right-10 top-1/2 h-0.5 bg-slate-200 -translate-y-1/2"></div>
    <div class="absolute left-4 sm:left-10 top-1/2 mt-6 sm:mt-8 text-[10px] sm:text-xs text-slate-400 font-medium">
      ${formatCurrencyShort(minCost)}
    </div>
    <div class="absolute right-4 sm:right-10 top-1/2 mt-6 sm:mt-8 text-[10px] sm:text-xs text-slate-400 font-medium">
      ${formatCurrencyShort(maxCost)}
    </div>
    <div class="absolute left-1/2 -translate-x-1/2 bottom-2 sm:bottom-4 text-[10px] sm:text-xs text-slate-500 font-semibold uppercase tracking-wider">
      Monthly Cost
    </div>
  `;

  positioned.forEach(item => {
    const color = getColor(item.color);
    const size = item.radius * 2;
    const domain = extractDomain(item.url);
    const logoUrl = domain
      ? `https://img.logo.dev/${domain}?token=pk_KuI_oR-IQ1-fqpAfz3FPEw&size=100&retina=true&format=png`
      : null;

    html += `
      <div
        class="beeswarm-dot absolute cursor-pointer group"
        data-id="${item.id}"
        style="left: ${item.x}px; top: ${item.y}px; width: ${size}px; height: ${size}px; transform: translate(-50%, -50%);"
      >
        <div
          class="w-full h-full rounded-full shadow-md sm:shadow-lg transition-all duration-200 hover:scale-110 hover:shadow-xl flex items-center justify-center overflow-hidden"
          style="background: linear-gradient(135deg, ${color.bg} 0%, ${color.accent} 100%); border: 2px solid ${color.accent};"
        >
          ${logoUrl
            ? `<img src="${logoUrl}" alt="${item.name}" class="w-3/4 h-3/4 object-contain rounded-sm sm:rounded-md" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';" /><span class="text-[10px] sm:text-sm font-bold hidden items-center justify-center" style="color: ${color.accent};">${item.name.charAt(0)}</span>`
            : `<span class="text-[10px] sm:text-sm font-bold" style="color: ${color.accent};">${item.name.charAt(0)}</span>`
          }
        </div>
        <div class="beeswarm-tooltip absolute bottom-full left-1/2 -translate-x-1/2 mb-2 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-20">
          <div class="bg-slate-900 text-white text-[10px] sm:text-xs rounded-lg px-2 py-1.5 sm:px-3 sm:py-2 whitespace-nowrap shadow-xl">
            <div class="font-semibold">${item.name}</div>
            <div class="text-slate-300">${formatCurrency(item.cost)}/mo</div>
          </div>
          <div class="absolute top-full left-1/2 -translate-x-1/2 border-4 border-transparent border-t-slate-900"></div>
        </div>
      </div>
    `;
  });

  container.innerHTML = html;

  // mobile needs tap-to-show-tooltip, then tap-again-to-edit
  // desktop just clicks to edit directly
  let activeTooltip = null;

  container.querySelectorAll(".beeswarm-dot").forEach(dot => {
    let tapCount = 0;
    let tapTimer = null;

    dot.addEventListener("click", e => {
      if (window.innerWidth < 500) {
        tapCount++;
        if (tapCount === 1) {
          if (activeTooltip && activeTooltip !== dot) {
            activeTooltip.classList.remove("active");
          }
          dot.classList.add("active");
          activeTooltip = dot;
          tapTimer = setTimeout(() => { tapCount = 0; }, 300);
        } else {
          clearTimeout(tapTimer);
          tapCount = 0;
          editSub(dot.dataset.id);
        }
      } else {
        editSub(dot.dataset.id);
      }
    });
  });

  container.addEventListener("click", e => {
    if (!e.target.closest(".beeswarm-dot") && activeTooltip) {
      activeTooltip.classList.remove("active");
      activeTooltip = null;
    }
  });
}

function extractDomain(url) {
  if (!url) return "";
  try {
    if (!url.startsWith("http")) url = "https://" + url;
    return new URL(url).hostname.replace("www.", "");
  } catch {
    return url.replace("www.", "");
  }
}
```

## File: `js/circlepack.js`
```javascript
// attempt at d3's circle packing without d3
// ref: https://observablehq.com/@d3/circle-packing

class CirclePack {
  constructor(width, height, padding = 20) {
    this.width = width;
    this.height = height;
    this.padding = padding;
    this.centerX = width / 2;
    this.centerY = height / 2;
  }

  layout(items) {
    if (!items.length) return [];

    // big circles are harder to fit later, so place them first
    const sorted = [...items].sort((a, b) => b.cost - a.cost);

    const costs = sorted.map(d => d.cost);
    const minCost = Math.min(...costs);
    const maxCost = Math.max(...costs);

    const availableArea = Math.min(this.width, this.height) * 0.45;
    const minRadius = 20;
    const maxRadius = Math.min(80, availableArea * 0.4);

    const withRadius = sorted.map(item => {
      // sqrt because circle area grows with r², not r
      const ratio = maxCost === minCost ? 0.5 : (item.cost - minCost) / (maxCost - minCost);
      const radius = minRadius + Math.sqrt(ratio) * (maxRadius - minRadius);
      return { ...item, radius };
    });

    return this._packCircles(withRadius);
  }

  _packCircles(circles) {
    if (circles.length === 0) return [];
    if (circles.length === 1) {
      return [{ ...circles[0], x: this.centerX, y: this.centerY }];
    }

    const placed = [];

    placed.push({
      ...circles[0],
      x: this.centerX,
      y: this.centerY
    });

    placed.push({
      ...circles[1],
      x: this.centerX + circles[0].radius + circles[1].radius + 4,
      y: this.centerY
    });

    for (let i = 2; i < circles.length; i++) {
      const circle = circles[i];
      const pos = this._findBestPosition(circle.radius, placed);
      placed.push({ ...circle, x: pos.x, y: pos.y });
    }

    return this._centerPack(placed);
  }

  _findBestPosition(radius, placed) {
    // prefer positions closer to center for a tighter pack
    let bestPos = null;
    let bestDist = Infinity;

    for (let i = 0; i < placed.length; i++) {
      for (let j = i + 1; j < placed.length; j++) {
        const positions = this._tangentPositions(placed[i], placed[j], radius);

        for (const pos of positions) {
          if (!this._hasCollision(pos.x, pos.y, radius, placed)) {
            const dist = Math.sqrt(
              Math.pow(pos.x - this.centerX, 2) +
              Math.pow(pos.y - this.centerY, 2)
            );
            if (dist < bestDist) {
              bestDist = dist;
              bestPos = pos;
            }
          }
        }
      }
    }

    // tangent-to-two failed, try tangent-to-one at fixed angles
    if (!bestPos) {
      for (const p of placed) {
        const angles = [0, Math.PI/4, Math.PI/2, 3*Math.PI/4, Math.PI, 5*Math.PI/4, 3*Math.PI/2, 7*Math.PI/4];
        for (const angle of angles) {
          const dist = p.radius + radius + 4;
          const x = p.x + Math.cos(angle) * dist;
          const y = p.y + Math.sin(angle) * dist;

          if (!this._hasCollision(x, y, radius, placed)) {
            const centerDist = Math.sqrt(
              Math.pow(x - this.centerX, 2) +
              Math.pow(y - this.centerY, 2)
            );
            if (centerDist < bestDist) {
              bestDist = centerDist;
              bestPos = { x, y };
            }
          }
        }
      }
    }

    // shouldn't happen, but just in case
    if (!bestPos) {
      bestPos = { x: this.centerX, y: this.centerY + 100 };
    }

    return bestPos;
  }

  _tangentPositions(c1, c2, r) {
    const d = Math.sqrt(Math.pow(c2.x - c1.x, 2) + Math.pow(c2.y - c1.y, 2));
    const r1 = c1.radius + r + 4; // 4px gap looks cleaner than touching
    const r2 = c2.radius + r + 4;

    if (d > r1 + r2) return [];
    if (d < Math.abs(r1 - r2)) return [];

    const a = (r1 * r1 - r2 * r2 + d * d) / (2 * d);
    const h2 = r1 * r1 - a * a;

    if (h2 < 0) return [];

    const h = Math.sqrt(h2);

    const px = c1.x + a * (c2.x - c1.x) / d;
    const py = c1.y + a * (c2.y - c1.y) / d;

    const dx = h * (c2.y - c1.y) / d;
    const dy = h * (c2.x - c1.x) / d;

    return [
      { x: px + dx, y: py - dy },
      { x: px - dx, y: py + dy }
    ];
  }

  _hasCollision(x, y, radius, placed) {
    const gap = 4;
    for (const p of placed) {
      const dist = Math.sqrt(Math.pow(x - p.x, 2) + Math.pow(y - p.y, 2));
      if (dist < radius + p.radius + gap) {
        return true;
      }
    }
    return false;
  }

  _centerPack(circles) {
    if (!circles.length) return circles;

    let minX = Infinity, maxX = -Infinity;
    let minY = Infinity, maxY = -Infinity;

    for (const c of circles) {
      minX = Math.min(minX, c.x - c.radius);
      maxX = Math.max(maxX, c.x + c.radius);
      minY = Math.min(minY, c.y - c.radius);
      maxY = Math.max(maxY, c.y + c.radius);
    }

    const packWidth = maxX - minX;
    const packHeight = maxY - minY;
    const packCenterX = (minX + maxX) / 2;
    const packCenterY = (minY + maxY) / 2;

    const scaleX = (this.width - this.padding * 2) / packWidth;
    const scaleY = (this.height - this.padding * 2) / packHeight;
    const scale = Math.min(1, scaleX, scaleY);

    return circles.map(c => ({
      ...c,
      x: this.centerX + (c.x - packCenterX) * scale,
      y: this.centerY + (c.y - packCenterY) * scale,
      radius: c.radius * scale
    }));
  }
}

function renderCirclePack() {
  const container = document.getElementById("circlepack-container");
  if (!container || !subs.length) {
    if (container) {
      container.innerHTML = `
        <div class="flex items-center justify-center h-full text-slate-400">
          <p>Add subscriptions to see the circle pack</p>
        </div>
      `;
    }
    return;
  }

  const rect = container.getBoundingClientRect();
  const width = rect.width || 800;
  const height = rect.height || 600;

  const items = subs.map(sub => ({ ...sub, cost: toMonthly(sub) }));
  const packer = new CirclePack(width, height, 30);
  const positioned = packer.layout(items);

  let html = "";

  positioned.forEach(item => {
    const color = getColor(item.color);
    const size = item.radius * 2;
    const domain = extractDomain(item.url);
    const logoUrl = domain
      ? `https://img.logo.dev/${domain}?token=pk_KuI_oR-IQ1-fqpAfz3FPEw&size=100&retina=true&format=png`
      : null;

    // these thresholds were tuned by eye
    const showName = item.radius > 28;
    const showPrice = item.radius > 38;

    const fontSize = Math.max(8, Math.min(item.radius * 0.22, 12));
    const priceSize = Math.max(9, Math.min(item.radius * 0.26, 14));
    const logoSize = Math.max(20, Math.min(item.radius * 0.7, 50));

    let content = "";

    const logoHtml = logoUrl ? `
      <img src="${logoUrl}" alt="${item.name}"
        class="object-contain rounded-md shrink-0"
        style="width: ${logoSize}px; height: ${logoSize}px;"
        onerror="this.style.display='none';" />
    ` : "";

    if (showPrice && showName) {
      content = `
        <div class="flex flex-col items-center justify-center gap-0.5 text-center px-1">
          ${logoHtml}
          <div class="font-semibold text-slate-800 truncate max-w-full" style="font-size: ${fontSize}px;">${item.name}</div>
          <div class="font-bold text-slate-900" style="font-size: ${priceSize}px;">${formatCurrencyShort(item.cost)}</div>
        </div>
      `;
    } else if (showName) {
      content = `
        <div class="flex flex-col items-center justify-center gap-0.5 text-center px-1">
          ${logoHtml}
          <div class="font-semibold text-slate-800 truncate max-w-full" style="font-size: ${fontSize}px;">${item.name}</div>
        </div>
      `;
    } else if (logoUrl) {
      content = `
        <img src="${logoUrl}" alt="${item.name}"
          class="object-contain rounded-sm"
          style="width: ${logoSize}px; height: ${logoSize}px;"
          onerror="this.parentElement.innerHTML='<span style=\\'font-size:${fontSize}px\\' class=\\'font-bold text-slate-700\\'>${item.name.charAt(0)}</span>';" />
      `;
    } else {
      content = `<span class="font-bold text-slate-700" style="font-size: ${fontSize}px;">${item.name.charAt(0)}</span>`;
    }

    html += `
      <div
        class="circlepack-bubble absolute cursor-pointer group transition-transform duration-200 hover:scale-105"
        data-id="${item.id}"
        style="left: ${item.x}px; top: ${item.y}px; width: ${size}px; height: ${size}px; transform: translate(-50%, -50%);"
      >
        <div
          class="w-full h-full rounded-full shadow-lg flex items-center justify-center overflow-hidden transition-shadow hover:shadow-xl"
          style="background: linear-gradient(135deg, ${color.bg} 0%, ${color.accent} 100%); border: 3px solid ${color.accent};"
        >
          ${content}
        </div>
        <div class="circlepack-tooltip absolute bottom-full left-1/2 -translate-x-1/2 mb-2 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-20">
          <div class="bg-slate-900 text-white text-xs rounded-lg px-3 py-2 whitespace-nowrap shadow-xl">
            <div class="font-semibold">${item.name}</div>
            <div class="text-slate-300">${formatCurrency(item.cost)}/mo</div>
          </div>
          <div class="absolute top-full left-1/2 -translate-x-1/2 border-4 border-transparent border-t-slate-900"></div>
        </div>
      </div>
    `;
  });

  container.innerHTML = html;

  // mobile: tap once to show tooltip, tap again to edit
  // desktop: just click to edit
  let activeTooltip = null;

  container.querySelectorAll(".circlepack-bubble").forEach(bubble => {
    let tapCount = 0;
    let tapTimer = null;

    bubble.addEventListener("click", e => {
      if (window.innerWidth < 500) {
        tapCount++;
        if (tapCount === 1) {
          if (activeTooltip && activeTooltip !== bubble) {
            activeTooltip.classList.remove("active");
          }
          bubble.classList.add("active");
          activeTooltip = bubble;
          tapTimer = setTimeout(() => { tapCount = 0; }, 300);
        } else {
          clearTimeout(tapTimer);
          tapCount = 0;
          editSub(bubble.dataset.id);
        }
      } else {
        editSub(bubble.dataset.id);
      }
    });
  });

  container.addEventListener("click", e => {
    if (!e.target.closest(".circlepack-bubble") && activeTooltip) {
      activeTooltip.classList.remove("active");
      activeTooltip = null;
    }
  });
}
```

## File: `js/modals.js`
```javascript
const backdrop = document.getElementById("modal-backdrop");
const panel = document.getElementById("modal-panel");
const modalInner = panel ? panel.querySelector("div") : null;

function showModal() {
  backdrop.classList.remove("hidden");
  panel.classList.remove("hidden");

  // rAF or the transition won't fire
  requestAnimationFrame(function() {
    backdrop.classList.remove("opacity-0");
    if (modalInner) {
      modalInner.classList.remove("translate-y-full", "sm:scale-95", "opacity-0");
      modalInner.classList.add("translate-y-0", "sm:translate-y-0", "sm:scale-100", "opacity-100");
    }
  });
}

function hideModal() {
  backdrop.classList.add("opacity-0");

  if (modalInner) {
    modalInner.classList.remove("translate-y-0", "sm:translate-y-0", "sm:scale-100", "opacity-100");
    modalInner.classList.add("translate-y-full", "sm:scale-95", "opacity-0");
  }

  setTimeout(function() {
    backdrop.classList.add("hidden");
    panel.classList.add("hidden");
  }, 300);
}

function openModal() {
  document.getElementById("sub-form").reset();
  document.getElementById("entry-id").value = "";
  document.getElementById("sub-currency").value = selectedCurrency;
  updateFavicon("");
  pickColor(randColor().id);

  document.getElementById("modal-title").innerText = "Add Subscription";
  document.querySelector("#sub-form button[type='submit']").innerText = "Save Item";

  showModal();
}

function closeModal() {
  hideModal();
}

function openModalWithPreset(presetIdx) {
  const preset = presets[presetIdx];
  if (!preset) return;

  document.getElementById("sub-form").reset();
  document.getElementById("entry-id").value = "";
  document.getElementById("sub-currency").value = selectedCurrency;
  document.getElementById("name").value = preset.name;
  document.getElementById("price").value = preset.price;
  document.getElementById("cycle").value = preset.cycle;
  document.getElementById("url").value = preset.domain;

  updateFavicon(preset.domain);
  pickColor(preset.color);

  document.getElementById("modal-title").innerText = "Add Subscription";
  document.querySelector("#sub-form button[type='submit']").innerText = "Save Item";

  showModal();
}


const settingsBackdrop = document.getElementById("settings-backdrop");
const settingsPanel = document.getElementById("settings-panel");
const settingsInner = settingsPanel ? settingsPanel.querySelector("div") : null;

function openSettings() {
  settingsBackdrop.classList.remove("hidden");
  settingsPanel.classList.remove("hidden");

  requestAnimationFrame(function() {
    settingsBackdrop.classList.remove("opacity-0");
    if (settingsInner) {
      settingsInner.classList.remove("translate-y-full", "sm:scale-95", "opacity-0");
      settingsInner.classList.add("translate-y-0", "sm:translate-y-0", "sm:scale-100", "opacity-100");
    }
  });
}

function closeSettings() {
  settingsBackdrop.classList.add("opacity-0");

  if (settingsInner) {
    settingsInner.classList.remove("translate-y-0", "sm:translate-y-0", "sm:scale-100", "opacity-100");
    settingsInner.classList.add("translate-y-full", "sm:scale-95", "opacity-0");
  }

  setTimeout(function() {
    settingsBackdrop.classList.add("hidden");
    settingsPanel.classList.add("hidden");
  }, 300);
}

let selectedCategory = null;

const presetsBackdrop = document.getElementById("presets-backdrop");
const presetsPanel = document.getElementById("presets-panel");
const presetsInner = presetsPanel ? presetsPanel.querySelector("div") : null;

function openPresetsBrowser() {
  selectedCategory = null;
  document.getElementById("presets-search").value = "";

  renderCategoryFilters();
  renderPresetsBrowserList();

  if (presetsBackdrop) presetsBackdrop.classList.remove("hidden");
  if (presetsPanel) presetsPanel.classList.remove("hidden");

  requestAnimationFrame(function() {
    if (presetsBackdrop) presetsBackdrop.classList.remove("opacity-0");
    if (presetsInner) {
      presetsInner.classList.remove("translate-y-full", "sm:scale-95", "opacity-0");
      presetsInner.classList.add("translate-y-0", "sm:translate-y-0", "sm:scale-100", "opacity-100");
    }
  });
}

function closePresetsBrowser() {
  if (presetsBackdrop) presetsBackdrop.classList.add("opacity-0");

  if (presetsInner) {
    presetsInner.classList.remove("translate-y-0", "sm:translate-y-0", "sm:scale-100", "opacity-100");
    presetsInner.classList.add("translate-y-full", "sm:scale-95", "opacity-0");
  }

  setTimeout(function() {
    if (presetsBackdrop) presetsBackdrop.classList.add("hidden");
    if (presetsPanel) presetsPanel.classList.add("hidden");
  }, 300);
}

function renderCategoryFilters() {
  const filtersEl = document.getElementById("category-filters");
  if (!filtersEl) return;

  const cats = getCategories();

  let html = '<button onclick="selectCategory(null)" class="category-btn px-3 py-1 rounded-full text-xs font-semibold transition-all ';
  html += selectedCategory ? 'bg-slate-100 text-slate-600 hover:bg-slate-200' : 'bg-slate-900 text-white';
  html += '">All</button>';

  for (let i = 0; i < cats.length; i++) {
    const cat = cats[i];
    const isActive = (selectedCategory === cat);
    html += '<button onclick="selectCategory(\'' + cat + '\')" class="category-btn px-3 py-1 rounded-full text-xs font-semibold transition-all ';
    html += isActive ? 'bg-slate-900 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200';
    html += '">' + cat + '</button>';
  }

  filtersEl.innerHTML = html;
}

function selectCategory(cat) {
  selectedCategory = cat;
  renderCategoryFilters();

  const searchInput = document.getElementById("presets-search");
  const query = searchInput ? searchInput.value : "";
  filterPresets(query);
}

function filterPresets(searchQuery) {
  const q = searchQuery.toLowerCase().trim();
  let results = presets;

  if (selectedCategory) {
    results = results.filter(function(p) {
      return p.category === selectedCategory;
    });
  }

  if (q.length > 0) {
    results = results.filter(function(p) {
      return p.name.toLowerCase().includes(q) ||
             p.category.toLowerCase().includes(q) ||
             p.domain.toLowerCase().includes(q);
    });
  }

  renderPresetsBrowserList(results);
}

function renderPresetsBrowserList(presetsToShow) {
  if (!presetsToShow) presetsToShow = presets;

  const container = document.getElementById("presets-browser-list");
  if (!container) return;

  if (presetsToShow.length === 0) {
    container.innerHTML = '<div class="text-center text-slate-400 py-8">No subscriptions found</div>';
    return;
  }

  const byCategory = {};
  for (let i = 0; i < presetsToShow.length; i++) {
    const p = presetsToShow[i];
    if (!byCategory[p.category]) {
      byCategory[p.category] = [];
    }
    byCategory[p.category].push(p);
  }

  let html = "";
  const categoryNames = Object.keys(byCategory);

  for (let c = 0; c < categoryNames.length; c++) {
    const catName = categoryNames[c];
    const items = byCategory[catName];

    html += '<div class="mb-5">';
    html += '<h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">' + catName + '</h4>';
    html += '<div class="grid grid-cols-2 gap-2">';

    for (let i = 0; i < items.length; i++) {
      const p = items[i];
      const idx = presets.indexOf(p);
      const logo = "https://img.logo.dev/" + p.domain + "?token=pk_KuI_oR-IQ1-fqpAfz3FPEw&size=100&retina=true&format=png";

      html += '<button onclick="selectPresetFromBrowser(' + idx + ')" ';
      html += 'class="flex items-center gap-3 rounded-xl border border-slate-100 bg-white p-3 text-left shadow-sm transition-all hover:border-indigo-200 hover:shadow-md active:scale-[0.98]">';
      html += '<img src="' + logo + '" class="h-10 w-10 rounded-lg object-contain shrink-0" crossorigin="anonymous" alt="' + p.name + '">';
      html += '<div class="min-w-0 flex-1">';
      html += '<div class="font-semibold text-slate-900 text-sm truncate">' + p.name + '</div>';
      html += '<div class="text-xs text-slate-500">$' + p.price + '/mo</div>';
      html += '</div></button>';
    }

    html += '</div></div>';
  }

  container.innerHTML = html;
}

function selectPresetFromBrowser(idx) {
  closePresetsBrowser();
  // small delay so the close animation finishes before opening the form
  setTimeout(function() {
    openModalWithPreset(idx);
  }, 300);
}

document.addEventListener("DOMContentLoaded", function() {
  if (backdrop) backdrop.addEventListener("click", closeModal);
  if (panel) {
    panel.addEventListener("click", closeModal);
    if (modalInner) modalInner.addEventListener("click", function(e) { e.stopPropagation(); });
  }

  if (settingsBackdrop) settingsBackdrop.addEventListener("click", closeSettings);
  if (settingsPanel) {
    settingsPanel.addEventListener("click", closeSettings);
    if (settingsInner) settingsInner.addEventListener("click", function(e) { e.stopPropagation(); });
  }

  if (presetsBackdrop) presetsBackdrop.addEventListener("click", closePresetsBrowser);
  if (presetsPanel) {
    presetsPanel.addEventListener("click", closePresetsBrowser);
    if (presetsInner) presetsInner.addEventListener("click", function(e) { e.stopPropagation(); });
  }

  const bankBackdrop = document.getElementById("bank-import-backdrop");
  const bankPanel = document.getElementById("bank-import-panel");
  const bankInner = bankPanel ? bankPanel.querySelector("div") : null;

  if (bankBackdrop) bankBackdrop.addEventListener("click", closeBankImport);
  if (bankPanel) {
    bankPanel.addEventListener("click", closeBankImport);
    if (bankInner) bankInner.addEventListener("click", function(e) { e.stopPropagation(); });
  }
});
```

## File: `js/presets.js`
```javascript
/*
 * popular subscription presets
 * prices are US monthly rates as of late 2024
 * these will definitely go out of date but gives users a starting point
 */
const presets = [

  // streaming services - everyone has like 5 of these now
  { name: "Netflix", domain: "netflix.com", price: 17.99, cycle: "Monthly", color: "rose", category: "Streaming", popular: true },
  { name: "Disney+", domain: "disneyplus.com", price: 15.99, cycle: "Monthly", color: "blue", category: "Streaming", popular: true },
  { name: "Max", domain: "max.com", price: 18.49, cycle: "Monthly", color: "purple", category: "Streaming" }, // was HBO Max
  { name: "Hulu", domain: "hulu.com", price: 9.99, cycle: "Monthly", color: "green", category: "Streaming" },
  { name: "Apple TV+", domain: "tv.apple.com", price: 9.99, cycle: "Monthly", color: "slate", category: "Streaming" },
  { name: "Paramount+", domain: "paramountplus.com", price: 7.99, cycle: "Monthly", color: "blue", category: "Streaming" },
  { name: "Peacock", domain: "peacocktv.com", price: 7.99, cycle: "Monthly", color: "purple", category: "Streaming" },
  { name: "Amazon Prime", domain: "amazon.com", price: 14.99, cycle: "Monthly", color: "orange", category: "Streaming", popular: true },
  { name: "Crunchyroll", domain: "crunchyroll.com", price: 7.99, cycle: "Monthly", color: "orange", category: "Streaming" },

  // music
  { name: "Spotify", domain: "spotify.com", price: 11.99, cycle: "Monthly", color: "green", category: "Music", popular: true },
  { name: "Apple Music", domain: "music.apple.com", price: 10.99, cycle: "Monthly", color: "pink", category: "Music" },
  { name: "YouTube Premium", domain: "youtube.com", price: 13.99, cycle: "Monthly", color: "rose", category: "Music", popular: true },
  { name: "Audible", domain: "audible.com", price: 14.95, cycle: "Monthly", color: "orange", category: "Music" },

  // gaming subscriptions
  { name: "Xbox Game Pass", domain: "xbox.com", price: 19.99, cycle: "Monthly", color: "green", category: "Gaming" },
  { name: "PlayStation Plus", domain: "playstation.com", price: 14.99, cycle: "Monthly", color: "blue", category: "Gaming" },
  { name: "Nintendo Switch Online", domain: "nintendo.com", price: 3.99, cycle: "Monthly", color: "rose", category: "Gaming" },
  { name: "EA Play", domain: "ea.com", price: 5.99, cycle: "Monthly", color: "blue", category: "Gaming" },

  // ai tools - these are getting expensive
  { name: "ChatGPT Plus", domain: "openai.com", price: 20, cycle: "Monthly", color: "teal", category: "AI", popular: true },
  { name: "Claude Pro", domain: "claude.ai", price: 20, cycle: "Monthly", color: "orange", category: "AI" },
  { name: "Midjourney", domain: "midjourney.com", price: 10, cycle: "Monthly", color: "indigo", category: "AI" },
  { name: "GitHub Copilot", domain: "github.com", price: 10, cycle: "Monthly", color: "slate", category: "AI" },

  // productivity
  { name: "Microsoft 365", domain: "microsoft.com", price: 9.99, cycle: "Monthly", color: "blue", category: "Productivity" },
  { name: "Notion", domain: "notion.so", price: 12, cycle: "Monthly", color: "slate", category: "Productivity" },
  { name: "Slack", domain: "slack.com", price: 8.75, cycle: "Monthly", color: "purple", category: "Productivity" },
  { name: "Linear", domain: "linear.app", price: 10, cycle: "Monthly", color: "indigo", category: "Productivity" },
  { name: "Canva Pro", domain: "canva.com", price: 15, cycle: "Monthly", color: "cyan", category: "Productivity" },
  { name: "Figma", domain: "figma.com", price: 15, cycle: "Monthly", color: "purple", category: "Productivity" },
  { name: "Adobe Creative Cloud", domain: "adobe.com", price: 59.99, cycle: "Monthly", color: "rose", category: "Productivity" }, // ouch

  // cloud storage
  { name: "iCloud+", domain: "icloud.com", price: 2.99, cycle: "Monthly", color: "blue", category: "Cloud" },
  { name: "Google One", domain: "one.google.com", price: 2.99, cycle: "Monthly", color: "cyan", category: "Cloud" },
  { name: "Dropbox", domain: "dropbox.com", price: 11.99, cycle: "Monthly", color: "blue", category: "Cloud" },

  // vpn / security
  { name: "NordVPN", domain: "nordvpn.com", price: 12.99, cycle: "Monthly", color: "indigo", category: "Security" },
  { name: "ExpressVPN", domain: "expressvpn.com", price: 12.95, cycle: "Monthly", color: "rose", category: "Security" },
  { name: "1Password", domain: "1password.com", price: 2.99, cycle: "Monthly", color: "blue", category: "Security" },

  // fitness
  { name: "Peloton", domain: "onepeloton.com", price: 12.99, cycle: "Monthly", color: "rose", category: "Fitness" },
  { name: "Apple Fitness+", domain: "fitness.apple.com", price: 9.99, cycle: "Monthly", color: "pink", category: "Fitness" },
  { name: "Strava", domain: "strava.com", price: 11.99, cycle: "Monthly", color: "orange", category: "Fitness" },

  // news / reading
  { name: "The Athletic", domain: "theathletic.com", price: 9.99, cycle: "Monthly", color: "slate", category: "News" },
  { name: "Kindle Unlimited", domain: "amazon.com/kindle", price: 11.99, cycle: "Monthly", color: "orange", category: "News" },
  { name: "Medium", domain: "medium.com", price: 5, cycle: "Monthly", color: "slate", category: "News" },

  // learning platforms
  { name: "Duolingo", domain: "duolingo.com", price: 12.99, cycle: "Monthly", color: "green", category: "Learning" },
  { name: "Skillshare", domain: "skillshare.com", price: 13.99, cycle: "Monthly", color: "teal", category: "Learning" },
  { name: "Coursera Plus", domain: "coursera.org", price: 59, cycle: "Monthly", color: "blue", category: "Learning" }
];

function getCategories() {
  const cats = [];
  for (let i = 0; i < presets.length; i++) {
    const cat = presets[i].category;
    if (cats.indexOf(cat) === -1) {
      cats.push(cat);
    }
  }
  return cats;
}
```

## File: `js/rates.js`
```javascript
const CACHE_KEY = "vexly_exchangeRates";
const DATE_KEY = "vexly_ratesLastUpdate";
const ONE_DAY = 24 * 60 * 60 * 1000; // 24 hours in milliseconds

function getCachedRates() {
    try {
        const cached = localStorage.getItem(CACHE_KEY);
        const lastUpdate = localStorage.getItem(DATE_KEY);
        if (!cached) return null;
        return { rates: JSON.parse(cached), lastUpdate: parseInt(lastUpdate) };
    } catch {
        return null;
    }
}

function saveRates(rates) {
    localStorage.setItem(CACHE_KEY, JSON.stringify(rates));
    localStorage.setItem(DATE_KEY, Date.now());
}

async function fetchRatesFromAPI() {
    try {
        const response = await fetch("https://open.er-api.com/v6/latest/USD");
        const data = await response.json();

        if (data.result === "success" && data.rates) {
            saveRates(data.rates);
            return data.rates;
        }
        throw new Error("Failed to fetch rates");
    } catch (error) {
        console.error("Error fetching exchange rates:", error);
        return null;
    }
}

async function loadRates() {
    const cachedRates = getCachedRates();

    if (cachedRates) {
        const timeElapsed = Date.now() - cachedRates.lastUpdate;

        // If cached rates are less than a day old, use them
        if (timeElapsed < ONE_DAY) {
            return cachedRates.rates;
        } else {
            const refreshedRates = await fetchRatesFromAPI();
            return refreshedRates || cachedRates.rates;
        }
    } else {
        const refreshedRates = await fetchRatesFromAPI();
        if (!refreshedRates) {
            console.warn("Failed to fetch rates, falling back to hardcoded rates.");
        }
        return refreshedRates;
    }
}

async function initRates() {
    const rates = await loadRates();
    if (rates && window.currencies) {
        Object.keys(window.currencies).forEach((currency) => {
            if (rates[currency]) {
                window.currencies[currency].rate = rates[currency];
            }
        });
    }
}

window.initRates = initRates;
```

## File: `js/storage.js`
```javascript
// localstorage keys - using vexly prefix for namespacing
// (this was the old name of the project)
const STORAGE_KEY = "vexly_flow_data";
const CURRENCY_KEY = "vexly_currency";

function load() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) {
      subs = JSON.parse(raw);
    }
  } catch (err) {
    // probably corrupted data, just start fresh
    console.warn("failed to load saved data:", err);
    subs = [];
  }
}

function save() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(subs));
  renderList();
}

function loadCurrency() {
  const saved = localStorage.getItem(CURRENCY_KEY);

  // make sure it's a valid currency code
  if (saved && currencies[saved]) {
    selectedCurrency = saved;
  } else {
    selectedCurrency = "USD";
  }
}

function saveCurrency(code) {
  selectedCurrency = code;
  localStorage.setItem(CURRENCY_KEY, code);

  renderList();
  if (step === 2) renderGrid();
}

function exportData() {
  const exportObj = {
    version: 1,
    exportedAt: new Date().toISOString(),
    currency: selectedCurrency,
    subscriptions: subs
  };

  const jsonStr = JSON.stringify(exportObj, null, 2);
  const blob = new Blob([jsonStr], { type: "application/json" });
  const blobUrl = URL.createObjectURL(blob);

  const link = document.createElement("a");
  link.href = blobUrl;
  link.download = "subgrid-backup-" + new Date().toISOString().split("T")[0] + ".json";
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);

  URL.revokeObjectURL(blobUrl);
}

function importData(evt) {
  const file = evt.target.files && evt.target.files[0];
  if (!file) return;

  const reader = new FileReader();

  reader.onload = function(e) {
    try {
      const data = JSON.parse(e.target.result);

      if (!data.subscriptions || !Array.isArray(data.subscriptions)) {
        throw new Error("Invalid file format");
      }

      for (let i = 0; i < data.subscriptions.length; i++) {
        const sub = data.subscriptions[i];
        if (!sub.id || !sub.name || typeof sub.price !== "number") {
          throw new Error("Invalid subscription data");
        }
      }

      let replaceExisting = true;
      if (subs.length > 0) {
        replaceExisting = confirm(
          "You have " + subs.length + " existing subscription(s).\n\n" +
          "Click OK to replace them with " + data.subscriptions.length + " imported subscription(s).\n\n" +
          "Click Cancel to merge (add imported to existing)."
        );
      }

      if (replaceExisting || subs.length === 0) {
        subs = data.subscriptions;
      } else {
        for (let i = 0; i < data.subscriptions.length; i++) {
          const imported = data.subscriptions[i];
          subs.push({
            id: Date.now().toString() + Math.random().toString(36).slice(2),
            name: imported.name,
            price: imported.price,
            currency: imported.currency || selectedCurrency || "USD",
            cycle: imported.cycle,
            url: imported.url || "",
            color: imported.color
          });
        }
      }

      if (data.currency && currencies[data.currency]) {
        saveCurrency(data.currency);
      }

      save();
      closeSettings();
      alert("Successfully imported " + data.subscriptions.length + " subscription(s)!");

    } catch (err) {
      alert("Failed to import: " + err.message);
    }
  };

  reader.readAsText(file);

  // reset the input so they can import the same file again if needed
  evt.target.value = "";
}
```

## File: `js/treemap.js`
```javascript
/*
 * squarified treemap layout
 * based on the bruls et al. algorithm
 * https://www.win.tue.nl/~vanwijk/stm.pdf
 */
class Treemap {
  constructor(width, height) {
    this.width = width;
    this.height = height;
    this.cellGap = 4; // gap between cells in px
  }

  layout(items) {
    if (items.length === 0) return [];

    let total = 0;
    for (let i = 0; i < items.length; i++) {
      total += items[i].val;
    }

    const normalized = [];
    const totalArea = this.width * this.height;

    for (let i = 0; i < items.length; i++) {
      const item = items[i];
      normalized.push({
        id: item.id,
        name: item.name,
        url: item.url,
        color: item.color,
        price: item.price,
        currency: item.currency,
        cycle: item.cycle,
        cost: item.cost,
        val: item.val,
        idx: item.idx,
        area: (item.val / total) * totalArea
      });
    }

    const rectangles = [];
    this._squarify(normalized, [], 0, 0, this.width, this.height, rectangles);
    return rectangles;
  }

  // recursive squarification - tries to make cells as square as possible
  _squarify(remaining, currentRow, x, y, w, h, output) {
    if (remaining.length === 0) {
      this._layoutRow(currentRow, x, y, w, h, output);
      return;
    }

    const next = remaining[0];
    const withNext = currentRow.concat([next]);

    if (currentRow.length === 0 || this._worstRatio(currentRow, w, h) >= this._worstRatio(withNext, w, h)) {
      this._squarify(remaining.slice(1), withNext, x, y, w, h, output);
    } else {
      const bounds = this._layoutRow(currentRow, x, y, w, h, output);
      this._squarify(remaining, [], bounds.nx, bounds.ny, bounds.nw, bounds.nh, output);
    }
  }

  _worstRatio(row, w, h) {
    if (row.length === 0) return Infinity;

    let areaSum = 0;
    for (let i = 0; i < row.length; i++) {
      areaSum += row[i].area;
    }

    const shortSide = Math.min(w, h);
    const rowThickness = areaSum / shortSide;

    let worstRatio = 0;
    for (let i = 0; i < row.length; i++) {
      const itemLength = row[i].area / rowThickness;
      const ratio = Math.max(rowThickness / itemLength, itemLength / rowThickness);
      if (ratio > worstRatio) {
        worstRatio = ratio;
      }
    }

    return worstRatio;
  }

  _layoutRow(row, x, y, w, h, output) {
    if (row.length === 0) {
      return { nx: x, ny: y, nw: w, nh: h };
    }

    let areaSum = 0;
    for (let i = 0; i < row.length; i++) {
      areaSum += row[i].area;
    }

    const horizontal = (w >= h);
    const shortSide = horizontal ? h : w;
    const thickness = areaSum / shortSide;
    const gap = this.cellGap;

    let offset = 0;

    for (let i = 0; i < row.length; i++) {
      const item = row[i];
      const length = item.area / thickness;

      if (horizontal) {
        output.push({
          id: item.id,
          name: item.name,
          url: item.url,
          color: item.color,
          price: item.price,
          currency: item.currency,
          cycle: item.cycle,
          cost: item.cost,
          val: item.val,
          idx: item.idx,
          area: item.area,
          x: x + gap / 2,
          y: y + offset + gap / 2,
          w: thickness - gap,
          h: length - gap
        });
      } else {
        output.push({
          id: item.id,
          name: item.name,
          url: item.url,
          color: item.color,
          price: item.price,
          currency: item.currency,
          cycle: item.cycle,
          cost: item.cost,
          val: item.val,
          idx: item.idx,
          area: item.area,
          x: x + offset + gap / 2,
          y: y + gap / 2,
          w: length - gap,
          h: thickness - gap
        });
      }

      offset += length;
    }

    if (horizontal) {
      return { nx: x + thickness, ny: y, nw: w - thickness, nh: h };
    } else {
      return { nx: x, ny: y + thickness, nw: w, nh: h - thickness };
    }
  }
}

function renderGrid() {
  const gridEl = document.getElementById("bento-grid");
  const totalDisplay = document.getElementById("step-2-total");
  const yearlyDisplay = document.getElementById("step-2-yearly");

  let monthlyTotal = 0;
  const items = [];

  for (let i = 0; i < subs.length; i++) {
    const sub = subs[i];
    const monthlyCost = toMonthly(sub);
    monthlyTotal += monthlyCost;

    items.push({
      id: sub.id,
      name: sub.name,
      url: sub.url,
      color: sub.color,
      price: sub.price,
      currency: sub.currency,
      cycle: sub.cycle,
      cost: monthlyCost
    });
  }

  items.sort(function(a, b) { return b.cost - a.cost; });

  totalDisplay.innerText = formatCurrency(monthlyTotal);
  yearlyDisplay.innerText = formatCurrency(monthlyTotal * 12);

  if (items.length === 0) {
    gridEl.innerHTML = '<div class="flex items-center justify-center h-full text-slate-400">Add subscriptions to see visualization</div>';
    return;
  }

  const bounds = gridEl.getBoundingClientRect();
  const gridWidth = bounds.width || 600;
  const gridHeight = bounds.height || 450;

  const treemapData = [];
  for (let i = 0; i < items.length; i++) {
    treemapData.push({
      id: items[i].id,
      name: items[i].name,
      url: items[i].url,
      color: items[i].color,
      price: items[i].price,
      currency: items[i].currency,
      cycle: items[i].cycle,
      cost: items[i].cost,
      val: items[i].cost,
      idx: i
    });
  }

  const treemap = new Treemap(gridWidth, gridHeight);
  const cells = treemap.layout(treemapData);

  let html = "";

  for (let i = 0; i < cells.length; i++) {
    const cell = cells[i];
    const percent = (cell.cost / monthlyTotal) * 100;
    const colorPalette = getColor(cell.color);

    const minDim = Math.min(cell.w, cell.h);
    const clampedPct = Math.max(3, Math.min(60, percent));

    const padding = Math.round(Math.max(6, Math.min(minDim * 0.08, 16)) + (clampedPct / 60) * 8);
    const borderRadius = Math.round(Math.max(6, Math.min(minDim * 0.12, 20)) + (clampedPct / 60) * 6);

    const innerWidth = cell.w - padding * 2;
    const innerHeight = cell.h - padding * 2;

    // font sizes - these formulas took some trial and error to get right
    const maxPriceFont = Math.min(Math.floor(innerWidth * 0.16), Math.floor(innerHeight * 0.28));
    const priceFont = Math.max(10, Math.min(12 + (clampedPct / 60) * 36, maxPriceFont, 48));
    const titleFont = Math.max(8, Math.min(9 + (clampedPct / 60) * 15, priceFont * 0.55, 24));
    const iconSize = Math.max(14, Math.min(18 + (clampedPct / 60) * 30, innerHeight * 0.3, innerWidth * 0.35, 48));

    const isMicro = minDim < 40 || (cell.w < 50 && cell.h < 50);
    const isTiny = minDim < 55 || (cell.w < 65 && cell.h < 65);
    const isSmall = minDim < 85 || cell.w < 95;

    let cellContent = "";

    if (isMicro) {
      const sz = Math.max(12, Math.min(iconSize, minDim * 0.5));
      cellContent = '<div class="flex items-center justify-center h-full w-full">' + iconHtml(cell, "w-[" + sz + "px] h-[" + sz + "px]") + '</div>';

    } else if (isTiny) {
      const sz = Math.max(14, Math.min(iconSize, minDim * 0.4));
      const ps = Math.max(9, Math.min(priceFont, 13, innerWidth * 0.16));
      cellContent = '<div class="flex flex-col items-center justify-center h-full w-full gap-1">';
      cellContent += iconHtml(cell, "w-[" + sz + "px] h-[" + sz + "px]");
      cellContent += '<div class="font-bold text-slate-900" style="font-size:' + ps + 'px">' + formatOriginalMonthlyShort(cell) + '</div>';
      cellContent += '</div>';

    } else if (isSmall) {
      const sz = Math.max(16, Math.min(iconSize, innerWidth * 0.35, innerHeight * 0.25));
      const ts = Math.max(8, Math.min(titleFont, 11, innerWidth * 0.12));
      const ps = Math.max(11, Math.min(priceFont, 18, innerWidth * 0.18));

      cellContent = '<div class="flex flex-col items-center justify-center h-full w-full gap-1 text-center">';
      cellContent += iconHtml(cell, "w-[" + sz + "px] h-[" + sz + "px]");
      cellContent += '<div class="min-w-0 w-full">';
      cellContent += '<div class="font-semibold text-slate-900 treemap-cell-name" style="font-size:' + ts + 'px">' + cell.name + '</div>';
      cellContent += '<div class="font-black text-slate-900" style="font-size:' + ps + 'px">' + formatOriginalMonthlyShort(cell) + '</div>';
      cellContent += '</div></div>';

    } else {
      const showPercentBadge = cell.w > 80 && cell.h > 70;
      const showYearlyEstimate = cell.h > 130 && cell.w > 110 && percent > 8;

      cellContent = '<div class="flex justify-between items-start">';
      cellContent += iconHtml(cell, "w-[" + iconSize + "px] h-[" + iconSize + "px]");
      if (showPercentBadge) {
        cellContent += '<span class="text-[10px] font-bold bg-white/70 px-2 py-1 rounded-full text-slate-700">' + Math.round(percent) + '%</span>';
      }
      cellContent += '</div>';
      cellContent += '<div class="mt-auto min-w-0">';
      cellContent += '<div class="font-bold text-slate-900 treemap-cell-name" style="font-size:' + titleFont + 'px">' + cell.name + '</div>';
      cellContent += '<div class="font-black text-slate-900 tracking-tight leading-none" style="font-size:' + priceFont + 'px">' + formatOriginalMonthly(cell) + '</div>';
      if (showYearlyEstimate) {
        cellContent += '<div class="text-xs font-medium text-slate-500 mt-1">~' + formatOriginalYearlyShort(cell) + '/yr</div>';
      }
      cellContent += '</div>';
    }

    html += '<div class="treemap-cell" data-id="' + cell.id + '" style="left:' + cell.x + 'px;top:' + cell.y + 'px;width:' + cell.w + 'px;height:' + cell.h + 'px;border-radius:' + borderRadius + 'px">';
    html += '<div class="treemap-cell-inner" style="background:linear-gradient(135deg,' + colorPalette.bg + ' 0%,' + colorPalette.accent + ' 100%);padding:' + padding + 'px;border-radius:' + Math.max(4, borderRadius - 3) + 'px">';
    html += cellContent;
    html += '</div></div>';
  }

  gridEl.innerHTML = html;
}

async function exportAsImage() {
  const exportContainer = document.getElementById("export-container");
  if (!exportContainer) return;

  const btn = event.target.closest("button");
  const originalHtml = btn.innerHTML;
  btn.innerHTML = '<span class="iconify h-5 w-5 animate-spin" data-icon="ph:spinner-bold"></span> Exporting...';
  btn.disabled = true;

  try {
    // using modern-screenshot library for this
    const pngUrl = await modernScreenshot.domToPng(exportContainer, {
      scale: 2, // 2x for retina
      backgroundColor: "#ffffff",
      style: {
        fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
        borderRadius: "2.5rem",
        overflow: "hidden"
      },
      onCloneNode: function(node) {
        // force font family on all cloned elements
        // otherwise the screenshot sometimes uses weird fonts
        if (node.style) {
          node.style.fontFamily = "system-ui, -apple-system, sans-serif";
        }
        if (node.querySelectorAll) {
          var elements = node.querySelectorAll("*");
          for (var i = 0; i < elements.length; i++) {
            if (elements[i].style) {
              elements[i].style.fontFamily = "system-ui, -apple-system, sans-serif";
            }
          }
        }
        return node;
      },
      fetch: { bypassingCache: true }
    });

    var downloadLink = document.createElement("a");
    downloadLink.href = pngUrl;
    downloadLink.download = "subs-" + new Date().toISOString().split("T")[0] + ".png";
    document.body.appendChild(downloadLink);
    downloadLink.click();
    downloadLink.remove();

  } catch (err) {
    console.error("export failed:", err);
    alert("Export failed: " + err.message);
  }

  btn.innerHTML = originalHtml;
  btn.disabled = false;
}
```

