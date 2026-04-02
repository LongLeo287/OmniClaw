# 🚀 CLAUDE.md — Tiem Nuoc Nho v5 (PRJ-004)
# Version: 1.1 | Updated: 2026-03-16
# Authority: Tier 0 (Project Constitution)
# Location: $OMNICLAW_ROOT\projects\PRJ-004\   ◄ Managed by OmniClaw
# Workspace: D:\Tiem_Nuoc_Nho_v5\

> **THIS IS THE FIRST FILE YOU READ** when working on this project.
> Managed centrally by OmniClaw. Do NOT move to project folder.

---

## ⚡ BOOT SEQUENCE

```
STEP 1 ──► Read this CLAUDE.md                          [THIS FILE — in OmniClaw\projects\PRJ-004\]
STEP 2 ──► Read OmniClaw Master                            [$OMNICLAW_ROOT\CLAUDE.md]
STEP 3 ──► Validate workspace via Gatekeeper            [gatekeeper.ps1 -CheckID PRJ-004]
STEP 4 ──► Read OmniClaw AGENTS.md                         [$OMNICLAW_ROOT\shared-context\AGENTS.md]
STEP 5 ──► Check Blackboard for pending tasks           [$OMNICLAW_ROOT\shared-context\blackboard.json]
STEP 6 ──► Begin work
```

---

## 🏪 PROJECT IDENTITY

| Field | Value |
|---|---|
| **Project ID** | PRJ-004 |
| **Name** | Tiem Nuoc Nho v5 |
| **Type** | POS / Restaurant order management |
| **Stack** | React 18 + TypeScript + Vite + Express + Google Apps Script |
| **Backend** | Google Sheets as database, GAS as API layer |
| **Dev URL** | http://localhost:7475 (port 7475 — Playwright-accessible) |
| **Start** | `npm run dev` in `D:\Tiem_Nuoc_Nho_v5` |
| **Config** | `$OMNICLAW_ROOT\projects\PRJ-004\` |
| **Workflows** | `$OMNICLAW_ROOT\projects\PRJ-004\workflows\` |

---

## 🗂️ WORKSPACE STRUCTURE

```
D:\Tiem_Nuoc_Nho_v5\             ◄ Source code only
├── .clauderules                  ◄ ONLY OmniClaw file here (Claude Code requirement)
├── src/
│   ├── components/
│   │   ├── Menu.tsx              ◄ Menu grid + item add flow
│   │   ├── Cart.tsx              ◄ Cart + checkout + edit modal
│   │   ├── CartItemRow.tsx       ◄ Individual cart row
│   │   ├── OrderHistory.tsx      ◄ Order management dashboard
│   │   ├── Invoice.tsx           ◄ Invoice view
│   │   └── GlobalQrModal.tsx     ◄ QR payment modal (Momo/Timo)
│   ├── context/
│   │   ├── CartContext.tsx       ◄ Cart state management
│   │   ├── DataContext.tsx       ◄ Orders & menu data (GAS API)
│   │   ├── UIContext.tsx         ◄ UI state (FAB, dark mode)
│   │   └── AuthContext.tsx       ◄ Auth state
│   └── types.ts                  ◄ Shared TypeScript types
├── DATA/GAS/                     ◄ Google Apps Script source
├── backend/                      ◄ Express server (API proxy)
└── server.ts                     ◄ Dev server entry point
```

---

## 🔑 KEY DECISIONS (Locked — Do NOT Reverse)

1. **Card tap = instant add** to cart (no popup), quantity 1, default options
2. **`+` button** only appears for items with customizations (`hasCustomizations: true`)
3. **Takeaway/Dine-in** selection happens at CHECKOUT, not per-item
4. **Split dialog** appears when editing a multi-quantity cart item with changed options
5. **No Topping module** — customer decided toppings are not needed
6. **GAS = Backend** — all data reads/writes go through Google Apps Script URL

---

## ✅ COMPLETED FEATURES

- [x] Menu quick-add (tap card → instant cart)
- [x] `+` button → QuantityModal → CustomizationModal flow
- [x] Edit cart item with Split dialog
- [x] Subtotal always visible (sticky footer)
- [x] Code audit — all orphaned states/components removed
- [x] TypeScript: 0 compile errors

---

## ✅ ALL FEATURES COMPLETE

- [x] QR Code checkout integration (GlobalQrModal connected in Cart.tsx L862)
- [x] Order History fast-action buttons (Receive / Complete / Cancel — OrderHistory.tsx L221)
- [x] Cart auto-save to localStorage (CartContext.tsx L21)
- [x] TypeScript: 0 compile errors (tsc --noEmit exit 0)

---

## 🤖 AGENT BEHAVIOR FOR THIS PROJECT

- **Language:** Vietnamese for user-facing messages, English for code/comments
- **Brand color:** `#C9252C` (red) — use consistently
- **UI framework:** Tailwind CSS + Framer Motion (`motion/react`)
- **Data layer:** `useData()` hook from `DataContext.tsx`
- **Cart operations:** `useCart()` hook from `CartContext.tsx`

---

## ⚠️ HARD RULES

1. Never modify `DATA/GAS/` scripts without testing on staging sheet
2. Never commit API keys or GAS URLs to git
3. Always run `npx tsc --noEmit` after any TypeScript change
4. Always test on mobile viewport (375px) — this is a mobile-first POS

---

*"Every cup of water is an order. Every order is a story. Make the system serve the story."*

