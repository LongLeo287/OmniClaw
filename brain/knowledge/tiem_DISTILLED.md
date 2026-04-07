---
id: tiem
type: knowledge
owner: OA_Triage
---
# tiem
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "react-example",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "tsx server.ts",
    "build": "vite build",
    "preview": "vite preview",
    "clean": "rm -rf dist",
    "lint": "tsc --noEmit"
  },
  "dependencies": {
    "@google/genai": "^1.29.0",
    "@tailwindcss/vite": "^4.1.14",
    "@types/d3": "^7.4.3",
    "@types/react-window": "^1.8.8",
    "@use-gesture/react": "^10.3.1",
    "@vitejs/plugin-react": "^5.0.4",
    "better-sqlite3": "^12.4.1",
    "clsx": "^2.1.1",
    "d3": "^7.9.0",
    "date-fns": "^4.1.0",
    "dotenv": "^17.2.3",
    "express": "^4.21.2",
    "framer-motion": "^12.34.5",
    "html-to-image": "^1.11.13",
    "idb": "^8.0.3",
    "jose": "^6.1.3",
    "js-cookie": "^3.0.5",
    "lucide-react": "^0.546.0",
    "lunar-javascript": "^1.7.7",
    "motion": "^12.34.3",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "react-qr-code": "^2.0.18",
    "react-router-dom": "^7.13.1",
    "react-virtuoso": "^4.18.3",
    "react-window": "^2.2.7",
    "recharts": "^3.7.0",
    "tailwind-merge": "^3.5.0",
    "vite": "^6.2.0",
    "ws": "^8.19.0"
  },
  "devDependencies": {
    "@types/express": "^4.17.21",
    "@types/node": "^22.14.0",
    "@types/ws": "^8.18.1",
    "autoprefixer": "^10.4.21",
    "tailwindcss": "^4.1.14",
    "tsx": "^4.21.0",
    "typescript": "~5.8.2",
    "vite": "^6.2.0"
  }
}

```

### File: README.md
```md
<div align="center">
<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />
</div>

# Run and deploy your AI Studio app

This contains everything you need to run your app locally.

View your app in AI Studio: https://ai.studio/apps/f6c079a6-dc83-4bc2-a153-8588dfa25702

## Run Locally

**Prerequisites:**  Node.js


1. Install dependencies:
   `npm install`
2. Set the `GEMINI_API_KEY` in [.env.local](.env.local) to your Gemini API key
3. Run the app:
   `npm run dev`

```

### File: index.html
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Google AI Studio App</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>


```

### File: metadata.json
```json
{
  "name": "TIỆM NƯỚC NHỎ V5",
  "description": "Hệ thống quản lý đơn hàng, tồn kho và tài chính cho Tiệm Nước Nhỏ.",
  "requestFramePermissions": []
}
```

### File: server.ts
```ts
import express from "express";
import { createServer as createViteServer } from "vite";
import { WebSocketServer, WebSocket } from "ws";
import http from "http";

async function startServer() {
  const app = express();
  const server = http.createServer(app);
  const wss = new WebSocketServer({ server });

  const PORT = 3000;

  // Store connected clients
  const clients = new Set<WebSocket>();

  wss.on("connection", (ws) => {
    clients.add(ws);
    console.log("New client connected via WebSocket");

    ws.on("message", (message) => {
      try {
        const data = JSON.parse(message.toString());
        // Broadcast new order to all other clients
        if (data.type === "NEW_ORDER") {
          console.log("New order received, broadcasting...");
          clients.forEach((client) => {
            // We broadcast to everyone including the sender for simplicity, 
            // or we could exclude the sender. Let's send to all.
            if (client.readyState === WebSocket.OPEN) {
              client.send(JSON.stringify({ 
                type: "NEW_ORDER_NOTIFICATION", 
                order: data.order,
                timestamp: new Date().toISOString()
              }));
            }
          });
        }
      } catch (e) {
        console.error("Error parsing message", e);
      }
    });

    ws.on("close", () => {
      clients.delete(ws);
      console.log("Client disconnected from WebSocket");
    });
  });

  // API routes
  app.get("/api/health", (req, res) => {
    res.json({ status: "ok" });
  });

  // Vite middleware for development
  if (process.env.NODE_ENV !== "production") {
    const vite = await createViteServer({
      server: { middlewareMode: true },
      appType: "spa",
    });
    app.use(vite.middlewares);
  } else {
    // Serve static files in production
    app.use(express.static("dist"));
    app.get("*", (req, res) => {
      res.sendFile("dist/index.html", { root: "." });
    });
  }

  server.listen(PORT, "0.0.0.0", () => {
    console.log(`Server running on http://localhost:${PORT}`);
  });
}

startServer();

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "experimentalDecorators": true,
    "useDefineForClassFields": false,
    "module": "ESNext",
    "lib": [
      "ES2022",
      "DOM",
      "DOM.Iterable"
    ],
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "isolatedModules": true,
    "moduleDetection": "force",
    "allowJs": true,
    "jsx": "react-jsx",
    "paths": {
      "@/*": [
        "./*"
      ]
    },
    "allowImportingTsExtensions": true,
    "noEmit": true
  }
}

```

### File: vite.config.ts
```ts
import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import {defineConfig, loadEnv} from 'vite';

export default defineConfig(({mode}) => {
  const env = loadEnv(mode, '.', '');
  return {
    plugins: [react(), tailwindcss()],
    define: {
      'process.env.GEMINI_API_KEY': JSON.stringify(env.GEMINI_API_KEY),
    },
    resolve: {
      alias: {
        '@': path.resolve(__dirname, '.'),
      },
    },
    server: {
      // HMR is disabled in AI Studio via DISABLE_HMR env var.
      // Do not modifyâfile watching is disabled to prevent flickering during agent edits.
      hmr: process.env.DISABLE_HMR !== 'true',
    },
  };
});

```

### File: src\index.css
```css
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=JetBrains+Mono:wght@400;500&display=swap');
@import "tailwindcss";

@custom-variant dark (&:where(.dark, .dark *));

@theme {
  --font-sans: "Plus Jakarta Sans", ui-sans-serif, system-ui, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, monospace;
  
  --color-primary: #C9252C;
  --color-primary-foreground: var(--color-white);
  
  --color-background: var(--color-white);
  --color-foreground: var(--color-stone-900);
  
  --color-card: var(--color-white);
  --color-card-foreground: var(--color-stone-900);
  
  --color-popover: var(--color-white);
  --color-popover-foreground: var(--color-stone-900);
  
  --color-muted: var(--color-stone-100);
  --color-muted-foreground: var(--color-stone-500);
  
  --color-accent: var(--color-red-100);
  --color-accent-foreground: var(--color-red-900);
  
  --color-destructive: var(--color-red-600);
  --color-destructive-foreground: var(--color-white);

  --color-border: var(--color-stone-200);
  --color-input: var(--color-stone-200);
  --color-ring: #C9252C;
}

@layer base {
  /* Hide scrollbar for Chrome, Safari and Opera */
  *::-webkit-scrollbar {
    display: none;
  }

  /* Hide scrollbar for IE, Edge and Firefox */
  * {
    -ms-overflow-style: none;  /* IE and Edge */
    scrollbar-width: none;  /* Firefox */
  }

  :root {
    --background: 0 0% 100%;
    --foreground: 240 10% 3.9%;
  }

  .dark {
    --background: 0 0% 0%; /* Black */
    --foreground: 0 0% 98%; /* White */
    
    --color-background: var(--color-black);
    --color-foreground: var(--color-white);
    
    --color-card: var(--color-stone-950);
    --color-card-foreground: var(--color-stone-50);
    
    --color-popover: var(--color-stone-950);
    --color-popover-foreground: var(--color-stone-50);
    
    --color-muted: var(--color-stone-800);
    --color-muted-foreground: var(--color-stone-400);
    
    --color-accent: var(--color-red-900);
    --color-accent-foreground: var(--color-red-50);
    
    --color-border: var(--color-stone-800);
    --color-input: var(--color-stone-800);
  }

  body {
    @apply bg-background text-foreground antialiased selection:bg-red-100 selection:text-red-900 overflow-x-hidden;
    -webkit-tap-highlight-color: transparent;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  /* Touch-friendly global rules */
  button, a, input, select, textarea, [role="button"] {
    touch-action: manipulation;
  }

  /* Focus states for accessibility */
  button:focus-visible, a:focus-visible, input:focus-visible, select:focus-visible, textarea:focus-visible {
    outline: 2px solid var(--color-ring);
    outline-offset: 2px;
  }
}

@layer components {
  .glass-header {
    @apply sticky top-0 z-40 bg-white dark:bg-black border-b border-stone-100 dark:border-stone-800;
  }
  
  .glass-nav {
    @apply sticky bottom-0 z-40 bg-white dark:bg-black border-t border-stone-100 dark:border-stone-800;
    padding-bottom: env(safe-area-inset-bottom);
  }

  .input-field {
    @apply w-full p-3 sm:p-4 rounded-xl sm:rounded-2xl bg-stone-50 dark:bg-stone-900 border-none focus:ring-2 focus:ring-[#C9252C]/20 focus:bg-white dark:focus:bg-black font-medium placeholder:text-stone-400 text-stone-800 dark:text-stone-200 text-sm sm:text-base;
  }

  .btn-primary {
    @apply w-full bg-[#C9252C] text-white py-3 sm:py-4 rounded-xl sm:rounded-[20px] font-black text-base sm:text-lg shadow-none flex items-center justify-center gap-2 hover:bg-[#B91C1C];
  }

  .btn-secondary {
    @apply w-full bg-stone-100 dark:bg-stone-800 text-stone-600 dark:text-stone-300 py-3 sm:py-4 rounded-xl sm:rounded-[20px] font-bold text-base sm:text-lg flex items-center justify-center gap-2 hover:bg-stone-200 dark:hover:bg-stone-700;
  }

  .card {
    @apply bg-white dark:bg-stone-900 rounded-xl sm:rounded-[24px] p-4 sm:p-5 shadow-none border border-stone-100 dark:border-stone-800;
  }
}

.tap-active {
  @apply active:opacity-80;
}
```

### File: src\types.ts
```ts
export interface DashboardData {
  revenue: {
    today: number;
    thisWeek: number;
    thisMonth: number;
  };
  orders: {
    today: number;
    thisWeek: number;
    thisMonth: number;
  };
  topItems?: { name: string; quantity: number }[];
}

export interface SoTayItem {
  id?: string;
  id_thu_chi?: string;
  thoi_gian: string;
  phan_loai: 'Thu' | 'Chi';
  danh_muc: string;
  so_tien: number;
  ghi_chu: string;
}

export interface MenuItem {
  id: string;
  name: string;
  price: number;
  category: string;
  image?: string;
  description?: string;
  isOutOfStock?: boolean;
  inventoryQty?: number;
  hasCustomizations?: boolean;
}

export interface CartItem extends MenuItem {
  cartItemId: string;
  quantity: number;
  unitPrice: number;
  note?: string;
  size?: string;
  temperature?: string;
  sugarLevel?: string;
  iceLevel?: string;
  toppings?: any[];
  hasCustomizations?: boolean;
}

export interface OrderRow {
  ORDER_ID: string;
  CUSTOMER_NAME: string;
  PHONE: string;
  TABLE_NO: string;
  ITEM_ID: string;
  ITEM_NAME: string;
  QTY: number;
  PRICE: number;
  TOTAL: number;
  STATUS: string;
  PAYMENT_METHOD: string;
  NOTES: string;
  TIMESTAMP: string;
}

export interface OrderData {
  orderId: string;
  customerName: string;
  phoneNumber: string;
  tableNumber: string;
  items: CartItem[];
  total: number;
  timestamp: string;
  notes?: string;
  paymentMethod: string;
  orderStatus: string;
  paymentStatus?: string;
  staffId?: string;
  staffName?: string;
}

export interface Expense {
  id: string;
  amount: number;
  description: string;
  category: string;
  date: string;
  type: 'expense' | 'income';
}

export type Role = 'staff' | 'manager';

export interface Staff {
  id: string;
  username: string;
  password?: string;
  name: string;
  role: Role;
  hourlyRate?: number;
  active: boolean;
  pin?: string;
}

export interface TimeSheet {
  id: string;
  staffId: string;
  checkIn: string;
  checkOut?: string;
  totalHours?: number;
  date: string;
}

```

### File: src\hooks\useAddToCartAnimation.ts
```ts
import { useCallback } from 'react';

export const useAddToCartAnimation = () => {
  const triggerAnimation = useCallback((itemId: string) => {
    // Step 3: Haptic feedback (nếu device hỗ trợ)
    try {
      if (typeof navigator !== 'undefined' && navigator.vibrate) {
        navigator.vibrate(30);
      }
    } catch (error) {
      console.warn('Vibration API not supported', error);
    }

    // Step 1: Item card animation
    // Giả định thẻ món ăn có id dạng `menu-item-${itemId}`
    const itemElement = document.getElementById(`menu-item-${itemId}`);
    if (itemElement) {
      // Scale animation: 1.0 -> 1.08 -> 1.0 (duration: 200ms, ease-out)
      itemElement.animate([
        { transform: 'scale(1)' },
        { transform: 'scale(1.08)' },
        { transform: 'scale(1)' }
      ], {
        duration: 200,
        easing: 'ease-out'
      });

      // Brief background flash: rgba(16,185,129,0.15) for 150ms
      const originalBg = itemElement.style.backgroundColor;
      itemElement.style.backgroundColor = 'rgba(16,185,129,0.15)';
      setTimeout(() => {
        itemElement.style.backgroundColor = originalBg;
      }, 150);
    }

    // Step 2: Cart badge (item count) animation
    // Giả định badge giỏ hàng có id `cart-badge`
    const badgeElement = document.getElementById('cart-badge');
    if (badgeElement) {
      // Bounce animation: translateY(0) -> translateY(-6px) -> translateY(0)
      badgeElement.animate([
        { transform: 'translateY(0)' },
        { transform: 'translateY(-6px)' },
        { transform: 'translateY(0)' }
      ], {
        duration: 250,
        easing: 'cubic-bezier(0.175, 0.885, 0.32, 1.275)' // Spring-like easing
      });

      // Badge background briefly flashes green then returns to normal
      const originalBadgeBg = badgeElement.style.backgroundColor;
      badgeElement.style.backgroundColor = '#10b981'; // emerald-500
      setTimeout(() => {
        badgeElement.style.backgroundColor = originalBadgeBg;
      }, 250);
    }
  }, []);

  return { triggerAnimation };
};

```

### File: src\hooks\usePermission.ts
```ts
import { useState, useEffect } from 'react';
import Cookies from 'js-cookie';

// Helper để decode JWT payload (client-side)
function decodeJwtPayload(token: string) {
  try {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
    return JSON.parse(jsonPayload);
  } catch (e) {
    return null;
  }
}

export function usePermission() {
  const [role, setRole] = useState<string | null>(null);

  useEffect(() => {
    // Đọc role từ JWT được lưu trong httpOnly cookie
    // Lưu ý: JS không thể đọc trực tiếp httpOnly cookie.
    // Trong thực tế, server sẽ cung cấp endpoint /api/auth/me hoặc set một cookie không httpOnly (ví dụ: 'user_role')
    // Ở đây chúng ta cố gắng đọc 'token' (nếu không httpOnly) hoặc 'user_role' từ cookie.
    const token = Cookies.get('token');
    const userRoleCookie = Cookies.get('user_role');
    
    if (userRoleCookie) {
      setRole(userRoleCookie);
    } else if (token) {
      const payload = decodeJwtPayload(token);
      if (payload && payload.role) {
        setRole(payload.role);
      }
    } else {
      // Fallback mặc định cho demo (nếu không có token)
      setRole('manager'); // Đặt là manager để có thể test UI
    }
  }, []);

  const can = (action: string) => {
    if (role === 'manager') return true;
    if (role === 'cashier') {
      const allowedActions = ['POST /api/orders', 'GET /api/menu', 'GET /api/orders/my'];
      return allowedActions.includes(action);
    }
    return false;
  };

  return {
    role,
    can,
    isManager: role === 'manager',
    isCashier: role === 'cashier'
  };
}

```

### File: src\hooks\useStaggeredList.ts
```ts
import { Variants } from 'framer-motion';

export const useStaggeredList = () => {
  // Container variants để stagger children
  const containerVariants: Variants = {
    hidden: { opacity: 0 },
    show: {
      opacity: 1,
      transition: {
        // Item N animates after: N × 40ms delay
        staggerChildren: 0.04, 
      },
    },
  };

  // Item variants cho từng phần tử
  const itemVariants: Variants = {
    // Animation: opacity 0 -> 1, translateY(8px) -> 0
    hidden: { opacity: 0, y: 8 },
    show: { 
      opacity: 1, 
      y: 0,
      transition: {
        // Duration: 200ms per item, ease-out
        duration: 0.2, 
        ease: 'easeOut'
      }
    },
  };

  return { containerVariants, itemVariants };
};

```

### File: src\lib\auth.ts
```ts
import { SignJWT, jwtVerify } from 'jose';

// Đọc JWT secret từ biến môi trường
const secret = new TextEncoder().encode(process.env.JWT_SECRET || 'default_secret_key_for_development');

/**
 * Tạo JWT token (expires 8h)
 */
export async function signToken(userId: string, role: string) {
  const alg = 'HS256';
  const jwt = await new SignJWT({ userId, role })
    .setProtectedHeader({ alg })
    .setIssuedAt()
    .setExpirationTime('8h')
    .sign(secret);
  return jwt;
}

/**
 * Decode và validate token
 */
export async function verifyToken(token: string) {
  try {
    const { payload } = await jwtVerify(token, secret);
    return payload;
  } catch (error) {
    throw new Error('Invalid token');
  }
}

/**
 * Middleware helper để kiểm tra role (dành cho Express/Node.js backend nếu cần)
 */
export function requireRole(role: string) {
  return async (req: any, res: any, next: any) => {
    const authHeader = req.headers.authorization;
    const token = authHeader?.split(' ')[1] || req.cookies?.token;
    
    if (!token) {
      return res.status(403).json({ error: 'Không có quyền truy cập' });
    }

    try {
      const decoded = await verifyToken(token);
      if (decoded.role !== role && decoded.role !== 'manager') {
        return res.status(403).json({ error: 'Không có quyền truy cập' });
      }
      // Gắn thông tin user vào request
      req.user = decoded;
      next();
    } catch (error) {
      return res.status(403).json({ error: 'Token không hợp lệ' });
    }
  };
}

```

### File: src\lib\conflictResolver.ts
```ts
import { getDb, SyncAction } from './localDb';
import { useNotificationStore } from './useNotification'; 

export const handleConflict = async (action: SyncAction, serverData: any) => {
  const db = await getDb();
  
  // 1. Loại bỏ phiên bản local (Discard local version)
  // 2. Ghi đè IndexedDB bằng dữ liệu mới nhất từ server
  if (action.entity === 'orders') {
    await db.put('orders', serverData);
  }
  
  // 3. Re-render UI silently: 
  // Dispatch một event để UI tự động cập nhật lại với dữ liệu từ server.
  window.dispatchEvent(new CustomEvent('pos:data-updated', { 
    detail: { entity: action.entity, data: serverData } 
  }));

  // 4. Hiển thị toast thông báo màu vàng
  // Sử dụng hàm addNotification từ store/hook
  const { addNotification } = useNotificationStore.getState();
  addNotification({
    type: 'warning',
    message: 'Dữ liệu đã được cập nhật từ thiết bị khác',
    // Auto-dismiss được xử lý trong useNotification hook (8 giây)
  });
};

```

### File: src\lib\inventoryWorker.ts
```ts
import { checkStockAlerts } from './stockAlerts';

/**
 * Xử lý trừ kho nguyên liệu dựa trên đơn hàng
 */
export async function triggerInventoryDeduction(orderId: string, appsScriptUrl: string) {
  if (!appsScriptUrl) return;
  
  try {
    const response = await fetch(appsScriptUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify({
        action: 'processOrderInventory',
        orderId,
        type: 'deduct'
      }),
    });
    
    const result = await response.json();
    if (result.status === 'success') {
      console.log(`[Inventory] Đã trừ kho cho đơn hàng ${orderId}`);
      if (result.warnings && result.warnings.length > 0) {
        // Trigger a custom event for warnings
        window.dispatchEvent(new CustomEvent('inventoryWarning', { detail: result.warnings }));
      }
    }
  } catch (error) {
    console.error(`[Inventory] Lỗi trừ kho:`, error);
  }
}

/**
 * Hoàn kho khi đơn hàng bị hủy
 */
export async function triggerInventoryRefund(orderId: string, appsScriptUrl: string) {
  if (!appsScriptUrl) return;
  
  try {
    const response = await fetch(appsScriptUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify({
        action: 'processOrderInventory',
        orderId,
        type: 'refund'
      }),
    });
    
    const result = await response.json();
    if (result.status === 'success') {
      console.log(`[Inventory] Đã hoàn kho cho đơn hàng ${orderId}`);
      window.dispatchEvent(new CustomEvent('inventoryRefunded', { detail: { orderId } }));
    }
  } catch (error) {
    console.error(`[Inventory] Lỗi hoàn kho:`, error);
  }
}

```

### File: src\lib\localDb.ts
```ts
import { openDB, DBSchema, IDBPDatabase } from 'idb';

export interface Order {
  id: string;
  version: number;
  updated_at: string;
  // ... other fields
  [key: string]: any;
}

export interface SyncAction {
  id: string; // unique id for the action
  type: 'CREATE' | 'UPDATE' | 'DELETE';
  entity: 'orders' | 'inventory' | 'products'; 
  payload: any;
  created_at: string;
  retry_count: number;
  status: 'pending' | 'failed';
}

interface POSDB extends DBSchema {
  orders: {
    key: string;
    value: Order;
  };
  sync_queue: {
    key: string;
    value: SyncAction;
    indexes: { 'by-status': string };
  };
}

let dbPromise: Promise<IDBPDatabase<POSDB>> | null = null;

// Khởi tạo IndexedDB
export const getDb = () => {
  if (!dbPromise) {
    dbPromise = openDB<POSDB>('pos-db', 1, {
      upgrade(db) {
        if (!db.objectStoreNames.contains('orders')) {
          db.createObjectStore('orders', { keyPath: 'id' });
        }
        if (!db.objectStoreNames.contains('sync_queue')) {
          const syncStore = db.createObjectStore('sync_queue', { keyPath: 'id' });
          syncStore.createIndex('by-status', 'status');
        }
      },
    });
  }
  return dbPromise;
};

// --- Helper methods cho Orders ---
export const saveOrderLocal = async (order: Order) => {
  const db = await getDb();
  await db.put('orders', order);
};

export const getOrderLocal = async (id: string) => {
  const db = await getDb();
  return db.get('orders', id);
};

export const getAllOrdersLocal = async () => {
  const db = await getDb();
  return db.getAll('orders');
};

// --- Helper methods cho Sync Queue ---
export const addSyncAction = async (action: Omit<SyncAction, 'retry_count' | 'status'>) => {
  const db = await getDb();
  await db.put('sync_queue', {
    ...action,
    retry_count: 0,
    status: 'pending',
  });
};

```

### File: src\lib\poller.ts
```ts
import { useEffect, useRef, useState } from 'react';
import { getDb } from './localDb';

// Hàm lấy dữ liệu thay đổi từ server (Delta Sync)
export const fetchDeltaSync = async () => {
  const lastSyncedAt = localStorage.getItem('last_synced_at') || new Date(0).toISOString();
  
  try {
    // Gọi API với tham số last_synced_at
    // const response = await fetch(`/api/sync?since=${lastSyncedAt}`);
    // if (!response.ok) throw new Error('Sync failed');
    // const data = await response.json();
    
    // Giả lập API response trả về ONLY records updated after that timestamp
    const data = {
      orders: [], // Chỉ chứa các order được cập nhật
      timestamp: new Date().toISOString()
    };
    
    if (data.orders && data.orders.length > 0) {
      const db = await getDb();
      const tx = db.transaction('orders', 'readwrite');
      for (const order of data.orders) {
        await tx.store.put(order);
      }
      await tx.done;
      
      // Báo cho UI biết có dữ liệu mới để re-render
      window.dispatchEvent(new CustomEvent('pos:data-updated'));
    }
    
    // Cập nhật thời gian sync cuối
    localStorage.setItem('last_synced_at', data.timestamp);
    
  } catch (error) {
    console.error('Delta sync error:', error);
  }
};

// Custom hook: useSmartPolling
export const useSmartPolling = () => {
  const [lastInteraction, setLastInteraction] = useState<number>(Date.now());
  const intervalRef = useRef<NodeJS.Timeout | null>(null);

  // Theo dõi tương tác người dùng (Track last user interaction timestamp)
  useEffect(() => {
    const handleInteraction = () => {
      setLastInteraction(Date.now());
    };

    window.addEventListener('touchstart', handleInteraction, { passive: true });
    window.addEventListener('mousedown', handleInteraction, { passive: true });

    return () => {
      window.removeEventListener('touchstart', handleInteraction);
      window.removeEventListener('mousedown', handleInteraction);
    };
  }, []);

  // Logic điều chỉnh chu kỳ Polling (Dynamic interval logic)
  useEffect(() => {
    const setupPolling = () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }

      const now = Date.now();
      const timeSinceLastInteraction = now - lastInteraction;
      const isIdle = timeSinceLastInteraction >= 2 * 60 * 1000; // 2 phút

      // Nếu idle >= 2 phút -> poll mỗi 30s. Ngược lại -> poll mỗi 5s.
      const pollInterval = isIdle ? 30000 : 5000;

      intervalRef.current = setInterval(() => {
        if (navigator.onLine) {
          fetchDeltaSync();
        }
      }, pollInterval);
    };

    setupPolling();

    // Cần setup lại định kỳ để kiểm tra trạng thái idle
    const checkIdleInterval = setInterval(setupPolling, 5000);

    return () => {
      if (intervalRef.current) clearInterval(intervalRef.current);
      clearInterval(checkIdleInterval);
    };
  }, [lastInteraction]);
};

```

### File: src\lib\stockAlerts.ts
```ts
// Giả lập database (Prisma hoặc SQL)
const db = {
  stock_alerts: {
    create: async (data: any) => console.log('Tạo cảnh báo mới:', data),
    findFirst: async (query: any) => null // Chưa có cảnh báo chưa giải quyết
  }
};

/**
 * Khi nguyên liệu giảm xuống dưới mức an toàn (safety_stock):
 * - Chèn bản ghi vào bảng `stock_alerts`
 */
export async function checkStockAlerts(ingredient: any) {
  if (ingredient.current_stock < ingredient.safety_stock) {
    // Kiểm tra xem đã có cảnh báo chưa giải quyết cho nguyên liệu này chưa
    const existingAlert = await db.stock_alerts.findFirst({
      where: {
        ingredient_id: ingredient.id,
        is_resolved: false
      }
    });

    if (!existingAlert) {
      // Insert record vào bảng stock_alerts
      await db.stock_alerts.create({
        data: {
          ingredient_id: ingredient.id,
          ingredient_name: ingredient.name,
          current_stock: ingredient.current_stock,
          safety_stock: ingredient.safety_stock,
          triggered_at: new Date(),
          is_resolved: false
        }
      });
      
      console.log(`[Alert] Đã tạo cảnh báo tồn kho thấp cho: ${ingredient.name}`);
    }
  }
}

```

### File: src\lib\syncWorker.ts
```ts
import { getDb, SyncAction } from './localDb';
import { handleConflict } from './conflictResolver';

const SYNC_INTERVAL = 5000; // 5 giây
let isSyncing = false;

// Hàm mô phỏng gửi dữ liệu lên server
const sendToServer = async (action: SyncAction) => {
  // Trong thực tế, bạn sẽ dùng fetch() để gọi API
  // const response = await fetch('/api/sync', {
  //   method: 'POST',
  //   headers: { 'Content-Type': 'application/json' },
  //   body: JSON.stringify(action),
  // });
  // return response;
  
  // Giả lập API call
  return new Promise<{ ok: boolean; status: number; json: () => Promise<any> }>((resolve) => {
    setTimeout(() => {
      resolve({ ok: true, status: 200, json: async () => ({}) });
    }, 500);
  });
};

export const startSyncWorker = () => {
  // Chạy background loop bằng setInterval
  setInterval(async () => {
    if (isSyncing) return;
    
    // Kiểm tra kết nối mạng trước khi sync
    if (!navigator.onLine) return;

    isSyncing = true;
    try {
      const db = await getDb();
      // Lấy các action đang pending từ sync_queue
      const pendingActions = await db.getAllFromIndex('sync_queue', 'by-status', 'pending');
      
      if (pendingActions.length === 0) {
        isSyncing = false;
        return;
      }

      // Xử lý tuần tự từng action
      for (const action of pendingActions) {
        try {
          const response = await sendToServer(action);
          
          if (response.ok) {
            // Thành công: xóa khỏi queue, đánh dấu đã sync
            await db.delete('sync_queue', action.id);
          } else if (response.status === 409) {
            // Xung đột phiên bản (Version conflict)
            const serverData = await response.json();
            await handleConflict(action, serverData);
            // Sau khi xử lý xung đột, xóa action khỏi queue
            await db.delete('sync_queue', action.id);
          } else {
            throw new Error('Server error');
          }
        } catch (error) {
          // Thất bại: tăng retry_count và áp dụng exponential backoff
          action.retry_count += 1;
          
          if (action.retry_count >= 3) {
            action.status = 'failed';
          }
          
          await db.put('sync_queue', action);
          
          // Exponential backoff: đợi 1s, 2s, 4s
          const backoffTime = Math.pow(2, action.retry_count - 1) * 1000;
          await new Promise(resolve => setTimeout(resolve, backoffTime));
        }
      }
    } catch (error) {
      console.error('Sync worker error:', error);
    } finally {
      isSyncing = false;
    }
  }, SYNC_INTERVAL);
};

```

### File: src\lib\useNotification.ts
```ts
import { useState, useEffect } from 'react';

export interface Notification {
  id: string;
  type: 'success' | 'warning' | 'error' | 'info';
  message: string;
  isExiting?: boolean; // Cờ để kích hoạt animation fade-out
}

// Simple global state for notifications
let globalNotifications: Notification[] = [];
let listeners: ((notifications: Notification[]) => void)[] = [];

const notifyListeners = () => {
  listeners.forEach(listener => listener([...globalNotifications]));
};

export const useNotificationStore = {
  getState: () => ({
    notifications: globalNotifications,
    addNotification: (notif: Omit<Notification, 'id'>) => {
      const id = Math.random().toString(36).substring(2, 9);
      globalNotifications = [...globalNotifications, { ...notif, id }];
      notifyListeners();
      return id;
    },
    removeNotification: (id: string) => {
      globalNotifications = globalNotifications.filter(n => n.id !== id);
      notifyListeners();
    },
    markAsExiting: (id: string) => {
      globalNotifications = globalNotifications.map(n => 
        n.id === id ? { ...n, isExiting: true } : n
      );
      notifyListeners();
    }
  }),
  subscribe: (listener: (notifications: Notification[]) => void) => {
    listeners.push(listener);
    return () => {
      listeners = listeners.filter(l => l !== listener);
    };
  }
};

export const useNotification = () => {
  const [notifications, setNotifications] = useState<Notification[]>(globalNotifications);

  useEffect(() => {
    const unsubscribe = useNotificationStore.subscribe(setNotifications);
    return unsubscribe;
  }, []);

  const { addNotification, removeNotification, markAsExiting } = useNotificationStore.getState();

  // Xử lý auto-dismiss 8s
  useEffect(() => {
    const timers: Record<string, NodeJS.Timeout> = {};

    notifications.forEach(notif => {
      // Chỉ đặt timer nếu thông báo chưa ở trạng thái exiting và chưa có timer
      if (!notif.isExiting && !timers[notif.id]) {
        // Đặt timer 8000ms (8 giây)
        timers[notif.id] = setTimeout(() => {
          // Bắt đầu animation fade-out (opacity 1 -> 0, 300ms)
          markAsExiting(notif.id);
          
          // Đợi 300ms cho animation hoàn tất rồi mới xóa khỏi state
          setTimeout(() => {
            removeNotification(notif.id);
          }, 300);
          
        }, 8000);
      }
    });

    return () => {
      // Use clearTimeout on unmount to prevent memory leaks
      Object.values(timers).forEach(clearTimeout);
    };
  }, [notifications, markAsExiting, removeNotification]);

  return { notifications, addNotification, removeNotification };
};

```

### File: src\services\NotificationService.ts
```ts
type NotificationCallback = (data: any) => void;

class NotificationService {
  private socket: WebSocket | null = null;
  private callbacks: Set<NotificationCallback> = new Set();
  private reconnectTimeout: any = null;

  constructor() {
    this.connect();
  }

  private connect() {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const host = window.location.host;
    this.socket = new WebSocket(`${protocol}//${host}`);

    this.socket.onopen = () => {
      console.log('Connected to notification server');
      if (this.reconnectTimeout) {
        clearTimeout(this.reconnectTimeout);
        this.reconnectTimeout = null;
      }
    };

    this.socket.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        this.callbacks.forEach(callback => callback(data));
      } catch (e) {
        console.error('Error parsing notification message', e);
      }
    };

    this.socket.onclose = () => {
      console.log('Disconnected from notification server, retrying...');
      this.reconnectTimeout = setTimeout(() => this.connect(), 3000);
    };

    this.socket.onerror = (error) => {
      console.error('WebSocket error:', error);
      this.socket?.close();
    };
  }

  public subscribe(callback: NotificationCallback) {
    this.callbacks.add(callback);
    return () => {
      this.callbacks.delete(callback);
    };
  }

  public notifyNewOrder(order: any) {
    if (this.socket && this.socket.readyState === WebSocket.OPEN) {
      this.socket.send(JSON.stringify({
        type: 'NEW_ORDER',
        order
      }));
    }
  }
}

export const notificationService = new NotificationService();

```

