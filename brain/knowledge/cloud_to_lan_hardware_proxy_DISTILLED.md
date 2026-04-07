---
title: "Cloud to LAN Hardware Integration (Local Proxy Server)"
description: "Mô hình và chiến lược kết nối ứng dụng Web nằm trên Public Cloud (Vercel/Netlify) với phần cứng ngoại vi nằm sâu trong mạng LAN (VD: Máy in hóa đơn nhiệt IP: 192.168.x.x) bằng cách sử dụng Local Node.js Proxy."
tags: ["hardware", "proxy", "websocket", "node.js", "cors", "lan", "printer"]
related_projects: ["Tiem_Nuoc_Nho_v5"]
---

# Tích hợp Cloud Web App với Thiết bị Mạng LAN

Khi một phần mềm POS (Point of sale) hoặc Dashboard được hosting trên Cloud (domain HTTPS), nó sẽ lập tức bị giới hạn ngặt nghèo về mặt kết nối:
1. **Trình duyệt tự động chặn (Mixed Content):** Một trang HTTPS không thể thực hiện fetch/gọi HTTP sang một địa chỉ IP nội bộ không mã hóa (ví dụ: `http://192.168.1.100`).
2. **Thiếu hỗ trợ Hardware Native:** Trình duyệt web không thể tự thân mở kết nối TCP Socket RAW dạng `net.createConnection()` tới thiết bị.

Để giải quyết vấn đề in ấn tại quầy mà không phải cấu hình Port Forwarding nguy hiểm ra Internet, dự án áp dụng mô hình **Local Hardware Proxy Server**.

## 1. Mô hình Hoạt động

**A. Đám mây (Cloud - Vercel):**
- Ứng dụng React hiển thị UI, thu thập thông tin và sinh ra Payload (Dữ liệu text mã Hex/ESC POS).
- Ứng dụng Cloud sử dụng `fetch` gọi đến một Agent chạy ngầm trên máy POS của khách hàng.

**B. Máy chủ Thu ngân (Localhost):**
- Tại máy tính thu ngân của cửa hàng (hoặc một Raspberry Pi trong mạng LAN đó), chạy một proxy server bé bé bằng Node.js (`server.ts` / Port: `3001`).
- Proxy này là một *Express Web Server* hỗ trợ nhận CORS từ `https://tiem-nuoc-nho.vercel.app`.

**C. Thiết bị ngoại vi (Thermal Printer - Mạng LAN):**
- Proxy nhận lệnh từ Cloud (thông qua Localhost Browser) và tiến hành mở Native TCP Socket (`net.Socket`) đến địa chỉ IP Máy In trong mạng LAN (VD: `192.168.68.68:9100`).

## 2. Ưu điểm & Triển khai thực tế

* **Không cần NAT/Port Forwarding:** Tránh hoàn toàn rủi ro bảo mật vì máy in không phơi mình ra Public Internet.
* **Tốc độ cục bộ:** Do gọi trực tiếp trên Local Network thay vì phải nhờ máy chủ Cloud đứng giữa phân phối, lệnh in đáp ứng siêu tốc dưới 100ms.
* **Cách Setup (Sử dụng ngầm/Daemon):**
  Sử dụng file script (VD: `start-printer.bat` hoặc dùng `pm2` / Windows Service) để luôn giữ server `localhost:3001` duy trì ngầm. 

## 3. Mã Nguồn Mẫu (server.ts Proxy)

```typescript
import express from 'express';
import cors from 'cors';
import net from 'net';

const app = express();
// Mở CORS hoàn toàn cho Client Vercel
app.use(cors({ origin: '*' }));
app.use(express.json());

app.post('/api/print', async (req, res) => {
  const { ip, port = 9100, bufferObject } = req.body;
  const buffer = Buffer.from(Object.values(bufferObject));

  const client = new net.Socket();
  // Set Timeout chống treo app (2500ms)
  client.setTimeout(2500);

  client.connect(port, ip, () => {
    // Thành công kết nối máy in
    client.write(buffer, (err) => {
      if (err) res.status(500).json({ status: 'error', message: 'Lỗi ghi dữ liệu xuống TCP' });
      else res.json({ status: 'success', message: 'Đã in xong' });
      client.destroy();
    });
  });

  client.on('error', (err) => {
    res.status(500).json({ status: 'error', message: `LAN Offline: ${err.message}` });
    client.destroy();
  });
});

app.listen(3001, () => console.log('Local Hardware Proxy is running on port 3001'));
```

## 4. Đặc điểm Kỹ thuật

- Kỹ thuật điều khiển in ấn: API `thermal-printer` sinh ra ESC/POS commands phía Browser hoặc Local Server, chuyển thành mảng bytes/Buffer rồi truyền thẳng xuống port `9100` của máy in.
- Có thể scale rộng để hỗ trợ máy đọc mã vạch, cân điện tử, hoặc phần cứng máy thu ngân (cash drawer kick-out) bằng cách dùng thư viện `serialport` ở file local proxy.
