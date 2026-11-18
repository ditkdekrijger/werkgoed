BODY = '''
<!-- hero in de beroepstint -->
<section style="background:var(--beroep-[[K]]);padding:clamp(28px,3.5vw,48px) var(--gutter) clamp(48px,6vw,96px)">
<nav aria-label="Kruimelpad" class="wg-small" style="color:var(--ink-muted);display:flex;flex-wrap:wrap;gap:8px;margin-bottom:clamp(28px,4vw,56px)"><a class="wg-ul" href="Main.dc.html">Home</a><span aria-hidden="true">/</span><a class="wg-ul" href="Main.dc.html#beroep">Per beroep</a><span aria-hidden="true">/</span><span style="color:var(--ink)">[[TITEL]]</span></nav>
<div style="display:flex;flex-wrap:wrap;gap:48px;align-items:flex-end;justify-content:space-between">
<div style="flex:1 1 560px;min-width:0;display:flex;flex-direction:column;gap:28px;align-items:flex-start">
<div style="display:flex;flex-wrap:wrap;gap:12px;align-items:center">
<span style="display:grid;place-items:center;width:56px;height:56px;border-radius:50%;background:var(--surface);color:var(--beroep-[[K]]-deep)"><x-import component-from-global-scope="Werkgoed.Icoon" naam="[[K]]" size="{{icoonMaat}}"></x-import></span>
<x-import component-from-global-scope="Werkgoed.Badge" tone="marine">per beroep</x-import>
</div>
<h1 class="wg-heading wg-mega" style="margin:0">[[NAAM]]<span style="color:var(--beroep-[[K]]-deep);font-weight:500">goed</span></h1>
<p class="wg-lead" style="margin:0;max-width:36ch">[[REGEL]]</p>
<div style="display:flex;flex-wrap:wrap;gap:12px">
<x-import component-from-global-scope="Werkgoed.Button" variant="signal" href="#pakket">Stel je pakket samen</x-import>
<x-import component-from-global-scope="Werkgoed.Button" variant="outline" arrow="{{no}}" href="tel:0184701212">Bel een kenner</x-import>
</div>
</div>
[[HEROBLOK]]
</div>

<!-- takenkiezer -->
<div style="margin-top:clamp(40px,5vw,72px);background:var(--surface);border-radius:var(--radius-card);padding:clamp(24px,3vw,40px);display:flex;flex-direction:column;gap:24px">
<div style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:8px 24px">
<h2 class="wg-heading wg-h3" style="margin:0;font-size:clamp(26px,2.6vw,36px)">Wat doe jij precies?</h2>
<span class="wg-small" style="color:var(--ink-muted)">Kies je taak. Wij laten zien wat er speelt en wat je nodig hebt.</span>
</div>
<div role="group" aria-label="Kies je taak" style="display:flex;flex-wrap:wrap;gap:10px">
<sc-for list="{{taken}}" as="t" hint-placeholder-count="5">
<x-import component-from-global-scope="Werkgoed.Tag" active="{{t.active}}" dot="{{yes}}" on-click="{{t.pick}}">{{t.naam}}</x-import>
</sc-for>
</div>
<div style="display:flex;flex-wrap:wrap;gap:24px 48px;border-top:1px solid var(--line);padding-top:24px">
<div style="flex:1 1 240px;min-width:0;display:flex;flex-direction:column;gap:12px">
<span class="wg-label" style="color:var(--ink-muted)">dit speelt bij {{taak.naam}}</span>
<div style="display:flex;flex-wrap:wrap;gap:8px">
<sc-for list="{{taak.risicos}}" as="r" hint-placeholder-count="3">
<x-import component-from-global-scope="Werkgoed.Badge" tone="risico" icoon="{{r.icoon}}">{{r.naam}}</x-import>
</sc-for>
</div>
</div>
<div style="flex:2 1 420px;min-width:0;display:flex;flex-direction:column;gap:12px">
<span class="wg-label" style="color:var(--ink-muted)">tip van de kenner</span>
<p class="wg-lead" style="margin:0;max-width:52ch">{{taak.tip}}</p>
<p class="wg-body" style="margin:0"><span style="font-weight:600">Wij pakken erbij:</span> {{taak.pakket}}</p>
</div>
</div>
</div>
</section>

<!-- een dag als -->
<section style="padding:clamp(56px,8vw,128px) var(--gutter)">
<div style="display:flex;flex-wrap:wrap;gap:48px 64px">
<div style="flex:1 1 320px;min-width:0;display:flex;flex-direction:column;gap:24px;align-self:flex-start">
<span class="wg-label" style="color:var(--ink-muted)">een dag als [[PERSOON]]</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="tot eind.">Je werk, van begin</x-import>
<p class="wg-lead" style="margin:0;max-width:34ch">[[DAGINTRO]]</p>
<div style="aspect-ratio:4/3;border-radius:var(--radius-tile);overflow:hidden">
<x-import component-from-global-scope="Werkgoed.FotoPlek" beroep="[[K]]">[[DAGFOTO]]</x-import>
</div>
</div>
<div style="flex:1.6 1 520px;min-width:0">
<x-import component-from-global-scope="Werkgoed.Werkdag" beroep="[[K]]" momenten="{{momenten}}"></x-import>
</div>
</div>
</section>

<!-- van top tot teen -->
<section style="background:var(--surface-sunken);border-radius:var(--radius-sheet) var(--radius-sheet) 0 0;padding:clamp(56px,8vw,128px) var(--gutter) clamp(48px,6vw,96px)">
<div style="display:flex;flex-direction:column;gap:24px;max-width:900px;margin-bottom:clamp(32px,4vw,56px)">
<span class="wg-label" style="color:var(--ink-muted)">van top tot teen</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="beschermd.">Elke plek goed</x-import>
<p class="wg-lead" style="margin:0;max-width:46ch">Kies een punt op het figuur. Je ziet wat er gevraagd wordt, wat wij erbij pakken en welke normen tellen.</p>
</div>
<x-import component-from-global-scope="Werkgoed.Lichaamskaart" beroep="[[K]]" zones="{{zones}}"></x-import>
<p class="wg-small" style="margin:32px 0 0;color:var(--ink-muted)">[VOORBEELDTEKST] Eisen en normcodes worden door Werkgoed gecontroleerd voordat ze live gaan.</p>
</section>

<!-- kenners weten dit -->
<section style="background:var(--surface-sunken);padding:0 var(--gutter) clamp(56px,8vw,128px)">
<div style="display:flex;flex-direction:column;gap:24px;max-width:900px;margin-bottom:40px">
<span class="wg-label" style="color:var(--ink-muted)">kenners weten dit</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="niet in de catalogus.">Wat je</x-import>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px">
<sc-for list="{{kenners}}" as="k" hint-placeholder-count="3">
<x-import component-from-global-scope="Werkgoed.Card" tone="marine">
<div style="display:flex;flex-direction:column;gap:16px;min-height:280px;padding:var(--space-3)">
<span style="display:flex;justify-content:space-between;align-items:center"><span style="font:800 56px/1 var(--font-sans);font-variation-settings:'wdth' 75;color:var(--vlam);font-variant-numeric:tabular-nums">{{k.nr}}</span><x-import component-from-global-scope="Werkgoed.Merkteken" size="36"></x-import></span>
<h3 class="wg-heading wg-h3" style="margin:auto 0 0;font-size:clamp(24px,2.2vw,30px)">{{k.kop}}</h3>
<p class="wg-body" style="margin:0;color:var(--on-night-muted)">{{k.tekst}}</p>
</div>
</x-import>
</sc-for>
</div>
</section>

<!-- pakket en ploeg -->
<section id="pakket" style="padding:clamp(56px,8vw,128px) var(--gutter) 0">
<div style="background:var(--canvas);border-radius:var(--radius-sheet);padding:clamp(28px,4vw,64px);display:flex;flex-wrap:wrap;gap:40px 56px;align-items:stretch">
<div style="flex:1.5 1 480px;min-width:0;display:flex;flex-direction:column;gap:24px">
<div style="display:flex;justify-content:space-between;align-items:flex-start;gap:16px"><span class="wg-label" style="color:var(--ink-muted)">jouw pakket</span><x-import component-from-global-scope="Werkgoed.Zegel" size="104" id="pakket" tekst="kennerspakket"></x-import></div>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="zelf samengesteld.">Het [[TITELKLEIN]]pakket,</x-import>
<p class="wg-lead" style="margin:0;max-width:44ch">Dit geven wij een [[PERSOON]] meestal mee. Zet uit wat je al hebt.</p>
<div role="group" aria-label="Onderdelen van het pakket" style="display:flex;flex-wrap:wrap;gap:10px">
<sc-for list="{{pakket}}" as="p" hint-placeholder-count="8">
<x-import component-from-global-scope="Werkgoed.Tag" active="{{p.active}}" dot="{{yes}}" on-click="{{p.pick}}">{{p.naam}}</x-import>
</sc-for>
</div>
</div>
<div style="flex:1 1 320px;min-width:0;background:var(--surface);border-radius:var(--radius-card);padding:clamp(24px,3vw,40px);box-sizing:border-box;display:flex;flex-direction:column;gap:20px">
<span class="wg-label" style="color:var(--ink-muted)">voor je ploeg</span>
<div style="display:flex;align-items:center;gap:16px">
<button class="wg-step" type="button" aria-label="Eén [[PERSOON]] minder" onClick="{{minder}}" style="width:48px;height:48px;border-radius:50%;border:1px solid var(--ink);background:transparent;color:var(--ink);font:600 24px/1 var(--font-sans);cursor:pointer">−</button>
<span aria-live="polite" style="font:800 72px/1 var(--font-sans);font-variation-settings:'wdth' 75;font-variant-numeric:tabular-nums;min-width:1.4em;text-align:center">{{aantal}}</span>
<button class="wg-step" type="button" aria-label="Eén [[PERSOON]] meer" onClick="{{meer}}" style="width:48px;height:48px;border-radius:50%;border:1px solid var(--ink);background:transparent;color:var(--ink);font:600 24px/1 var(--font-sans);cursor:pointer">+</button>
<span class="wg-lead">{{aantalWoord}}</span>
</div>
<p class="wg-body" style="margin:0;border-top:1px solid var(--line);padding-top:16px">{{samenvatting}}</p>
<x-import component-from-global-scope="Werkgoed.Button" variant="signal" href="mailto:info@werkgoed.nl">Vraag een offerte voor je ploeg</x-import>
<p class="wg-small" style="margin:0;color:var(--ink-muted)">Wij komen terug met een voorstel op maat. Liever passen? Kom langs in de showroom.</p>
</div>
</div>
</section>

<!-- producten -->
<section style="padding:clamp(56px,8vw,128px) var(--gutter) 0">
<div style="display:flex;flex-wrap:wrap;gap:24px;justify-content:space-between;align-items:flex-end">
<div style="display:flex;flex-direction:column;gap:24px;max-width:700px">
<span class="wg-label" style="color:var(--ink-muted)">uit voorraad leverbaar</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="voor [[MV]].">Gekozen</x-import>
</div>
<div role="group" aria-label="Filter soort" style="display:flex;flex-wrap:wrap;gap:10px">
<sc-for list="{{filters}}" as="f" hint-placeholder-count="5">
<x-import component-from-global-scope="Werkgoed.Tag" active="{{f.active}}" on-click="{{f.pick}}">{{f.naam}}</x-import>
</sc-for>
</div>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:24px 16px;margin-top:40px">
<sc-for list="{{producten}}" as="p" hint-placeholder-count="4">
<x-import component-from-global-scope="Werkgoed.ProductKaart" merk="{{p.merk}}" naam="{{p.naam}}" prijs-ex="{{p.prijsEx}}" image="{{p.foto}}" kenner="{{p.kenner}}" href="Product.dc.html"></x-import>
</sc-for>
</div>
</section>

<!-- vragen -->
<section style="padding:clamp(56px,8vw,128px) var(--gutter) 0">
<div style="display:flex;flex-wrap:wrap;gap:40px 64px">
<div style="flex:1 1 320px;min-width:0;display:flex;flex-direction:column;gap:24px;align-self:flex-start">
<span class="wg-label" style="color:var(--ink-muted)">vragen uit de praktijk</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="ons vaak.">Dit vragen [[MV]]</x-import>
</div>
<div style="flex:1.6 1 520px;min-width:0;border-bottom:1px solid var(--line)">
<sc-for list="{{vragen}}" as="v" hint-placeholder-count="3">
<details class="wg-faq" style="border-top:1px solid var(--line)">
<summary style="display:flex;justify-content:space-between;align-items:center;gap:16px;padding:22px 0;font:600 22px/1.25 var(--font-sans);font-variation-settings:'wdth' 90;letter-spacing:-.02em"><span>{{v.vraag}}</span><span class="wg-faq-plus" aria-hidden="true" style="font:400 28px/1 var(--font-sans);color:var(--ink-muted);transition:transform .16s ease">+</span></summary>
<p class="wg-body" style="margin:0 0 24px;max-width:60ch;color:var(--ink-muted)">{{v.antwoord}}</p>
</details>
</sc-for>
</div>
</div>
</section>

<!-- advies -->
<section style="padding:clamp(56px,8vw,128px) var(--gutter) 0">
<x-import component-from-global-scope="Werkgoed.Card" tone="signal">
<div style="display:flex;flex-wrap:wrap;gap:32px;align-items:center;justify-content:space-between;padding:clamp(8px,2vw,32px)">
<div style="flex:1 1 380px;display:flex;flex-direction:column;gap:12px">
<h2 class="wg-heading wg-h1" style="margin:0;font-size:clamp(32px,4vw,56px)">Twijfel je? Vraag het een kenner.</h2>
<p class="wg-lead" style="margin:0;max-width:40ch">Vertel wat je doet en waar je tegenaan loopt. Wij zeggen wat je nodig hebt, en wat niet.</p>
</div>
<div style="display:flex;flex-wrap:wrap;gap:12px">
<x-import component-from-global-scope="Werkgoed.Button" variant="ink" href="tel:0184701212">Bel 0184-701212</x-import>
<x-import component-from-global-scope="Werkgoed.Button" variant="outline" arrow="{{no}}" href="mailto:info@werkgoed.nl">Mail je vraag</x-import>
</div>
</div>
</x-import>
</section>

<!-- andere beroepen -->
<section style="padding:clamp(56px,8vw,128px) var(--gutter)">
<div style="display:flex;flex-direction:column;gap:24px;max-width:900px;margin-bottom:40px">
<span class="wg-label" style="color:var(--ink-muted)">andere beroepen</span>
<x-import component-from-global-scope="Werkgoed.Heading" size="h2" accent="ander werk?">Of doe je</x-import>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px">
<sc-for list="{{andere}}" as="b" hint-placeholder-count="7">
<x-import component-from-global-scope="Werkgoed.BeroepKaart" beroep="{{b.k}}" naam="{{b.naam}}" regel="{{b.regel}}" risicos="{{b.risicos}}" href="{{b.href}}"></x-import>
</sc-for>
</div>
</section>

<div style="padding:0 var(--gutter)"><x-import component-from-global-scope="Werkgoed.Lat" height="{{latHoogte}}"></x-import></div>
'''

SCRIPT = '''<script type="text/x-dc" data-dc-script data-props='{"menuOpen":{"editor":"boolean","default":false},"$preview":{"width":1440,"height":[[H]]}}'>
class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { taak: 0, uit: {}, aantal: 5, soort: 'Alles', menu: !!this.props.menuOpen };
  }
  renderVals() {
    const D = [[DATA]];
    const s = this.state;
    const taak = D.taken[s.taak] || D.taken[0];
    const pakket = D.pakket.map((naam, i) => ({
      naam: naam,
      active: !s.uit[i],
      pick: () => this.setState({ uit: Object.assign({}, s.uit, { [i]: !s.uit[i] }) })
    }));
    const gekozen = pakket.filter((p) => p.active).length;
    const soorten = ['Alles'].concat(D.producten.map((p) => p.soort).filter((x, i, a) => a.indexOf(x) === i));
    return {
      yes: true,
      no: false,
      icoonMaat: 28,
      streepHoogte: 24,
      latHoogte: 28,
[[MENU_JS]]      taken: D.taken.map((t, i) => ({ naam: t.naam, active: i === s.taak, pick: () => this.setState({ taak: i }) })),
      taak: taak,
      momenten: D.momenten,
      zones: D.zones,
      kenners: D.kenners,
      pakket: pakket,
      aantal: s.aantal,
      aantalWoord: s.aantal === 1 ? D.persoon : D.mv,
      minder: () => this.setState({ aantal: Math.max(1, s.aantal - 1) }),
      meer: () => this.setState({ aantal: Math.min(250, s.aantal + 1) }),
      samenvatting: gekozen + ' onderdelen per persoon. ' + (gekozen * s.aantal) + ' artikelen voor de hele ploeg.',
      filters: soorten.map((f) => ({ naam: f, active: f === s.soort, pick: () => this.setState({ soort: f }) })),
      producten: D.producten.filter((x) => s.soort === 'Alles' || x.soort === s.soort).map((x) => Object.assign({ foto: '', kenner: false }, x)),
      vragen: D.vragen,
      andere: D.andere
    };
  }
}
</script>
</body>
</html>
'''
