# BeroepKaart

De ingang naar een beroep. Een kaart in de beroepstint met het icoon, het woordmerk ("las" + "goed" in de diepe beroepskleur), één regel over het werk en de drie grootste risico's.

- Jij levert `beroep` (`las`, `straat`, `bouw`, `techniek`, `magazijn`, `chauffeur`, `groen`, `schilder`), `naam` zonder "goed" ("las"), `regel`, `risicos` (namen uit `Icoon`, maximaal drie) en `href`.
- Kleine letters in het woordmerk. "goed" zet de kaart er zelf achter.
- Zet acht kaarten in een raster van vier of twee kolommen. Elke kaart is één link.
- De opbouw is vast: icoon en pijl, woordmerk, één regel van maximaal twee regels hoog, en onderaan achter een haarlijn de risico's. Het woordmerk schaalt mee met de kaartbreedte, zodat ook "chauffeursgoed" op één regel past.
- Doe niet: een eigen kleur kiezen. Elk beroep heeft vaste tokens: `beroep-<naam>` en `beroep-<naam>-deep`.
