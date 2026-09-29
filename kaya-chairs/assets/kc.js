/* Kaya Chairs — prototype behaviour. Chair data is placeholder until real models arrive. */

const CHAIRS = [
  { id: 'rib-side', name: 'Rib Side Chair', type: 'dining', art: 'c-rib', badge: 'Bestseller', meta: 'Glass-fibre reinforced PP', tags: ['Stackable', 'Indoor / outdoor'],
    finishes: [['Anthracite', '#3B4150'], ['Sand', '#D9C7A7'], ['Olive', '#6F7458'], ['White', '#F2F0EA']] },
  { id: 'rib-arm', name: 'Rib Armchair', type: 'dining', art: 'c-arm', badge: '', meta: 'Glass-fibre reinforced PP', tags: ['Stackable', 'Indoor / outdoor'],
    finishes: [['Anthracite', '#3B4150'], ['Sand', '#D9C7A7'], ['Terracotta', '#B86B4B']] },
  { id: 'ege-bistro', name: 'Ege Bistro Chair', type: 'outdoor', art: 'c-bistro', badge: 'New', meta: 'Powder-coated aluminium, woven back', tags: ['Outdoor', 'UV resistant'],
    finishes: [['Navy', '#1E2B45'], ['Cream', '#EDE3D0'], ['Sage', '#9AA78F']] },
  { id: 'harbor-bar', name: 'Harbor Bar Stool', type: 'bar', art: 'c-stool', badge: '', meta: 'Steel frame, 75 cm seat height', tags: ['Bar height', 'Footrest'],
    finishes: [['Black', '#1C1C1C'], ['Walnut', '#6B4A34']] },
  { id: 'harbor-counter', name: 'Harbor Counter Stool', type: 'bar', art: 'c-stool', badge: '', meta: 'Steel frame, 65 cm seat height', tags: ['Counter height', 'Footrest'],
    finishes: [['Black', '#1C1C1C'], ['Walnut', '#6B4A34'], ['Sand', '#D9C7A7']] },
  { id: 'bosphorus-lounge', name: 'Bosphorus Lounge', type: 'lounge', art: 'c-lounge', badge: '', meta: 'Upholstered, solid beech legs', tags: ['Lobby', 'Hotel room'],
    finishes: [['Oat', '#DCCFB8'], ['Ink', '#27324A'], ['Rust', '#9C5438']] },
];
const TYPES = { dining: 'Dining', bar: 'Bar & counter', lounge: 'Lounge', outdoor: 'Outdoor' };

const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const art = (id, cls = 'art') => `<svg class="${cls}" viewBox="0 0 120 140" aria-hidden="true"><use href="#${id}"/></svg>`;
const icon = n => `<svg class="i" aria-hidden="true"><use href="#i-${n}"/></svg>`;

/* ---------- Quote list (kept for this browser session) ---------- */
const QKEY = 'kc-quote';
const readQuote = () => { try { return JSON.parse(sessionStorage.getItem(QKEY)) || []; } catch (e) { return []; } };
const writeQuote = list => { try { sessionStorage.setItem(QKEY, JSON.stringify(list)); } catch (e) {} updateCount(); };
const inQuote = id => readQuote().some(x => x.id === id);
function updateCount() {
  const n = readQuote().length;
  $$('.quote-count').forEach(el => { el.textContent = n; el.hidden = !n; });
}

/* ---------- Cards ---------- */
function card(c) {
  const on = inQuote(c.id);
  return `<li><article class="card" data-id="${c.id}">
    <div class="card-img" style="--tint:${c.finishes[0][1]}">${c.badge ? `<span class="badge">${esc(c.badge)}</span>` : ''}${art(c.art)}<span class="finish-name">${esc(c.finishes[0][0])}</span></div>
    <div class="card-row"><h3 class="h3">${esc(c.name)}</h3><span class="small muted">${TYPES[c.type]}</span></div>
    <p class="small muted">${esc(c.meta)}</p>
    <div class="tags">${c.tags.map(t => `<span class="tag">${esc(t)}</span>`).join('')}</div>
    <div class="card-row">
      <div class="swatches" role="group" aria-label="Colours for ${esc(c.name)}">${c.finishes.map(([n, hex], i) => `<button type="button" class="swatch" style="--tint:${hex}" data-i="${i}" aria-label="${esc(n)}" aria-pressed="${!i}"></button>`).join('')}</div>
      <button type="button" class="btn btn-line-dark add-btn" data-add="${c.id}" aria-pressed="${on}">${on ? `${icon('check')} In quote` : `${icon('plus')} Add to quote`}</button>
    </div>
  </article></li>`;
}

document.addEventListener('click', e => {
  const sw = e.target.closest('.swatch');
  if (sw) {
    const el = sw.closest('.card'), c = CHAIRS.find(x => x.id === el.dataset.id), i = +sw.dataset.i;
    $('.card-img', el).style.setProperty('--tint', c.finishes[i][1]);
    $('.finish-name', el).textContent = c.finishes[i][0];
    $$('.swatch', el).forEach((s, j) => s.setAttribute('aria-pressed', i === j));
    return;
  }
  const add = e.target.closest('[data-add]');
  if (add) {
    const el = add.closest('.card'), id = add.dataset.add;
    const finish = $('.swatch[aria-pressed=true]', el)?.getAttribute('aria-label') || '';
    let list = readQuote();
    if (list.some(x => x.id === id)) list = list.filter(x => x.id !== id);
    else list.push({ id, finish, qty: '' });
    writeQuote(list);
    const on = inQuote(id);
    add.setAttribute('aria-pressed', on);
    add.innerHTML = on ? `${icon('check')} In quote` : `${icon('plus')} Add to quote`;
    const st = $('#quoteStatus'); if (st) st.textContent = on ? `${CHAIRS.find(c => c.id === id).name} added to your quote.` : 'Removed from your quote.';
  }
});

/* ---------- Global ---------- */
function initGlobal() {
  const btn = $('#menuBtn'), menu = $('#mobileMenu');
  if (btn) {
    const set = open => { menu.hidden = !open; btn.setAttribute('aria-expanded', open); btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu'); $('use', btn).setAttribute('href', open ? '#i-close' : '#i-menu'); };
    btn.addEventListener('click', () => set(menu.hidden));
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && !menu.hidden) { set(false); btn.focus(); } });
  }
  // Ticker pause/play
  $$('.ticker').forEach(t => {
    const b = $('.ticker-toggle', t); if (!b) return;
    b.addEventListener('click', () => {
      const paused = t.classList.toggle('paused');
      b.setAttribute('aria-label', paused ? 'Play scrolling strip' : 'Pause scrolling strip');
      $('use', b).setAttribute('href', paused ? '#i-play' : '#i-pause');
    });
  });
  $$('.js-year').forEach(el => el.textContent = new Date().getFullYear());
  updateCount();
}

/* ---------- Home ---------- */
function initHome() {
  const el = $('#featured'); if (!el) return;
  el.innerHTML = ['rib-side', 'ege-bistro', 'harbor-bar', 'bosphorus-lounge'].map(id => card(CHAIRS.find(c => c.id === id))).join('');
}

/* ---------- Collection ---------- */
function initCollection() {
  const grid = $('#collectionGrid'); if (!grid) return;
  const chips = $$('.chip');
  const render = f => {
    chips.forEach(c => c.setAttribute('aria-pressed', c.dataset.f === f));
    const list = CHAIRS.filter(c => f === 'all' || c.type === f);
    grid.innerHTML = list.length ? list.map(card).join('') : `<li class="empty"><p class="h3">No chairs in this category yet</p></li>`;
    $('#resultCount').textContent = `${list.length} ${list.length === 1 ? 'model' : 'models'}`;
  };
  chips.forEach(c => c.addEventListener('click', () => { render(c.dataset.f); history.replaceState(null, '', c.dataset.f === 'all' ? location.pathname : '#' + c.dataset.f); }));
  const h = location.hash.slice(1);
  render(TYPES[h] ? h : 'all');
}

/* ---------- Quote & contact ---------- */
function renderQuoteList() {
  const box = $('#qlist'); if (!box) return;
  const list = readQuote();
  box.innerHTML = list.length ? list.map((q, i) => {
    const c = CHAIRS.find(x => x.id === q.id); if (!c) return '';
    const hex = (c.finishes.find(f => f[0] === q.finish) || c.finishes[0])[1];
    return `<div class="qitem" data-i="${i}">
      <span class="thumb" style="--tint:${hex}">${art(c.art)}</span>
      <span><strong>${esc(c.name)}</strong><br><span class="small muted">${esc(q.finish || c.finishes[0][0])}</span></span>
      <label class="sr" style="position:absolute;left:-9999px" for="qq${i}">Quantity for ${esc(c.name)}</label>
      <input id="qq${i}" type="number" min="1" inputmode="numeric" placeholder="Qty" value="${esc(q.qty)}">
      <button type="button" class="rm" aria-label="Remove ${esc(c.name)}">${icon('close')}</button>
    </div>`;
  }).join('') : `<p class="qempty">No chairs added yet. <a class="link" href="collection.html">Browse the collection ${icon('arrow')}</a> and tap "Add to quote", or describe what you need below.</p>`;
  $$('.qitem', box).forEach(row => {
    const i = +row.dataset.i;
    $('input', row).addEventListener('change', e => { const l = readQuote(); l[i].qty = e.target.value; writeQuote(l); });
    $('.rm', row).addEventListener('click', () => { const l = readQuote(); l.splice(i, 1); writeQuote(l); renderQuoteList(); });
  });
}

function validate(form) {
  const errors = [];
  $$('[required]', form).forEach(input => {
    const field = input.closest('.field');
    let msg = '';
    if (!input.value.trim()) msg = field.dataset.msg || 'This field is required.';
    else if (input.type === 'email' && !input.checkValidity()) msg = 'Enter an email like name@company.com.';
    field.classList.toggle('invalid', !!msg);
    input.setAttribute('aria-invalid', !!msg);
    $('.err', field).textContent = msg;
    if (msg) errors.push({ input, msg, label: $('label', field).textContent.replace('*', '').trim() });
  });
  return errors;
}

function initQuote() {
  const form = $('#quoteForm'); if (!form) return;
  renderQuoteList();
  const summary = $('.error-summary', form);
  // Clear an error as soon as it's fixed (while typing), so nothing shifts under the submit click
  $$('input,select,textarea', form).forEach(i => ['input', 'change'].forEach(ev => i.addEventListener(ev, () => { if (i.closest('.field.invalid')) validate(form); })));
  form.addEventListener('submit', e => {
    e.preventDefault();
    const errors = validate(form);
    if (errors.length) {
      summary.innerHTML = `<strong>Please fix ${errors.length} ${errors.length === 1 ? 'field' : 'fields'}:</strong><ul>${errors.map(er => `<li><a href="#${er.input.id}">${esc(er.label)}: ${esc(er.msg)}</a></li>`).join('')}</ul>`;
      summary.classList.add('show'); summary.focus(); return;
    }
    summary.classList.remove('show');
    const b = $('button[type=submit]', form); b.disabled = true; b.textContent = 'Sending…';
    setTimeout(() => { form.hidden = true; const s = $('#quoteSuccess'); s.classList.add('show'); s.focus(); writeQuote([]); }, 700);
  });
}

document.addEventListener('DOMContentLoaded', () => { initGlobal(); initHome(); initCollection(); initQuote(); });
