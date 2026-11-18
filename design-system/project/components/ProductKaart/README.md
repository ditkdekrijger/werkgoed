# ProductKaart

Productkaart voor de hardlopers en de beroepspagina: foto op `surface-sunken` (3:2), merk, naam, prijs exclusief btw groot en inclusief btw klein, en de voorraadstatus.

- Jij levert `naam`, `prijsEx` als tekst ("€148,68", met "Vanaf" erbij als er varianten zijn), optioneel `prijsIn`, `merk`, `image`, `href` en `badge`.
- `badge` zet één `vlam`-badge linksboven op de foto, zoals "Hardloper". Maximaal één per kaart.
- `voorraad` is `true` of `false`. De status heeft altijd een woord, nooit alleen een kleur. Laat `voorraad` weg als je het niet weet.
- Geen productfoto aangeleverd: de kaart toont een gelabeld vlak, nooit een stockfoto.
