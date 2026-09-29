/* Kaya site — shared behaviour (draft). Product data is placeholder. */

const PRODUCTS = [
  { id: 'arden-sofa', name: 'Arden Sofa', cat: 'living', material: 'fabric', art: 'sofa', vb: '0 0 200 110', meta: 'Linen · solid oak · 3-seater', badge: 'New', finishes: [['Natural linen', '#E9E4D8'], ['Charcoal', '#3A3A3A'], ['Sand', '#D8CBB4']], dims: [['Width', '220 cm'], ['Depth', '95 cm'], ['Height', '78 cm'], ['Seat height', '44 cm']] },
  { id: 'lune-lounge', name: 'Lune Lounge Chair', cat: 'living', material: 'fabric', art: 'lounge', vb: '0 0 200 110', meta: 'Bouclé · walnut legs', badge: '', finishes: [['Ivory bouclé', '#F1EEE6'], ['Stone', '#BDB8AE']], dims: [['Width', '78 cm'], ['Depth', '82 cm'], ['Height', '74 cm'], ['Seat height', '40 cm']] },
  { id: 'halo-side', name: 'Halo Side Table', cat: 'living', material: 'stone', art: 'side', vb: '0 0 120 130', meta: 'Travertine top · steel base', badge: '', finishes: [['Travertine', '#E4D9C6'], ['Black marble', '#1E1E1E']], dims: [['Diameter', '50 cm'], ['Height', '55 cm']] },
  { id: 'sora-dining-table', name: 'Sora Dining Table', cat: 'dining', material: 'wood', art: 'table', vb: '0 0 200 110', meta: 'Solid oak · seats 6', badge: 'Bestseller', finishes: [['Natural oak', '#C9A87C'], ['Smoked oak', '#5B4634']], dims: [['Length', '200 cm'], ['Width', '95 cm'], ['Height', '75 cm']] },
  { id: 'rhea-chair', name: 'Rhea Dining Chair', cat: 'dining', material: 'wood', art: 'chair', vb: '0 0 120 130', meta: 'Ash wood · woven seat', badge: '', finishes: [['Natural ash', '#D9C4A0'], ['Black ash', '#222222']], dims: [['Width', '48 cm'], ['Depth', '52 cm'], ['Height', '80 cm'], ['Seat height', '46 cm']] },
  { id: 'noma-bed', name: 'Noma Bed Frame', cat: 'bedroom', material: 'fabric', art: 'bed', vb: '0 0 200 110', meta: 'Upholstered · king', badge: '', finishes: [['Oat', '#DCD2BF'], ['Graphite', '#474747']], dims: [['Width', '196 cm'], ['Length', '218 cm'], ['Headboard height', '105 cm']] },
  { id: 'ember-lamp', name: 'Ember Floor Lamp', cat: 'decor', material: 'metal', art: 'lamp', vb: '0 0 120 140', meta: 'Linen shade · brushed brass', badge: '', finishes: [['Brass', '#B9975B'], ['Black', '#1A1A1A']], dims: [['Shade diameter', '45 cm'], ['Height', '160 cm']] },
  { id: 'olea-planter', name: 'Olea Planter', cat: 'decor', material: 'stone', art: 'plant', vb: '0 0 120 140', meta: 'Hand-finished concrete', badge: '', finishes: [['Grey', '#A9A9A4'], ['Off-white', '#EFEDE7']], dims: [['Diameter', '40 cm'], ['Height', '45 cm']] },
];
const CATS = { living: 'Living', dining: 'Dining', bedroom: 'Bedroom', decor: 'Décor' };
const MATERIALS = { wood: 'Wood', fabric: 'Upholstery', stone: 'Stone', metal: 'Metal' };

const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const art = (p, cls = 'art') => `<svg class="${cls}" viewBox="${p.vb}" aria-hidden="true"><use href="#${p.art}"/></svg>`;

function productCard(p) {
  return `<li class="reveal"><a class="pcard" href="product.html?id=${p.id}">
    <div class="pcard-img card">${p.badge ? `<span class="badge">${esc(p.badge)}</span>` : ''}${art(p)}</div>
    <div class="pcard-meta"><h3 class="t-h3">${esc(p.name)}</h3><span class="t-small">From <span class="ph">[SAR —]</span></span></div>
    <div class="pcard-meta"><span class="t-small">${esc(p.meta)}</span><span class="swatches" aria-label="${p.finishes.length} finishes">${p.finishes.map(f => `<i style="background:${f[1]}"></i>`).join('')}</span></div>
  </a></li>`;
}

/* ---------- Global: nav, reveal, year ---------- */
function initGlobal() {
  const btn = $('#menuBtn'), menu = $('#mobileMenu');
  if (btn) {
    const set = open => {
      menu.hidden = !open;
      btn.setAttribute('aria-expanded', open);
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      $('use', btn).setAttribute('href', open ? '#i-close' : '#i-menu');
    };
    btn.addEventListener('click', () => set(menu.hidden));
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && !menu.hidden) { set(false); btn.focus(); } });
  }
  const nf = $('#newsletter');
  if (nf) nf.addEventListener('submit', e => {
    e.preventDefault();
    const input = $('input', nf);
    $('#nlStatus').textContent = input.checkValidity() && input.value ? 'Thanks — you’re on the list. (Draft: not connected yet.)' : 'Please enter a valid email address.';
  });
  $$('.js-year').forEach(el => el.textContent = new Date().getFullYear());
  observeReveal();
}
let io;
function observeReveal() {
  if (!('IntersectionObserver' in window)) { $$('.reveal').forEach(el => el.classList.add('in')); return; }
  io = io || new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .1 });
  $$('.reveal:not(.in)').forEach(el => io.observe(el));
}

/* ---------- Home ---------- */
function initHome() {
  const el = $('#featured');
  if (el) { el.innerHTML = PRODUCTS.slice(0, 4).map(productCard).join(''); observeReveal(); }
}

/* ---------- Catalog ---------- */
function initCatalog() {
  const grid = $('#catalogGrid'); if (!grid) return;
  const params = new URLSearchParams(location.search);
  const pre = params.get('cat');
  const catBox = $('#fCat'), matBox = $('#fMat');
  const count = (key, v) => PRODUCTS.filter(p => p[key] === v).length;
  catBox.innerHTML += Object.entries(CATS).map(([k, v]) => `<label class="check"><input type="checkbox" name="cat" value="${k}" ${pre === k ? 'checked' : ''}> ${v}<span class="t-small count">${count('cat', k)}</span></label>`).join('');
  matBox.innerHTML += Object.entries(MATERIALS).map(([k, v]) => `<label class="check"><input type="checkbox" name="mat" value="${k}"> ${v}<span class="t-small count">${count('material', k)}</span></label>`).join('');
  if (pre && CATS[pre]) $('#catalogTitle').textContent = CATS[pre];

  const render = () => {
    const cats = $$('input[name=cat]:checked').map(i => i.value);
    const mats = $$('input[name=mat]:checked').map(i => i.value);
    let list = PRODUCTS.filter(p => (!cats.length || cats.includes(p.cat)) && (!mats.length || mats.includes(p.material)));
    const sort = $('#sort').value;
    if (sort === 'az') list = [...list].sort((a, b) => a.name.localeCompare(b.name));
    if (sort === 'za') list = [...list].sort((a, b) => b.name.localeCompare(a.name));
    grid.innerHTML = list.length ? list.map(productCard).join('') : `<li class="empty card"><h3 class="t-h3">No pieces match these filters</h3><p class="t-body" style="margin:8px 0 24px">Try removing a filter.</p><button class="btn btn-ghost" type="button" id="clearEmpty">Clear filters</button></li>`;
    $('#resultCount').textContent = `${list.length} ${list.length === 1 ? 'piece' : 'pieces'}`;
    const ce = $('#clearEmpty'); if (ce) ce.addEventListener('click', clear);
    observeReveal();
  };
  const clear = () => { $$('.filters input').forEach(i => i.checked = false); $('#catalogTitle').textContent = 'All furniture'; render(); };
  $('#filters').addEventListener('change', render);
  $('#sort').addEventListener('change', render);
  $('#clearFilters').addEventListener('click', clear);
  const ft = $('#filtersToggle');
  ft.addEventListener('click', () => { const open = $('#filters').classList.toggle('open'); ft.setAttribute('aria-expanded', open); });
  render();
}

/* ---------- Product ---------- */
function initProduct() {
  const root = $('#pdp'); if (!root) return;
  const id = new URLSearchParams(location.search).get('id');
  const p = PRODUCTS.find(x => x.id === id) || PRODUCTS[0];
  document.title = `${p.name} — Kaya`;
  $$('.js-name').forEach(el => el.textContent = p.name);
  $('.js-cat').textContent = CATS[p.cat];
  $('.js-cat').href = `catalog.html?cat=${p.cat}`;
  $('.js-meta').textContent = p.meta;
  if (p.badge) { $('.js-badge').textContent = p.badge; $('.js-badge').hidden = false; }

  // Gallery: four placeholder "views" of the drawing
  const views = [['Front', 1, 0], ['Detail', 1.8, 0], ['Angle', 1, -8], ['Scale', .6, 0]];
  const main = $('#galleryMain');
  const show = i => {
    const [label, s, r] = views[i];
    main.innerHTML = `<svg class="art" viewBox="${p.vb}" role="img" aria-label="${esc(p.name)}, ${label.toLowerCase()} view" style="transform:scale(${s}) rotate(${r}deg)"><use href="#${p.art}"/></svg>`;
    $$('.thumb').forEach((t, j) => t.setAttribute('aria-pressed', i === j));
  };
  $('#thumbs').innerHTML = views.map(([label, s, r], i) => `<button type="button" class="thumb" aria-label="Show ${label.toLowerCase()} view" aria-pressed="false"><svg class="art" viewBox="${p.vb}" aria-hidden="true" style="transform:scale(${s}) rotate(${r}deg)"><use href="#${p.art}"/></svg></button>`).join('');
  $$('.thumb').forEach((t, i) => t.addEventListener('click', () => show(i)));
  show(0);

  // Finishes
  $('#finishes').innerHTML = p.finishes.map(([n, c], i) => `<label class="finish"><input type="radio" name="finish" value="${esc(n)}" ${i ? '' : 'checked'}><span><i style="background:${c}"></i>${esc(n)}</span></label>`).join('');
  const fl = $('#finishLabel');
  const syncFinish = () => fl.textContent = $('input[name=finish]:checked').value;
  $('#finishes').addEventListener('change', syncFinish); syncFinish();

  // Qty
  const q = $('#qty');
  const clamp = v => Math.max(1, Math.min(999, parseInt(v, 10) || 1));
  $('#qtyMinus').addEventListener('click', () => q.value = clamp(+q.value - 1));
  $('#qtyPlus').addEventListener('click', () => q.value = clamp(+q.value + 1));
  q.addEventListener('change', () => q.value = clamp(q.value));

  // Dimensions table
  $('#dims').innerHTML = p.dims.map(([k, v]) => `<tr><th scope="row">${k}</th><td>${v}</td></tr>`).join('');

  // CTAs carry the selection
  const link = base => `${base}?product=${encodeURIComponent(p.id)}&qty=${q.value}&finish=${encodeURIComponent($('input[name=finish]:checked').value)}`;
  $('#enquireBtn').addEventListener('click', () => location.href = link('contact.html'));
  $('#wholesaleBtn').addEventListener('click', () => location.href = link('wholesale.html'));

  // Related
  $('#related').innerHTML = PRODUCTS.filter(x => x.id !== p.id).sort((a, b) => (b.cat === p.cat) - (a.cat === p.cat)).slice(0, 4).map(productCard).join('');
  observeReveal();
}

/* ---------- Forms ---------- */
function validate(form) {
  const errors = [];
  $$('[required]', form).forEach(input => {
    const field = input.closest('.field');
    let msg = '';
    if (!input.value.trim()) msg = field.dataset.required || 'This field is required.';
    else if (input.type === 'email' && !input.checkValidity()) msg = 'Enter an email like name@company.com.';
    else if (input.type === 'number' && !input.checkValidity()) msg = 'Enter a quantity of 1 or more.';
    field.classList.toggle('invalid', !!msg);
    input.setAttribute('aria-invalid', !!msg);
    const err = $('.err', field); if (err) err.textContent = msg;
    if (msg) errors.push({ input, msg, label: $('label', field).textContent.replace('*', '').trim() });
  });
  return errors;
}
function wireForm(form, onSuccess) {
  const summary = $('.error-summary', form);
  $$('input,select,textarea', form).forEach(i => i.addEventListener('blur', () => {
    if (i.closest('.field.invalid')) validate(form); // re-check once the user has seen an error
  }));
  form.addEventListener('submit', e => {
    e.preventDefault();
    const errors = validate(form);
    if (errors.length) {
      summary.innerHTML = `<strong>Please fix ${errors.length} ${errors.length === 1 ? 'field' : 'fields'}:</strong><ul>${errors.map(er => `<li><a href="#${er.input.id}">${esc(er.label)}: ${esc(er.msg)}</a></li>`).join('')}</ul>`;
      summary.classList.add('show');
      summary.focus();
      return;
    }
    summary.classList.remove('show');
    const btn = $('button[type=submit]', form);
    btn.disabled = true; btn.textContent = 'Sending…';
    setTimeout(onSuccess, 700); // Draft: no backend yet
  });
}

function prefillFromQuery(form) {
  const q = new URLSearchParams(location.search);
  const p = PRODUCTS.find(x => x.id === q.get('product'));
  return { p, qty: q.get('qty'), finish: q.get('finish') };
}

function initWholesale() {
  const form = $('#quoteForm'); if (!form) return;
  const lines = $('#lines');
  const opts = PRODUCTS.map(p => `<option value="${p.id}">${esc(p.name)}</option>`).join('');
  let n = 0;
  const addLine = (pid = '', qty = '') => {
    n++;
    const row = document.createElement('div');
    row.className = 'line';
    row.innerHTML = `
      <div class="field"><label for="lp${n}">Product <span class="req">*</span></label><select id="lp${n}" required><option value="">Choose a piece</option>${opts}<option value="custom">Custom / not listed</option></select><span class="err"></span></div>
      <div class="field"><label for="lq${n}">Quantity <span class="req">*</span></label><input id="lq${n}" type="number" min="1" inputmode="numeric" required value="${esc(qty)}"><span class="err"></span></div>
      <button type="button" class="icon-btn remove" aria-label="Remove this product"><svg class="icon icon-sm"><use href="#i-close"/></svg></button>`;
    $('select', row).value = pid;
    $('.remove', row).addEventListener('click', () => { if ($$('.line', lines).length > 1) { row.remove(); $('select', lines).focus(); } });
    lines.appendChild(row);
    return row;
  };
  const { p, qty, finish } = prefillFromQuery(form);
  addLine(p ? p.id : '', qty || '');
  if (finish) $('#q-notes').value = `Finish: ${finish}`;
  $('#addLine').addEventListener('click', () => $('select', addLine()).focus());
  wireForm(form, () => { form.hidden = true; $('#quoteSuccess').classList.add('show'); $('#quoteSuccess').focus(); window.scrollTo({ top: $('#quoteSuccess').offsetTop - 120 }); });
}

function initContact() {
  const form = $('#contactForm'); if (!form) return;
  const { p, finish } = prefillFromQuery(form);
  if (p) { $('#c-subject').value = 'product'; $('#c-msg').value = `I'd like to know more about the ${p.name}${finish ? ` (${finish})` : ''}.`; }
  wireForm(form, () => { form.hidden = true; $('#contactSuccess').classList.add('show'); $('#contactSuccess').focus(); });
}

document.addEventListener('DOMContentLoaded', () => {
  initGlobal(); initHome(); initCatalog(); initProduct(); initWholesale(); initContact();
});
