/* In The Loop · motor do deck (v1)
   Monta cada <section class="itl">: grade, masthead, paginação, glows, logos, imagens embutidas,
   pedidos de imagem, coreografias dos componentes (odômetro, fluxo, prêmio, vencedor…).
   Ajusta títulos (linha por máscara, encolhe até caber) · animação de entrada (CSS padrão = estado final)
   · navegação · visão geral · notas · tela sempre ativa · verificação · PDF.
   Teclas: ← → espaço clique navegam · F tela cheia · G visão geral · N notas · R repete · V verifica · Home/End
   Endereço: #N abre o slide N · ?estatico sem animação · ?reserva simula máquina sem Helvetica Neue */
(function () {
  const AS = window.ITL_ASSETS || {};
  const IMAGENS = JSON.parse((document.getElementById('itl-imagens') || {}).textContent || '{}');
  const ANO = document.body.dataset.ano || '2026';
  const palco = document.getElementById('palco'), fit = document.getElementById('fit');
  const slides = [...palco.querySelectorAll('section.itl')];
  const $$ = (s, r) => [...(r || document).querySelectorAll(s)];
  const pad = n => String(n).padStart(2, '0');
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const el = (html) => { const t = document.createElement('template'); t.innerHTML = html.trim(); return t.content.firstChild; };
  const glow = (cls, img, inner) => el(`<div class="itl-glow ${cls}">${inner ? `<div><img src="${AS[img]}" alt=""></div>` : `<img src="${AS[img]}" alt="">`}</div>`);
  if (/[?&]reserva\b/.test(location.search)) document.documentElement.classList.add('reserva');

  /* ---------- montagem de cada slide ---------- */
  let nAbertura = 0;
  function monta(s, i) {
    s.id = 's' + (i + 1);
    s.querySelectorAll('img[data-src]').forEach(im => { im.src = IMAGENS[im.dataset.src] || ''; });
    s.querySelectorAll('[data-pedido]').forEach(p => { p.classList.add('itl-pedido'); if (!p.textContent.trim()) p.textContent = p.dataset.pedido; });
    s.querySelectorAll('.itl-pessoa .itl-foto>img,.itl-pessoa>img,.itl-pessoa>[data-pedido]').forEach(f => {
      if (!f.parentElement.classList.contains('itl-foto')) { const w = el('<div class="itl-foto"></div>'); f.replaceWith(w); w.append(f); }
    });
    s.querySelectorAll('.itl-figura>img,.itl-figura>[data-pedido]').forEach(f => { const w = el('<div></div>'); f.replaceWith(w); w.append(f); });
    if (!s.hasAttribute('data-limpo')) {
      s.prepend(el(`<div class="itl-grade">${Array.from({ length: 13 }, (_, k) => `<i style="left:${100 + k * 1720 / 12}px;--k:${k}"></i>`).join('')}</div>`));
      s.append(el(`<div class="itl-mast"><span>IN THE LOOP</span><span>${esc(ANO)}</span><img src="${AS.logoVolund}" alt=""></div>`));
      s.append(el(`<div class="itl-pg"><b>${pad(i + 1)}</b> — ${pad(slides.length)}</div>`));
    }
    /* componentes com cenografia própria */
    const capa = s.querySelector('.itl-capa');
    if (capa) {
      s.prepend(glow('itl-capa-shape', 'shape'));
      s.append(el(`<div class="itl-capa-logo l1"><img src="${AS.logoItl}" alt="In the loop"></div>`), el(`<div class="itl-capa-logo l2"><img src="${AS.logoItl}" alt=""></div>`), el(`<img class="itl-capa-volund" src="${AS.logoVolund}" alt="Volund">`));
    }
    const ab = s.querySelector('.itl-abertura');
    if (ab) {
      nAbertura++;
      s.prepend(glow('itl-shape', 'shape', true));
      s.append(el(`<img class="itl-logo-sm" src="${AS.logoItl}" alt="in the loop">`));
      const q = ab.querySelector('.itl-quem'); if (q) q.dataset.n = pad(nAbertura);
    }
    if (s.querySelector('.itl-fecho')) s.prepend(glow('itl-shape', 'shape', true));
    if (s.querySelector('.itl-citacao')) s.prepend(glow('infinito', 'infinito'));
    const pr = s.querySelector('.itl-premio');
    if (pr) {
      s.prepend(el('<div class="itl-fusivel"></div>'), glow('itl-anel e', 'anel', true), glow('itl-anel d', 'anel', true), el('<div class="itl-clarao"></div>'), el('<div class="itl-choque"><i style="--k:0"></i><i style="--k:1"></i><i style="--k:2"></i></div>'));
      pr.innerHTML = [...pr.textContent.trim()].map((c, k) => `<span style="--i:${k}">${c === ' ' ? '&nbsp;' : esc(c)}</span>`).join('');
      s.append(el(`<img class="itl-premio-logo" src="${AS.logoItl}" alt="in the loop">`));
    }
    const v = s.querySelector('.itl-vencedor');
    if (v) {
      const linha = Array(5).fill(esc(v.dataset.premio || '')).join(' ');
      [1, 2, 3, 4, 5, 6].forEach(k => v.prepend(el(`<div class="itl-eco" style="top:${145 + (k - 1) * 155}px;--k:${k};--de:${k % 2 ? -700 : 700}px;--para:${k % 2 ? 220 : -220}px">${linha}</div>`)));
      $$(':scope>b', v).forEach((b, k) => { b.classList.add('itl-cabe'); b.dataset.d = k ? '2.15' : '1.9'; });
      s.append(el(`<img class="itl-logo-sm" src="${AS.logoItl}" alt="in the loop">`), el(`<p class="itl-kicker itl-vencedor-k">${esc(v.dataset.premio || '')}</p>`));
    }
    s.querySelectorAll('.itl-agenda').forEach(a => {
      const at = parseInt(a.dataset.atual, 10), n = a.children.length;
      if (at > 0) [...a.children].forEach((li, k) => li.classList.toggle('apagado', k !== at - 1));
      const b = el('<i class="itl-agenda-barra"></i>'); b.style.setProperty('--atual', at > 0 ? at - 1 : 0); b.style.setProperty('--fim', `calc(${n - 1} * var(--rh))`); a.prepend(b);
    });
    s.querySelectorAll('.itl-polo').forEach((p, k) => p.style.setProperty('--k', k));
    s.querySelectorAll('.itl-fluxo').forEach(f => {
      const li = [...f.children]; f.style.setProperty('--n', li.length); li.forEach((x, k) => x.style.setProperty('--i', k));
      f.append(el('<i class="itl-pacote"></i>'));
    });
    s.querySelectorAll('.itl-barra').forEach((b, k) => {
      b.style.setProperty('--k', k);
      if (!b.querySelector('.trilho')) { const t = el('<div class="trilho"><i></i></div>'); const val = b.querySelector('b'); val ? b.insertBefore(t, val) : b.append(t); }
    });
    ['.itl-lista>li', '.itl-pessoa', '.itl-captura', '.itl-figura', '.itl-capa>li'].forEach(sel => s.querySelectorAll(sel).forEach((x, k) => x.style.setProperty('--k', k)));
    /* odômetro: inteiro de até 2 dígitos com data-de */
    s.querySelectorAll('.itl-numero[data-de]').forEach(n => {
      const m = n.textContent.trim().match(/^(\+?)(\d{1,2})(%?)$/); if (!m) return;
      const para = +m[2]; let de = parseInt(n.dataset.de, 10); if (!(de >= 0 && de < para)) de = 0;
      const tira = len => Array.from({ length: len }, (_, k) => `<span>${k % 10}</span>`).join('');
      const cols = para >= 10 ? [[Math.floor(de / 10), Math.floor(para / 10)], [de, para]] : [[de, para]];
      n.classList.add('itl-odometro'); n.removeAttribute('data-conta');
      n.innerHTML = (m[1] ? `<span>${m[1]}</span>` : '') + cols.map(([a, b]) => `<span class="itl-dg" style="--de:${a};--para:${b}"><span class="itl-strip">${tira(b + 1)}</span></span>`).join('') + (m[3] ? `<span>${m[3]}</span>` : '');
    });
    /* números que contam: data-conta (vazio = usa o próprio texto) */
    s.querySelectorAll('[data-conta]').forEach(n => { if (!n.dataset.conta) n.dataset.conta = n.textContent.trim(); });
    /* atrasos da animação genérica em ordem de leitura */
    let k = 0; s.querySelectorAll('[data-a],.itl-metrica,.itl-topico,.itl-apoio li,.itl-filete').forEach(x => { if (!x.style.getPropertyValue('--d')) x.style.setProperty('--d', (.15 + k++ * .09).toFixed(2) + 's'); });
  }

  /* ---------- ajuste de texto (antes da primeira exibição) ---------- */
  function palavras(raiz) {
    /* quebra o texto em palavras, preservando trechos destacados e <br> */
    const out = [];
    const anda = (n, cls) => [...n.childNodes].forEach(c => {
      if (c.nodeType === 3) {
        c.textContent.split(/(\s+)/).forEach(p => { if (!p) return; if (/^\s+$/.test(p)) out.push({ sp: 1 }); else out.push({ w: p, cls }); });
      } else if (c.nodeName === 'BR') out.push({ br: 1 });
      else if (c.nodeType === 1) anda(c, (c.className || 'itl-destaque') + (c.nodeName === 'EM' ? ' itl-destaque' : ''));
    });
    anda(raiz, '');
    return out;
  }
  function linhas(t) {
    const tk = palavras(t), max = +(t.dataset.linhas || 3), min = parseFloat(getComputedStyle(t).fontSize) * .5;
    let html = '', sp = false;
    tk.forEach(x => { if (x.br) { html += '<br>'; sp = false; } else if (x.sp) sp = true; else { html += (sp ? ' ' : '') + `<span class="w${x.cls ? ' ' + esc(x.cls) : ''}" data-g="${sp || !html ? 0 : 1}">${esc(x.w)}</span>`; sp = false; } });
    t.innerHTML = html;
    let fs = parseFloat(getComputedStyle(t).fontSize), grupos, guarda = 0;
    const mede = () => { grupos = []; let topo = null, atual = null; [...t.childNodes].forEach(n => {
      if (n.nodeName === 'BR') { atual = null; return; } if (n.nodeType !== 1) return;
      const cola = n.dataset.g === '1', y = n.offsetTop;
      if (atual === null || (!cola && Math.abs(y - topo) > 2)) { atual = []; grupos.push(atual); topo = y; }
      atual.push((atual.length && !cola ? ' ' : '') + `<span class="${n.className.replace(/^w ?/, '')}">${n.innerHTML}</span>`); }); };
    mede();
    while ((grupos.length > max || t.scrollWidth > t.clientWidth + 2) && fs > min && guarda++ < 40) { fs = Math.max(min, fs * .94); t.style.fontSize = fs + 'px'; mede(); }
    if (grupos.length > max || t.scrollWidth > t.clientWidth + 2) t.dataset.estouro = 'linhas';
    t.innerHTML = grupos.map((g, l) => `<span class="itl-ln"><span style="--l:${l}">${g.join('')}</span></span>`).join('');
  }
  const largura = e => { const r = document.createRange(); r.selectNodeContents(e); return r.getBoundingClientRect().width / escala(); };
  function cabe(e, maxw, minFrac) {
    let fs = parseFloat(getComputedStyle(e).fontSize); const min = fs * (minFrac || .45); let g = 0;
    while (largura(e) > maxw + 1 && fs > min && g++ < 60) { fs = Math.max(min, fs * .95); e.style.fontSize = fs + 'px'; }
    if (largura(e) > maxw + 2) e.dataset.estouro = 'largura';
  }
  const escala = () => { const m = getComputedStyle(fit).transform.match(/matrix\(([^,]+)/); return m ? parseFloat(m[1]) : 1; };
  function ajustaTexto(s) {
    s.querySelectorAll('[data-a=linhas],.itl-frase,.itl-fecho .itl-titulo').forEach(linhas);
    s.querySelectorAll('.itl-gigante,.itl-palavra,.itl-cabe,.itl-polo figcaption>b').forEach(e => {
      const maxw = parseFloat(getComputedStyle(e).maxWidth) || (e.parentElement.clientWidth || 1720);
      cabe(e, Math.min(maxw, e.closest('.itl-polo') ? 840 : 1752), .5);
      if (!e.querySelector('.itl-ln')) e.innerHTML = `<span class="itl-ln"><span style="--d:${e.dataset.d || .25}s">${e.innerHTML}</span></span>`;
    });
    s.querySelectorAll('.itl-numero').forEach(n => { const box = n.parentElement.clientWidth || 1720; cabe(n, box, .35); });
    /* números lado a lado ficam todos do tamanho do menor */
    s.querySelectorAll('.itl-metricas').forEach(g => {
      const ns = $$('.itl-metrica:not(.destaque) .itl-numero', g); if (ns.length < 2) return;
      const m = Math.min(...ns.map(n => parseFloat(getComputedStyle(n).fontSize))); ns.forEach(n => n.style.fontSize = m + 'px');
    });
    s.querySelectorAll('.itl-numeros').forEach(g => {
      const ns = $$('b', g); ns.forEach(n => cabe(n, n.parentElement.clientWidth - 8, .5));
      const m = Math.min(...ns.map(n => parseFloat(getComputedStyle(n).fontSize))); ns.forEach(n => n.style.fontSize = m + 'px');
    });
  }

  /* ---------- animações de JS: contagens e odômetro ---------- */
  let timers = [];
  function parseNum(s) { const m = String(s).match(/^([^\d]*)([\d.,]+)(.*)$/); if (!m) return null; return { pre: m[1], n: parseFloat(m[2].replace(/\./g, '').replace(',', '.')), dec: (m[2].split(',')[1] || '').length, suf: m[3], grp: /\./.test(m[2]) }; }
  function conta(s) {
    s.querySelectorAll('[data-conta]').forEach((e, k) => {
      const p = parseNum(e.dataset.conta); if (!p || isNaN(p.n)) return;
      const fmt = v => p.pre + v.toLocaleString('pt-BR', { minimumFractionDigits: p.dec, maximumFractionDigits: p.dec, useGrouping: p.grp }) + p.suf;
      e.textContent = fmt(0);
      const atraso = (parseFloat(getComputedStyle(e.closest('[style*="--d"]') || e).getPropertyValue('--d')) || .4) * 1000;
      timers.push(setTimeout(() => { const t0 = performance.now(); const passo = t => { const q = Math.min(1, (t - t0) / 1300); e.textContent = q < 1 ? fmt(p.n * (1 - Math.pow(1 - q, 3))) : e.dataset.conta; if (q < 1 && s.classList.contains('run')) requestAnimationFrame(passo); else e.textContent = e.dataset.conta; }; requestAnimationFrame(passo); }, atraso));
    });
    s.querySelectorAll('.itl-odometro').forEach(o => { o.classList.add('itl-pendente'); void o.offsetWidth; timers.push(setTimeout(() => o.classList.remove('itl-pendente'), 350)); });
  }
  function final() { timers.forEach(clearTimeout); timers = []; $$('[data-conta]').forEach(e => e.textContent = e.dataset.conta); $$('.itl-pendente').forEach(o => o.classList.remove('itl-pendente')); }
  const estatico = /[?&]estatico\b/.test(location.search);
  const tocar = s => { final(); s.classList.remove('run'); if (estatico) return; void s.offsetWidth; s.classList.add('run'); conta(s); };

  slides.forEach(monta);

  /* ---------- navegação ---------- */
  let atual = -1;
  function ajusta() {
    const k = Math.min(innerWidth / 1920, innerHeight / 1080);
    fit.style.transform = `translate(-50%,-50%) scale(${k})`;
    document.documentElement.style.setProperty('--kg', (Math.min(innerWidth - 80, 1760) / 4 - 24) / 1920);
  }
  function mostra(i, animar = true) {
    i = Math.max(0, Math.min(slides.length - 1, i));
    slides.forEach((s, j) => { s.classList.toggle('on', j === i); if (j !== i) s.classList.remove('run'); });
    if (i !== atual && animar) tocar(slides[i]);
    atual = i;
    history.replaceState(null, '', location.pathname + location.search + '#' + (i + 1));
    document.querySelector('#pg span').textContent = `${i + 1} / ${slides.length}`;
    const n = slides[i].querySelector('.itl-notas'); document.getElementById('notas').innerHTML = n ? n.innerHTML : '<em>Sem notas neste slide.</em>';
  }
  const visao = on => { document.body.classList.toggle('geral', on); if (on) final(); };
  addEventListener('keydown', e => {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    const k = e.key.toLowerCase();
    if (k === 'arrowright' || k === 'pagedown' || k === ' ' || k === 'arrowdown') { e.preventDefault(); mostra(atual + 1); }
    else if (k === 'arrowleft' || k === 'pageup' || k === 'arrowup') mostra(atual - 1);
    else if (k === 'home') mostra(0);
    else if (k === 'end') mostra(slides.length - 1);
    else if (k === 'f') document.fullscreenElement ? document.exitFullscreen() : document.documentElement.requestFullscreen().catch(() => {});
    else if (k === 'g' || k === 'escape') visao(k !== 'escape' && !document.body.classList.contains('geral'));
    else if (k === 'n') document.body.classList.toggle('com-notas');
    else if (k === 'r') tocar(slides[atual]);
    else if (k === 'v') { const p = verificar(); console.table(p); alert(p.length ? p.map(x => `Slide ${x.slide}: ${x.erro} — "${x.txt}"`).join('\n') : 'Tudo cabe: nenhum texto fora do container, da área ou do slide.'); }
  });
  fit.addEventListener('click', e => {
    if (document.body.classList.contains('geral')) { const s = e.target.closest('section.itl'); if (s) { visao(false); atual = -1; mostra(slides.indexOf(s)); } return; }
    mostra(e.clientX < innerWidth / 5 ? atual - 1 : atual + 1);
  });
  addEventListener('resize', ajusta);
  addEventListener('hashchange', () => { const n = parseInt(location.hash.slice(1), 10); if (n && n - 1 !== atual) mostra(n - 1); });

  /* ---------- verificação: todo texto dentro do slide, da área ou do seu componente ---------- */
  const CONTAINERS = '.itl-area,.itl-abertura,.itl-capa,.itl-citacao,.itl-polo,.itl-vencedor,.itl-fecho,.itl-metrica,.itl-topico,.itl-barra,.itl-pessoa,.itl-figura,.itl-fluxo li,.itl-numeros>div,.itl-apoio li,.itl-agenda li,.itl-col';
  const folhas = raiz => [...raiz.querySelectorAll('*')].filter(x => [...x.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()) && !x.closest('.itl-notas,.itl-mast,.itl-pg,.itl-pedido,.itl-eco,.itl-strip,.itl-premio,.itl-vencedor-k'));
  function verificar() {
    const probs = [], geral = document.body.classList.contains('geral');
    if (geral) visao(false);
    slides.forEach((s, i) => {
      const on = s.classList.contains('on'), run = s.classList.contains('run');
      s.classList.add('on'); s.classList.remove('run');
      const R = s.getBoundingClientRect();
      const fora = (a, b, tv = 1) => a.left < b.left - 1 || a.right > b.right + 1 || a.top < b.top - tv || a.bottom > b.bottom + tv;
      const add = (x, erro) => probs.push({ slide: i + 1, txt: x.textContent.trim().replace(/\s+/g, ' ').slice(0, 40), erro });
      s.querySelectorAll('[data-estouro]').forEach(x => add(x, 'título não cabe nem no menor tamanho'));
      folhas(s).forEach(x => {
        const rg = document.createRange(); rg.selectNodeContents(x); const r = rg.getBoundingClientRect(); if (!r.width) return;
        const tv = Math.max(2, parseFloat(getComputedStyle(x).fontSize) * .22 * (R.width / 1920));
        if (fora(r, R, tv)) return add(x, 'fora do slide');
        const c = x.parentElement.closest(CONTAINERS);
        if (!c) return add(x, 'texto solto (fora de itl-area ou de um componente)');
        const cr = c.getBoundingClientRect(), otico = x.closest('.itl-palavra,.itl-gigante') ? 24 * R.width / 1920 : 0; /* recuo óptico de propósito */
        if (fora(r, { left: cr.left - otico, right: cr.right, top: cr.top, bottom: cr.bottom }, tv)) add(x, 'fora do container ' + ([...c.classList].find(y => y.startsWith('itl-')) || c.tagName.toLowerCase()));
      });
      s.querySelectorAll('.itl-area').forEach(a => { if (a.scrollHeight > a.clientHeight + 2) add(a, 'conteúdo maior que a itl-area'); });
      s.classList.toggle('on', on); if (run) s.classList.add('run');
    });
    if (geral) visao(true);
    return probs;
  }

  /* ---------- tela sempre ativa ---------- */
  let trava = null; const luz = document.querySelector('#pg i');
  const marca = ok => { luz.className = ok ? 'ok' : 'falha'; luz.title = ok ? 'Tela sempre ativa' : 'A tela pode apagar: clique no slide'; };
  const acorda = async () => {
    if (!('wakeLock' in navigator)) return marca(false);
    try { if (!trava && document.visibilityState === 'visible') { trava = await navigator.wakeLock.request('screen'); marca(true); trava.addEventListener('release', () => { trava = null; marca(false); }); } } catch (_) { marca(false); }
  };
  addEventListener('click', acorda, true); addEventListener('keydown', acorda, true);
  document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible') acorda(); });
  document.addEventListener('fullscreenchange', acorda);

  /* PDF: tudo no estado final */
  addEventListener('beforeprint', () => { final(); slides.forEach(s => s.classList.remove('run')); });

  const fontes = document.fonts ? Promise.all([document.fonts.load('500 100px "DM Mono"'), document.fonts.load('500 100px "ITL Reserva"'), document.fonts.ready]).catch(() => {}) : Promise.resolve();
  const imgs = Promise.all($$('img').map(im => im.complete ? 0 : new Promise(r => { im.onload = im.onerror = r; })));
  Promise.all([fontes, imgs]).then(() => {
    ajusta();
    slides.forEach(s => { s.classList.add('on'); ajustaTexto(s); s.classList.remove('on'); });
    mostra((parseInt(location.hash.slice(1), 10) || 1) - 1); acorda();
  });
  window.ITL = { mostra, tocar, slides, visao, verificar };
})();
