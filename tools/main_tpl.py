BODY = '''
<!-- hero: de belofte, vol in beeld -->
<section style="padding:clamp(36px,5vw,80px) var(--gutter) clamp(56px,7vw,112px)">
<h1 class="wg-heading" style="margin:0;font:800 clamp(44px,7.9vw,116px)/.92 var(--font-sans);font-variation-settings:'wdth' 82;letter-spacing:-.045em">Past altijd <mark class="wg-mark">goed.</mark><br>Bij &rsquo;t werk wat je doet.</h1>
<div style="display:flex;flex-wrap:wrap;gap:40px 48px;margin-top:clamp(32px,4vw,56px);align-items:stretch">
<div style="flex:1 1 340px;min-width:0;display:flex;flex-direction:column;gap:28px;justify-content:space-between">
<p class="wg-lead" style="margin:0;max-width:34ch">Wij kennen het werk van lassers, stratenmakers, bouwers en monteurs. En we weten wat je dan nodig hebt, van helm tot werkschoen.</p>
<div style="display:flex;flex-direction:column;gap:14px">
<span class="wg-label" style="color:var(--ink-muted)">welk werk doe jij?</span>
<div style="display:flex;flex-wrap:wrap;gap:8px">
<a class="wg-pill" href="Lasgoed.dc.html" style="display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 16px 0 8px;border-radius:var(--radius-pill);background:var(--beroep-las);border:1px solid transparent;font:600 15px/1 var(--font-sans)"><span style="display:grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--surface);color:var(--beroep-las-deep)"><x-import component-from-global-scope="Werkgoed.Icoon" naam="las" size="18"></x-import></span>Lasgoed</a>
<a class="wg-pill" href="Straatgoed.dc.html" style="display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 16px 0 8px;border-radius:var(--radius-pill);background:var(--beroep-straat);border:1px solid transparent;font:600 15px/1 var(--font-sans)"><span style="display:grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--surface);color:var(--beroep-straat-deep)"><x-import component-from-global-scope="Werkgoed.Icoon" naam="straat" size="18"></x-import></span>Straatgoed</a>
<a class="wg-pill" href="Bouwgoed.dc.html" style="display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 16px 0 8px;border-radius:var(--radius-pill);background:var(--beroep-bouw);border:1px solid transparent;font:600 15px/1 var(--font-sans)"><span style="display:grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--surface);color:var(--beroep-bouw-deep)"><x-import component-from-global-scope="Werkgoed.Icoon" naam="bouw" size="18"></x-import></span>Bouwgoed</a>
<a class="wg-pill" href="#beroep" style="display:inline-flex;align-items:center;min-height:44px;padding:0 16px;border-radius:var(--radius-pill);border:1px solid var(--line-strong);font:600 15px/1 var(--font-sans)">Alle beroepen</a>
</div>
<div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:12px">
<x-import component-from-global-scope="Werkgoed.Button" variant="signal" href="#beroep">Kies je beroep</x-import>
<x-import component-from-global-scope="Werkgoed.Button" variant="outline" arrow="{{no}}" href="Showroom.dc.html">Kom langs in de showroom</x-import>
</div>
</div>
</div>
<div style="flex:2 1 560px;min-width:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));grid-template-rows:repeat(2,minmax(0,1fr));gap:12px;min-height:520px">
<div style="grid-column:span 2;grid-row:span 2;border-radius:var(--radius-sheet);overflow:hidden;background:var(--canvas)"><img class="wg-foto" src="[[IMG_dassy]]" alt="Monteur in een wind- en waterdichte werkjas van Dassy aan het werk in de staalbouw"></div>
<div style="border-radius:var(--radius-card);overflow:hidden;background:var(--canvas)"><img class="wg-foto" src="[[IMG_softshell]]" alt="Bouwvakker in een softshell jack van Snickers Workwear draagt een buis op de bouwplaats"></div>
<div style="border-radius:var(--radius-card);overflow:hidden;background:var(--canvas)"><img class="wg-foto" src="[[IMG_kask]]" alt="Werken op hoogte met een KASK veiligheidshelm"></div>
</div>
</div>
</section>

<!-- beroepenwand -->
<section id="beroep" style="background:var(--surface-sunken);border-radius:var(--radius-sheet) var(--radius-sheet) 0 0;padding:clamp(56px,8vw,128px) var(--gutter)">
<div style="display:flex;flex-wrap:wrap;gap:24px 48px;justify-content:space-between;align-items:flex-end;margin-bottom:40px">
<div style="display:flex;flex-direction:column;gap:24px;max-width:820px">
<span class="wg-label" style="color:var(--ink-muted)">per beroep</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="doe jij?">Wat voor werk</x-import>
</div>
<p class="wg-lead" style="margin:0;max-width:36ch">Kies je beroep. Je ziet je werkdag, wat er gevraagd wordt van top tot teen, en wat wij erbij pakken.</p>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px">
<sc-for list="{{beroepen}}" as="b" hint-placeholder-count="8">
<x-import component-from-global-scope="Werkgoed.BeroepKaart" beroep="{{b.k}}" naam="{{b.naam}}" regel="{{b.regel}}" risicos="{{b.risicos}}" href="{{b.href}}"></x-import>
</sc-for>
</div>
</section>

<!-- zo ver gaat onze kennis -->
<section style="padding:clamp(56px,8vw,128px) var(--gutter) 0">
<div style="display:flex;flex-direction:column;gap:24px;max-width:900px;margin-bottom:clamp(32px,4vw,56px)">
<span class="wg-label" style="color:var(--ink-muted)">onze kennis</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="tot teen.">Een lasser, van top</x-import>
<p class="wg-lead" style="margin:0;max-width:46ch">Zo ver gaat onze kennis, voor elk beroep. Kies een punt en zie wat er gevraagd wordt.</p>
</div>
<x-import component-from-global-scope="Werkgoed.Lichaamskaart" beroep="las" zones="{{zones}}"></x-import>
<div style="margin-top:32px">
<x-import component-from-global-scope="Werkgoed.Button" variant="ink" href="Lasgoed.dc.html">Bekijk alles over lasgoed</x-import>
</div>
</section>

<!-- zo werkt het -->
<section style="padding:clamp(56px,8vw,128px) var(--gutter) 0">
<div style="display:flex;flex-wrap:wrap;gap:24px 48px;align-items:flex-end;margin-bottom:40px">
<div style="flex:1 1 420px;display:flex;flex-direction:column;gap:24px">
<span class="wg-label" style="color:var(--ink-muted)">wie wij zijn</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="die het werk kent.">Een ploeg</x-import>
</div>
<div style="flex:1.3 1 480px;min-width:0;aspect-ratio:1004/650;border-radius:var(--radius-card);overflow:hidden;background:var(--canvas)"><img class="wg-foto" src="[[IMG_team]]" alt="Het team van Werkgoed in de showroom in Hardinxveld-Giessendam"></div>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px">
<x-import component-from-global-scope="Werkgoed.Card" tone="sunken">
<div style="display:flex;flex-direction:column;gap:16px;min-height:220px;padding:var(--space-2)">
<span style="display:flex;justify-content:space-between;align-items:center"><span style="font:800 48px/1 var(--font-sans);font-variation-settings:'wdth' 75;color:var(--ink-muted)">01</span><x-import component-from-global-scope="Werkgoed.Icoon" naam="advies" size="32"></x-import></span>
<h3 class="wg-heading wg-h3" style="margin:auto 0 0">Jij vertelt wat je doet.</h3>
<p class="wg-body" style="margin:0">Lassen, straten, bouwen, monteren. Je werk is ons beginpunt, niet de catalogus.</p>
</div>
</x-import>
<x-import component-from-global-scope="Werkgoed.Card" tone="canvas">
<div style="display:flex;flex-direction:column;gap:16px;min-height:220px;padding:var(--space-2)">
<span style="display:flex;justify-content:space-between;align-items:center"><span style="font:800 48px/1 var(--font-sans);font-variation-settings:'wdth' 75;color:var(--ink-muted)">02</span><x-import component-from-global-scope="Werkgoed.Icoon" naam="helm" size="32"></x-import></span>
<h3 class="wg-heading wg-h3" style="margin:auto 0 0">Wij kennen de praktijk.</h3>
<p class="wg-body" style="margin:0">Waar je kleding slijt, waar het misgaat en welke normen tellen. Per beroep, per taak.</p>
</div>
</x-import>
<x-import component-from-global-scope="Werkgoed.Card" tone="marine">
<div style="display:flex;flex-direction:column;gap:16px;min-height:220px;padding:var(--space-2)">
<span style="display:flex;justify-content:space-between;align-items:center"><span style="font:800 48px/1 var(--font-sans);font-variation-settings:'wdth' 75;color:var(--vlam)">03</span><x-import component-from-global-scope="Werkgoed.Icoon" naam="voorraad" size="32"></x-import></span>
<h3 class="wg-heading wg-h3" style="margin:auto 0 0">Jij krijgt wat past.</h3>
<p class="wg-body" style="margin:0;color:var(--on-night-muted)">Kleding en PBM die kloppen met je werk. Uit voorraad leverbaar, of passen in de showroom.</p>
</div>
</x-import>
</div>
</section>

<!-- per soort -->
<section id="soort" style="padding:clamp(56px,8vw,128px) var(--gutter) 0">
<div style="display:flex;flex-direction:column;gap:24px;max-width:900px">
<span class="wg-label" style="color:var(--ink-muted)">per soort</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="je werk.">Alles voor</x-import>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-top:40px">
<sc-for list="{{categorieen}}" as="c" hint-placeholder-count="4">
<x-import component-from-global-scope="Werkgoed.Card" tone="{{c.tone}}">
<div style="display:flex;flex-direction:column;gap:20px;min-height:440px;padding:var(--space-2)">
<div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px">
<h3 class="wg-heading wg-h3" style="margin:0;font-size:clamp(26px,2.4vw,36px)">{{c.naam}}</h3>
<x-import component-from-global-scope="Werkgoed.Icoon" naam="{{c.icoon}}" size="32"></x-import>
</div>
<img src="{{c.foto}}" alt="{{c.alt}}" style="width:96px;height:96px;border-radius:var(--radius-tile);object-fit:cover">
<ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;flex:1">
<sc-for list="{{c.items}}" as="i" hint-placeholder-count="5">
<li style="border-top:1px solid {{c.line}}"><a class="wg-ul" href="Categorie.dc.html" style="display:flex;justify-content:space-between;gap:12px;padding:13px 0;font:500 17px/1.3 var(--font-sans)"><span>{{i}}</span><span aria-hidden="true">→</span></a></li>
</sc-for>
</ul>
</div>
</x-import>
</sc-for>
</div>
</section>

<!-- merken -->
<section id="merken" style="padding:clamp(56px,8vw,128px) var(--gutter) 0">
<div style="display:flex;flex-wrap:wrap;gap:24px;justify-content:space-between;align-items:flex-end">
<div style="display:flex;flex-direction:column;gap:24px;max-width:700px">
<span class="wg-label" style="color:var(--ink-muted)">merken</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="merken.">Sterke</x-import>
</div>
<div role="group" aria-label="Filter merken" style="display:flex;flex-wrap:wrap;gap:10px">
<sc-for list="{{merkFilters}}" as="f" hint-placeholder-count="4">
<x-import component-from-global-scope="Werkgoed.Tag" active="{{f.active}}" on-click="{{f.pick}}">{{f.naam}}</x-import>
</sc-for>
</div>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px;margin-top:40px">
<sc-for list="{{merken}}" as="m" hint-placeholder-count="14">
<a class="wg-tile" href="Merken.dc.html" style="display:flex;flex-direction:column;justify-content:space-between;gap:28px;min-height:150px;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-tile);padding:20px;box-sizing:border-box;transition:background-color .16s ease,border-color .16s ease">
<span class="wg-small" style="color:var(--ink-muted)">{{m.soort}}</span>
<sc-if value="{{m.logo}}" hint-placeholder-val="{{yes}}">
<img src="{{m.logo}}" alt="{{m.naam}}" style="height:44px;width:auto;max-width:100%;object-fit:contain;object-position:left center;align-self:flex-start">
</sc-if>
<sc-if value="{{m.geenLogo}}" hint-placeholder-val="{{no}}">
<span style="font:700 26px/1.05 var(--font-sans);font-variation-settings:'wdth' 90;letter-spacing:-.03em">{{m.naam}}</span>
</sc-if>
</a>
</sc-for>
</div>
</section>

<!-- hardlopers -->
<section style="padding:clamp(56px,8vw,128px) var(--gutter) 0">
<div style="display:flex;flex-direction:column;gap:24px;max-width:900px">
<span class="wg-label" style="color:var(--ink-muted)">hardlopers</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="gekocht.">Dit wordt het meest</x-import>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:24px 16px;margin-top:40px">
<sc-for list="{{producten}}" as="p" hint-placeholder-count="4">
<x-import component-from-global-scope="Werkgoed.ProductKaart" merk="{{p.merk}}" naam="{{p.naam}}" prijs-ex="{{p.prijsEx}}" prijs-in="{{p.prijsIn}}" voorraad="{{p.voorraad}}" image="{{p.foto}}" kenner="{{p.kenner}}" href="Product.dc.html"></x-import>
</sc-for>
</div>
</section>

<!-- streep + showroom -->
<div style="margin-top:clamp(56px,8vw,128px);padding:0 var(--gutter) 0">
<x-import component-from-global-scope="Werkgoed.Lat" height="{{latHoogte}}"></x-import>
</div>
<div style="height:24px"></div>
<section id="showroom" class="wg-night" style="background:var(--marine);color:var(--on-night);padding:clamp(56px,8vw,128px) var(--gutter);display:flex;flex-wrap:wrap;gap:48px;align-items:flex-end;border-bottom:1px solid rgba(255,255,255,.2)">
<div style="flex:1 1 480px;min-width:0;display:flex;flex-direction:column;gap:28px;align-items:flex-start">
<span style="display:flex;align-items:center;gap:12px"><x-import component-from-global-scope="Werkgoed.Merkteken" size="32"></x-import><span class="wg-label" style="color:var(--on-night-muted)">showroom en voetscan</span></span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" tone="night" accent="pas je bij ons.">Je werkschoen</x-import>
<p class="wg-lead" style="margin:0;max-width:40ch;color:var(--on-night-muted)">Loop binnen langs de A15. Pas je werkschoen en laat je voeten scannen, dan weet je zeker dat hij goed zit.</p>
<div style="width:100%;aspect-ratio:3/2;border-radius:var(--radius-card);overflow:hidden;margin-top:8px"><img class="wg-foto" src="[[IMG_showroom]]" alt="De showroom van Werkgoed in Hardinxveld-Giessendam"></div>
<div style="display:flex;flex-wrap:wrap;gap:12px">
<x-import component-from-global-scope="Werkgoed.Button" variant="signal" href="Showroom.dc.html#voetscan">Plan je voetscan</x-import>
<x-import component-from-global-scope="Werkgoed.Button" variant="outline-light" arrow="{{no}}" href="Showroom.dc.html">Bekijk de showroom</x-import>
</div>
</div>
<div style="flex:1 1 320px;min-width:0;display:flex;flex-direction:column;border-top:1px solid rgba(255,255,255,.2)">
<div style="padding:20px 0;border-bottom:1px solid rgba(255,255,255,.2)"><span class="wg-label" style="display:flex;align-items:center;gap:8px;color:var(--on-night-muted)"><x-import component-from-global-scope="Werkgoed.Icoon" naam="locatie" size="18"></x-import>adres</span><div style="font:700 24px/1.2 var(--font-sans);font-variation-settings:'wdth' 90;margin-top:6px">Wiedhaak 1<br>3371 KD Hardinxveld-Giessendam</div></div>
<div style="padding:20px 0;border-bottom:1px solid rgba(255,255,255,.2)"><span class="wg-label" style="display:flex;align-items:center;gap:8px;color:var(--on-night-muted)"><x-import component-from-global-scope="Werkgoed.Icoon" naam="klok" size="18"></x-import>open</span><div style="font:700 24px/1.2 var(--font-sans);font-variation-settings:'wdth' 90;margin-top:6px">08:30 tot 17:30</div></div>
<div style="padding:20px 0;border-bottom:1px solid rgba(255,255,255,.2)"><span class="wg-label" style="display:flex;align-items:center;gap:8px;color:var(--on-night-muted)"><x-import component-from-global-scope="Werkgoed.Icoon" naam="telefoon" size="18"></x-import>bel of mail</span><div style="font:700 24px/1.2 var(--font-sans);font-variation-settings:'wdth' 90;margin-top:6px">0184-701212<br>info@werkgoed.nl</div></div>
</div>
</section>
'''

SCRIPT = '''<script type="text/x-dc" data-dc-script data-props='{"menuOpen":{"editor":"boolean","default":false},"$preview":{"width":1440,"height":[[H]]}}'>
class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { merk: 'Alle', menu: !!this.props.menuOpen };
  }
  renderVals() {
    const D = [[DATA]];
    const s = this.state;
    const m = s.merk;
    const filters = ['Alle', 'Schoenen', 'Kleding', 'PBM'];
    const dark = 'rgba(255,255,255,.2)';
    const light = 'rgba(22,33,44,.16)';
    return {
      yes: true,
      no: false,
      streepHoogte: 24,
      latHoogte: 28,
[[MENU_JS]]      beroepen: D.beroepen,
      zones: D.zones,
      categorieen: [
        { naam: 'Werkkleding', icoon: 'jas', foto: D.img['cat-kleding'], alt: 'Werkbroeken van Snickers Workwear', tone: 'sunken', line: light, items: ['Jassen', 'Broeken', 'Overalls', 'Shirts en truien', 'Regenkleding'] },
        { naam: 'Werkschoenen', icoon: 'schoen', foto: D.img['cat-schoenen'], alt: 'Werkschoenen van HAIX', tone: 'marine', line: dark, items: ['Lage werkschoenen', 'Hoge werkschoenen', 'Laarzen', 'Inlegzolen', 'Voetscan en maat'] },
        { naam: 'Werkhandschoenen', icoon: 'handschoen', foto: D.img['cat-handschoenen'], alt: 'Werkhandschoenen', tone: 'canvas', line: light, items: ['Montage', 'Snijbestendig', 'Lashandschoenen', 'Chauffeurs', 'Winter'] },
        { naam: 'PBM', icoon: 'helm', foto: D.img['cat-pbm'], alt: 'Veiligheidshelm van KASK', tone: 'surface', line: light, items: ['Hoofd en gezicht', 'Gehoor', 'Ademhaling', 'Veiligheidsbrillen', 'Valbeveiliging'] }
      ],
      merkFilters: filters.map((f) => ({ naam: f, active: f === m, pick: () => this.setState({ merk: f }) })),
      merken: D.merken.filter((x) => m === 'Alle' || x.soort === m).map((x) => Object.assign({}, x, { logo: D.logos[x.naam] || '', geenLogo: !D.logos[x.naam] })),
      producten: [
        { merk: 'Werkhandschoenen', naam: 'Chauffeurshandschoenen 10419', prijsEx: 'Vanaf €2,99', prijsIn: '€3,62', foto: D.img['p-handschoen'], kenner: false },
        { merk: 'Havep', naam: 'Gore-Tex jas Revolve 50468', prijsEx: 'Vanaf €379,95', prijsIn: '€459,74', foto: D.img['p-havep'], kenner: true },
        { merk: 'HAIX', naam: 'Black Eagle 50 Mid S3', prijsEx: 'Vanaf €148,68', prijsIn: '€179,90', voorraad: true, foto: D.img['p-haix'], kenner: false },
        { merk: 'Solid Gear', naam: 'Prime GTX S7S Mid BOA', prijsEx: 'Vanaf €305,50', prijsIn: '€369,66', foto: D.img['p-solidgear'], kenner: false }
      ]
    };
  }
}
</script>
</body>
</html>
'''

MERKEN = [
    {'naam': 'HAIX', 'soort': 'Schoenen'}, {'naam': 'LOWA Work', 'soort': 'Schoenen'}, {'naam': 'Sixton', 'soort': 'Schoenen'},
    {'naam': 'Solid Gear', 'soort': 'Schoenen'}, {'naam': 'Grisport Safety', 'soort': 'Schoenen'}, {'naam': 'PUMA Safety', 'soort': 'Schoenen'},
    {'naam': 'Redbrick', 'soort': 'Schoenen'}, {'naam': 'Snickers Workwear', 'soort': 'Kleding'}, {'naam': 'Tricorp Workwear', 'soort': 'Kleding'},
    {'naam': 'Santino', 'soort': 'Kleding'}, {'naam': 'Dassy', 'soort': 'Kleding'}, {'naam': 'Havep', 'soort': 'Kleding'},
    {'naam': 'BLS', 'soort': 'PBM'}, {'naam': 'KASK', 'soort': 'PBM'}
]
