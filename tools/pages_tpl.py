import json
from shared import IMG, MERK_LOGO, MENU_JS, BEROEPEN
from prod import p

KRUIMEL = '<nav aria-label="Kruimelpad" class="wg-small" style="color:var(--ink-muted);display:flex;flex-wrap:wrap;gap:8px">%s</nav>'


def kruimel(*items):
    out = []
    for i, (t, h) in enumerate(items):
        if h:
            out.append('<a class="wg-ul" href="%s">%s</a>' % (h, t))
        else:
            out.append('<span style="color:var(--ink)">%s</span>' % t)
        if i < len(items) - 1:
            out.append('<span aria-hidden="true">/</span>')
    return KRUIMEL % ''.join(out)


def ico(n, s=20):
    return '<x-import component-from-global-scope="Werkgoed.Icoon" naam="%s" size="%d"></x-import>' % (n, s)


LAT = '<div style="padding:0 var(--gutter)"><x-import component-from-global-scope="Werkgoed.Lat" height="{{latHoogte}}"></x-import></div>\n'


def script(h, init, data, body_js):
    return '''<script type="text/x-dc" data-dc-script data-props='{"menuOpen":{"editor":"boolean","default":false},"$preview":{"width":1440,"height":%d}}'>
class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = Object.assign({ menu: !!this.props.menuOpen }, %s);
  }
  renderVals() {
    const D = %s;
    const s = this.state;
    const eur = (n) => '€' + n.toFixed(2).replace('.', ',').replace(/\\B(?=(\\d{3})+(?!\\d))/g, '.');
%s
    return Object.assign({
      yes: true,
      no: false,
      latHoogte: 28,
%s    }, extra);
  }
}
</script>
</body>
</html>
''' % (h, json.dumps(init, ensure_ascii=False), json.dumps(data, ensure_ascii=False), body_js, MENU_JS)


# ------------------------------------------------------------------ Categorie
JASSEN = [
    {'id': 'havep', 'merk': 'Havep', 'naam': 'Gore-Tex jas Revolve 50468', 'prijsEx': 'Vanaf €379,95', 'prijsIn': '€459,74', 'foto': IMG['p-havep'], 'soort': 'Regenjas', 'beroepen': ['straat', 'chauffeur', 'groen', 'bouw'], 'kenner': True},
    p('snickers1112', soort='Winterjas', beroepen=['bouw', 'straat', 'techniek'], kenner=True),
    p('engel1871', soort='Winterjas', beroepen=['magazijn', 'chauffeur', 'bouw'], kenner=False),
    p('havep50171', soort='Regenjas', beroepen=['straat', 'groen', 'chauffeur'], kenner=False),
    p('dassynordix', soort='Winterjas', beroepen=['bouw', 'techniek', 'magazijn'], kenner=False),
    p('dassyaustin', soort='Winterjas', beroepen=['bouw', 'magazijn'], kenner=False),
    p('havep50461', soort='Softshell', beroepen=['techniek', 'chauffeur', 'bouw', 'schilder'], kenner=True),
    p('carthago', soort='Softshell', beroepen=['techniek', 'magazijn', 'chauffeur'], kenner=False),
    p('oxxapilot', soort='Winterjas', beroepen=['magazijn', 'chauffeur'], kenner=False),
    p('dassypulse', soort='Sweatjas', beroepen=['magazijn', 'techniek', 'schilder'], kenner=False),
    p('oxxawaldo', soort='Regenpak', beroepen=['groen', 'straat'], kenner=False),
    {'id': 'las', 'merk': '[MERK]', 'naam': 'Lasjas klasse 2 [VOORBEELD]', 'prijsEx': '€ [PRIJS]', 'prijsIn': '', 'foto': '', 'soort': 'Lasjas', 'beroepen': ['las'], 'kenner': True},
]
TIPS = {
    'las': 'Voor lassers raden wij laskleding aan die op spatten getest is. Klasse 2 bij elektrode, MAG en boven je hoofd lassen.',
    'straat': 'Langs de weg wil je gezien worden en droog blijven. Welke klasse signaalkleding je nodig hebt, zoeken wij met je uit.',
    'bouw': 'Op de bouw draag je laagjes: een softshell voor de wind, een regenjas in de bus, en zichtbaar waar de bouwplaats dat vraagt.',
    'techniek': 'Werk je bij spanning, kies dan een multinorm jas die op vlamboog getest is. Anders een softshell die meebeweegt.',
    'magazijn': 'Een lichte jas voor de hal, een thermojas voor de vriescel. Zichtbaar waar heftrucks rijden.',
    'chauffeur': 'Een jas die je snel aantrekt bij het lossen, met reflectie. Droog bij regen, niet te warm in de cabine.',
    'groen': 'Waterdicht en ademend, want je bent de hele dag buiten. Langs de berm met signaalkleding.',
    'schilder': 'Ademend en wasbaar. Wit, zodat je ziet waar je tegen natte verf zat.',
}
NAMEN = {b['k']: (b['naam'] + 'goed').capitalize() for b in BEROEPEN}
HREFS = {b['k']: b['href'] for b in BEROEPEN}

CATEGORIE_BODY = '''
<section style="padding:clamp(28px,3.5vw,48px) var(--gutter) 0;display:flex;flex-direction:column;gap:24px">
''' + kruimel(('Home', 'Main.dc.html'), ('Werkkleding', 'Categorie.dc.html'), ('Jassen', None)) + '''
<div style="display:flex;flex-wrap:wrap;gap:24px 48px;justify-content:space-between;align-items:flex-end">
<div style="display:flex;flex-direction:column;gap:20px;max-width:760px">
<h1 class="wg-heading" style="margin:0;font:800 clamp(52px,7vw,104px)/.92 var(--font-sans);font-variation-settings:'wdth' 82;letter-spacing:-.045em">Werkjassen</h1>
<p class="wg-lead" style="margin:0;max-width:44ch">Voor elk werk een andere jas. Kies je beroep, dan zetten wij bovenaan wat past.</p>
</div>
<div role="group" aria-label="Soort werkkleding" style="display:flex;flex-wrap:wrap;gap:8px">
<a class="wg-pill" href="Categorie.dc.html" style="display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 18px;border-radius:var(--radius-pill);background:var(--marine);color:var(--on-night);font:600 15px/1 var(--font-sans)">''' + ico('jas', 18) + '''Jassen</a>
<a class="wg-pill" href="Categorie.dc.html" style="display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 18px;border-radius:var(--radius-pill);border:1px solid var(--line-strong);font:600 15px/1 var(--font-sans)">''' + ico('broek', 18) + '''Broeken</a>
<a class="wg-pill" href="Categorie.dc.html" style="display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border-radius:var(--radius-pill);border:1px solid var(--line-strong);font:600 15px/1 var(--font-sans)">Overalls</a>
<a class="wg-pill" href="Categorie.dc.html" style="display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border-radius:var(--radius-pill);border:1px solid var(--line-strong);font:600 15px/1 var(--font-sans)">Shirts en truien</a>
<a class="wg-pill" href="Categorie.dc.html" style="display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border-radius:var(--radius-pill);border:1px solid var(--line-strong);font:600 15px/1 var(--font-sans)">Regenkleding</a>
</div>
</div>
</section>

<!-- beroepsfilter -->
<section style="margin:32px var(--gutter) 0;background:var(--canvas);border-radius:var(--radius-card);padding:clamp(20px,2.5vw,32px);display:flex;flex-direction:column;gap:18px">
<div style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:8px 24px">
<h2 class="wg-heading wg-h3" style="margin:0">Voor welk werk zoek je een jas?</h2>
<span class="wg-small" style="color:var(--ink-muted)">Wij zetten bovenaan wat bij jouw werk past.</span>
</div>
<div role="group" aria-label="Kies je beroep" style="display:flex;flex-wrap:wrap;gap:8px">
<sc-for list="{{beroepFilters}}" as="b" hint-placeholder-count="9">
<x-import component-from-global-scope="Werkgoed.Tag" active="{{b.active}}" dot="{{yes}}" on-click="{{b.pick}}">{{b.naam}}</x-import>
</sc-for>
</div>
<sc-if value="{{tip}}" hint-placeholder-val="{{no}}">
<div style="display:flex;flex-wrap:wrap;gap:16px 32px;align-items:center;justify-content:space-between;background:var(--surface);border-radius:var(--radius-tile);padding:18px 20px">
<div style="display:flex;gap:14px;align-items:flex-start;flex:1 1 420px">
<x-import component-from-global-scope="Werkgoed.Merkteken" size="36"></x-import>
<p class="wg-body" style="margin:0;max-width:70ch"><span style="font-weight:700">Tip van de kenner.</span> {{tip}}</p>
</div>
<a class="wg-ul" href="{{tipHref}}" style="font:600 16px/1.3 var(--font-sans);white-space:nowrap">Alles over {{tipNaam}} →</a>
</div>
</sc-if>
</section>

<!-- lijst met filters -->
<section style="padding:32px var(--gutter) clamp(56px,8vw,112px);display:flex;flex-wrap:wrap;gap:32px 40px;align-items:flex-start">
<aside aria-label="Filters" style="flex:0 1 260px;min-width:220px;display:flex;flex-direction:column;gap:28px">
<div style="display:flex;flex-direction:column;gap:12px">
<span class="wg-label" style="color:var(--ink-muted)">soort jas</span>
<div style="display:flex;flex-wrap:wrap;gap:8px">
<sc-for list="{{soortFilters}}" as="f" hint-placeholder-count="7">
<x-import component-from-global-scope="Werkgoed.Tag" active="{{f.active}}" on-click="{{f.pick}}">{{f.naam}}</x-import>
</sc-for>
</div>
</div>
<div style="display:flex;flex-direction:column;gap:12px">
<span class="wg-label" style="color:var(--ink-muted)">merk</span>
<sc-for list="{{merkFilters}}" as="m" hint-placeholder-count="5">
<label style="display:flex;align-items:center;gap:12px;min-height:36px;font:500 16px/1.2 var(--font-sans);cursor:pointer"><input type="checkbox" checked="{{m.active}}" onChange="{{m.pick}}" style="width:20px;height:20px;accent-color:#ff6a13;margin:0">{{m.naam}}</label>
</sc-for>
</div>
<x-import component-from-global-scope="Werkgoed.Waslabel" titel="hulp bij kiezen" regels="{{hulp}}" voet="Bel 0184-701212 of kom langs in de showroom."></x-import>
</aside>
<div style="flex:999 1 560px;min-width:0;display:flex;flex-direction:column;gap:20px">
<div style="display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:14px">
<span class="wg-body" style="font-weight:600">{{aantalTekst}}</span>
<span class="wg-small" style="display:flex;align-items:center;gap:8px;color:var(--ink-muted)"><x-import component-from-global-scope="Werkgoed.Zegel" size="28" id="uitleg" tekst="kennerskeuze"></x-import>Kennerskeuze: wat wij het vaakst adviseren</span>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:28px 16px">
<sc-for list="{{producten}}" as="p" hint-placeholder-count="9">
<x-import component-from-global-scope="Werkgoed.ProductKaart" merk="{{p.merk}}" naam="{{p.naam}}" prijs-ex="{{p.prijsEx}}" prijs-in="{{p.prijsIn}}" image="{{p.foto}}" kenner="{{p.kenner}}" href="Product.dc.html"></x-import>
</sc-for>
</div>
<sc-if value="{{leeg}}" hint-placeholder-val="{{no}}">
<p class="wg-lead" style="margin:0">Geen jassen met deze filters. Zet een filter uit, of bel ons, dan zoeken we het voor je uit.</p>
</sc-if>
</div>
</section>
'''

CATEGORIE_JS = '''    const beroepen = [{ k: '', naam: 'Alles' }].concat(D.beroepen);
    const soorten = ['Alles'].concat(D.jassen.map((p) => p.soort).filter((x, i, a) => a.indexOf(x) === i));
    const merken = D.jassen.map((p) => p.merk).filter((x, i, a) => x && x.indexOf('[') < 0 && a.indexOf(x) === i);
    let lijst = D.jassen.filter((p) => (s.soort === 'Alles' || p.soort === s.soort) && (!s.merken.length || s.merken.indexOf(p.merk) >= 0));
    if (s.beroep) lijst = lijst.filter((p) => p.beroepen.indexOf(s.beroep) >= 0).sort((a, b) => (b.kenner ? 1 : 0) - (a.kenner ? 1 : 0));
    const extra = {
      beroepFilters: beroepen.map((b) => ({ naam: b.naam, active: s.beroep === b.k, pick: () => this.setState({ beroep: b.k }) })),
      soortFilters: soorten.map((f) => ({ naam: f, active: s.soort === f, pick: () => this.setState({ soort: f }) })),
      merkFilters: merken.map((m) => ({ naam: m, active: s.merken.indexOf(m) >= 0, pick: () => this.setState({ merken: s.merken.indexOf(m) >= 0 ? s.merken.filter((x) => x !== m) : s.merken.concat([m]) }) })),
      tip: s.beroep ? D.tips[s.beroep] : '',
      tipNaam: s.beroep ? D.namen[s.beroep] : '',
      tipHref: s.beroep ? D.hrefs[s.beroep] : '#',
      producten: lijst,
      leeg: lijst.length === 0,
      aantalTekst: lijst.length + (lijst.length === 1 ? ' jas' : ' jassen'),
      hulp: D.hulp
    };'''

CATEGORIE = {
    'file': 'Categorie.dc.html', 'title': 'Werkgoed productlijst werkjassen', 'h': 3400, 'active': None,
    'body': CATEGORIE_BODY, 'init': {'beroep': '', 'soort': 'Alles', 'merken': []},
    'data': {'jassen': JASSEN, 'tips': TIPS, 'namen': NAMEN, 'hrefs': HREFS,
             'beroepen': [{'k': b['k'], 'naam': NAMEN[b['k']]} for b in BEROEPEN],
             'hulp': [{'label': 'Regen', 'waarde': 'Regenjas'}, {'label': 'Wind en kou', 'waarde': 'Softshell'}, {'label': 'Langs de weg', 'waarde': 'Signaaljas'}, {'label': 'Lassen', 'waarde': 'Lasjas'}, {'label': 'Spanning', 'waarde': 'Multinorm'}]},
    'js': CATEGORIE_JS,
}

# ------------------------------------------------------------------ Product
PRODUCT_BODY = '''
<section style="padding:clamp(28px,3.5vw,48px) var(--gutter) 0">
''' + kruimel(('Home', 'Main.dc.html'), ('Werkkleding', 'Categorie.dc.html'), ('Jassen', 'Categorie.dc.html'), ('Gore-Tex jas Revolve 50468', None)) + '''
</section>

<section style="padding:28px var(--gutter) clamp(56px,7vw,96px);display:flex;flex-wrap:wrap;gap:40px 56px;align-items:flex-start">
<!-- beeld -->
<div style="flex:1.2 1 520px;min-width:0;display:flex;flex-direction:column;gap:12px">
<div style="position:relative;aspect-ratio:1/1;background:var(--surface-sunken);border-radius:var(--radius-sheet);overflow:hidden;display:grid;place-items:center">
<img src="''' + IMG['p-havep'] + '''" alt="Gore-Tex jas Revolve 50468 van Havep in blauw" style="width:82%;height:82%;object-fit:contain;mix-blend-mode:multiply">
<div style="position:absolute;top:20px;right:20px"><x-import component-from-global-scope="Werkgoed.Zegel" size="112" id="product" tekst="kennerskeuze"></x-import></div>
</div>
<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px">
<div style="aspect-ratio:1/1;background:var(--surface-sunken);border-radius:var(--radius-tile);border:2px solid var(--ink);display:grid;place-items:center;overflow:hidden"><img src="''' + IMG['p-havep'] + '''" alt="" style="width:80%;height:80%;object-fit:contain;mix-blend-mode:multiply"></div>
<div style="aspect-ratio:1/1;border-radius:var(--radius-tile);overflow:hidden"><x-import component-from-global-scope="Werkgoed.FotoPlek" beroep="straat">Achterkant</x-import></div>
<div style="aspect-ratio:1/1;border-radius:var(--radius-tile);overflow:hidden"><x-import component-from-global-scope="Werkgoed.FotoPlek" beroep="chauffeur">Aan het werk</x-import></div>
</div>
</div>

<!-- koopblok -->
<div style="flex:1 1 400px;min-width:0;display:flex;flex-direction:column;gap:24px">
<div style="display:flex;flex-direction:column;gap:12px">
<img src="''' + MERK_LOGO['Havep'] + '''" alt="Havep" style="height:28px;width:auto;align-self:flex-start">
<h1 class="wg-heading" style="margin:0;font:800 clamp(36px,3.6vw,52px)/1 var(--font-sans);font-variation-settings:'wdth' 85;letter-spacing:-.035em">Gore-Tex jas Revolve 50468</h1>
<p class="wg-body" style="margin:0;color:var(--ink-muted)">Waterdicht en ademend. Voor wie de hele dag buiten werkt.</p>
</div>
<div style="display:flex;flex-direction:column;gap:4px">
<span style="font:800 40px/1 var(--font-sans);font-variation-settings:'wdth' 85;letter-spacing:-.02em">Vanaf €379,95 <span class="wg-small" style="color:var(--ink-muted)">excl. btw</span></span>
<span class="wg-small" style="color:var(--ink-muted)">€459,74 incl. btw</span>
</div>

<div style="display:flex;flex-direction:column;gap:10px">
<span class="wg-label" style="color:var(--ink-muted)">kleur: blauw</span>
<div style="display:flex;gap:10px"><span aria-label="Blauw, gekozen" role="img" style="width:40px;height:40px;border-radius:50%;background:#2b3f73;outline:2px solid var(--ink);outline-offset:3px"></span></div>
</div>

<div style="display:flex;flex-direction:column;gap:10px">
<div style="display:flex;justify-content:space-between;align-items:baseline"><span class="wg-label" style="color:var(--ink-muted)">maat: {{maat}}</span><a class="wg-ul" href="Showroom.dc.html" style="font:600 14px/1 var(--font-sans)">Twijfel je? Pas hem bij ons</a></div>
<div role="group" aria-label="Kies je maat" style="display:flex;flex-wrap:wrap;gap:8px">
<sc-for list="{{maten}}" as="m" hint-placeholder-count="7">
<x-import component-from-global-scope="Werkgoed.Tag" active="{{m.active}}" on-click="{{m.pick}}">{{m.naam}}</x-import>
</sc-for>
</div>
<span class="wg-small" style="color:var(--ink-muted)">[MATEN CONTROLEREN MET DE WEBSHOP]</span>
</div>

<div style="display:flex;flex-wrap:wrap;gap:12px;align-items:center">
<div style="display:flex;align-items:center;gap:6px;border:1px solid var(--line-strong);border-radius:var(--radius-pill);padding:2px">
<button class="wg-step" type="button" aria-label="Eén minder" onClick="{{minder}}" style="width:44px;height:44px;border-radius:50%;border:0;background:transparent;color:var(--ink);font:600 22px/1 var(--font-sans);cursor:pointer">−</button>
<span aria-live="polite" style="min-width:2ch;text-align:center;font:700 18px/1 var(--font-sans);font-variant-numeric:tabular-nums">{{aantal}}</span>
<button class="wg-step" type="button" aria-label="Eén meer" onClick="{{meer}}" style="width:44px;height:44px;border-radius:50%;border:0;background:transparent;color:var(--ink);font:600 22px/1 var(--font-sans);cursor:pointer">+</button>
</div>
<x-import component-from-global-scope="Werkgoed.Button" variant="signal" href="Winkelwagen.dc.html">In je winkelwagen</x-import>
</div>

<ul style="list-style:none;margin:0;padding:18px 0 0;border-top:1px solid var(--line);display:flex;flex-direction:column;gap:12px;font:500 15px/1.4 var(--font-sans)">
<li style="display:flex;gap:12px;align-items:center">''' + ico('verzending', 20) + '''Gratis verzending vanaf €100 excl. btw</li>
<li style="display:flex;gap:12px;align-items:center">''' + ico('levering', 20) + '''Snelle levering</li>
<li style="display:flex;gap:12px;align-items:center">''' + ico('locatie', 20) + '''Pas hem in de showroom in Hardinxveld-Giessendam</li>
<li style="display:flex;gap:12px;align-items:center">''' + ico('advies', 20) + '''Bestel je voor je ploeg? <a class="wg-ul" href="mailto:info@werkgoed.nl" style="font-weight:600">Vraag een offerte</a></li>
</ul>
</div>
</section>

<!-- waarom en specs -->
<section style="background:var(--surface-sunken);border-radius:var(--radius-sheet) var(--radius-sheet) 0 0;padding:clamp(56px,7vw,112px) var(--gutter);display:flex;flex-wrap:wrap;gap:40px 64px">
<div style="flex:1.4 1 480px;min-width:0;display:flex;flex-direction:column;gap:24px">
<span class="wg-label" style="color:var(--ink-muted)">waarom een kenner deze kiest</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="van binnen.">Droog van buiten, droog</x-import>
<p class="wg-lead" style="margin:0;max-width:46ch">Een Gore-Tex membraan houdt regen buiten en laat vocht van binnen naar buiten. Je wordt niet nat van de bui, en ook niet van je eigen zweet.</p>
<div style="display:flex;flex-direction:column;gap:12px">
<span class="wg-label" style="color:var(--ink-muted)">past bij</span>
<div style="display:flex;flex-wrap:wrap;gap:8px">
<a class="wg-pill" href="Straatgoed.dc.html" style="display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 16px 0 8px;border-radius:var(--radius-pill);background:var(--beroep-straat);font:600 15px/1 var(--font-sans);border:1px solid transparent"><span style="display:grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--surface);color:var(--beroep-straat-deep)">''' + ico('straat', 18) + '''</span>Straatgoed</a>
<a class="wg-pill" href="Chauffeursgoed.dc.html" style="display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 16px 0 8px;border-radius:var(--radius-pill);background:var(--beroep-chauffeur);font:600 15px/1 var(--font-sans);border:1px solid transparent"><span style="display:grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--surface);color:var(--beroep-chauffeur-deep)">''' + ico('chauffeur', 18) + '''</span>Chauffeursgoed</a>
<a class="wg-pill" href="Groengoed.dc.html" style="display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 16px 0 8px;border-radius:var(--radius-pill);background:var(--beroep-groen);font:600 15px/1 var(--font-sans);border:1px solid transparent"><span style="display:grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--surface);color:var(--beroep-groen-deep)">''' + ico('groen', 18) + '''</span>Groengoed</a>
<a class="wg-pill" href="Bouwgoed.dc.html" style="display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 16px 0 8px;border-radius:var(--radius-pill);background:var(--beroep-bouw);font:600 15px/1 var(--font-sans);border:1px solid transparent"><span style="display:grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--surface);color:var(--beroep-bouw-deep)">''' + ico('bouw', 18) + '''</span>Bouwgoed</a>
</div>
<span class="wg-small" style="color:var(--ink-muted)">[VOORBEELD] Door Werkgoed te controleren.</span>
</div>
</div>
<div style="flex:1 1 340px;min-width:0;max-width:440px">
<x-import component-from-global-scope="Werkgoed.Waslabel" titel="havep 50468" regels="{{specs}}" voet="Overige specificaties en wasvoorschrift overnemen uit de webshop."></x-import>
</div>
</section>

<!-- samen gekocht -->
<section style="padding:clamp(56px,7vw,112px) var(--gutter)">
<div style="display:flex;flex-direction:column;gap:24px;margin-bottom:40px">
<span class="wg-label" style="color:var(--ink-muted)">maak het af</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="samen gekocht.">Vaak</x-import>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:28px 16px">
<sc-for list="{{samen}}" as="p" hint-placeholder-count="3">
<x-import component-from-global-scope="Werkgoed.ProductKaart" merk="{{p.merk}}" naam="{{p.naam}}" prijs-ex="{{p.prijsEx}}" prijs-in="{{p.prijsIn}}" image="{{p.foto}}" voorraad="{{p.voorraad}}" href="Product.dc.html"></x-import>
</sc-for>
</div>
</section>

<!-- advies -->
<section style="padding:0 var(--gutter) clamp(56px,7vw,112px)">
<div style="background:var(--marine);color:var(--on-night);border-radius:var(--radius-sheet);overflow:hidden;display:flex;flex-wrap:wrap" class="wg-night">
<div style="flex:1 1 380px;min-width:0;padding:clamp(28px,4vw,56px);display:flex;flex-direction:column;gap:20px;justify-content:center">
<x-import component-from-global-scope="Werkgoed.Merkteken" size="44"></x-import>
<h2 class="wg-heading wg-h1" style="margin:0;font-size:clamp(32px,3.6vw,52px)">Vraag het een kenner.</h2>
<p class="wg-lead" style="margin:0;color:var(--on-night-muted);max-width:36ch">Welke maat, welke klasse, welke jas voor jouw ploeg. Bel of kom langs.</p>
<div style="display:flex;flex-wrap:wrap;gap:12px">
<x-import component-from-global-scope="Werkgoed.Button" variant="signal" href="tel:0184701212">Bel 0184-701212</x-import>
<x-import component-from-global-scope="Werkgoed.Button" variant="outline-light" arrow="{{no}}" href="Showroom.dc.html">Kom langs</x-import>
</div>
</div>
<div style="flex:1 1 380px;min-width:0;min-height:320px"><img class="wg-foto" src="''' + IMG['team'] + '''" alt="Het team van Werkgoed in de showroom"></div>
</div>
</section>
'''

PRODUCT_JS = '''    const extra = {
      maten: D.maten.map((m) => ({ naam: m, active: s.maat === m, pick: () => this.setState({ maat: m }) })),
      maat: s.maat || 'kies je maat',
      aantal: s.aantal,
      minder: () => this.setState({ aantal: Math.max(1, s.aantal - 1) }),
      meer: () => this.setState({ aantal: s.aantal + 1 }),
      specs: D.specs,
      samen: D.samen
    };'''

PRODUCT = {
    'file': 'Product.dc.html', 'title': 'Werkgoed productpagina Havep Gore-Tex jas', 'h': 3300, 'active': None,
    'body': PRODUCT_BODY, 'init': {'maat': 'L', 'aantal': 1},
    'data': {'maten': ['S', 'M', 'L', 'XL', 'XXL', '3XL'],
             'specs': [{'label': 'Merk', 'waarde': 'Havep'}, {'label': 'Artikel', 'waarde': '50468'}, {'label': 'Model', 'waarde': 'Revolve'},
                       {'label': 'Membraan', 'waarde': 'Gore-Tex'}, {'label': 'Kleur', 'waarde': 'Blauw'}, {'label': 'Normen', 'waarde': '[CONTROLEREN]'}],
             'samen': [p('havep10094'), {'merk': 'Werkhandschoenen', 'naam': 'Chauffeurshandschoenen 10419', 'prijsEx': 'Vanaf €2,99', 'prijsIn': '€3,62', 'foto': IMG['p-handschoen']},
                       {'merk': 'HAIX', 'naam': 'Black Eagle 50 Mid S3', 'prijsEx': 'Vanaf €148,68', 'prijsIn': '€179,90', 'foto': IMG['p-haix'], 'voorraad': True},
                       {'merk': 'Solid Gear', 'naam': 'Prime GTX S7S Mid BOA', 'prijsEx': 'Vanaf €305,50', 'prijsIn': '€369,66', 'foto': IMG['p-solidgear']}]},
    'js': PRODUCT_JS,
}

# ------------------------------------------------------------------ Merken
MERKEN = [
    ('HAIX', 'Schoenen'), ('LOWA Work', 'Schoenen'), ('Sixton', 'Schoenen'), ('Solid Gear', 'Schoenen'), ('Grisport Safety', 'Schoenen'),
    ('PUMA Safety', 'Schoenen'), ('Redbrick', 'Schoenen'), ('Snickers Workwear', 'Kleding'), ('Tricorp Workwear', 'Kleding'), ('Santino', 'Kleding'),
    ('Dassy', 'Kleding'), ('Havep', 'Kleding'), ('BLS', 'PBM'), ('KASK', 'PBM')]

MERKEN_BODY = '''
<section style="padding:clamp(28px,3.5vw,48px) var(--gutter) clamp(40px,5vw,72px);display:flex;flex-direction:column;gap:28px">
''' + kruimel(('Home', 'Main.dc.html'), ('Merken', None)) + '''
<div style="display:flex;flex-wrap:wrap;gap:24px 48px;justify-content:space-between;align-items:flex-end">
<h1 class="wg-heading" style="margin:0;font:800 clamp(52px,7vw,104px)/.92 var(--font-sans);font-variation-settings:'wdth' 82;letter-spacing:-.045em;max-width:12ch">Sterke merken. Wij kennen ze <mark class="wg-mark">allemaal.</mark></h1>
<p class="wg-lead" style="margin:0;max-width:36ch">Welke werkschoen valt ruim, welke jas houdt het langst. Dat weet je pas als je ze elke dag verkoopt.</p>
</div>
<div role="group" aria-label="Filter merken" style="display:flex;flex-wrap:wrap;gap:8px">
<sc-for list="{{filters}}" as="f" hint-placeholder-count="4">
<x-import component-from-global-scope="Werkgoed.Tag" active="{{f.active}}" on-click="{{f.pick}}">{{f.naam}}</x-import>
</sc-for>
</div>
</section>

<section style="padding:0 var(--gutter) clamp(56px,7vw,112px)">
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px">
<sc-for list="{{merken}}" as="m" hint-placeholder-count="14">
<a class="wg-tile" href="Categorie.dc.html" style="display:flex;flex-direction:column;justify-content:space-between;gap:28px;min-height:240px;padding:28px;box-sizing:border-box;border:1px solid var(--line);border-radius:var(--radius-card);background:var(--surface);transition:border-color .16s ease">
<div style="display:flex;justify-content:space-between;align-items:center;gap:12px">
<span style="display:inline-flex;align-items:center;gap:8px" class="wg-small"><x-import component-from-global-scope="Werkgoed.Icoon" naam="{{m.icoon}}" size="18"></x-import>{{m.soort}}</span>
<span aria-hidden="true" style="display:grid;place-items:center;width:40px;height:40px;border-radius:50%;border:1px solid var(--line-strong)">→</span>
</div>
<sc-if value="{{m.logo}}" hint-placeholder-val="{{yes}}">
<img src="{{m.logo}}" alt="{{m.naam}}" style="height:56px;width:auto;max-width:100%;object-fit:contain;object-position:left center;align-self:flex-start">
</sc-if>
<sc-if value="{{m.geenLogo}}" hint-placeholder-val="{{no}}">
<span style="font:800 40px/1 var(--font-sans);font-variation-settings:'wdth' 82;letter-spacing:-.04em">{{m.naam}}</span>
</sc-if>
<span class="wg-body" style="font-weight:600">Bekijk {{m.naam}}</span>
</a>
</sc-for>
</div>
</section>

<section style="padding:0 var(--gutter) clamp(56px,7vw,112px)">
<div style="background:var(--canvas);border-radius:var(--radius-sheet);padding:clamp(28px,4vw,56px);display:flex;flex-wrap:wrap;gap:32px 56px;align-items:center">
<div style="flex:1 1 360px;display:flex;flex-direction:column;gap:20px">
<span class="wg-label" style="color:var(--ink-muted)">onze eigen webshops</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="eigen winkel.">Een paar merken hebben bij ons een</x-import>
</div>
<ul style="flex:1 1 420px;list-style:none;margin:0;padding:0;display:flex;flex-direction:column">
<li style="border-top:1px solid var(--line)"><a class="wg-ul" href="#" style="display:flex;justify-content:space-between;gap:16px;padding:18px 0;font:700 24px/1.2 var(--font-sans);font-variation-settings:'wdth' 90">HAIX werkschoenen<span aria-hidden="true">→</span></a></li>
<li style="border-top:1px solid var(--line)"><a class="wg-ul" href="https://lowa-werkschoenen.nl/" style="display:flex;justify-content:space-between;gap:16px;padding:18px 0;font:700 24px/1.2 var(--font-sans);font-variation-settings:'wdth' 90">LOWA werkschoenen<span aria-hidden="true">→</span></a></li>
<li style="border-top:1px solid var(--line)"><a class="wg-ul" href="#" style="display:flex;justify-content:space-between;gap:16px;padding:18px 0;font:700 24px/1.2 var(--font-sans);font-variation-settings:'wdth' 90">Cofra werkschoenen<span aria-hidden="true">→</span></a></li>
<li style="border-top:1px solid var(--line);border-bottom:1px solid var(--line)"><a class="wg-ul" href="#" style="display:flex;justify-content:space-between;gap:16px;padding:18px 0;font:700 24px/1.2 var(--font-sans);font-variation-settings:'wdth' 90">BLS adembescherming<span aria-hidden="true">→</span></a></li>
</ul>
</div>
</section>
'''

MERKEN_JS = '''    const soorten = ['Alle', 'Schoenen', 'Kleding', 'PBM'];
    const icoon = { Schoenen: 'schoen', Kleding: 'jas', PBM: 'helm' };
    const extra = {
      filters: soorten.map((f) => ({ naam: f, active: s.soort === f, pick: () => this.setState({ soort: f }) })),
      merken: D.merken.filter((m) => s.soort === 'Alle' || m.soort === s.soort).map((m) => Object.assign({}, m, { icoon: icoon[m.soort], logo: D.logos[m.naam] || '', geenLogo: !D.logos[m.naam] }))
    };'''

MERKEN_PAGE = {
    'file': 'Merken.dc.html', 'title': 'Werkgoed merken', 'h': 2900, 'active': 'Merken',
    'body': MERKEN_BODY, 'init': {'soort': 'Alle'},
    'data': {'merken': [{'naam': n, 'soort': s} for n, s in MERKEN], 'logos': MERK_LOGO},
    'js': MERKEN_JS,
}

# ------------------------------------------------------------------ Showroom
SHOWROOM_BODY = '''
<section style="padding:clamp(28px,3.5vw,48px) var(--gutter) 0;display:flex;flex-direction:column;gap:28px">
''' + kruimel(('Home', 'Main.dc.html'), ('Showroom en voetscan', None)) + '''
<h1 class="wg-heading" style="margin:0;font:800 clamp(52px,8vw,124px)/.9 var(--font-sans);font-variation-settings:'wdth' 82;letter-spacing:-.045em">Pas het <mark class="wg-mark">bij ons.</mark></h1>
</section>
<section style="padding:clamp(28px,3vw,40px) var(--gutter) 0">
<div style="position:relative;aspect-ratio:16/7;border-radius:var(--radius-sheet);overflow:hidden;background:var(--canvas)">
<img class="wg-foto" src="''' + IMG['showroom'] + '''" alt="De showroom van Werkgoed met werkschoenen, werkkleding en een lange tafel">
<div style="position:absolute;left:clamp(16px,2vw,32px);bottom:clamp(16px,2vw,32px);background:var(--surface);border-radius:var(--radius-card);padding:20px 24px;display:flex;align-items:center;gap:16px;max-width:420px">
<x-import component-from-global-scope="Werkgoed.Merkteken" size="44"></x-import>
<span style="font:700 20px/1.2 var(--font-sans);font-variation-settings:'wdth' 90">Werkschoenen en werkkleding om te passen, naast de A15.</span>
</div>
</div>
</section>

<section style="padding:clamp(40px,5vw,72px) var(--gutter) 0">
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px">
<div style="background:var(--surface-sunken);border-radius:var(--radius-card);padding:28px;display:flex;flex-direction:column;gap:14px">''' + ico('locatie', 32) + '''<span class="wg-label" style="color:var(--ink-muted)">adres</span><span style="font:700 22px/1.25 var(--font-sans);font-variation-settings:'wdth' 90">Wiedhaak 1<br>3371 KD Hardinxveld-Giessendam</span></div>
<div style="background:var(--surface-sunken);border-radius:var(--radius-card);padding:28px;display:flex;flex-direction:column;gap:14px">''' + ico('klok', 32) + '''<span class="wg-label" style="color:var(--ink-muted)">open</span><span style="font:700 22px/1.25 var(--font-sans);font-variation-settings:'wdth' 90">08:30 tot 17:30<br><span class="wg-small" style="color:var(--ink-muted)">[OPENINGSDAGEN AANVULLEN]</span></span></div>
<div style="background:var(--surface-sunken);border-radius:var(--radius-card);padding:28px;display:flex;flex-direction:column;gap:14px">''' + ico('levering', 32) + '''<span class="wg-label" style="color:var(--ink-muted)">route</span><span style="font:700 22px/1.25 var(--font-sans);font-variation-settings:'wdth' 90">Direct naast de A15, in Hardinxveld-Giessendam.</span></div>
<div style="background:var(--marine);color:var(--on-night);border-radius:var(--radius-card);padding:28px;display:flex;flex-direction:column;gap:14px" class="wg-night">''' + ico('telefoon', 32) + '''<span class="wg-label" style="color:var(--on-night-muted)">bel of mail</span><span style="font:700 22px/1.25 var(--font-sans);font-variation-settings:'wdth' 90">0184-701212<br>info@werkgoed.nl</span></div>
</div>
</section>

<!-- voetscan -->
<section id="voetscan" style="padding:clamp(56px,8vw,128px) var(--gutter) 0">
<div style="display:flex;flex-wrap:wrap;gap:40px 64px;align-items:flex-start">
<div style="flex:1 1 400px;min-width:0;display:flex;flex-direction:column;gap:24px">
<span class="wg-label" style="color:var(--ink-muted)">3D voetscan</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="niet je maat.">Je voet is</x-import>
<p class="wg-lead" style="margin:0;max-width:40ch">Je schoenmaat zegt weinig over hoe je voet is. Met de 3D voetscanner meten we lengte, breedte en je voetboog. Daarna kies je een werkschoen en inlegzool die echt past.</p>
<ol style="list-style:none;margin:8px 0 0;padding:0;display:flex;flex-direction:column">
<sc-for list="{{stappen}}" as="st" hint-placeholder-count="3">
<li style="display:flex;gap:20px;padding:20px 0;border-top:1px solid var(--line)">
<span style="font:800 40px/1 var(--font-sans);font-variation-settings:'wdth' 75;color:var(--vlam);min-width:1.4em">{{st.nr}}</span>
<span style="display:flex;flex-direction:column;gap:6px"><span style="font:700 22px/1.2 var(--font-sans);font-variation-settings:'wdth' 90">{{st.kop}}</span><span class="wg-body" style="color:var(--ink-muted)">{{st.tekst}}</span></span>
</li>
</sc-for>
</ol>
</div>

<!-- afspraak -->
<form style="flex:1 1 380px;min-width:0;background:var(--canvas);border-radius:var(--radius-sheet);padding:clamp(24px,3vw,44px);display:flex;flex-direction:column;gap:18px">
<div style="display:flex;justify-content:space-between;align-items:flex-start;gap:16px">
<h3 class="wg-heading wg-h3" style="margin:0;font-size:clamp(26px,2.4vw,34px)">Plan je voetscan</h3>
<x-import component-from-global-scope="Werkgoed.Zegel" size="84" id="scan" tekst="pasvorm"></x-import>
</div>
<sc-if value="{{nietVerstuurd}}" hint-placeholder-val="{{yes}}">
<label style="display:flex;flex-direction:column;gap:6px;font:600 14px/1.3 var(--font-sans)">Je naam<input type="text" autocomplete="name" style="height:48px;border:1px solid var(--line-strong);border-radius:var(--radius-sm);padding:0 14px;font:400 16px var(--font-sans);background:var(--surface);color:var(--ink)"></label>
<label style="display:flex;flex-direction:column;gap:6px;font:600 14px/1.3 var(--font-sans)">Telefoon<input type="tel" autocomplete="tel" style="height:48px;border:1px solid var(--line-strong);border-radius:var(--radius-sm);padding:0 14px;font:400 16px var(--font-sans);background:var(--surface);color:var(--ink)"></label>
<label style="display:flex;flex-direction:column;gap:6px;font:600 14px/1.3 var(--font-sans)">Welke dag past je?<input type="date" style="height:48px;border:1px solid var(--line-strong);border-radius:var(--radius-sm);padding:0 14px;font:400 16px var(--font-sans);background:var(--surface);color:var(--ink)"></label>
<div style="display:flex;flex-direction:column;gap:8px"><span style="font:600 14px/1.3 var(--font-sans)">Waarvoor kom je?</span>
<div role="group" aria-label="Waarvoor kom je" style="display:flex;flex-wrap:wrap;gap:8px">
<sc-for list="{{doelen}}" as="d" hint-placeholder-count="3">
<x-import component-from-global-scope="Werkgoed.Tag" active="{{d.active}}" on-click="{{d.pick}}">{{d.naam}}</x-import>
</sc-for>
</div></div>
<x-import component-from-global-scope="Werkgoed.Button" variant="signal" on-click="{{verstuur}}">Vraag je afspraak aan</x-import>
<span class="wg-small" style="color:var(--ink-muted)">Of plan direct via werkschoenenaanmeten.nl.</span>
</sc-if>
<sc-if value="{{verstuurd}}" hint-placeholder-val="{{no}}">
<div style="display:flex;flex-direction:column;gap:12px;padding:12px 0">
<span style="display:flex;align-items:center;gap:10px;font:700 22px/1.2 var(--font-sans);color:var(--ok)">''' + ico('check', 28) + '''Aanvraag ontvangen</span>
<p class="wg-body" style="margin:0">Wij bellen je om de afspraak te bevestigen. Neem je huidige werkschoenen mee, dan kijken we ook naar je slijtage.</p>
</div>
</sc-if>
</form>
</div>
</section>

<section style="padding:clamp(56px,8vw,128px) var(--gutter)">
<div style="display:flex;flex-wrap:wrap;gap:32px 56px;align-items:center">
<div style="flex:1.3 1 480px;min-width:0;aspect-ratio:1004/650;border-radius:var(--radius-sheet);overflow:hidden"><img class="wg-foto" src="''' + IMG['team'] + '''" alt="Het team van Werkgoed in de showroom"></div>
<div style="flex:1 1 340px;min-width:0;display:flex;flex-direction:column;gap:20px">
<span class="wg-label" style="color:var(--ink-muted)">wie je treft</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="meedenken.">Kenners die</x-import>
<p class="wg-lead" style="margin:0;max-width:34ch">Ons team helpt je kiezen. Voor jezelf, of voor je hele ploeg.</p>
</div>
</div>
</section>
'''

SHOWROOM_JS = '''    const extra = {
      stappen: D.stappen,
      doelen: D.doelen.map((d) => ({ naam: d, active: s.doel === d, pick: () => this.setState({ doel: d }) })),
      verstuur: () => this.setState({ verstuurd: true }),
      verstuurd: !!s.verstuurd,
      nietVerstuurd: !s.verstuurd
    };'''

SHOWROOM = {
    'file': 'Showroom.dc.html', 'title': 'Werkgoed showroom en voetscan', 'h': 3600, 'active': 'Showroom',
    'body': SHOWROOM_BODY, 'init': {'doel': 'Werkschoenen', 'verstuurd': False},
    'data': {'stappen': [
        {'nr': '1', 'kop': 'We scannen je voeten', 'tekst': 'Je staat even op de 3D voetscanner. Lengte, breedte en voetboog staan dan vast.'},
        {'nr': '2', 'kop': 'We adviseren', 'tekst': 'Op basis van de scan en je werk kiezen we schoenen en zo nodig een inlegzool of steunzool.'},
        {'nr': '3', 'kop': 'Je past en loopt', 'tekst': 'Pas de schoenen, loop een rondje en voel het verschil. Pas als het goed zit, ga je naar huis.'}],
        'doelen': ['Werkschoenen', 'Inlegzolen', 'Kleding voor de ploeg']},
    'js': SHOWROOM_JS,
}

# ------------------------------------------------------------------ Winkelwagen
WAGEN_BODY = '''
<section style="padding:clamp(28px,3.5vw,48px) var(--gutter) 0;display:flex;flex-direction:column;gap:24px">
''' + kruimel(('Home', 'Main.dc.html'), ('Winkelwagen', None)) + '''
<h1 class="wg-heading" style="margin:0;font:800 clamp(48px,6vw,88px)/.92 var(--font-sans);font-variation-settings:'wdth' 82;letter-spacing:-.045em">Je winkelwagen</h1>
</section>

<section style="padding:32px var(--gutter) clamp(56px,7vw,112px);display:flex;flex-wrap:wrap;gap:32px 48px;align-items:flex-start">
<div style="flex:999 1 560px;min-width:0;display:flex;flex-direction:column">
<sc-for list="{{regels}}" as="r" hint-placeholder-count="2">
<div style="display:flex;flex-wrap:wrap;gap:20px;align-items:center;padding:24px 0;border-top:1px solid var(--line)">
<div style="width:120px;height:120px;flex:none;background:var(--surface-sunken);border-radius:var(--radius-tile);display:grid;place-items:center;overflow:hidden"><img src="{{r.foto}}" alt="" style="width:86%;height:86%;object-fit:contain;mix-blend-mode:multiply"></div>
<div style="flex:1 1 220px;min-width:0;display:flex;flex-direction:column;gap:6px">
<span class="wg-small" style="color:var(--ink-muted)">{{r.merk}}</span>
<a class="wg-ul" href="Product.dc.html" style="font:700 22px/1.2 var(--font-sans);font-variation-settings:'wdth' 90">{{r.naam}}</a>
<span class="wg-small" style="color:var(--ink-muted)">{{r.optie}}</span>
</div>
<div style="display:flex;align-items:center;gap:6px;border:1px solid var(--line-strong);border-radius:var(--radius-pill);padding:2px">
<button class="wg-step" type="button" aria-label="Eén minder" onClick="{{r.minder}}" style="width:40px;height:40px;border-radius:50%;border:0;background:transparent;color:var(--ink);font:600 20px/1 var(--font-sans);cursor:pointer">−</button>
<span aria-live="polite" style="min-width:2ch;text-align:center;font:700 17px/1 var(--font-sans);font-variant-numeric:tabular-nums">{{r.aantal}}</span>
<button class="wg-step" type="button" aria-label="Eén meer" onClick="{{r.meer}}" style="width:40px;height:40px;border-radius:50%;border:0;background:transparent;color:var(--ink);font:600 20px/1 var(--font-sans);cursor:pointer">+</button>
</div>
<div style="min-width:140px;text-align:right;display:flex;flex-direction:column;gap:4px">
<span style="font:800 22px/1 var(--font-sans);font-variation-settings:'wdth' 85">{{r.totaal}}</span>
<span class="wg-small" style="color:var(--ink-muted)">{{r.stuk}} per stuk excl. btw</span>
</div>
</div>
</sc-for>
<div style="border-top:1px solid var(--line);padding-top:24px;display:flex;flex-wrap:wrap;gap:12px;justify-content:space-between;align-items:center">
<a class="wg-ul" href="Categorie.dc.html" style="font:600 16px/1.3 var(--font-sans)">← Verder winkelen</a>
<span class="wg-small" style="color:var(--ink-muted)">Bestel je voor je ploeg? <a class="wg-ul" href="mailto:info@werkgoed.nl" style="color:var(--ink);font-weight:600">Vraag een offerte</a></span>
</div>
</div>

<aside aria-label="Overzicht" style="flex:1 1 340px;min-width:0;background:var(--canvas);border-radius:var(--radius-sheet);padding:clamp(24px,3vw,40px);display:flex;flex-direction:column;gap:18px">
<h2 class="wg-heading wg-h3" style="margin:0">Overzicht</h2>
<div style="display:flex;flex-direction:column;gap:10px;background:var(--surface);border-radius:var(--radius-tile);padding:16px">
<span class="wg-small" style="display:flex;align-items:center;gap:8px;font-weight:600">''' + ico('verzending', 20) + '''{{verzendTekst}}</span>
<div role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="{{verzendPct}}" aria-label="Op weg naar gratis verzending" style="height:10px;border-radius:5px;background:var(--surface-sunken);overflow:hidden"><div style="height:100%;width:{{verzendBreedte}};background:var(--vlam);border-radius:5px"></div></div>
</div>
<dl style="margin:0;display:flex;flex-direction:column;font:500 16px/1.4 var(--font-sans)">
<div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid var(--line)"><dt>Subtotaal excl. btw</dt><dd style="margin:0;font-weight:700">{{subtotaal}}</dd></div>
<div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid var(--line)"><dt>Verzending</dt><dd style="margin:0;font-weight:700">{{verzending}}</dd></div>
<div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid var(--line)"><dt>Btw 21%</dt><dd style="margin:0;font-weight:700">{{btw}}</dd></div>
<div style="display:flex;justify-content:space-between;align-items:baseline;padding:14px 0 0"><dt style="font-weight:700">Totaal incl. btw</dt><dd style="margin:0;font:800 32px/1 var(--font-sans);font-variation-settings:'wdth' 85">{{totaal}}</dd></div>
</dl>
<x-import component-from-global-scope="Werkgoed.Button" variant="signal" href="#">Ga verder naar afrekenen</x-import>
<ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px;font:500 14px/1.4 var(--font-sans);color:var(--ink-muted)">
<li style="display:flex;gap:10px;align-items:center">''' + ico('voorraad', 18) + '''Uit voorraad leverbaar</li>
<li style="display:flex;gap:10px;align-items:center">''' + ico('levering', 18) + '''Snelle levering</li>
<li style="display:flex;gap:10px;align-items:center">''' + ico('locatie', 18) + '''Of haal het op in de showroom</li>
</ul>
</aside>
</section>
'''

WAGEN_JS = '''    const regels = D.regels.map((r, i) => {
      const n = s.aantallen[i];
      return Object.assign({}, r, {
        aantal: n, stuk: eur(r.prijs), totaal: eur(r.prijs * n),
        minder: () => { const a = s.aantallen.slice(); a[i] = Math.max(1, a[i] - 1); this.setState({ aantallen: a }); },
        meer: () => { const a = s.aantallen.slice(); a[i] = a[i] + 1; this.setState({ aantallen: a }); }
      });
    });
    const sub = D.regels.reduce((t, r, i) => t + r.prijs * s.aantallen[i], 0);
    const gratis = sub >= 100;
    const pct = Math.min(100, Math.round(sub));
    const extra = {
      regels: regels,
      subtotaal: eur(sub),
      verzending: gratis ? 'Gratis' : '[VERZENDKOSTEN]',
      btw: eur(sub * 0.21),
      totaal: eur(sub * 1.21),
      verzendTekst: gratis ? 'Je verzending is gratis.' : 'Nog ' + eur(100 - sub) + ' tot gratis verzending.',
      verzendPct: pct,
      verzendBreedte: pct + '%'
    };'''

WAGEN = {
    'file': 'Winkelwagen.dc.html', 'title': 'Werkgoed winkelwagen', 'h': 2200, 'active': None,
    'body': WAGEN_BODY, 'init': {'aantallen': [1, 12]},
    'data': {'regels': [
        {'merk': 'Havep', 'naam': 'Gore-Tex jas Revolve 50468', 'optie': 'Blauw, maat L', 'prijs': 379.95, 'foto': IMG['p-havep']},
        {'merk': 'Werkhandschoenen', 'naam': 'Chauffeurshandschoenen 10419', 'optie': 'Ongevoerd', 'prijs': 2.99, 'foto': IMG['p-handschoen']}]},
    'js': WAGEN_JS,
}

PAGES = [CATEGORIE, PRODUCT, MERKEN_PAGE, SHOWROOM, WAGEN]
