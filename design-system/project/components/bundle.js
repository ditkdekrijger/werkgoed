/* @ds-bundle: {"format":4,"namespace":"Werkgoed","components":[{"name":"Button"},{"name":"Tag"},{"name":"Badge"},{"name":"Icoon"},{"name":"Heading"},{"name":"Card"},{"name":"Streep"},{"name":"ProductKaart"},{"name":"BeroepKaart"},{"name":"Lichaamskaart"},{"name":"Werkdag"},{"name":"BeroepKiezer"}]} */
(function () {
  var React = window.React;
  var h = React.createElement;

  function cx() {
    return Array.prototype.slice.call(arguments).filter(Boolean).join(' ');
  }

  /* Lijniconen, 24-raster, lijn 1,5px, ronde uiteinden. Voorlopige set tot Werkgoed een eigen set heeft. */
  var ICONS = {
    las: ['M4 20l8.5-8.5', 'M12.5 11.5l2-2 2 2-2 2z', 'M18 3.5v3', 'M16.5 5h3', 'M20.5 9.5l-1.5.8', 'M14.5 3.2l.6 1.6'],
    straat: ['M10 3.5h4l4.5 15.5h-13z', 'M8.1 10h7.8', 'M6.9 14.5h10.2', 'M3 21h18'],
    bouw: ['M3 17.5h18', 'M5 17.5V15a7 7 0 0 1 14 0v2.5', 'M10 8.4V5.5h4v2.9', 'M8 20h8'],
    techniek: ['M14.6 4.2a4.2 4.2 0 0 0-5 5.4L3.8 15.4a1.9 1.9 0 0 0 2.7 2.7l5.8-5.8a4.2 4.2 0 0 0 5.4-5l-2.5 2.5-2.4-.5-.5-2.4z'],
    magazijn: ['M4 8l8-4 8 4v8l-8 4-8-4z', 'M4 8l8 4 8-4', 'M12 12v8', 'M8 6l8 4'],
    chauffeur: ['M12 4a8 8 0 1 0 0 16 8 8 0 1 0 0-16z', 'M12 10a2 2 0 1 0 0 4 2 2 0 1 0 0-4z', 'M12 14v6', 'M10.1 11.4L4.4 9.7', 'M13.9 11.4l5.7-1.7'],
    groen: ['M5 19c0-8 5.5-13 14-14 0 8.5-5 14-13.2 14z', 'M5 19l8-8'],
    schilder: ['M5 4h11v4H5z', 'M16 6h2.5v5H12v3', 'M11 14h2v6.5h-2z'],
    vonk: ['M12 3v4', 'M12 17v4', 'M3 12h4', 'M17 12h4', 'M5.6 5.6l2.8 2.8', 'M15.6 15.6l2.8 2.8', 'M5.6 18.4l2.8-2.8', 'M15.6 8.4l2.8-2.8'],
    hitte: ['M12 21c-3.9 0-6.5-2.6-6.5-6 0-3.5 2.5-5.3 3.5-8.5 1.5 1.5 2 3 2 4.5 1-1 1.5-2.5 1.5-4.5 3 2 6 5.5 6 8.5 0 3.4-2.6 6-6.5 6z'],
    regen: ['M7 14h10a3.5 3.5 0 0 0 .3-7A5.5 5.5 0 0 0 6.6 8.6 2.8 2.8 0 0 0 7 14z', 'M9 17.5l-1 2.5', 'M13 17.5l-1 2.5', 'M17 17.5l-1 2.5'],
    kou: ['M12 3v18', 'M4.2 7.5l15.6 9', 'M4.2 16.5l15.6-9', 'M9.5 4.5L12 6l2.5-1.5', 'M9.5 19.5L12 18l2.5 1.5'],
    zicht: ['M2.5 12s3.5-6 9.5-6 9.5 6 9.5 6-3.5 6-9.5 6-9.5-6-9.5-6z', 'M12 9.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 1 0 0-5z'],
    lawaai: ['M4 9h3l5-4v14l-5-4H4z', 'M16 9a4 4 0 0 1 0 6', 'M18.5 6.5a7.5 7.5 0 0 1 0 11'],
    stof: ['M4 9.5c2.2-1.2 4.6-1.8 8-1.8s5.8.6 8 1.8V12c0 4-3.6 7-8 7s-8-3-8-7z', 'M4 10.5L2 9', 'M20 10.5L22 9', 'M9 13h6', 'M10 16h4'],
    snijden: ['M3 21l10.5-10.5', 'M13.5 10.5L20 4c1 3.2-.1 6.2-3.2 8.3l-3.3-1.8z'],
    chemie: ['M9 3h6', 'M10 3v5l-5 9a2.5 2.5 0 0 0 2.2 3.8h9.6A2.5 2.5 0 0 0 19 17l-5-9V3', 'M7.4 14h9.2'],
    knielen: ['M7 4.5a1.5 1.5 0 1 0 3 0 1.5 1.5 0 1 0-3 0', 'M8.5 7.5l1.5 6h4.5l2.5 6', 'M10 13.5L6.5 20', 'M8.5 7.5L5 11', 'M3 20.5h18'],
    hoogte: ['M6 3v18', 'M14 3v18', 'M6 7h8', 'M6 12h8', 'M6 17h8', 'M18 6l2 2-2 2', 'M20 8h-3'],
    pijl: ['M5 12h14', 'M13 6l6 6-6 6'],
    check: ['M5 12.5l4.5 4.5L19 7.5'],
    levering: ['M2.5 6.5h11v9h-11z', 'M13.5 9.5h4l3 3.2v2.8h-7', 'M6.5 18.2a1.8 1.8 0 1 0 0-.1z', 'M16.5 18.2a1.8 1.8 0 1 0 0-.1z'],
    voorraad: ['M4 7.5l8-4 8 4v9l-8 4-8-4z', 'M4 7.5l8 4 8-4', 'M12 11.5v9', 'M8.5 14.5l1.5 1.5 3-3'],
    verzending: ['M3 7h11v8H3z', 'M6 10.5h5', 'M17 9l4 2-4 2', 'M21 11h-6'],
    klok: ['M12 3.5a8.5 8.5 0 1 0 0 17 8.5 8.5 0 1 0 0-17z', 'M12 7.5V12l3 2'],
    telefoon: ['M6.5 3.5h3l1.5 4-2 1.3a10 10 0 0 0 6.2 6.2l1.3-2 4 1.5v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 4.5 5.7a2 2 0 0 1 2-2.2z'],
    mail: ['M3.5 6h17v12h-17z', 'M3.5 6.5l8.5 6.5 8.5-6.5'],
    locatie: ['M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z', 'M12 7.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 1 0 0-5z'],
    zoek: ['M10.5 4a6.5 6.5 0 1 0 0 13 6.5 6.5 0 1 0 0-13z', 'M15.3 15.3L20 20'],
    wagen: ['M3 4h2.5l2.2 11h10.6l2-7.5H6.6', 'M9 19.2a1.3 1.3 0 1 0 0-.1z', 'M17 19.2a1.3 1.3 0 1 0 0-.1z'],
    account: ['M12 4a4 4 0 1 0 0 8 4 4 0 1 0 0-8z', 'M4.5 20.5a7.5 7.5 0 0 1 15 0'],
    menu: ['M4 7h16', 'M4 12h16', 'M4 17h16'],
    sluit: ['M6 6l12 12', 'M18 6L6 18'],
    omlaag: ['M6 9.5l6 6 6-6'],
    jas: ['M9 3.5L4.5 6 3 13l2.5.8V20.5h13v-6.7L21 13l-1.5-7L15 3.5', 'M9 3.5a3 3 0 0 0 6 0', 'M12 6.5v14'],
    broek: ['M6.5 3.5h11l1.5 17h-4.5L12 9.5l-2.5 11H5z', 'M6.5 6.5h11'],
    schoen: ['M3.5 6.5h5l1 6 9 2.5a2.5 2.5 0 0 1 2 2.4v1.1H3.5z', 'M3.5 15.5h17.5', 'M9.5 10.5l2-1', 'M10.2 12.6l2-1'],
    handschoen: ['M7 21v-5.5L4.5 12a1.6 1.6 0 0 1 2.4-2L9 12V5a1.5 1.5 0 0 1 3 0v5', 'M12 5.5V4a1.5 1.5 0 0 1 3 0v6', 'M15 5.5a1.5 1.5 0 0 1 3 0v8.5a7 7 0 0 1-2 5V21'],
    helm: ['M3 17.5h18', 'M5 17.5V15a7 7 0 0 1 14 0v2.5', 'M10 8.4V5.5h4v2.9'],
    voet: ['M8 21c-2.5 0-3.5-2.5-3-5.5S7 9 9 9s2.5 2 2.2 4.5-.7 4-1 5.5S9.5 21 8 21z', 'M11.5 5.2a1.2 1.2 0 1 0 0-.1z', 'M14.5 6.2a1 1 0 1 0 0-.1z', 'M16.8 8a.9.9 0 1 0 0-.1z', 'M18.5 10.2a.8.8 0 1 0 0-.1z'],
    advies: ['M4 5.5h16v10H10l-4.5 4v-4H4z', 'M8 9.5h8', 'M8 12h5']
  };

  function Icoon(p) {
    var paths = ICONS[p.naam] || ICONS.vonk;
    var size = p.size || 24;
    var label = p.label;
    return h('svg', {
      className: cx('wg-icoon', p.className), width: size, height: size, viewBox: '0 0 24 24', fill: 'none',
      stroke: 'currentColor', strokeWidth: p.stroke || 1.5, strokeLinecap: 'round', strokeLinejoin: 'round',
      role: label ? 'img' : undefined, 'aria-label': label || undefined, 'aria-hidden': label ? undefined : 'true', focusable: 'false'
    }, paths.map(function (d, k) { return h('path', { key: k, d: d }); }));
  }

  function Button(p) {
    var variant = p.variant || 'signal';
    var cls = cx('wg-btn', 'wg-btn-' + variant, p.className);
    var arrow = p.arrow === false ? null : h('span', { className: 'wg-btn-arrow', 'aria-hidden': 'true' }, '→');
    if (p.href) {
      return h('a', { className: cls, href: p.href, onClick: p.onClick }, p.children, arrow);
    }
    return h('button', { type: 'button', className: cls, onClick: p.onClick, disabled: p.disabled }, p.children, arrow);
  }

  function Tag(p) {
    return h('button', {
      type: 'button',
      className: cx('wg-tag', p.className),
      'aria-pressed': p.active ? 'true' : 'false',
      onClick: p.onClick
    }, p.dot ? h('span', { className: 'wg-tag-dot', 'aria-hidden': 'true' }) : null, p.children);
  }

  function Badge(p) {
    var tone = p.tone || 'vlam';
    return h('span', { className: cx('wg-badge', 'wg-badge-' + tone, p.className) },
      p.icoon ? h(Icoon, { naam: p.icoon, size: 16, stroke: 1.75 }) : null, p.children);
  }

  function Heading(p) {
    var size = p.size || 'h2';
    var tag = p.as || (size === 'display' || size === 'h1' || size === 'mega' ? 'h1' : size === 'h2' ? 'h2' : 'h3');
    var cls = cx('wg-heading', 'wg-' + size, p.className);
    var kids = [p.children];
    if (p.accent) {
      kids.push(' ');
      kids.push(h('mark', { key: 'accent', className: cx('wg-mark', p.tone === 'night' ? 'wg-mark-on-night' : '') }, p.accent));
    }
    return h.apply(null, [tag, { className: cls }].concat(kids));
  }

  function Card(p) {
    var tone = p.tone || 'sunken';
    var style = p.beroep ? { background: 'var(--beroep-' + p.beroep + ')' } : undefined;
    return h('div', { className: cx('wg-card', 'wg-card-' + tone, p.className), style: style }, p.children);
  }

  function Streep(p) {
    return h('div', { className: 'wg-streep', 'aria-hidden': 'true', style: { height: (p && p.height) || 16 } });
  }

  function ProductKaart(p) {
    var voorraad = p.voorraad;
    var foto = h('div', { className: 'wg-product-foto' },
      p.image ? h('img', { src: p.image, alt: '' }) : h('span', null, 'Productfoto uit de webshop'),
      p.badge ? h(Badge, { tone: 'vlam' }, p.badge) : null);
    var status = voorraad === undefined ? null : h('span', { className: cx('wg-voorraad', voorraad ? 'wg-voorraad-ok' : 'wg-voorraad-nee') },
      h('i', { 'aria-hidden': 'true' }), voorraad ? 'Uit voorraad leverbaar' : 'Niet op voorraad');
    return h('a', { className: 'wg-product', href: p.href || '#' },
      foto,
      h('div', { className: 'wg-product-body' },
        p.merk ? h('span', { className: 'wg-product-merk' }, p.merk) : null,
        h('h3', { className: 'wg-product-naam' }, p.naam),
        h('div', { className: 'wg-product-prijs' },
          h('span', { className: 'wg-price' }, p.prijsEx),
          h('span', { className: 'wg-product-incl' }, 'excl. btw' + (p.prijsIn ? ', ' + p.prijsIn + ' incl.' : ''))),
        status));
  }

  var RISICO_NAAM = { vonk: 'Vonken', hitte: 'Hitte', regen: 'Regen', kou: 'Kou', zicht: 'Zichtbaarheid', lawaai: 'Lawaai', stof: 'Stof en rook', snijden: 'Scherpe randen', chemie: 'Chemie', knielen: 'Knielen', hoogte: 'Hoogte' };

  function BeroepKaart(p) {
    var b = p.beroep || 'las';
    var style = { '--bk-tint': 'var(--beroep-' + b + ')', '--bk-deep': 'var(--beroep-' + b + '-deep)' };
    var risicos = (p.risicos || []).slice(0, 3);
    return h('a', { className: cx('wg-bk', p.className), href: p.href || '#', style: style },
      h('div', { className: 'wg-bk-top' },
        h('span', { className: 'wg-bk-icoon' }, h(Icoon, { naam: p.icoon || b, size: 28 })),
        h('span', { className: 'wg-bk-pijl', 'aria-hidden': 'true' }, '→')),
      h('h3', { className: 'wg-bk-naam' }, p.naam, h('span', { className: 'wg-bk-goed' }, 'goed')),
      p.regel ? h('p', { className: 'wg-bk-regel' }, p.regel) : null,
      risicos.length ? h('div', { className: 'wg-bk-risicos' }, risicos.map(function (r) {
        return h(Badge, { key: r, tone: 'risico', icoon: ICONS[r] ? r : null }, RISICO_NAAM[r] || r);
      })) : null);
  }

  /* Plaats van elk punt op het figuur, in procent van 200 x 440. */
  var ZONE_POS = { hoofd: [50, 2.8], ogen: [27, 9.1], gehoor: [73, 9.1], adem: [50, 17.5], romp: [50, 32], handen: [17, 53], benen: [40, 70], knieen: [61, 66], voeten: [63, 93.5] };

  function Figuur() {
    return h('svg', { viewBox: '0 0 200 440', 'aria-hidden': 'true', focusable: 'false' },
      h('circle', { cx: 100, cy: 40, r: 22, fill: 'currentColor' }),
      h('rect', { x: 62, y: 74, width: 76, height: 124, rx: 22, fill: 'currentColor' }),
      h('path', { d: 'M70 96 L40 226 M130 96 L160 226', stroke: 'currentColor', strokeWidth: 22, strokeLinecap: 'round', fill: 'none' }),
      h('path', { d: 'M82 188 L76 400 M118 188 L124 400', stroke: 'currentColor', strokeWidth: 26, strokeLinecap: 'round', fill: 'none' }),
      h('rect', { x: 48, y: 396, width: 40, height: 22, rx: 11, fill: 'currentColor' }),
      h('rect', { x: 112, y: 396, width: 40, height: 22, rx: 11, fill: 'currentColor' }));
  }

  function Lichaamskaart(p) {
    var zones = p.zones || [];
    var st = React.useState(p.defaultIndex || 0);
    var i = st[0];
    var setI = st[1];
    var b = p.beroep;
    var style = b ? { '--lk-tint': 'var(--beroep-' + b + ')', '--lk-deep': 'var(--beroep-' + b + '-deep)' } : undefined;
    return h('div', { className: cx('wg-lk', p.className), style: style },
      h('div', { className: 'wg-lk-stage' },
        h('div', { className: 'wg-lk-fig' },
          h(Figuur),
          zones.map(function (z, k) {
            var pos = ZONE_POS[z.zone] || [50, 50];
            return h('button', {
              key: z.zone + k, type: 'button', className: 'wg-lk-pin', style: { left: pos[0] + '%', top: pos[1] + '%' },
              'aria-pressed': k === i ? 'true' : 'false', 'aria-label': (k + 1) + ', ' + z.titel, onClick: function () { setI(k); }
            }, k + 1);
          }))),
      h('ol', { className: 'wg-lk-list' }, zones.map(function (z, k) {
        var open = k === i;
        return h('li', { key: z.zone + k, className: 'wg-lk-item' },
          h('button', { type: 'button', className: 'wg-lk-row', 'aria-expanded': open ? 'true' : 'false', onClick: function () { setI(k); } },
            h('span', { className: 'wg-lk-num', 'aria-hidden': 'true' }, k + 1),
            h('span', { className: 'wg-lk-titel' }, z.titel),
            h('span', { className: 'wg-lk-plus', 'aria-hidden': 'true' }, open ? '−' : '+')),
          open ? h('div', { className: 'wg-lk-detail' },
            h('p', { className: 'wg-lk-eis' }, z.eis),
            z.product ? h('div', { className: 'wg-lk-product' }, h('span', null, 'Wij pakken erbij'), h('span', null, z.product)) : null,
            (z.normen && z.normen.length) ? h('div', { className: 'wg-dag-chips' }, z.normen.map(function (n) { return h(Badge, { key: n, tone: 'norm' }, n); })) : null) : null);
      })));
  }

  function Werkdag(p) {
    var b = p.beroep;
    var style = b ? { '--dag-deep': 'var(--beroep-' + b + '-deep)' } : undefined;
    return h('ol', { className: cx('wg-dag', p.className), style: style }, (p.momenten || []).map(function (m, k) {
      return h('li', { key: m.tijd + k, className: 'wg-dag-item' },
        h('span', { className: 'wg-dag-tijd' }, m.tijd),
        h('div', { className: 'wg-dag-body' },
          h('h3', { className: 'wg-dag-titel' }, m.titel),
          m.tekst ? h('p', { className: 'wg-dag-tekst' }, m.tekst) : null,
          h('div', { className: 'wg-dag-chips' },
            (m.risicos || []).map(function (r) { return h(Badge, { key: 'r' + r, tone: 'risico', icoon: ICONS[r] ? r : null }, RISICO_NAAM[r] || r); }),
            (m.goed || []).map(function (g) { return h(Badge, { key: 'g' + g, tone: 'outline', icoon: 'check' }, g); }))));
    }));
  }

  function BeroepKiezer(p) {
    var list = p.beroepen || [];
    var st = React.useState(p.defaultIndex || 0);
    var i = st[0];
    var setI = st[1];
    var b = list[i] || list[0];
    if (!b) return null;
    var tint = b.beroep ? { '--kz-tint': 'var(--beroep-' + b.beroep + ')' } : undefined;
    return h('div', { className: 'wg-kiezer' },
      h('div', { className: 'wg-kiezer-tags', role: 'group', 'aria-label': 'Kies je beroep' },
        list.map(function (x, k) {
          return h(Tag, { key: x.naam, active: k === i, dot: true, onClick: function () { setI(k); } }, x.naam);
        })),
      h('div', { className: 'wg-kiezer-panels' },
        h('div', { className: 'wg-kiezer-vraag wg-night' },
          h('span', { className: 'wg-label' }, 'dit wordt gevraagd bij'),
          h('h3', { className: 'wg-heading wg-h1' }, b.naam),
          h('p', { className: 'wg-lead' }, b.regel),
          h('ul', { className: 'wg-kiezer-eisen' },
            (b.eisen || []).map(function (e) { return h('li', { key: e }, e); }))),
        h('div', { className: 'wg-kiezer-pakket', style: tint },
          h('span', { className: 'wg-label' }, 'dit pakken wij erbij'),
          h('ul', { className: 'wg-kiezer-links' },
            (b.pakket || []).map(function (n) {
              return h('li', { key: n }, h('a', { href: '#' }, h('span', null, n), h('span', { 'aria-hidden': 'true' }, '→')));
            })),
          h(Button, { href: b.href || p.href || '#' }, p.knop || 'Bekijk het hele assortiment'))));
  }

  window.Werkgoed = window.Werkgoed || {};
  Object.assign(window.Werkgoed, {
    Button: Button, Tag: Tag, Badge: Badge, Icoon: Icoon, Heading: Heading, Card: Card, Streep: Streep,
    ProductKaart: ProductKaart, BeroepKaart: BeroepKaart, Lichaamskaart: Lichaamskaart, Werkdag: Werkdag, BeroepKiezer: BeroepKiezer
  });
})();
