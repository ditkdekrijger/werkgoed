Werkgoed is een Nederlandse leverancier van bedrijfskleding en persoonlijke beschermingsmiddelen (PBM) met een webshop en showroom in Hardinxveld-Giessendam. Het merk is praktisch, direct en vakkundig. De belofte is "Past altijd goed. Bij 't werk wat je doet." De kracht van het merk is dat Werkgoed het werk kent: wat een lasser, een stratenmaker of een timmerman de hele dag doet, waar het misgaat en welke kleding en PBM daar tegen beschermen.

Het volledige merkverhaal staat in de sectie Brandstory: waarom Werkgoed bestaat, waar het in gelooft, wat het kan bewijzen en hoe het klinkt. Schrijf elke tekst voor Werkgoed vanuit dat verhaal.

## Basis en next level

De basis is werkgoed.nl: de topbalk met levertijd en gratis verzending, de hoofdcategorieën werkschoenen, werkkleding, werkhandschoenen en PBM, de merken, de hardlopers met prijzen exclusief en inclusief btw, de showroom en de voetscan. Dit systeem tilt dat op: de site start bij het beroep in plaats van bij de productgroep, elk beroep heeft een eigen kleur en een eigen pagina die het werk laat zien, prijzen en voorraad staan altijd op dezelfde plek, en elk blok is een component dat je hergebruikt.

## Content fundamentals

- Schrijf in het Nederlands, met je en jij, nooit u. Voorbeeld: "Kies je beroep." "Pas je werkschoen in de showroom."
- Korte zinnen met een punt. Concreet in plaats van groots. Praktijk boven productpraat: begin bij wat iemand op het werk doet, daarna pas bij het artikel. "Uren op je knieën. Daar slijt je broek het eerst." is beter dan "Duurzame werkbroek met kniezakken."
- Praat als een collega van de vakman. Noem de handeling (knippen, slijpen, boven het hoofd lassen), het moment (06:30 langs de weg) en het gevolg (spatten in je kraag).
- Beroepen heten "-goed": Lasgoed, Straatgoed, Bouwgoed, Techniekgoed, Magazijngoed, Chauffeursgoed, Groengoed, Schildersgoed. Een nieuw beroep krijgt dezelfde vorm. In het woordmerk staan ze in kleine letters: "las" + "goed".
- Geen hoofdletters in koppen en kickers. Geen uitroeptekens, geen emoji, geen gedachtestreepjes. Gebruik een komma of een punt.
- Knoptekst heeft een werkwoord en de jij-vorm: "Kies je beroep", "Plan je voetscan", "Vraag een offerte voor je ploeg".
- Prijzen: exclusief btw staat groot, inclusief btw klein eronder. Komma als decimaalteken, euroteken voor het bedrag: "€148,68 excl. btw". Gebruik "Vanaf" bij varianten.
- Beloftes die op de site staan mag je herhalen: "Uit voorraad leverbaar", "Snelle levering", "Gratis verzending vanaf €100 excl. btw". Verzin geen cijfers of keurmerken. Normcodes (EN ISO 20471) zijn bestaande normen, maar welke norm bij welk product hoort controleert Werkgoed. Markeer zulke tekst als voorbeeld tot hij gecontroleerd is.

## Visual foundations

### Kleur

Het palet komt uit de werkplaats, niet uit een kleurwaaier: het marine van een klassieke werkjas, het canvas van een bouwbroek, kalk en beton, het signaalgeel van een hesje en het fluo-oranje van een afzetting.

- Verhouding: ongeveer 60 procent wit en `surface-sunken` (kalk), 25 procent `marine` en `canvas`, 10 procent beroepstinten, 5 procent `signal` en `vlam`. Geel en oranje zijn kruiden, geen saus.
- `ink` is een zeer donker marine, geen zwart. Labels en bijschriften `ink-muted`.
- `marine` is het donkere vlak: topbalk, het vraagpaneel, de showroom en de footer. Tekst erop is `on-night`. (`night` bestaat nog als alias.)
- `canvas` is het warme vlak voor sheets en kaarten die rust geven, zoals de advieskaart of de pakketbouwer.
- `signal` is het merkaccent: de ene hoofdknop, de markering in een kop en de Streep. Nooit tekstkleur op wit. Tekst erop is `on-signal`.
- `vlam` is de steunkleur. Hij markeert wat aandacht vraagt: risicobadges (`vlam-soft` met icoon in `vlam-ink`), het gekozen punt op de lichaamskaart, de onderlijn van een link en één aanbiedingsbadge. Nooit een groot vlak.
- `staal` is voor informatie: normcodes en hun rand.
- Elk beroep heeft een vaste tint en een diepe kleur: `beroep-las` (leer van een lasschort), `beroep-straat` (fluo van de weg), `beroep-bouw` (canvas), `beroep-techniek` (staal), `beroep-magazijn` (beton), `beroep-chauffeur` (cabineblauw), `beroep-groen` (blad), `beroep-schilder` (gebroken wit), elk met een `-deep`. De tint is het vlak van de beroepskaart, de hero en de lichaamskaart. De diepe kleur zet "goed" in het woordmerk, de iconen, het figuur en de tijden in de werkdag. Tekst op een tint is altijd `ink`.
- Status heeft altijd een woord: `ok` bij "Uit voorraad", `alert` bij "Niet leverbaar". Kleur alleen is nooit de boodschap.

### Typografie

- Eén lettertype, Archivo (Google Fonts), variabel in gewicht en breedte. Koppen in 700 met breedte 90% (de klasse `wg-heading` zet die) en tracking -.03em.
- `wg-mega` (800, breedte 80%) is alleen voor het beroepswoordmerk bovenaan een beroepspagina: "las" in `ink`, "goed" in gewicht 500 en de diepe beroepskleur.
- `wg-code` (breedte 75%, tabelcijfers) voor normcodes, artikelnummers en tijden.
- Verder `wg-display`, `wg-h1`, `wg-h2`, `wg-h3` voor koppen en `wg-lead`, `wg-body`, `wg-small`, `wg-label`, `wg-price` voor de rest.
- Accentwoord in een kop: één woord of de slotzin krijgt een `signal`-markering (component `Heading` met `accent`). Eén per kop, nooit in lopende tekst.

### Vorm, ruimte en beweging

- Pil (`radius-pill`) voor knoppen, tags en badges, sheet (`radius-sheet`, alleen bovenhoeken) voor grote vlakken die over elkaar schuiven, kaart (`radius-card`), tegel (`radius-tile`, foto 3:2). Geen schaduwen. Diepte komt uit overlappende sheets, tintverschil en lijnen van 1px (`line`).
- Ruimte: schaal `space-1` tot `space-10` (4, 8, 12, 16, 24, 32, 48, 64, 96, 128). Zijmarge clamp(20px, 4.2vw, 72px), sectie clamp(56px, 8vw, 128px), maximale breedte 1440px.
- De Streep: een diagonale band in `signal` en `marine` (component `Streep`) verwijst naar afzetting en werkkleding. Maximaal één per pagina, als scheiding boven de showroom of de footer.
- Beeld: eigen foto's van klanten die werken, in beeld met hun kleding en PBM. Geen stockbeeld. Productfoto's uit de webshop op `surface-sunken`.
- Beweging: kort en strak. Knop, tag en punt verkleuren in 160 ms. Niets beweegt continu. Respecteer `prefers-reduced-motion`.
- Focus: een ring van 3px in `focus` met 3px afstand. Op `marine` is de ring `signal`.

## Het beroepsmodel

Werkgoed verkoopt geen jassen, Werkgoed kent het werk. Elke pagina bewijst dat.

1. **De beroepenwand** (homepage): acht `BeroepKaart`en, elk in de eigen tint, met de drie grootste risico's van dat werk.
2. **De beroepspagina** heeft een vaste opbouw:
   - Hero in de beroepstint met het woordmerk (`wg-mega`), één zin over het werk en een takenkiezer: "Wat doe jij precies?" (bij lassen: MIG/MAG, TIG, elektrode, slijpen en snijden, op locatie). De gekozen taak toont de risico's van die taak en een concrete tip.
   - **Een dag als ...** (`Werkdag`): het werk van begin tot eind, per moment de risico's en wat je dan draagt.
   - **Van top tot teen** (`Lichaamskaart`): per zone wat er gevraagd wordt, wat Werkgoed erbij pakt en welke normen tellen.
   - **Kenners weten dit**: drie dingen die alleen een vakman weet, zoals "Je broek over de schoen, nooit erin" bij lassen.
   - **Pakket**: een basispakket om af te vinken en een teller voor de ploeg, met een offerteknop.
   - De producten met een filter, vragen uit de praktijk, advies en de andere beroepen.
3. **De BeroepKiezer** is de compacte vorm voor plekken met weinig ruimte.

Eisen, tips en normen komen van Werkgoed zelf. Wat nu in de componenten en pagina's staat is voorbeeldtekst en moet door Werkgoed worden gecontroleerd.

## Iconografie

Er is nog geen eigen iconenset. Gebruik component `Icoon`: lijniconen op een 24-raster met lijn 1,5px, ronde uiteinden, kleur `currentColor`. Er zijn iconen voor de acht beroepen en voor de risico's (vonk, hitte, regen, kou, zicht, lawaai, stof, snijden, chemie, knielen, hoogte). Geen emoji. Vervang de set zodra Werkgoed een eigen set heeft.

## Logo

Er is geen logo aangeleverd. Zet de naam voorlopig als tekst: "werkgoed" in gewicht 800, breedte 90%, kleine letters, met een kleine `signal`-stip erachter, en daaronder "bedrijfskleding & PBM" in `wg-small`. Vervang dit door het echte logo zodra het in `assets/Logos` staat.

## Gebruik in code

De componenten staan in `components/bundle.js` als `window.Werkgoed` en verwachten React 18. Laad `tokens.css` en `components/bundle.css` eerst. Componenten: `Button`, `Tag`, `Badge`, `Icoon`, `Heading`, `Card`, `Streep`, `ProductKaart`, `BeroepKaart`, `Lichaamskaart`, `Werkdag`, `BeroepKiezer`.

De homepage: topbalk (`marine`), header, hero met `Heading size="display"`, de beroepenwand met `BeroepKaart`, zo werkt het, per soort in `Card`, merken als `Tag`-filter met tegels, hardlopers met `ProductKaart`, Streep, showroom op `marine`, footer.
