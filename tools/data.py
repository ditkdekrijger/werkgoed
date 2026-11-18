R = {
    'vonk': ('vonk', 'Vonken en spatten'), 'hitte': ('hitte', 'Hitte'), 'uv': ('zicht', 'UV-straling'), 'rook': ('stof', 'Lasrook'),
    'stof': ('stof', 'Stof'), 'kwarts': ('stof', 'Kwartsstof'), 'lawaai': ('lawaai', 'Lawaai'), 'snijden': ('snijden', 'Scherpe randen'),
    'regen': ('regen', 'Regen'), 'kou': ('kou', 'Kou en wind'), 'zicht': ('zicht', 'Gezien worden'), 'ogen': ('zicht', 'Scherven in je ogen'),
    'knielen': ('knielen', 'Knielen'), 'hoogte': ('hoogte', 'Hoogte'), 'cement': ('chemie', 'Natte cement'), 'damp': ('chemie', 'Dampen'),
    'trillen': ('lawaai', 'Trillingen'),
}


from prod import p
from shared import IMG


def risicos(*keys):
    return [{'icoon': R[k][0], 'naam': R[k][1]} for k in keys]


def zone(z, titel, eis, product, normen):
    return {'zone': z, 'titel': titel, 'eis': eis, 'product': product, 'normen': normen}


LAS = {
    'k': 'las', 'naam': 'las', 'titel': 'Lasgoed', 'persoon': 'lasser', 'mv': 'lassers', 'h': 6900,
    'regel': 'Vonken, spatten, hitte en lasrook. Wij weten wat dat met je kleding doet, en wat je ertegen draagt.',
    'heroimg': 'dassy', 'heroalt': 'Monteur in de staalbouw in een wind- en waterdichte werkjas van Dassy',
    'dagintro': 'Van omkleden tot opruimen. Elk moment vraagt iets anders van je kleding.',
    'dagfoto': 'de werkplaats, een lasser die boven het hoofd last',
    'data': {
        'persoon': 'lasser', 'mv': 'lassers',
        'taken': [
            {'naam': 'MIG/MAG', 'risicos': risicos('vonk', 'hitte', 'rook'), 'tip': 'Veel spatten en flinke hitte. Laskleding klasse 2 en dikke lashandschoenen zijn hier geen luxe.', 'pakket': 'lasjas klasse 2, lashandschoenen type A, automatische lashelm.'},
            {'naam': 'TIG', 'risicos': risicos('uv', 'hitte'), 'tip': 'Weinig spatten, wel felle UV-straling en fijn werk. Je wilt gevoel in je vingers, dus een dunne, soepele handschoen.', 'pakket': 'TIG-handschoenen type B, lashelm met fijn instelbaar filter, laskleding klasse 1.'},
            {'naam': 'Elektrode', 'risicos': risicos('vonk', 'hitte', 'rook'), 'tip': 'Elektrodelassen spat het meest, ook op locatie. Kies klasse 2, een lasmuts en schoenen zonder open veters.', 'pakket': 'lasoverall klasse 2, lasmuts, lasschoenen met flap.'},
            {'naam': 'Slijpen en snijden', 'risicos': risicos('vonk', 'lawaai', 'snijden'), 'tip': 'Slijpvonken vliegen verder dan je denkt. Een gelaatsscherm over je bril en gehoorbescherming horen erbij.', 'pakket': 'gelaatsscherm, veiligheidsbril, oorkappen, snijbestendige handschoenen.'},
            {'naam': 'Op locatie', 'risicos': risicos('vonk', 'regen', 'kou'), 'tip': 'Buiten lassen is wind, regen en kou erbij. Kies regenkleding die ook vlamvertragend is, zodat een spat geen gat brandt.', 'pakket': 'vlamvertragende regenjas, lasjas klasse 2, thermo onderlaag van wol.'},
        ],
        'momenten': [
            {'tijd': '07:00', 'titel': 'Omkleden in de werkplaats', 'tekst': 'Lasjas dicht tot boven, broek over de schoen. Geen synthetisch shirt eronder: dat smelt bij een spat.', 'risicos': ['hitte'], 'goed': ['Lasjas', 'Katoenen onderlaag']},
            {'tijd': '08:30', 'titel': 'MAG-lassen aan een frame', 'tekst': 'De hele ochtend spatten. Je handen en onderarmen vangen het meeste.', 'risicos': ['vonk', 'hitte'], 'goed': ['Lashandschoenen type A', 'Automatische lashelm']},
            {'tijd': '10:30', 'titel': 'Naden slijpen', 'tekst': 'Helm omhoog, scherm omlaag. Slijpvonken en lawaai tegelijk.', 'risicos': ['vonk', 'lawaai'], 'goed': ['Gelaatsscherm', 'Oorkappen']},
            {'tijd': '13:00', 'titel': 'Boven je hoofd lassen', 'tekst': 'Nu vallen de spatten naar beneden. Op je schouders, in je kraag, op je schoenen.', 'risicos': ['vonk'], 'goed': ['Lasmuts', 'Lasjas klasse 2', 'Schoen met flap']},
            {'tijd': '15:00', 'titel': 'Plaat sorteren', 'tekst': 'Scherpe randen en zware stukken. Je lashandschoen is daar niet voor gemaakt.', 'risicos': ['snijden'], 'goed': ['Snijbestendige handschoenen', 'Veiligheidsschoenen']},
            {'tijd': '16:30', 'titel': 'Einde dag', 'tekst': 'Kleding nakijken. Een gat of een dunne plek in laskleding betekent vervangen, niet doorwerken.', 'risicos': [], 'goed': ['Reservejas uit voorraad']},
        ],
        'zones': [
            zone('hoofd', 'Hoofd en nek', 'Een lasmuts van vlamvertragende stof onder je helm. Anders vallen spatten in je kraag.', 'Lasmutsen', ['EN ISO 11611']),
            zone('ogen', 'Ogen en gezicht', 'Een lashelm met automatisch filter. Bij slijpen een veiligheidsbril eronder.', 'Lashelmen en veiligheidsbrillen', ['EN 175', 'EN 379', 'EN 166']),
            zone('gehoor', 'Gehoor', 'Slijpen en hameren op staal gaat hard. Oordoppen die onder je helm passen.', 'Gehoorbescherming', ['EN 352']),
            zone('adem', 'Adem', 'Lasrook wil je niet inademen. Eerst afzuiging bij de bron, adembescherming waar dat niet genoeg is.', 'Adembescherming en helmen met luchttoevoer', ['EN 12941']),
            zone('romp', 'Romp en armen', 'Laskleding die niet doorbrandt. Hoge kraag, afgedekte zakken, geen open naden.', 'Lasjassen en lasoveralls', ['EN ISO 11611', 'EN ISO 11612']),
            zone('handen', 'Handen', 'Dik leer voor elektrode en MAG. Dun en soepel voor TIG.', 'Lashandschoenen', ['EN 12477']),
            zone('benen', 'Benen', 'Een broek zonder omslag, over de schoen. Een omslag vangt spatten op.', 'Lasbroeken', ['EN ISO 11611']),
            zone('voeten', 'Voeten', 'Een zool die tegen hitte kan en geen open veters, of een flap erover.', 'Lasschoenen', ['EN ISO 20345']),
        ],
        'kenners': [
            {'nr': '01', 'kop': 'Broek over de schoen, nooit erin.', 'tekst': 'Stop je je broek in je schoen, dan valt een spat er zo in. En geen omslag: die vangt vonken.'},
            {'nr': '02', 'kop': 'Synthetisch eronder is vragen om ellende.', 'tekst': 'Fleece en polyester smelten bij hitte en plakken op je huid. Draag katoen of wol onder je laskleding.'},
            {'nr': '03', 'kop': 'Olie en vet branden mee.', 'tekst': 'Laskleding vol olie beschermt minder. Was hem volgens het label en vervang hem als hij versleten is.'},
        ],
        'pakket': ['Lasjas', 'Lasbroek', 'Lasmuts', 'Lashandschoenen', 'Automatische lashelm', 'Veiligheidsbril', 'Gehoorbescherming', 'Lasschoenen'],
        'producten': [
            {'soort': 'Kleding', 'merk': '[MERK]', 'naam': 'Lasjas klasse 2 [VOORBEELD]', 'prijsEx': '€ [PRIJS]'},
            {'soort': 'Kleding', 'merk': '[MERK]', 'naam': 'Lasbroek zonder omslag [VOORBEELD]', 'prijsEx': '€ [PRIJS]'},
            {'soort': 'Handschoenen', 'merk': '[MERK]', 'naam': 'Lashandschoen type A [VOORBEELD]', 'prijsEx': '€ [PRIJS]'},
            {'soort': 'Handschoenen', 'merk': '[MERK]', 'naam': 'TIG-handschoen type B [VOORBEELD]', 'prijsEx': '€ [PRIJS]'},
            {'soort': 'Schoenen', 'merk': '[MERK]', 'naam': 'Lasschoen met flap [VOORBEELD]', 'prijsEx': '€ [PRIJS]'},
            {'soort': 'PBM', 'merk': '[MERK]', 'naam': 'Automatische lashelm [VOORBEELD]', 'prijsEx': '€ [PRIJS]'},
            {'soort': 'PBM', 'merk': 'BLS', 'naam': 'Adembescherming [VOORBEELD]', 'prijsEx': '€ [PRIJS]'},
            {'soort': 'PBM', 'merk': '[MERK]', 'naam': 'Lasmuts [VOORBEELD]', 'prijsEx': '€ [PRIJS]'},
        ],
        'vragen': [
            {'vraag': 'Welke klasse laskleding heb ik nodig?', 'antwoord': 'Klasse 1 is voor licht laswerk met weinig spatten, zoals TIG. Klasse 2 is voor zwaarder werk met meer spatten, zoals elektrode en MAG, en voor lassen boven je hoofd of in krappe ruimtes. Twijfel je, dan kijken we met je mee.'},
            {'vraag': 'Is vlamvertragend hetzelfde als laskleding?', 'antwoord': 'Nee. Vlamvertragende kleding beschermt tegen hitte en vlammen. Laskleding is daarnaast getest op spatten van gesmolten metaal. Voor lassen wil je allebei.'},
            {'vraag': 'Hoe lang gaat laskleding mee?', 'antwoord': 'Dat hangt af van hoeveel je last en hoe je hem wast. Zie je gaten, dunne plekken of plekken vol olie, vervang hem dan.'},
        ],
    },
}

STRAAT = {
    'k': 'straat', 'naam': 'straat', 'titel': 'Straatgoed', 'persoon': 'stratenmaker', 'mv': 'stratenmakers', 'h': 6900,
    'regel': 'Op je knieën, langs de weg, in weer en wind. Wij weten waar je kleding het eerst slijt.',
    'heroimg': 'softshell', 'heroalt': 'Bouwvakker in een softshell jack van Snickers Workwear draagt een buis over de bouwplaats',
    'dagintro': 'Vroeg in het donker, laat in de regen. Je kleding moet de hele dag mee.',
    'dagfoto': 'een werkvak langs de weg in de ochtend',
    'data': {
        'persoon': 'stratenmaker', 'mv': 'stratenmakers',
        'taken': [
            {'naam': 'Bestraten', 'risicos': risicos('knielen', 'regen', 'kou'), 'tip': 'Uren op je knieën in het zand. Kniestukken in je broek, en een broek die op de knie versterkt is.', 'pakket': 'werkbroek met kniezakken, kniestukken, werkschoenen met beschermde neus.'},
            {'naam': 'Knippen en zagen', 'risicos': risicos('kwarts', 'lawaai', 'ogen'), 'tip': 'Zagen in betonsteen geeft fijn stof dat je niet wilt inademen. Nat zagen of afzuigen, en een stofmasker, bril en gehoorbescherming.', 'pakket': 'FFP3 stofmasker, veiligheidsbril, oorkappen.'},
            {'naam': 'Langs het verkeer', 'risicos': risicos('zicht', 'kou'), 'tip': 'Welke klasse signaalkleding je nodig hebt, hangt af van de weg en je opdrachtgever. Wij zoeken het voor je uit.', 'pakket': 'signaaljas en signaalbroek in de klasse die het werk vraagt.'},
            {'naam': 'Asfalt', 'risicos': risicos('hitte', 'damp'), 'tip': 'Heet asfalt en dampen. Schoenen met een zool die tegen hitte kan, en kleding die het vuil weer loslaat.', 'pakket': 'asfaltschoenen met hittebestendige zool, signaalkleding.'},
            {'naam': 'Trilplaat en machines', 'risicos': risicos('lawaai', 'trillen'), 'tip': 'Een trilplaat gaat hard en trilt door in je handen. Gehoorbescherming en handschoenen met demping.', 'pakket': 'oorkappen, anti-vibratiehandschoenen.'},
        ],
        'momenten': [
            {'tijd': '06:30', 'titel': 'Aankomst langs de weg', 'tekst': 'Het is nog donker. Je moet gezien worden voordat je de eerste kegel zet.', 'risicos': ['zicht', 'kou'], 'goed': ['Signaaljas', 'Thermo onderlaag']},
            {'tijd': '07:00', 'titel': 'Werkvak afzetten', 'tekst': 'Kegels, hekken, borden. Het verkeer rijdt vlak langs je.', 'risicos': ['zicht'], 'goed': ['Signaalbroek', 'Werkhandschoenen']},
            {'tijd': '08:00', 'titel': 'Zandbed en straten', 'tekst': 'Uren op je knieën. Daar slijt je broek het eerst, en je knieën ook.', 'risicos': ['knielen'], 'goed': ['Kniestukken', 'Broek met kniezakken']},
            {'tijd': '10:30', 'titel': 'Stenen knippen en zagen', 'tekst': 'Stof, scherven en lawaai tegelijk.', 'risicos': ['stof', 'lawaai', 'zicht'], 'goed': ['FFP3 stofmasker', 'Veiligheidsbril', 'Oorkappen']},
            {'tijd': '13:00', 'titel': 'Een bui', 'tekst': 'Je stopt niet voor een bui. Je wilt droog blijven zonder te koken in je jas.', 'risicos': ['regen'], 'goed': ['Ademende regenjas', 'Regenbroek']},
            {'tijd': '15:00', 'titel': 'Aftrillen', 'tekst': 'De trilplaat gaat over het werk. Hard, en het trilt door tot in je schouders.', 'risicos': ['lawaai'], 'goed': ['Oorkappen', 'Handschoenen met demping']},
            {'tijd': '16:30', 'titel': 'Opruimen', 'tekst': 'Hekken terug, materiaal op de wagen. Zware stukken en natte handen.', 'risicos': ['snijden'], 'goed': ['Werkschoenen S3', 'Grip-handschoenen']},
        ],
        'zones': [
            zone('ogen', 'Ogen', 'Bij knippen en zagen vliegen scherven. Een bril die niet beslaat, ook niet met een masker op.', 'Veiligheidsbrillen', ['EN 166']),
            zone('gehoor', 'Gehoor', 'Zaag, knipper en trilplaat. Oorkappen die je snel op en af zet.', 'Gehoorbescherming', ['EN 352']),
            zone('adem', 'Adem', 'Fijn stof uit beton en natuursteen. Nat zagen of afzuigen eerst, een stofmasker erbij.', 'Stofmaskers', ['EN 149']),
            zone('romp', 'Romp', 'Zichtbaar, ook als je jas open hangt. Fluo met reflectie rondom, en droog bij regen.', 'Signaaljassen en regenkleding', ['EN ISO 20471', 'EN 343']),
            zone('handen', 'Handen', 'Grip op natte stenen en bescherming tegen schuren en snijden.', 'Werkhandschoenen', ['EN 388']),
            zone('knieen', 'Knieën', 'Kniestukken in de kniezakken van je broek. Kies broek en kniestuk samen.', 'Kniestukken en werkbroeken', ['EN 14404']),
            zone('voeten', 'Voeten', 'Een S3 werkschoen met een neus die tegen schuren kan. Op je knieën slijt de neus het eerst.', 'Werkschoenen', ['EN ISO 20345']),
        ],
        'kenners': [
            {'nr': '01', 'kop': 'Je neus slijt eerder dan je zool.', 'tekst': 'Wie straat, zit op zijn knieën en tenen. Een schoen met een beschermde neus houdt het veel langer vol.'},
            {'nr': '02', 'kop': 'Kniestukken werken alleen in de goede broek.', 'tekst': 'Een kniestuk moet op zijn plek blijven als je knielt. Daarom kiezen we broek en kniestuk samen.'},
            {'nr': '03', 'kop': 'Laagjes in plaats van één dikke jas.', 'tekst': 'Koud om half zeven, warm om tien uur. Met een signaaljas, een softshell en een thermo onderlaag zit je de hele dag goed.'},
        ],
        'pakket': ['Signaaljas', 'Signaalbroek met kniezakken', 'Kniestukken', 'Regenpak', 'Thermo onderlaag', 'Werkhandschoenen', 'Stofmasker', 'Veiligheidsbril', 'Gehoorbescherming', 'Werkschoenen S3'],
        'producten': [p('havep80626', soort='Kleding', kenner=True), p('portwestrws', soort='Kleding'), p('havep50171', soort='Kleding'), p('oxxawaldo', soort='Kleding'), p('snickers9110', soort='PBM', kenner=True),
                      {'soort': 'PBM', 'merk': 'BLS', 'naam': 'FFP3 stofmasker [VOORBEELD]', 'prijsEx': '€ [PRIJS]'}, {'soort': 'Schoenen', 'merk': '[MERK]', 'naam': 'Werkschoen S3 met neus [VOORBEELD]', 'prijsEx': '€ [PRIJS]'}],
        'vragen': [
            {'vraag': 'Welke klasse signaalkleding heb ik nodig?', 'antwoord': 'Dat hangt af van waar je werkt en wat je opdrachtgever vraagt. Bel ons met je project, dan zoeken we het uit.'},
            {'vraag': 'Hoe was ik signaalkleding?', 'antwoord': 'Volg het waslabel. Na veel wassen worden fluo en reflectie minder. Dan is het tijd voor een nieuwe.'},
            {'vraag': 'Welke kniestukken passen in mijn broek?', 'antwoord': 'Niet elk kniestuk past in elke broek. Neem je broek mee naar de showroom, of zeg welk merk je draagt.'},
        ],
    },
}

BOUW = {
    'k': 'bouw', 'naam': 'bouw', 'titel': 'Bouwgoed', 'persoon': 'bouwer', 'mv': 'bouwers', 'h': 6900,
    'regel': 'Hoogte, stof, lawaai en weer. Op de bouw komt alles samen. Wij weten wat je wanneer nodig hebt.',
    'heroimg': 'kask', 'heroalt': 'Werken op hoogte met een KASK veiligheidshelm met kinband',
    'dagintro': 'Van de keet tot de bovenste vloer. Elke klus vraagt iets anders.',
    'dagfoto': 'een bouwplaats met steiger en betonvloer',
    'data': {
        'persoon': 'bouwer', 'mv': 'bouwers',
        'taken': [
            {'naam': 'Ruwbouw en beton', 'risicos': risicos('cement', 'stof', 'lawaai'), 'tip': 'Natte cement is bijtend voor je huid. Handschoenen met nitril en laarzen waar het beton niet in loopt.', 'pakket': 'nitril handschoenen, S5 laarzen, werkbroek met kniezakken.'},
            {'naam': 'Werken op hoogte', 'risicos': risicos('hoogte', 'kou'), 'tip': 'Op de steiger of het dak wil je een helm met kinband, zodat hij blijft zitten als je bukt of valt.', 'pakket': 'helm met kinband, harnas, softshell jas.'},
            {'naam': 'Timmeren en afbouw', 'risicos': risicos('lawaai', 'snijden', 'stof'), 'tip': 'Zagen en tackeren gaat hard. Gehoorbescherming die je makkelijk op en af zet, en holsterzakken voor je gereedschap.', 'pakket': 'werkbroek met holsterzakken, oorkappen, montagehandschoenen.'},
            {'naam': 'Boren en slijpen', 'risicos': risicos('kwarts', 'lawaai', 'vonk'), 'tip': 'Boren en slijpen in beton geeft kwartsstof. Afzuiging aan de machine, en een FFP3 masker als het nodig is.', 'pakket': 'FFP3 masker, veiligheidsbril, oorkappen.'},
            {'naam': 'Grondwerk', 'risicos': risicos('regen', 'kou', 'knielen'), 'tip': 'Modder en water. Laarzen met teen- en zoolbescherming en een regenpak dat tegen een stootje kan.', 'pakket': 'S5 laarzen, stevig regenpak, werkhandschoenen met grip.'},
        ],
        'momenten': [
            {'tijd': '07:00', 'titel': 'De bouwplaats op', 'tekst': 'Helm op, hesje aan als de bouwplaats dat vraagt, schoenen dicht.', 'risicos': ['zicht'], 'goed': ['Veiligheidshelm', 'Signaalvest', 'Werkschoenen S3']},
            {'tijd': '08:00', 'titel': 'De steiger op', 'tekst': 'Bukken, klimmen, tillen. Je helm moet blijven zitten en je broek moet meebewegen.', 'risicos': ['hoogte'], 'goed': ['Helm met kinband', 'Stretch werkbroek']},
            {'tijd': '10:00', 'titel': 'Sparingen boren in beton', 'tekst': 'Stof en lawaai. Het stof is het gevaarlijkste deel, want je ziet het niet.', 'risicos': ['stof', 'lawaai'], 'goed': ['FFP3 masker', 'Oorkappen', 'Veiligheidsbril']},
            {'tijd': '12:30', 'titel': 'Beton storten', 'tekst': 'Natte cement op je handen en tegen je laarzen.', 'risicos': ['chemie'], 'goed': ['Nitril handschoenen', 'S5 laarzen']},
            {'tijd': '14:00', 'titel': 'Bekisting zagen', 'tekst': 'Cirkelzaag, spijkers, splinters.', 'risicos': ['lawaai', 'snijden'], 'goed': ['Oorkappen', 'Montagehandschoenen']},
            {'tijd': '16:00', 'titel': 'Wind op de bovenste vloer', 'tekst': 'Boven waait het altijd. Laagjes die je snel uit en aan doet.', 'risicos': ['kou'], 'goed': ['Softshell jas', 'Bodywarmer']},
        ],
        'zones': [
            zone('hoofd', 'Hoofd', 'Een helm die past bij je werk. Op hoogte een helm met kinband.', 'Veiligheidshelmen', ['EN 397', 'EN 12492']),
            zone('ogen', 'Ogen', 'Bij boren, slijpen en zagen een bril die goed aansluit.', 'Veiligheidsbrillen', ['EN 166']),
            zone('gehoor', 'Gehoor', 'Zagen, breken en tackeren. Oorkappen op je helm of oordoppen op maat.', 'Gehoorbescherming', ['EN 352']),
            zone('adem', 'Adem', 'Kwartsstof uit beton en steen is te fijn om te zien. Afzuigen eerst, een FFP3 masker erbij.', 'Stofmaskers', ['EN 149']),
            zone('romp', 'Romp', 'Zichtbaar waar de bouwplaats dat vraagt, en laagjes tegen wind en kou.', 'Softshells, bodywarmers en signaalvesten', ['EN ISO 20471']),
            zone('handen', 'Handen', 'Grip en gevoel bij montage. Nitril bij nat beton.', 'Werkhandschoenen', ['EN 388']),
            zone('knieen', 'Knieën', 'Vloeren, bekisting, afwerking. Kniestukken in de broek.', 'Kniestukken en werkbroeken', ['EN 14404']),
            zone('voeten', 'Voeten', 'Teen- en zoolbescherming tegen spijkers en vallende stukken. S3, of S5 als je in nat beton staat.', 'Werkschoenen en laarzen', ['EN ISO 20345']),
        ],
        'kenners': [
            {'nr': '01', 'kop': 'Een helm heeft een houdbaarheid.', 'tekst': 'Zon en gebruik maken een helm ouder. Kijk naar de datum in de helm en vervang hem altijd na een flinke klap.'},
            {'nr': '02', 'kop': 'Stof is het gevaar dat je niet ziet.', 'tekst': 'Kwartsstof uit beton en steen is te fijn om te zien. Afzuigen bij de bron gaat voor, een masker komt erbij.'},
            {'nr': '03', 'kop': 'Holsterzakken zijn geen luxe.', 'tekst': 'Een broek met holster- en kniezakken scheelt je elke dag lopen, bukken en zoeken.'},
        ],
        'pakket': ['Veiligheidshelm', 'Werkbroek met holsterzakken', 'Kniestukken', 'Softshell jas', 'Signaalvest', 'Werkhandschoenen', 'Gehoorbescherming', 'Veiligheidsbril', 'FFP3 maskers', 'Werkschoenen S3'],
        'producten': [p('snickers6371', soort='Kleding', kenner=True), p('dassyaustin', soort='Kleding'), p('havep50461', soort='Kleding'), p('snickers1112', soort='Kleding'), p('snickers9110', soort='PBM', kenner=True),
                      {'soort': 'PBM', 'merk': 'KASK', 'naam': 'Helm met kinband [VOORBEELD]', 'prijsEx': '€ [PRIJS]'}, {'soort': 'Schoenen', 'merk': '[MERK]', 'naam': 'Laars S5 [VOORBEELD]', 'prijsEx': '€ [PRIJS]'}],
        'vragen': [
            {'vraag': 'Wat is het verschil tussen S3 en S5?', 'antwoord': 'S3 is een veiligheidsschoen met teen- en zoolbescherming en een waterafstotende bovenkant. S5 is die bescherming in een laars van rubber of kunststof, voor nat werk.'},
            {'vraag': 'Welke helm neem ik voor werk op hoogte?', 'antwoord': 'Een helm met kinband blijft zitten als je bukt of valt. Vraag ons welke helm past bij jouw werk en je bouwplaats.'},
            {'vraag': 'Kunnen jullie mijn hele ploeg aankleden?', 'antwoord': 'Ja. Vertel met hoeveel mensen je bent en wat jullie doen. Dan maken we een voorstel.'},
        ],
    },
}
