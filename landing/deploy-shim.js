/* Lớp nối phần động — chạy sau khi trang đã vẽ.
   Nó làm hai việc, và cả hai đều cần máy chủ nên trang không còn là web tĩnh:
   1. Mọi <form> trên trang gửi thật tới /api/lead, có trạng thái đang gửi / lỗi / xong
   2. Đọc /data/site.json lúc chạy rồi dán một dòng trạng thái deployment vào chân trang */
(function () {
  'use strict';

  /* --- Gắn lại metadata sau khi bộ giải nén thay cả thẻ <html> ---
     Bộ giải nén gọi document.documentElement.replaceWith(), nên mọi thẻ trong
     <head> của lớp bọc bị xoá sạch: title thành rỗng, mất lang, mất canonical,
     mất og:*. Bộ quét của Facebook/Zalo không chạy JS nên chúng đọc lớp bọc
     tĩnh (đã vá riêng); đoạn này lo cho trình duyệt và thanh tiêu đề. */
  var META = {"title": "OmniClaw — Hệ điều hành tám daemon", "description": "Hệ điều hành agent tám daemon cho Claude Code và Google Antigravity. Zero-trust, bộ nhớ ba tầng, 578 kỹ năng đã đăng ký.", "url": "https://omniclaw-longleo.vercel.app", "image": "https://omniclaw-longleo.vercel.app/cover.jpg"};

  function setMeta(sel, attr, key, val) {
    var el = document.head.querySelector(sel);
    if (!el) {
      el = document.createElement('meta');
      el.setAttribute(attr, key);
      document.head.appendChild(el);
    }
    el.setAttribute('content', val);
  }

  function restoreHead() {
    if (!document.head) return;
    if (document.title !== META.title) document.title = META.title;
    document.documentElement.lang = 'vi';
    setMeta('meta[name="description"]', 'name', 'description', META.description);
    setMeta('meta[property="og:title"]', 'property', 'og:title', META.title);
    setMeta('meta[property="og:description"]', 'property', 'og:description', META.description);
    setMeta('meta[property="og:url"]', 'property', 'og:url', META.url);
    setMeta('meta[property="og:image"]', 'property', 'og:image', META.image);
    setMeta('meta[property="og:type"]', 'property', 'og:type', 'website');
    setMeta('meta[name="twitter:card"]', 'name', 'twitter:card', 'summary_large_image');
    setMeta('meta[name="twitter:title"]', 'name', 'twitter:title', META.title);
    setMeta('meta[name="twitter:image"]', 'name', 'twitter:image', META.image);
    var c = document.head.querySelector('link[rel="canonical"]');
    if (!c) {
      c = document.createElement('link');
      c.rel = 'canonical';
      document.head.appendChild(c);
    }
    c.href = META.url + '/';
  }

  restoreHead();
  /* Giải nén có thể xong sau shim — chạy lại cho chắc. */
  setTimeout(restoreHead, 400);
  setTimeout(restoreHead, 1500);
  var ENDPOINT = '/api/lead';

  function findInput(form) {
    return form.querySelector('input[type=email], input[type=tel], input[type=text]');
  }

  function statusEl(form) {
    var p = form.querySelector('[aria-live]');
    if (p) return p;
    p = document.createElement('p');
    p.setAttribute('aria-live', 'polite');
    p.style.cssText = 'font-size:12px;margin:6px 0 0;min-height:17px';
    form.appendChild(p);
    return p;
  }

  function wire(form) {
    if (form.dataset.wired) return;
    form.dataset.wired = '1';
    var btn = form.querySelector('button[type=submit], button:not([type])');
    var input = findInput(form);
    if (!input) return;

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      e.stopPropagation();
      var out = statusEl(form);
      var value = (input.value || '').trim();
      if (!value) { out.textContent = 'Chưa nhập ' + (input.type === 'tel' ? 'số điện thoại' : 'email'); return; }

      var label = btn ? btn.textContent : '';
      if (btn) { btn.disabled = true; btn.textContent = 'Đang gửi…'; }
      out.textContent = '';

      fetch(ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ value: value, note: document.title })
      })
        .then(function (r) { return r.json().then(function (j) { return { status: r.status, body: j }; }); })
        .then(function (r) {
          if (r.body && r.body.ok) {
            out.textContent = r.body.message + ' (mã ' + r.body.id + ')';
            input.value = '';
          } else {
            out.textContent = (r.body && r.body.error) || 'Gửi không thành công. Thử lại sau.';
          }
        })
        .catch(function () {
          out.textContent = 'Không nối được máy chủ. Kiểm tra mạng rồi thử lại.';
        })
        .then(function () {
          if (btn) { btn.disabled = false; btn.textContent = label; }
        });
    }, true);
  }

  function wireAll() {
    var forms = document.querySelectorAll('form');
    for (var i = 0; i < forms.length; i++) wire(forms[i]);
  }

  function stampFooter() {
    fetch('/data/site.json', { cache: 'no-store' })
      .then(function (r) { return r.json(); })
      .then(function (site) {
        return fetch('/api/health', { cache: 'no-store' })
          .then(function (r) { return r.json(); })
          .then(function (h) { return { site: site, health: h }; })
          .catch(function () { return { site: site, health: null }; });
      })
      .then(function (d) {
        var footer = document.querySelector('footer');
        if (!footer) return;
        var line = document.createElement('p');
        var sha = d.health && d.health.commit ? String(d.health.commit).slice(0, 7) : 'local';
        var region = d.health && d.health.region ? d.health.region : '—';
        line.style.cssText = 'font-family:ui-monospace,monospace;font-size:10.5px;opacity:.55;margin:14px 0 0;text-align:center';
        line.textContent = d.site.name + ' · dữ liệu đọc lúc chạy · cập nhật ' + d.site.updated + ' · commit ' + sha + ' · region ' + region;
        footer.appendChild(line);
      })
      .catch(function () { /* không có máy chủ thì bỏ qua, trang vẫn đọc đủ */ });
  }

  function start() { wireAll(); stampFooter(); setTimeout(wireAll, 1200); }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
