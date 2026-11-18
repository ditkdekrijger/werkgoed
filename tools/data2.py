from data import risicos, zone, R

R.update({'vlamboog': ('vonk', 'Vlamboog'), 'zitten': ('knielen', 'Lang zitten'), 'steenslag': ('zicht', 'Steenslag en splinters'),
          'kettingzaag': ('snijden', 'Kettingzaag'), 'tillen': ('knielen', 'Tillen en bukken'), 'mes': ('snijden', 'Snijden met een mes')})


def prod(soort, merk, naam):
    return {'soort': soort, 'merk': merk, 'naam': naam + ' [VOORBEELD]', 'prijsEx': '€ [PRIJS]'}


TECHNIEK = {
    'k': 'techniek', 'naam': 'techniek', 'titel': 'Techniekgoed', 'persoon': 'monteur', 'mv': 'monteurs',
    'regel': 'Kruipen, knielen, boven je hoofd werken. En soms spanning in de buurt. Wij weten wat je kleding dan moet kunnen.',
    'fotoplek': 'Een monteur in een kruipruimte of bij een verdeelkast, met overall en kniestukken in beeld.',
    'dagintro': 'Van de bus inladen tot de oplevering bij de klant.',
    'dagfoto': 'Een installateur die boven zijn hoofd boort, met bril en stofmasker.',
    'data': {
        'persoon': 'monteur', 'mv': 'monteurs',
        'taken': [
            {'naam': 'Installatiewerk', 'risicos': risicos('knielen', 'snijden', 'stof'), 'tip': 'Veel op je knieën en tussen scherpe randen. Een broek met kniezakken en een handschoen met gevoel zijn je basis.', 'pakket': 'werkbroek met kniezakken, kniestukken, montagehandschoenen.'},
            {'naam': 'Elektrotechniek', 'risicos': risicos('vlamboog', 'hitte'), 'tip': 'Werk je aan of bij installaties onder spanning, dan kan een vlamboog ontstaan. Dan heb je kleding nodig die daarop getest is. Wij zoeken met je uit wat jouw werk vraagt.', 'pakket': 'multinorm kleding, gelaatsscherm, isolerende handschoenen.'},
            {'naam': 'Kruipruimte en plafond', 'risicos': risicos('knielen', 'stof', 'ogen'), 'tip': 'Liggen, kruipen en boven je hoofd boren. Een overall houdt zand buiten, een bril en stofmasker de rest.', 'pakket': 'overall, kniestukken, veiligheidsbril, stofmasker FFP2.'},
            {'naam': 'Onderhoud in de industrie', 'risicos': risicos('damp', 'lawaai', 'zicht'), 'tip': 'Elke fabriek heeft zijn eigen regels. Neem ze mee, dan stellen wij een pakket samen dat er precies aan voldoet.', 'pakket': 'pakket op maat voor de locatie.'},
        ],
        'momenten': [
            {'tijd': '07:30', 'titel': 'De bus inladen', 'tekst': 'Materiaal, gereedschap en een reservebroek. Je weet nooit hoe vies het wordt.', 'risicos': ['snijden'], 'goed': ['Montagehandschoenen', 'Werkschoenen']},
            {'tijd': '08:30', 'titel': 'De kruipruimte in', 'tekst': 'Zand, kou en geen ruimte om rechtop te zitten.', 'risicos': ['knielen', 'stof'], 'goed': ['Overall', 'Kniestukken']},
            {'tijd': '10:30', 'titel': 'Boven je hoofd boren', 'tekst': 'Stof valt recht naar beneden, in je ogen en je kraag.', 'risicos': ['stof', 'zicht'], 'goed': ['Veiligheidsbril', 'Stofmasker FFP2']},
            {'tijd': '13:00', 'titel': 'Aan de verdeelkast', 'tekst': 'Werk bij spanning vraagt kleding en een scherm die op een vlamboog getest zijn.', 'risicos': ['vonk', 'hitte'], 'goed': ['Multinorm jas', 'Gelaatsscherm']},
            {'tijd': '16:00', 'titel': 'Oplevering bij de klant', 'tekst': 'Netjes binnenkomen, geen zand op de vloer.', 'risicos': [], 'goed': ['Schone overschoenen', 'Softshell jas']},
        ],
        'zones': [
            zone('ogen', 'Ogen', 'Een bril die goed aansluit bij boren boven je hoofd. Bij werk aan spanning een gelaatsscherm.', 'Veiligheidsbrillen en gelaatsschermen', ['EN 166']),
            zone('gehoor', 'Gehoor', 'Breken en boren in beton gaat hard, zeker in een kleine ruimte.', 'Gehoorbescherming', ['EN 352']),
            zone('adem', 'Adem', 'Stof uit plafonds en kruipruimtes. Een FFP2 masker bij boren en zagen.', 'Stofmaskers', ['EN 149']),
            zone('romp', 'Romp', 'Een overall in de kruipruimte. Bij elektrisch werk multinorm kleding die op vlamboog getest is.', 'Overalls en multinorm kleding', ['EN 61482-2', 'EN ISO 11612']),
            zone('handen', 'Handen', 'Gevoel en grip bij montage. Isolerende handschoenen bij werk aan spanning.', 'Montagehandschoenen', ['EN 388', 'EN 60903']),
            zone('knieen', 'Knieën', 'Kniestukken die op hun plek blijven, ook als je kruipt.', 'Kniestukken', ['EN 14404']),
            zone('voeten', 'Voeten', 'Een lichte veiligheidsschoen met grip, ook op de trap en de ladder.', 'Werkschoenen', ['EN ISO 20345']),
        ],
        'kenners': [
            {'nr': '01', 'kop': 'Een overall in de kruipruimte.', 'tekst': 'Geen kier op je rug als je ligt of kruipt. Zand en kou blijven buiten.'},
            {'nr': '02', 'kop': 'Multinorm is geen marketingwoord.', 'tekst': 'Bij werk aan installaties onder spanning tellen de tests op vlamboog en hitte. Die moet je kleding echt hebben.'},
            {'nr': '03', 'kop': 'Een lichte schoen voor de ladder.', 'tekst': 'Je staat veel op trappen en ladders. Een lichte schoen met een stroeve zool scheelt aan het eind van de dag.'},
        ],
        'pakket': ['Werkbroek met kniezakken', 'Kniestukken', 'Overall', 'Softshell jas', 'Montagehandschoenen', 'Veiligheidsbril', 'Stofmasker FFP2', 'Gehoorbescherming', 'Werkschoenen'],
        'producten': [prod('Kleding', 'Snickers Workwear', 'Werkbroek met kniezakken'), prod('Kleding', '[MERK]', 'Overall'), prod('Kleding', '[MERK]', 'Multinorm jas'),
                      prod('PBM', '[MERK]', 'Kniestukken'), prod('Handschoenen', '[MERK]', 'Montagehandschoen'), prod('Schoenen', 'Solid Gear', 'Lichte werkschoen')],
        'vragen': [
            {'vraag': 'Wat is multinorm kleding?', 'antwoord': 'Kleding die op meerdere normen tegelijk getest is, bijvoorbeeld op hitte en vlammen, vlamboog en antistatisch. Welke combinatie je nodig hebt, hangt af van je werk.'},
            {'vraag': 'Welke handschoen voor fijn montagewerk?', 'antwoord': 'Een dunne handschoen met een coating op de handpalm geeft grip en gevoel. Voor scherpe randen kies je een snijbestendige versie.'},
            {'vraag': 'Overall of jas en broek?', 'antwoord': 'In een kruipruimte of bij vuil werk is een overall handiger. Wissel je vaak tussen binnen en buiten, dan is een losse jas en broek flexibeler.'},
        ],
    },
}

MAGAZIJN = {
    'k': 'magazijn', 'naam': 'magazijn', 'titel': 'Magazijngoed', 'persoon': 'magazijnmedewerker', 'mv': 'magazijnmedewerkers',
    'regel': 'Pallets, heftrucks, koude hallen en dozen openen. Wij weten wat je de hele dag op de vloer nodig hebt.',
    'fotoplek': 'Een orderpicker tussen de stellingen, met signaalvest en handschoenen in beeld.',
    'dagintro': 'Van de eerste order tot de laatste vracht. Binnen, buiten en in de koelcel.',
    'dagfoto': 'Een heftruckchauffeur op het laadperron.',
    'data': {
        'persoon': 'magazijnmedewerker', 'mv': 'magazijnmedewerkers',
        'taken': [
            {'naam': 'Orderpicken', 'risicos': risicos('tillen', 'mes'), 'tip': 'Je loopt en bukt de hele dag. Een lichte veiligheidsschoen met demping en een handschoen met grip maken het verschil.', 'pakket': 'lichte veiligheidsschoenen, grip-handschoenen, werkbroek met stretch.'},
            {'naam': 'Heftruck rijden', 'risicos': risicos('zicht', 'kou'), 'tip': 'Op en neer tussen hal en laadperron. Een jas die je makkelijk open en dicht doet, en zichtbaar voor collega\'s te voet.', 'pakket': 'softshell jas, signaalvest, werkhandschoenen.'},
            {'naam': 'Koel- en vriescel', 'risicos': risicos('kou'), 'tip': 'In en uit de kou lopen vraagt kleding die je snel aan en uit doet. Een thermojas en thermobroek over je gewone kleding.', 'pakket': 'thermojas, thermobroek, gevoerde handschoenen.'},
            {'naam': 'Laden en lossen', 'risicos': risicos('zicht', 'regen', 'snijden'), 'tip': 'Buiten op het perron, vaak in de regen en tussen vrachtwagens. Gezien worden en droog blijven.', 'pakket': 'signaaljas, regenjas, veiligheidsschoenen S3.'},
        ],
        'momenten': [
            {'tijd': '06:00', 'titel': 'Start in de hal', 'tekst': 'De deuren staan open en het is koud. Laagjes die je straks weer uittrekt.', 'risicos': ['kou'], 'goed': ['Fleece', 'Bodywarmer']},
            {'tijd': '07:00', 'titel': 'Orderpicken', 'tekst': 'Bukken, tillen, lopen. Uren lang.', 'risicos': ['knielen'], 'goed': ['Lichte veiligheidsschoen', 'Grip-handschoenen']},
            {'tijd': '10:00', 'titel': 'Heftruck op het perron', 'tekst': 'Collega\'s te voet moeten je zien, en jij hen.', 'risicos': ['zicht'], 'goed': ['Signaalvest']},
            {'tijd': '12:30', 'titel': 'De vriescel in', 'tekst': 'Van de hal de kou in en weer terug.', 'risicos': ['kou'], 'goed': ['Thermojas', 'Thermobroek']},
            {'tijd': '15:00', 'titel': 'Retouren uitpakken', 'tekst': 'Dozen openen met een mes. Daar gaat het vaak mis.', 'risicos': ['snijden'], 'goed': ['Snijbestendige handschoenen']},
        ],
        'zones': [
            zone('hoofd', 'Hoofd', 'Een stootpet waar je onder stellingen en laadkleppen door loopt.', 'Stootpetten', ['EN 812']),
            zone('romp', 'Romp', 'Zichtbaar waar heftrucks rijden, ook binnen in de hal.', 'Signaalvesten en softshells', ['EN ISO 20471']),
            zone('handen', 'Handen', 'Grip bij tillen, snijbestendig bij dozen openen.', 'Werkhandschoenen', ['EN 388']),
            zone('benen', 'Benen', 'Een thermobroek over je werkbroek in de koel- en vriescel.', 'Thermokleding', ['EN 342']),
            zone('voeten', 'Voeten', 'Een lichte veiligheidsschoen met demping. Je loopt er de hele dag op.', 'Veiligheidsschoenen', ['EN ISO 20345']),
        ],
        'kenners': [
            {'nr': '01', 'kop': 'Zichtbaar binnen telt ook.', 'tekst': 'Waar heftrucks rijden, wil je gezien worden. Ook binnen in de hal.'},
            {'nr': '02', 'kop': 'Een snijbestendige handschoen voor het mes.', 'tekst': 'Bij dozen openen gaat het vaak mis. Een dunne snijbestendige handschoen voel je nauwelijks.'},
            {'nr': '03', 'kop': 'Licht loopt beter.', 'tekst': 'Een zware bouwschoen is niet nodig op een gladde hallenvloer. Een lichte veiligheidsschoen met demping wel.'},
        ],
        'pakket': ['Signaalvest', 'Werkbroek met stretch', 'Fleece', 'Thermojas', 'Thermobroek', 'Grip-handschoenen', 'Snijbestendige handschoenen', 'Veiligheidsschoenen'],
        'producten': [prod('Kleding', 'Tricorp Workwear', 'Signaalvest'), prod('Kleding', '[MERK]', 'Thermojas'), prod('Kleding', 'Santino', 'Fleece vest'),
                      prod('Handschoenen', '[MERK]', 'Snijbestendige handschoen'), prod('Schoenen', 'PUMA Safety', 'Lichte veiligheidsschoen'), prod('PBM', '[MERK]', 'Stootpet')],
        'vragen': [
            {'vraag': 'Heb ik in het magazijn een S3 schoen nodig?', 'antwoord': 'Dat hangt af van je werk en de regels van je werkgever. Binnen volstaat vaak een lichtere veiligheidsschoen. Werk je ook buiten, dan is S3 handig.'},
            {'vraag': 'Welke handschoen voor de vriescel?', 'antwoord': 'Een gevoerde handschoen die warm houdt en toch grip geeft. Wij laten je verschillende passen in de showroom.'},
            {'vraag': 'Kunnen jullie het hele magazijn aankleden?', 'antwoord': 'Ja. Vertel met hoeveel mensen je bent en wat er gebeurt in de hal. Dan maken we een voorstel.'},
        ],
    },
}

CHAUFFEUR = {
    'k': 'chauffeur', 'naam': 'chauffeurs', 'titel': 'Chauffeursgoed', 'persoon': 'chauffeur', 'mv': 'chauffeurs',
    'regel': 'Uren rijden, dan ineens laden en lossen in de regen. Wij weten wat je in de cabine en ernaast nodig hebt.',
    'fotoplek': 'Een chauffeur bij de laadklep, met signaalvest en chauffeurshandschoenen in beeld.',
    'dagintro': 'Vroeg de weg op, tussen de ritten laden en lossen.',
    'dagfoto': 'Een chauffeur die spanbanden vastzet.',
    'data': {
        'persoon': 'chauffeur', 'mv': 'chauffeurs',
        'taken': [
            {'naam': 'Rijden', 'risicos': risicos('zitten'), 'tip': 'Uren achter het stuur. Kleding die niet knelt als je zit en een schoen die niet te zwaar is op het pedaal.', 'pakket': 'werkbroek met stretch, lichte veiligheidsschoenen.'},
            {'naam': 'Laden en lossen', 'risicos': risicos('zicht', 'snijden', 'regen'), 'tip': 'Spanbanden, pallets en een laadklep. Zichtbaar zijn en een handschoen die tegen schuren kan.', 'pakket': 'signaalvest, chauffeurshandschoenen, regenjas.'},
            {'naam': 'Distributie in de stad', 'risicos': risicos('zicht', 'regen'), 'tip': 'Veel in en uit de cabine, vaak op straat. Een jas die je snel aan doet en gezien wordt.', 'pakket': 'softshell met reflectie, regenjas, werkschoenen.'},
            {'naam': 'Koeltransport', 'risicos': risicos('kou'), 'tip': 'Van een warme cabine de koelcel in. Een thermojas die je snel aantrekt.', 'pakket': 'thermojas, gevoerde handschoenen.'},
        ],
        'momenten': [
            {'tijd': '05:30', 'titel': 'Vertrek', 'tekst': 'Donker en koud op het terrein. Je wilt gezien worden bij de wagen.', 'risicos': ['zicht', 'kou'], 'goed': ['Softshell jas', 'Signaalvest']},
            {'tijd': '08:00', 'titel': 'Eerste losadres', 'tekst': 'Spanbanden los, pallets eruit.', 'risicos': ['snijden'], 'goed': ['Chauffeurshandschoenen']},
            {'tijd': '11:00', 'titel': 'Rijden', 'tekst': 'Uren zitten. Niets mag knellen.', 'risicos': [], 'goed': ['Werkbroek met stretch', 'Lichte veiligheidsschoen']},
            {'tijd': '13:00', 'titel': 'Lossen in de regen', 'tekst': 'Een bui midden op het laadperron.', 'risicos': ['regen'], 'goed': ['Regenjas met reflectie']},
            {'tijd': '16:00', 'titel': 'Koelcel bij de klant', 'tekst': 'Even de kou in en weer naar de cabine.', 'risicos': ['kou'], 'goed': ['Thermojas']},
        ],
        'zones': [
            zone('hoofd', 'Hoofd en nek', 'Een muts en een hoge kraag voor de vroege ritten.', 'Mutsen en softshells', []),
            zone('romp', 'Romp', 'Zichtbaar bij laden en lossen, droog bij regen.', 'Signaalvesten en regenjassen', ['EN ISO 20471', 'EN 343']),
            zone('handen', 'Handen', 'Leer tegen spanbanden en touwen.', 'Chauffeurshandschoenen', ['EN 388']),
            zone('benen', 'Benen', 'Een broek die meebeweegt als je instapt en zit.', 'Werkbroeken met stretch', []),
            zone('voeten', 'Voeten', 'Veilig, maar licht genoeg om in te rijden.', 'Veiligheidsschoenen', ['EN ISO 20345']),
        ],
        'kenners': [
            {'nr': '01', 'kop': 'Een schoen om in te rijden.', 'tekst': 'Een zware bouwschoen is onhandig op het pedaal. Kies een lichtere veiligheidsschoen met een smallere zool.'},
            {'nr': '02', 'kop': 'Je hesje hoort in de cabine.', 'tekst': 'Bij pech of laden langs de weg wil je het binnen handbereik hebben, niet achter in de laadbak.'},
            {'nr': '03', 'kop': 'Leer voor de spanbanden.', 'tekst': 'Spanbanden en touwen schuren. Een leren chauffeurshandschoen houdt dat lang vol.'},
        ],
        'pakket': ['Chauffeurshandschoenen', 'Signaalvest', 'Softshell jas', 'Regenjas met reflectie', 'Werkbroek met stretch', 'Veiligheidsschoenen'],
        'producten': [{'soort': 'Handschoenen', 'merk': 'Werkgoed', 'naam': 'Chauffeurshandschoenen 10419', 'prijsEx': 'Vanaf €2,99'},
                      {'soort': 'Kleding', 'merk': 'Havep', 'naam': 'Gore-Tex jas Revolve 50468', 'prijsEx': 'Vanaf €379,95'},
                      prod('Kleding', 'Tricorp Workwear', 'Signaalvest'), prod('Kleding', '[MERK]', 'Werkbroek met stretch'),
                      prod('Schoenen', 'PUMA Safety', 'Lichte veiligheidsschoen'), prod('Kleding', '[MERK]', 'Thermojas')],
        'vragen': [
            {'vraag': 'Moet ik als chauffeur veiligheidsschoenen dragen?', 'antwoord': 'Bij laden en lossen vaak wel. Dat hangt af van je werkgever en de adressen waar je komt. Een lichte veiligheidsschoen rijdt prima.'},
            {'vraag': 'Welke handschoen voor laden en lossen?', 'antwoord': 'Een leren chauffeurshandschoen geeft grip en kan tegen schuren. Voor koud weer is er een gevoerde versie.'},
            {'vraag': 'Kunnen jullie ons hele wagenpark aankleden?', 'antwoord': 'Ja. Vertel met hoeveel chauffeurs je bent en wat jullie rijden. Dan maken we een voorstel.'},
        ],
    },
}

GROEN = {
    'k': 'groen', 'naam': 'groen', 'titel': 'Groengoed', 'persoon': 'hovenier', 'mv': 'hoveniers',
    'regel': 'Buiten met machines, takken en weer. Wij weten wat je nodig hebt, van bosmaaier tot kettingzaag.',
    'fotoplek': 'Een hovenier met bosmaaier, helm met vizier en oorkappen in beeld.',
    'dagintro': 'Van de eerste maaibeurt tot het laatste snoeiwerk. Altijd buiten.',
    'dagfoto': 'Een boomverzorger met kettingzaag en zaagbroek.',
    'data': {
        'persoon': 'hovenier', 'mv': 'hoveniers',
        'taken': [
            {'naam': 'Maaien en bosmaaien', 'risicos': risicos('lawaai', 'steenslag'), 'tip': 'Steentjes en takjes vliegen alle kanten op. Een helm met gaasvizier en oorkappen, en een bril eronder.', 'pakket': 'helm met vizier en oorkappen, veiligheidsbril, werkbroek.'},
            {'naam': 'Snoeien en zagen', 'risicos': risicos('kettingzaag', 'hoogte'), 'tip': 'Werk je met een kettingzaag, dan heb je zaagbeschermende kleding en schoenen nodig. Wij helpen je kiezen en passen.', 'pakket': 'zaagbroek, zaaglaarzen, helm met vizier en oorkappen.'},
            {'naam': 'Tuinaanleg en bestraten', 'risicos': risicos('knielen', 'stof'), 'tip': 'Op je knieën in zand en grond. Kniestukken en een broek die daar sterk is.', 'pakket': 'werkbroek met kniezakken, kniestukken, werkschoenen.'},
            {'naam': 'Spuiten', 'risicos': risicos('damp'), 'tip': 'Middelen spuiten vraagt handschoenen en adembescherming die daarbij passen. Lees het etiket en vraag ons mee te kijken.', 'pakket': 'chemiebestendige handschoenen, adembescherming.'},
        ],
        'momenten': [
            {'tijd': '07:00', 'titel': 'Bus laden', 'tekst': 'Machines, benzine en het weerbericht checken.', 'risicos': [], 'goed': ['Regenpak in de bus']},
            {'tijd': '08:00', 'titel': 'Bosmaaien langs de berm', 'tekst': 'Lawaai, steenslag en verkeer vlak langs je.', 'risicos': ['lawaai', 'zicht'], 'goed': ['Helm met vizier', 'Signaalkleding']},
            {'tijd': '10:30', 'titel': 'Hagen snoeien', 'tekst': 'Takken in je gezicht en doornen in je handen.', 'risicos': ['snijden'], 'goed': ['Veiligheidsbril', 'Werkhandschoenen']},
            {'tijd': '13:00', 'titel': 'Een bui', 'tekst': 'Doorwerken in de regen, op een glad talud.', 'risicos': ['regen'], 'goed': ['Regenpak', 'Schoenen met profiel']},
            {'tijd': '14:30', 'titel': 'Boom snoeien', 'tekst': 'Kettingzaag aan, hoog en laag zagen.', 'risicos': ['snijden', 'lawaai'], 'goed': ['Zaagbroek', 'Zaaglaarzen']},
        ],
        'zones': [
            zone('hoofd', 'Hoofd', 'Een helm met gaasvizier en oorkappen in één, voor zagen en bosmaaien.', 'Bosbouwhelmen', ['EN 397', 'EN 1731']),
            zone('ogen', 'Ogen', 'Een gaas houdt takken tegen, fijne splinters niet altijd. Draag er een bril onder.', 'Veiligheidsbrillen', ['EN 166']),
            zone('gehoor', 'Gehoor', 'Bosmaaier, bladblazer, kettingzaag. Oorkappen op de helm.', 'Gehoorbescherming', ['EN 352']),
            zone('handen', 'Handen', 'Grip en bescherming tegen doornen en takken.', 'Werkhandschoenen', ['EN 388']),
            zone('benen', 'Benen', 'Een zaagbroek als je met de kettingzaag werkt.', 'Zaagbroeken', ['EN ISO 11393']),
            zone('voeten', 'Voeten', 'Grip op nat gras. Met zaagbescherming als je zaagt.', 'Werkschoenen en zaaglaarzen', ['EN ISO 20345', 'EN ISO 17249']),
        ],
        'kenners': [
            {'nr': '01', 'kop': 'Een gaas voor je gezicht, een bril eronder.', 'tekst': 'Een gaasvizier houdt takken en steentjes tegen, fijne splinters niet altijd. Draag er een bril onder.'},
            {'nr': '02', 'kop': 'Een zaagbroek werkt alleen als hij past.', 'tekst': 'Te ruim of te kort en de bescherming zit niet waar de zaag komt. Pas hem in de showroom.'},
            {'nr': '03', 'kop': 'Profiel dat modder loslaat.', 'tekst': 'Een zool die dichtslibt geeft geen grip. Kies een profiel dat modder loslaat, op een nat talud merk je het verschil.'},
        ],
        'pakket': ['Werkbroek', 'Regenpak', 'Helm met vizier en oorkappen', 'Zaagbroek', 'Werkhandschoenen', 'Veiligheidsbril', 'Werkschoenen'],
        'producten': [prod('Kleding', 'Snickers Workwear', 'Werkbroek'), prod('Kleding', '[MERK]', 'Regenpak'), prod('Kleding', '[MERK]', 'Zaagbroek'),
                      prod('PBM', 'KASK', 'Bosbouwhelm met vizier'), prod('Handschoenen', '[MERK]', 'Werkhandschoen'), prod('Schoenen', '[MERK]', 'Zaaglaars')],
        'vragen': [
            {'vraag': 'Welke zaagbroek heb ik nodig?', 'antwoord': 'Dat hangt af van je zaag en hoe je zaagt. Zaagbroeken worden getest in klassen. Wij kijken met je mee en laten je passen.'},
            {'vraag': 'Kan ik gewone werkschoenen dragen bij zagen?', 'antwoord': 'Voor werk met de kettingzaag zijn er schoenen en laarzen met zaagbescherming. Die raden wij aan.'},
            {'vraag': 'Hoe lang gaat een helm mee?', 'antwoord': 'Kijk naar de datum in de helm en de aanwijzingen van de maker. Na een flinke klap vervang je hem altijd.'},
        ],
    },
}

SCHILDER = {
    'k': 'schilder', 'naam': 'schilders', 'titel': 'Schildersgoed', 'persoon': 'schilder', 'mv': 'schilders',
    'regel': 'Verf, stof, dampen en uren op de trap. Wij weten wat een schilder nodig heeft, binnen en buiten.',
    'fotoplek': 'Een schilder op de steiger in witte werkkleding.',
    'dagintro': 'Van afplakken tot opleveren. Binnen en buiten.',
    'dagfoto': 'Een schilder die een kozijn schuurt, met stofmasker.',
    'data': {
        'persoon': 'schilder', 'mv': 'schilders',
        'taken': [
            {'naam': 'Binnen schilderen', 'risicos': risicos('damp', 'knielen'), 'tip': 'Ademende, wasbare kleding en kniestukken voor de plinten.', 'pakket': 'schildersbroek, polo, kniestukken.'},
            {'naam': 'Schuren', 'risicos': risicos('stof', 'lawaai'), 'tip': 'Schuurstof van oude verf wil je niet inademen. Afzuiging aan de schuurmachine en een stofmasker.', 'pakket': 'stofmasker FFP2 of FFP3, veiligheidsbril.'},
            {'naam': 'Spuiten', 'risicos': risicos('damp', 'ogen'), 'tip': 'Bij spuiten heb je adembescherming met het juiste filter nodig. Wij kijken mee welk filter bij jouw verf past.', 'pakket': 'halfgelaatsmasker met filter, overall, nitril handschoenen.'},
            {'naam': 'Buiten op de steiger', 'risicos': risicos('hoogte', 'regen'), 'tip': 'Wind, regen en een steiger. Een schildersjas die ademt en schoenen met grip.', 'pakket': 'schildersjas, werkschoenen met grip.'},
        ],
        'momenten': [
            {'tijd': '07:30', 'titel': 'Afplakken en afdekken', 'tekst': 'Op je knieën langs de plinten.', 'risicos': ['knielen'], 'goed': ['Kniestukken', 'Schildersbroek']},
            {'tijd': '09:00', 'titel': 'Schuren', 'tekst': 'Fijn stof van oude verflagen.', 'risicos': ['stof'], 'goed': ['Stofmasker', 'Veiligheidsbril']},
            {'tijd': '11:00', 'titel': 'Gronden en lakken', 'tekst': 'Dampen in een kleine ruimte. Ramen open, masker op als het moet.', 'risicos': ['chemie'], 'goed': ['Halfgelaatsmasker', 'Nitril handschoenen']},
            {'tijd': '13:30', 'titel': 'De steiger op', 'tekst': 'Buitenwerk aan de kozijnen.', 'risicos': ['hoogte', 'regen'], 'goed': ['Schildersjas', 'Werkschoenen met grip']},
            {'tijd': '15:30', 'titel': 'Kwasten uitwassen', 'tekst': 'Verdunner en verf op je handen.', 'risicos': ['chemie'], 'goed': ['Nitril handschoenen']},
        ],
        'zones': [
            zone('ogen', 'Ogen', 'Spatten als je boven je hoofd werkt, stof bij schuren.', 'Veiligheidsbrillen', ['EN 166']),
            zone('adem', 'Adem', 'Tegen schuurstof een FFP-masker, tegen dampen een masker met koolfilter.', 'Stofmaskers en halfgelaatsmaskers', ['EN 149', 'EN 14387']),
            zone('romp', 'Romp', 'Ademend en wasbaar. Wit, zodat je ziet waar je tegenaan zat.', 'Schildersjassen en polo\'s', []),
            zone('handen', 'Handen', 'Nitril tegen verf en oplosmiddel.', 'Chemiebestendige handschoenen', ['EN ISO 374']),
            zone('knieen', 'Knieën', 'Kniestukken voor plinten en vloeren.', 'Kniestukken', ['EN 14404']),
            zone('voeten', 'Voeten', 'Een lichte schoen met grip op de trap en de steiger.', 'Werkschoenen', ['EN ISO 20345']),
        ],
        'kenners': [
            {'nr': '01', 'kop': 'Wit is niet alleen traditie.', 'tekst': 'Op wit zie je meteen waar je tegen natte verf hebt gezeten. Zo neem je het niet mee naar de volgende kamer.'},
            {'nr': '02', 'kop': 'Een stofmasker is geen dampmasker.', 'tekst': 'Tegen schuurstof helpt een FFP-masker. Tegen dampen van oplosmiddel heb je een masker met koolfilter nodig.'},
            {'nr': '03', 'kop': 'Nitril, geen latex.', 'tekst': 'Nitril houdt veel verven en oplosmiddelen goed tegen en geeft minder kans op allergie dan latex.'},
        ],
        'pakket': ['Schildersbroek', 'Schildersjas', 'Polo', 'Overall', 'Kniestukken', 'Nitril handschoenen', 'Stofmasker', 'Halfgelaatsmasker met filter', 'Veiligheidsbril', 'Werkschoenen'],
        'producten': [prod('Kleding', '[MERK]', 'Schildersbroek'), prod('Kleding', '[MERK]', 'Schildersjas'), prod('Kleding', '[MERK]', 'Overall wit'),
                      prod('PBM', 'BLS', 'Halfgelaatsmasker'), prod('Handschoenen', '[MERK]', 'Nitril handschoen'), prod('Schoenen', '[MERK]', 'Lichte werkschoen')],
        'vragen': [
            {'vraag': 'Welk filter heb ik nodig bij spuiten?', 'antwoord': 'Dat hangt af van de verf en het oplosmiddel. Neem het product of het veiligheidsblad mee, dan zoeken we het juiste filter.'},
            {'vraag': 'Op hoeveel graden was ik schilderskleding?', 'antwoord': 'Volg het waslabel. Verfvlekken eerst voorbehandelen werkt beter dan heter wassen.'},
            {'vraag': 'Hebben jullie ook kniestukken voor schildersbroeken?', 'antwoord': 'Ja. Neem je broek mee of noem het merk, dan zoeken we een kniestuk dat past.'},
        ],
    },
}

ALLE = [TECHNIEK, MAGAZIJN, CHAUFFEUR, GROEN, SCHILDER]
