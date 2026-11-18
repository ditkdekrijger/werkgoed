# Button

De actieknop in pilvorm. Gebruik `signal` voor de ene hoofdactie per scherm, `ink` (marine) en `outline` voor de rest, `light` en `outline-light` op `marine`, en `link` voor een tekstactie met een oranje onderlijn.

- Tekst heeft een werkwoord en de jij-vorm: "Kies je beroep", "Plan je voetscan".
- De pijl staat standaard achter de tekst. Zet `arrow={false}` voor een knop als "Klantportaal" of "Winkelwagen".
- Jij levert: de tekst als children en `href` of `onClick`. Met `href` wordt het een link.
- Doe niet: twee `signal`-knoppen naast elkaar, of een knop zonder werkwoord.
