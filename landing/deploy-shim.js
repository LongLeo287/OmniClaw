/* Lớp nối phần động — chạy sau khi trang đã vẽ.
   Nó làm hai việc, và cả hai đều cần máy chủ nên trang không còn là web tĩnh:
   1. Mọi <form> trên trang gửi thật tới /api/lead, có trạng thái đang gửi / lỗi / xong
   2. Đọc /data/site.json lúc chạy rồi dán một dòng trạng thái deployment vào chân trang */
(function () {
  'use strict';

  /* ---------- Cuộn mượt ----------
     Đo ngày 11/09/2026: scroll-behavior khong duoc khai bao o bat ky trang
     nao trong tam, computed value la 'auto'. Bam muc nav la nhay phich sang
     vi tri moi, khong co gi noi cho mat theo kip.

     Trinh duyet tu tat cuon muot khi may bat prefers-reduced-motion, nen khoi
     @media duoi day chi la viet ro y dinh chu khong phai bat buoc. Nut len dau
     trang da tu chon 'auto' hay 'smooth' theo dung thiet lap do. */
  (function () {
    /* Phai chen lai nhieu lan. Bo dong goi thay ca documentElement bang
       replaceWith sau khi giai nen, keo theo toan bo <head> — ke ca <style>
       vua chen. Do ngay 11/09/2026: ban dau toi chen mot lan, tren trang that
       #__cuon_muot khong ton tai, scroll-behavior van la 'auto'.
       __totop_css va __focus_fix song duoc chinh vi chung chen lai. */
    function chen() {
      if (document.getElementById('__cuon_muot')) return;
      var st = document.createElement('style');
      st.id = '__cuon_muot';
      st.textContent =
        'html{scroll-behavior:smooth}' +
        '@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}';
      (document.head || document.documentElement).appendChild(st);
    }
    chen();
    setTimeout(chen, 400);
    setTimeout(chen, 1200);
    setTimeout(chen, 2500);
  })();

  /* ---------- Gỡ liên kết chết "Design System ←" ----------
     Bộ soạn thảo để lại một liên kết chân trang trỏ tới
     "Design System 8 Landing Page.dc.html" — file không có trong gói phát
     hành, bấm vào là 404. Đo ngày 11/09/2026: có trên cả 8 trang, hiện rõ
     58x68 px ở chân trang chứ không phải ẩn.

     Nó đứng trong hàng ba liên kết cùng "GitHub ↗" và "Portfolio ↗"; hai cái
     kia trả 200. Gỡ hẳn thay vì giữ lại chữ — một nhãn không dẫn đi đâu nằm
     giữa hàng liên kết thì khó hiểu hơn là không có. */
  (function () {
    function go() {
      var ds = document.querySelectorAll('a[href]');
      for (var i = ds.length - 1; i >= 0; i--) {
        if ((ds[i].getAttribute('href') || '').indexOf('.dc.html') !== -1) {
          ds[i].parentNode.removeChild(ds[i]);
        }
      }
    }
    go();
    setTimeout(go, 700);
    setTimeout(go, 1800);
  })();

  /* ---------- Lưới an toàn cho reveal theo cuộn ----------
     Cả 8 trang đặt .xx-rv{opacity:0} rồi chờ JS gắn .xx-in. Nội dung vì thế
     phụ thuộc vào JS chạy trót lọt. Trang đã chặn trường hợp thiếu
     IntersectionObserver, nhưng không chặn trường hợp IO có mà không bắn, hay
     script chết trước khi gắn observer — khi đó 23-34 khối nằm lại opacity:0
     và trang trông như hỏng. Khung xem trước của tôi đúng là như vậy: có IO,
     không bắn lần nào.

     Lưới chỉ ra tay khi có bằng chứng cơ chế đã chết, chứ không ép hiện hết
     sau vài giây — làm thế là giết luôn hiệu ứng cuộn. */
  (function () {
    var CHO = 3000;

    function danhSach() {
      var ds = document.querySelectorAll('[class*="-rv"]');
      var out = [];
      for (var i = 0; i < ds.length; i++) {
        var m = (ds[i].className || '').match(/(?:^|\s)([a-z]{2,4})-rv(?:\s|$)/);
        if (m) out.push({ el: ds[i], tien: m[1] });
      }
      return out;
    }

    function trongKhungNhin(el) {
      var r = el.getBoundingClientRect();
      var cao = window.innerHeight || document.documentElement.clientHeight || 0;
      if (!cao) return false;
      return r.top < cao && r.bottom > 0 && r.width > 0 && r.height > 0;
    }

    /* chiDoan = chỉ chẩn đoán, không sửa gì. */
    function kiem(chiDoan) {
      var ds = danhSach();
      if (!ds.length) return 'khong-co';

      var daHien = false;
      for (var i = 0; i < ds.length; i++) {
        if (ds[i].el.classList.contains(ds[i].tien + '-in')) { daHien = true; break; }
      }
      if (daHien) return 'dang-chay';   /* cơ chế đang chạy, không đụng vào */

      var coTrongKhung = false;
      for (var j = 0; j < ds.length; j++) {
        if (trongKhungNhin(ds[j].el)) { coTrongKhung = true; break; }
      }
      if (!coTrongKhung) return 'chua-cuon-toi';

      if (chiDoan) return 'hong';

      /* Có phần tử nằm trong khung nhìn mà vẫn chưa được hiện -> cơ chế hỏng. */
      for (var k = 0; k < ds.length; k++) {
        ds[k].el.classList.add(ds[k].tien + '-in');
      }
      if (window.console && console.warn) {
        console.warn('[shim] reveal theo cuộn không chạy — đã hiện ' + ds.length +
                     ' khối nội dung để trang không bị trắng.');
      }
    }

    /* Xác nhận hai nhịp. Trang nặng 350-660 KB và phải hydrate React; trên
       máy yếu 3 giây có thể chưa đủ. Bắn nhầm thì mất hiệu ứng cuộn, nên
       chỉ ra tay khi lần kiểm thứ hai vẫn thấy hỏng. Trường hợp hỏng thật
       thì nội dung vốn đã vô hình, chờ thêm 2 giây không mất gì. */
    setTimeout(function () {
      if (kiem(true) !== 'hong') return;
      setTimeout(function () {
        if (kiem(true) === 'hong') kiem();
      }, 2000);
    }, CHO);
  })();

  /* ---------- Nâng tương phản cho nhãn số thứ tự ----------
     Đo ngày 10/09/2026 trên seosona-os: 5 số 01-05 cỡ 30px, rgb(36,26,61)
     trên nền rgb(22,15,41) = 1.14:1, gần như vô hình. Mục đó tên là "Năm
     năng lực, xếp theo thứ tự chúng chạy" nên con số mang thông tin thật,
     không phải hoạ tiết.
     Giữ nguyên hue va do bao hoa, chi nang do sang toi khi dat 3:1 (nguong
     AA cho chu lon). Chi dung toi nhan hai chu so dang khong dat. */
  (function () {
    function soRGB(s) {
      var m = (s || '').match(/[\d.]+/g);
      return m ? m.slice(0, 3).map(Number) : null;
    }
    function sang(c) {
      var f = c.map(function (v) {
        v /= 255;
        return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
      });
      return 0.2126 * f[0] + 0.7152 * f[1] + 0.0722 * f[2];
    }
    function tyLe(a, b) {
      var x = sang(a), y = sang(b);
      return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05);
    }
    function nenCua(el) {
      var e = el;
      while (e) {
        var cs = getComputedStyle(e);
        if (cs.backgroundImage && cs.backgroundImage !== 'none') return null;
        var p = soRGB(cs.backgroundColor);
        if (p && cs.backgroundColor.indexOf('rgba(0, 0, 0, 0)') === -1 &&
            cs.backgroundColor !== 'transparent') return p;
        e = e.parentElement;
      }
      return [255, 255, 255];
    }
    /* RGB -> HSL -> RGB, chỉ để đổi mỗi độ sáng. */
    function rgb2hsl(c) {
      var r = c[0] / 255, g = c[1] / 255, b = c[2] / 255;
      var mx = Math.max(r, g, b), mn = Math.min(r, g, b), d = mx - mn;
      var l = (mx + mn) / 2, h = 0, s = 0;
      if (d) {
        s = l > 0.5 ? d / (2 - mx - mn) : d / (mx + mn);
        h = mx === r ? (g - b) / d + (g < b ? 6 : 0)
          : mx === g ? (b - r) / d + 2 : (r - g) / d + 4;
        h /= 6;
      }
      return [h, s, l];
    }
    function hsl2rgb(h, s, l) {
      function q(p, q2, t) {
        if (t < 0) t += 1;
        if (t > 1) t -= 1;
        if (t < 1 / 6) return p + (q2 - p) * 6 * t;
        if (t < 1 / 2) return q2;
        if (t < 2 / 3) return p + (q2 - p) * (2 / 3 - t) * 6;
        return p;
      }
      if (!s) { var v = Math.round(l * 255); return [v, v, v]; }
      var b2 = l < 0.5 ? l * (1 + s) : l + s - l * s, a2 = 2 * l - b2;
      return [q(a2, b2, h + 1 / 3), q(a2, b2, h), q(a2, b2, h - 1 / 3)]
        .map(function (v) { return Math.round(v * 255); });
    }

    function sua() {
      var ds = document.querySelectorAll('body *');
      for (var i = 0; i < ds.length; i++) {
        var el = ds[i];
        if (el.children.length) continue;
        var t = (el.textContent || '').trim();
        if (!/^\d{2}$/.test(t)) continue;              /* chỉ nhãn hai chữ số */
        if (el.dataset.tuongPhanDaSua) continue;

        var cs = getComputedStyle(el);
        var fg = soRGB(cs.color), nen = nenCua(el);
        if (!fg || !nen) continue;
        var co = parseFloat(cs.fontSize) || 16;
        var dam = parseInt(cs.fontWeight, 10) || 400;
        var can = (co >= 24 || (co >= 18.66 && dam >= 700)) ? 3 : 4.5;
        if (tyLe(fg, nen) >= can) continue;

        /* Nền tối thì kéo sáng lên, nền sáng thì kéo tối xuống. */
        var hsl = rgb2hsl(fg), toi = sang(nen) < 0.18;
        var lo = hsl[2], hi = toi ? 1 : 0, moi = null;
        for (var k = 0; k < 30; k++) {
          var mid = (lo + hi) / 2;
          var thu = hsl2rgb(hsl[0], hsl[1], mid);
          if (tyLe(thu, nen) < can + 0.05) { lo = mid; } else { hi = mid; moi = thu; }
        }
        if (!moi) continue;
        el.style.setProperty('color', 'rgb(' + moi.join(',') + ')', 'important');
        el.dataset.tuongPhanDaSua = '1';
      }
    }

    sua();
    setTimeout(sua, 800);
    setTimeout(sua, 1900);
  })();

  /* ---------- Gỡ nút đổi ngôn ngữ VI/EN ----------
     Đo trên 4 trang: bấm EN không đổi một chữ. Không có [data-i18n], không hàm
     i18n, và không có nội dung tiếng Anh ở đâu — 0 khối ẩn, 0 template, 0 dấu
     vết trong window.__resources. Nút lại đặt aria-pressed nên hứa với trình
     đọc màn hình rằng nó dùng được.
     Đặt lại thành false khi đã có bản tiếng Anh thật. */
  var GO_BO_NUT_NGON_NGU = true;

  (function () {
    if (!GO_BO_NUT_NGON_NGU) return;

    function isLangBtn(el) {
      var t = (el.textContent || '').trim();
      return (t === 'VI' || t === 'EN') && el.children.length === 0;
    }

    function strip() {
      var btns = [].slice.call(document.querySelectorAll('button, a'))
        .filter(isLangBtn);
      if (btns.length < 2) return;

      /* Gỡ cả khung bọc nếu khung đó chỉ chứa đúng mấy nút này — để không
         chừa lại một ô trống trong thanh điều hướng. */
      var parent = btns[0].parentElement;
      if (parent && parent.children.length === btns.length &&
          [].every.call(parent.children, isLangBtn)) {
        parent.remove();
      } else {
        btns.forEach(function (b) { b.remove(); });
      }
    }

    strip();
    setTimeout(strip, 600);
    setTimeout(strip, 1700);
  })();

  /* ---------- Nút lên đầu trang + nới khối giảm chuyển động ----------
     HTML và CSS thật nằm trong khối đã nén nên không sửa trực tiếp được; chèn
     ở đây vì shim chạy sau khi bộ giải nén thay thẻ <html>. */
  (function () {
    var CSS =
      '#__totop{position:fixed;right:18px;bottom:18px;z-index:9999;' +
      'width:46px;height:46px;display:grid;place-items:center;cursor:pointer;' +
      'border-radius:999px;border:1px solid;' +
      '-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);' +
      'opacity:0;transform:translateY(12px) scale(.9);pointer-events:none;' +
      'transition:opacity .28s cubic-bezier(.16,1,.3,1),' +
      'transform .28s cubic-bezier(.16,1,.3,1),border-color .2s}' +
      '#__totop.on{opacity:1;transform:none;pointer-events:auto}' +
      '#__totop:hover{transform:translateY(-3px)}' +
      '#__totop:active{transform:translateY(-1px) scale(.94)}' +
      '#__totop svg{width:20px;height:20px;display:block}' +
      '@media (max-width:640px){#__totop{right:12px;bottom:12px}}' +
      /* Giữ phản hồi hover/focus khi hệ điều hành bật giảm chuyển động.
         Chuẩn chỉ đòi bỏ thứ gây chóng mặt, không đòi bỏ hết phản hồi. */
      '@media (prefers-reduced-motion:reduce){' +
      'a,button,summary,label,input,select,textarea,[role=button],[tabindex],' +
      '[class*=btn],[class*=card],[class*=chip],[class*=tile]{' +
      'transition-duration:.12s!important}' +
      '#__totop{transition-duration:.12s!important}}';

    function injectCss() {
      if (document.getElementById('__totop_css') || !document.head) return;
      var st = document.createElement('style');
      st.id = '__totop_css';
      st.textContent = CSS;
      document.head.appendChild(st);
    }

    /* Màu nút phải tính từ nền thật. KHÔNG dùng color:inherit — <body> của các
       trang này để màu chữ mặc định là đen, màu thật nằm ở phần tử con, nên
       thừa hưởng sẽ ra mũi tên đen trên nền tối. */
    function pageBg() {
      var el = document.body;
      while (el) {
        var c = getComputedStyle(el).backgroundColor;
        if (c && c.indexOf('rgba(0, 0, 0, 0)') === -1 && c !== 'transparent') return c;
        el = el.parentElement;
      }
      return 'rgb(255,255,255)';
    }

    function isDark(c) {
      var m = (c.match(/[\d.]+/g) || [255, 255, 255]).map(Number);
      var f = m.slice(0, 3).map(function (v) {
        v /= 255;
        return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
      });
      return (0.2126 * f[0] + 0.7152 * f[1] + 0.0722 * f[2]) < 0.35;
    }

    function paint(b) {
      var dark = isDark(pageBg());
      b.style.color = dark ? '#f4f7f6' : '#14181c';
      b.style.background = dark ? 'rgba(255,255,255,.10)' : 'rgba(0,0,0,.055)';
      b.style.borderColor = dark ? 'rgba(255,255,255,.30)' : 'rgba(0,0,0,.20)';
    }

    function build() {
      if (document.getElementById('__totop') || !document.body) return;
      var b = document.createElement('button');
      b.id = '__totop';
      b.type = 'button';
      b.setAttribute('aria-label', 'Lên đầu trang');
      b.setAttribute('title', 'Lên đầu trang');
      b.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" ' +
        'aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>';
      paint(b);

      b.addEventListener('click', function () {
        var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
        window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
        var h = document.querySelector('h1');
        if (h) { h.setAttribute('tabindex', '-1'); h.focus({ preventScroll: true }); }
      });
      document.body.appendChild(b);

      /* Một classList.toggle quá rẻ để cần tiết lưu, mà requestAnimationFrame
         lại thêm một chỗ có thể không chạy. Đọc vị trí theo ba cách vì trình
         duyệt cũ đặt scrollTop ở nơi khác. */
      function pos() {
        return window.scrollY || document.documentElement.scrollTop ||
               document.body.scrollTop || 0;
      }
      function onScroll() { b.classList.toggle('on', pos() > 600); }
      addEventListener('scroll', onScroll, { passive: true });
      addEventListener('resize', onScroll, { passive: true });
      onScroll();

      /* SEOSONA UX-UI có công tắc sáng/tối — tính lại màu khi chủ đề đổi. */
      try {
        new MutationObserver(function () { paint(b); }).observe(
          document.documentElement, { attributes: true,
            attributeFilter: ['class', 'data-theme', 'style'] });
      } catch (e) {}
    }

    function go() { injectCss(); build(); }
    go();
    /* Bộ giải nén có thể xong sau shim — chạy lại cho chắc. */
    setTimeout(go, 500);
    setTimeout(go, 1600);
  })();

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
