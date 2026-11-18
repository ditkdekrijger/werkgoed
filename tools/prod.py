# Echte producten van werkgoed.nl/werkkleding (opgehaald 18 november 2026). Prijzen excl. en incl. btw zoals op de site.
P = {
    'engel4202': {'merk': 'F. Engel', 'naam': 'Extend Winteroverall met reflectie Engel 4202', 'prijsEx': '€244,00', 'prijsIn': '€295,24', 'foto': '/_blob/204645d09f367abc90dc12926f849eef'},
    'engel1871': {'merk': 'F. Engel', 'naam': 'FE Engel Cargo winterjas 1871', 'prijsEx': '€167,50', 'prijsIn': '€202,68', 'foto': '/_blob/bfde7c2dbd00aec17ed36180aa467c52'},
    'snickers1112': {'merk': 'Snickers Workwear', 'naam': 'Waterdichte Winterjas Snickers Workwear 1112', 'prijsEx': '€218,95', 'prijsIn': '€264,93', 'foto': '/_blob/3763245c92e34c3c85f6582fd694ce17'},
    'havep50171': {'merk': 'Havep', 'naam': 'Waterdichte parka Havep Attitude 50171', 'prijsEx': '€133,02', 'prijsIn': '€160,95', 'foto': '/_blob/b9088d800dba9dc9f2e2933d7690537b'},
    'oxxapilot': {'merk': 'OXXA', 'naam': 'OXXA Pilotjack marineblauw', 'prijsEx': '€34,95', 'prijsIn': '€42,29', 'foto': '/_blob/5d940d2a8717f82445d914ce88d558a8'},
    'dassynordix': {'merk': 'Dassy', 'naam': 'Winterjas Dassy Nordix', 'prijsEx': '€176,50', 'prijsIn': '€213,57', 'foto': '/_blob/eb1e62054fb30ab0b066013d57f48c0c'},
    'dassypulse': {'merk': 'Dassy', 'naam': 'Sweatshirtjas Dassy Pulse', 'prijsEx': '€75,40', 'prijsIn': '€91,23', 'foto': '/_blob/009087d02778359673056519da6999e3'},
    'dassyaustin': {'merk': 'Dassy', 'naam': 'Winterjas Dassy Austin Canvas', 'prijsEx': '€114,90', 'prijsIn': '€139,03', 'foto': '/_blob/08214389e2211cabaaa82fb6bfafe119'},
    'portwesthoodie': {'merk': 'Portwest', 'naam': 'Hoodie met rits zwart Portwest', 'prijsEx': '€27,50', 'prijsIn': '€33,28', 'foto': '/_blob/2d6633d1a72860d4a9fe1686f6c4fb8c'},
    'dassyhelix': {'merk': 'Dassy', 'naam': 'Werkbroek Dassy Helix', 'prijsEx': '€72,80', 'prijsIn': '€88,09', 'foto': '/_blob/c49bbd5024ddde5b363ae962433bab89'},
    'oxxawaldo': {'merk': 'OXXA', 'naam': 'PU Stretch Regenpak OXXA Waldo 5100', 'prijsEx': '€34,95', 'prijsIn': '€42,29', 'foto': '/_blob/2e242e27ad1ab396798933b367fcc2e9'},
    'carthago': {'merk': 'Carthago', 'naam': 'Softshell jas Carthago Proteq', 'prijsEx': '€49,95', 'prijsIn': '€60,44', 'foto': '/_blob/ebc859a68ae16820bfe687fbdcfc4bae'},
    'oxxamalia': {'merk': 'OXXA', 'naam': 'Vlamvertragende antistatische overall OXXA Malia 5320', 'prijsEx': '€46,00', 'prijsIn': '€55,66', 'foto': '/_blob/d5e82d63a237980fdc196e2d16eef793'},
    'snickers6371': {'merk': 'Snickers Workwear', 'naam': 'Full Stretch Werkbroek Snickers Workwear 6371', 'prijsEx': '€134,50', 'prijsIn': '€162,75', 'foto': '/_blob/b0685efeebc90cc497767271ef6439ef'},
    'havep10094': {'merk': 'Havep', 'naam': 'Poloshirt Havep 10094', 'prijsEx': '€20,95', 'prijsIn': '€25,35', 'foto': '/_blob/aab429eb9a88b57d7f250de40f12ac81'},
    'havep80626': {'merk': 'Havep', 'naam': 'Werkbroek met Stretch Havep RWS+ 80626', 'prijsEx': '€72,95', 'prijsIn': '€88,27', 'foto': '/_blob/b2ced15d815f2d0aecab424acbcb834e'},
    'snickers9110': {'merk': 'Snickers Workwear', 'naam': 'Kniebeschermers Snickers Workwear 9110', 'prijsEx': '€26,75', 'prijsIn': '€32,37', 'foto': '/_blob/366ea3a7a7ad12657a7e202a58ebb898'},
    'klmoverall': {'merk': '', 'naam': 'Kwaliteitsoverall met kniezakken (KLM-imitatie) 100% katoen', 'prijsEx': '€42,75', 'prijsIn': '€51,73', 'foto': '/_blob/ee0220e8053545eb882d681ffc4fe2b3'},
    'portwestrws': {'merk': 'Portwest', 'naam': 'Portwest RWS Sweater met Capuchon', 'prijsEx': '€44,96', 'prijsIn': '€54,40', 'foto': '/_blob/d5ad0e5b5c5143346a924e207726b008'},
    'havep50461': {'merk': 'Havep', 'naam': 'Revolve Softshell jack Havep 50461', 'prijsEx': '€109,95', 'prijsIn': '€133,04', 'foto': '/_blob/6cedb06a9e98d8cb409f919c99350264'},
}
def p(k, **extra):
    d = dict(P[k]); d.update(extra); return d
