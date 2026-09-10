# OmniClaw — landing

Trang phát hành cho **OmniClaw**. Đây **không phải web tĩnh**: nó có serverless
function, kiểm dữ liệu phía máy chủ và đọc dữ liệu lúc chạy.

## Cấu trúc

```
index.html          Trang, tự chứa (font đã nhúng)
deploy-shim.js      Nối form với API, dán trạng thái deployment vào chân trang
webgl-stage.js      Hạ tầng WebGL dùng chung (chỉ có ở trang dùng 3D WebGL)
data/site.json      Dữ liệu đọc lúc chạy — sửa file này không cần dựng lại trang
api/lead.js         POST /api/lead — nhận lead, kiểm dữ liệu, chống spam theo IP
api/health.js       GET /health — commit, region, env của deployment đang chạy
vercel.json         Header bảo mật, cache, rewrite /health
```

## Không có bước build

`framework: null`, `buildCommand: null`. Vercel phục vụ file tĩnh và chạy
function trong `api/`. Không npm install, không bundler.

## Kiểm sau khi deploy

```bash
curl https://<domain>/health
curl -X POST https://<domain>/api/lead \
  -H 'Content-Type: application/json' \
  -d '{"value":"ban@congty.vn"}'
```

Lead ghi vào **Vercel Runtime Logs**. Muốn chuyển tiếp đi đâu thì đặt biến môi
trường `LEAD_WEBHOOK_URL` — không đặt cũng chạy, chỉ là lead nằm trong log.
