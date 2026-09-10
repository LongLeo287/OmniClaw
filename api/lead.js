// Vercel Serverless Function — OmniClaw
// Đây là phần khiến trang KHÔNG còn là web tĩnh: form gửi thật tới đây, có
// kiểm dữ liệu phía máy chủ, có mã tác vụ trả về, và có thể chuyển tiếp đi đâu đó.
//
// Cấu hình (Vercel → Settings → Environment Variables), tất cả đều tuỳ chọn:
//   LEAD_WEBHOOK_URL  chuyển tiếp lead sang Zalo/Slack/Google Apps Script
//   LEAD_NOTIFY_TO    email nhận thông báo, chỉ ghi vào log nếu chưa nối dịch vụ gửi thư

const PROJECT = "OmniClaw";
const SLUG = "omniclaw";
const FIELD = "email";

const RE_EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const RE_TEL = /^[0-9+().\s-]{8,20}$/;

// Chống spam đơn giản theo IP, đủ cho một landing page
const seen = new Map();
const RATE_WINDOW = 60000;
const RATE_MAX = 5;

function rateLimited(ip) {
  const now = Date.now();
  const hits = (seen.get(ip) || []).filter((t) => now - t < RATE_WINDOW);
  hits.push(now);
  seen.set(ip, hits);
  if (seen.size > 500) seen.clear();
  return hits.length > RATE_MAX;
}

function id() {
  return SLUG.slice(0, 4) + '_' + Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
}

export default async function handler(req, res) {
  res.setHeader('Content-Type', 'application/json; charset=utf-8');

  if (req.method === 'OPTIONS') {
    res.setHeader('Allow', 'POST, OPTIONS');
    return res.status(204).end();
  }
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST, OPTIONS');
    return res.status(405).json({ ok: false, error: 'Chỉ nhận POST' });
  }

  const ip = (req.headers['x-forwarded-for'] || '').split(',')[0].trim() || 'unknown';
  if (rateLimited(ip)) {
    return res.status(429).json({ ok: false, error: 'Gửi quá nhanh. Thử lại sau một phút.' });
  }

  let body = req.body;
  if (typeof body === 'string') {
    try { body = JSON.parse(body); } catch (e) { body = {}; }
  }
  body = body || {};

  const value = String(body.value || '').trim();
  const note = String(body.note || '').slice(0, 500);

  if (!value) {
    return res.status(400).json({ ok: false, error: 'Chưa nhập ' + (FIELD === 'tel' ? 'số điện thoại' : 'email') });
  }
  const valid = FIELD === 'tel' ? RE_TEL.test(value) : RE_EMAIL.test(value);
  if (!valid) {
    return res.status(400).json({ ok: false, error: FIELD === 'tel' ? 'Số điện thoại không hợp lệ' : 'Email không hợp lệ' });
  }

  const lead = {
    id: id(),
    project: PROJECT,
    slug: SLUG,
    field: FIELD,
    value,
    note,
    referer: req.headers.referer || null,
    userAgent: (req.headers['user-agent'] || '').slice(0, 200),
    at: new Date().toISOString()
  };

  // Log ra Vercel Runtime Logs — luôn có, không cần cấu hình gì
  console.log('[lead]', JSON.stringify(lead));

  if (process.env.LEAD_WEBHOOK_URL) {
    try {
      await fetch(process.env.LEAD_WEBHOOK_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(lead)
      });
    } catch (err) {
      // Webhook lỗi thì vẫn coi là nhận được lead — đã có trong log
      console.error('[lead] webhook thất bại:', err && err.message);
    }
  }

  return res.status(200).json({
    ok: true,
    id: lead.id,
    message: FIELD === 'tel' ? 'Đã nhận. Tôi gọi lại trong giờ mở quán.' : 'Đã nhận. Kiểm tra email trong ít phút.'
  });
}
