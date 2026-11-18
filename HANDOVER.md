# Handover: Werkgoed redesign en design system

Datum: 18 november 2026. Eigenaar: Dick de Krijger (HORIZON Group). Werkgoed Bedrijfskleding & PBM, werkgoed.nl, Hardinxveld-Giessendam.

## Opdracht

Redesign van werkgoed.nl, next level. Kernboodschap: "Past altijd goed. Bij 't werk wat je doet." De magie: Werkgoed weet wat er in elk beroep gevraagd wordt en koppelt dat aan het juiste type kleding en PBM. De site start daarom bij het beroep (lasgoed, straatgoed, bouwgoed) en toont daarnaast de categorieën (jassen, broeken, enzovoort) en de merken.

Schrijfregels van Dick: Nederlands, je en jij, kort en direct, geen gedachtestreepjes of em-dashes in teksten.

## Update: versie 3 (18 november 2026, eind van de middag)

Op verzoek van Dick:
- **Geel is weg.** Oranje (`vlam`, `#ff6a13`) is het enige accent: hoofdknop, markering in koppen, de Streep, het oproepvlak. `signal` is nu een alias van `vlam`. De beroepstint van Straatgoed is rode klinker geworden in plaats van fluogeel.
- **De belofte vol in beeld**: de hero van Home is "Past altijd goed. Bij 't werk wat je doet." over de hele breedte, met een fotocollage eronder.
- **Foto's van werkgoed.nl** (team, showroom, sfeerbeelden van Dassy, Snickers en KASK, categorie- en productfoto's) staan als assets op het canvas. Kopieën in `assets/fotos/`. Lasgoed gebruikt nu een staalbouwfoto; een echte lasfoto ontbreekt nog.
- **Het echte logo** van werkgoed.nl (W-blok, WERKGOED, "werkt beter!") in header en footer, met het blok in oranje. Ook als asset in het design system (groep Logos). Kopie in `assets/logo/`.
- **Merklogo's**: 8 van 14 opgehaald van de merksites (HAIX, LOWA, PUMA Safety, Snickers, Tricorp, Santino, Havep, KASK), in `assets/merken/`. Sixton, Solid Gear, Grisport, Redbrick, Dassy en BLS staan nog als tekst: hun sites waren niet bereikbaar. Vraag Werkgoed of de merken om logobestanden.
- **Iconen** in topbalk, header, menu, categorieën, showroom en footer. De set heeft er 22 bij (assortiment en service).
- **Uitklapmenu "Assortiment"** in de header op elke pagina: soort, merken en toepassing (lasser, stratenmaker en meer), plus een showroomtegel. Op het canvas klik je op Assortiment; de tweak `menuOpen` zet het standaard open.
- Showroomkop is nu "Je werkschoen pas je bij ons."


## Update: Werkgoed 2.0 (18 november 2026, middag)

**Design system versie 2.** Minder zwart, wit en geel. Het palet komt nu uit de werkplaats:
- `marine` `#1c2d3f` vervangt zwart als donker vlak (`night` is een alias), `ink` is zeer donker marine `#16212c`.
- Warme vlakken: `surface-sunken` (kalk `#f5f3ee`) en nieuw `canvas` (werkkatoen `#ebe5d8`).
- `signal` geel blijft merkaccent, maar alleen voor de hoofdknop, de markering en de Streep.
- `vlam` oranje `#ff6a13` blijft de steunkleur, met een duidelijkere rol: risicobadges (`vlam-soft`, `vlam-ink`), het gekozen punt op de lichaamskaart, de onderlijn van links, één aanbiedingsbadge.
- `staal` voor normcodes.
- Acht beroepskleuren, elk een tint en een `-deep`: las (leer), straat (fluo), bouw (canvas), techniek (staal), magazijn (beton), chauffeur (cabineblauw), groen (blad), schilder (gebroken wit). Contrast gecontroleerd in licht en donker (`tools/contrast.py`).
- Nieuwe tekststijlen `wg-mega` (beroepswoordmerk) en `wg-code` (normen, tijden).
- Nieuwe componenten: `Badge`, `Icoon` (voorlopige set van 21 lijniconen: beroepen en risico's), `BeroepKaart`, `Lichaamskaart`, `Werkdag`. `Tag`, `Card`, `ProductKaart` en `BeroepKiezer` uitgebreid.

**Canvas.** Home herschreven: beroepenwand met acht BeroepKaarten, een lichaamskaart van de lasser als bewijs van kennis, en het nieuwe palet. Drie beroepspagina's met dezelfde opbouw: Lasgoed, Straatgoed, Bouwgoed. Per pagina: hero in de beroepstint met woordmerk, takenkiezer ("Wat doe jij precies?"), een werkdag, de lichaamskaart, "kenners weten dit", pakketbouwer met ploegteller, producten met filter, vragen, advies en de andere beroepen.

**Bron in deze repo.** `design-system/project/` en `canvas/project/` zijn kopieën van de artifacts. De pagina's worden gegenereerd: pas teksten aan in `tools/data.py` (beroepen) of `tools/main_tpl.py` (home), draai `python3 tools/gen.py canvas/project` en publiceer de gewijzigde `.dc.html`. `tools/tokcss.py` maakt `tokens.css` voor het canvas uit `tokens.json`.

**Nieuwe open punten.**
- Normcodes (EN ISO 11611, EN 12477, EN ISO 20471, EN 14404 en meer) zijn bestaande normen, maar de koppeling aan product en taak moet Werkgoed controleren. Hetzelfde geldt voor alle tips, werkdagen en vragen.
- De hoogtes van de pagina's op het canvas (7000 en 8200) zijn geschat. Controleer ze in het canvas en pas `h` aan als er witruimte of afsnijding is.
- Volgende beroepspagina's: Techniekgoed, Magazijngoed, Chauffeursgoed, Groengoed, Schildersgoed. Voeg een blok toe in `tools/data.py` en in `gen.py`, en een board in `canvas.json`.

## Wat er staat

| Wat | Artifact | Slug |
| --- | --- | --- |
| Redesign (Design canvas) | https://claude.ai/artifact/7v7hXJvJY5XafGd1N9M5xi | 38016145-a41f-47e3-97be-eea7858753ef |
| Werkgoed design system | https://claude.ai/artifact/GTsmYp2yGHseFoxGkRV8LA | 7d39b471-a239-4c25-9ffb-b90bafbdd553 |

De bronbestanden staan ook in `werkgoed-bronbestanden.zip` (mappen `canvas/` en `design-system/`). De artifacts zijn de bron van waarheid, de zip is een kopie.

### Canvas (redesign)

- `project/canvas.json`: index. Boards: `Main.dc.html` (Home, 1440 breed, expand fill, interactief) en `Lasgoed.dc.html` (beroepspagina). Design system record: namespace `wg`, verwijst naar het Werkgoed design system.
- `project/Main.dc.html`: topbalk, header, hero, beroepskiezer, onze kennis (3 kaarten), per soort (4 kaarten), merken met filter, hardlopers, streep, showroom, footer.
- `project/Lasgoed.dc.html`: hero, wat een lasser vraagt, pakket met filter, adviesblok, andere beroepen, footer.
- `project/ds/wg/`: kopie van het design system (tokens.json, tokens.css, components/bundle.css, bundle.js, index.d.ts).
- Componenten worden gemount met `<x-import component-from-global-scope="Werkgoed.Button">` enzovoort.

### Design system

- `project/tokens.json`: kleuren (licht en donker), typografie, ruimte, radius.
- `project/README.md`: het merkboek (toon, visual foundations, beroepsmodel, iconografie, logo, gebruik).
- `project/brandstory.md`: het merkverhaal (waarom, overtuigingen, belofte, bewijs, korte en lange versie, toon, voorbeeldzinnen).
- `project/components/`: Button, Tag, Heading, Card, Streep, ProductKaart, BeroepKiezer, Cover. Elk met README en preview.html. `bundle.js` (namespace `Werkgoed`), `bundle.css`, `index.d.ts`.

## Ontwerpbeslissingen

- Huisstijl is een voorstel van Claude, geen overname van de huidige site. Kleuren: signaalgeel `#ffd400` als merkaccent, zwart `#111315`, wit, betongrijs `#f4f4f2`, tweede accent fluo-oranje `#ff6a13` alleen op kleine badges. Geel is nooit tekstkleur op wit.
- Lettertype: Archivo (Google Fonts, variabel). Koppen 700 met `font-variation-settings: 'wdth' 90`, tracking -.03em. Accentwoord in een kop krijgt een gele markering (`Heading` met `accent`).
- Vorm: pillen voor knoppen en tags, sheets met ronde bovenhoeken, geen schaduwen. Merkmotief: de Streep (diagonale geel-zwarte band), maximaal één per pagina.
- Prijzen: exclusief btw groot, inclusief btw klein. Voorraadstatus altijd met een woord.
- Beroepen heten "-goed": Lasgoed, Straatgoed, Bouwgoed, Techniekgoed, Magazijngoed, Chauffeursgoed, Groengoed, Schildersgoed. De lijst en de eisen per beroep zijn voorbeeldtekst van Claude.
- Het eerste ontwerp gebruikte per ongeluk het JUST.LEAD brandkit. Dat is volledig vervangen door het Werkgoed design system en uit het canvas verwijderd.

## Feiten van werkgoed.nl die gebruikt zijn

Topbalk: snelle levering, uit voorraad leverbaar, gratis verzending vanaf €100 excl. btw, showroom open 08:30 tot 17:30. Navigatie: werkschoenen, werkkleding, werkhandschoenen, PBM, diensten. Showroom: Wiedhaak 1, 3371 KD Hardinxveld-Giessendam, naast de A15. Telefoon 0184-701212, info@werkgoed.nl. Voetscan via werkschoenenaanmeten.nl. Merken: HAIX, LOWA Work, Sixton, Solid Gear, Grisport Safety, PUMA Safety, Redbrick, Snickers Workwear, Tricorp Workwear, Santino, Dassy, Havep, BLS, KASK. Zusterwebshops: Cofra, LOWA en Haix werkschoenen (goede-werkschoenen.nl) en BLS adembescherming. Hardlopers met prijzen excl. btw: Chauffeurshandschoenen 10419 vanaf €2,99, Gore-Tex jas Revolve Havep 50468 vanaf €379,95, Haix Black Eagle 50 Mid S3 vanaf €148,68, Solid Gear Prime GTX S7S Mid BOA vanaf €305,50.

## Open punten

1. Logo en merkkleuren: de site noemt `Logo_Werkgoed_White.svg` en een favicon, maar beide waren niet op te halen en er kwamen geen hexcodes uit de pagina. Vraag Dick om het logo en de huidige merkkleuren. Pas daarna `tokens.json` en het woordmerk aan (nu een tekstwoordmerk "werkgoed" met gele stip).
2. Eisen per beroep en normen: door Werkgoed te laten controleren. Verzin geen normen of keurmerken.
3. Brandstory: placeholders [OPRICHTINGSJAAR], [AANTAL KLANTEN], [KEURMERKEN] invullen.
4. Foto's: overal gelabelde placeholders. Eigen foto's van klanten aan het werk nodig, geen stockbeeld. Productfoto's uit de webshop.
5. Lasgoed-pagina: producten zijn placeholders met [MERK] en € [PRIJS].
6. Niets is visueel gecontroleerd in een browser. Open beide artifacts en loop alle breedtes na, vooral de beroepskiezer en het merkenfilter.
7. Geen iconenset. Voorlopig lijniconen op een 24-raster, lijn 1,5px.
8. Het donkere thema bestaat in de tokens maar is niet op de pagina's getest.

## Werkwijze en valkuilen

- Beide artifacts zijn "typed" artifacts. Wijzig alleen bestanden onder `project/`. Verstuur nooit `index.html`, `SKILL.md` of `artifact-type/`.
- Publiceer één bestand of één call tegelijk, met `base_version` van de laatste versie en modus patch. Bij een conflict de bestanden opnieuw lezen.
- `canvas.json` pas aanpassen als de layout verandert, en dan eerst opnieuw lezen. Mensen verplaatsen boards op het canvas.
- `tokens.css` in het canvas (`project/ds/wg/tokens.css`) is met de hand gegenereerd uit `tokens.json`. Pas je tokens aan, werk dan ook die file bij, en kopieer `bundle.css`, `bundle.js` en `index.d.ts` opnieuw uit het design system.
- Het design system genereert zelf `tokens.css`, `manifest.json` en `api/`-kaarten. Schrijf die daar niet met de hand.
- Previews en canvas laden Archivo via Google Fonts. Er is geen lokaal fontbestand.
- Teksten: geen gedachtestreepjes, geen hoofdletters in koppen, knoppen met werkwoord en jij-vorm.

## Volgende stappen (voorstel)

1. Logo en kleuren van Dick binnenhalen en tokens bijwerken.
2. Beroepspagina's voor Straatgoed en Bouwgoed bouwen, dezelfde opbouw als Lasgoed.
3. Een mobiele versie van Home en een productlijstpagina (categorie) toevoegen.
4. Daarna de bouw: kies platform (WooCommerce thema of headless). Zet `tokens.json` om naar CSS variabelen en de componenten naar templates. De site draait nu op WooCommerce.
5. Eigen foto's en echte productdata koppelen, placeholders vervangen.

## Startprompt voor Claude Code

"Lees HANDOVER.md. Open het Werkgoed design system (slug 7d39b471-a239-4c25-9ffb-b90bafbdd553) en lees project/README.md en project/brandstory.md. Het redesign staat in canvas 38016145-a41f-47e3-97be-eea7858753ef. Werk de open punten uit en bouw daarna de volgende pagina."
