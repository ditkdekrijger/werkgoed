LOGO = '/_blob/4ae74013851478061537ab80687f318f'
LOGO_WIT = '/_blob/dd24f422379e7ed500375de8e10eb692'
IMG = {
    'team': '/_blob/aa66271e9f65dd927ab58f85b6b7b34e', 'showroom': '/_blob/6bdd95d6ecbd918a1370a9976eb22927',
    'kask': '/_blob/194eef2839742df9f5a62e3be4fd04a3', 'dassy': '/_blob/ba871752485c5a0ec3eb9a47f5a0e42b',
    'softshell': '/_blob/5352b1286406cabb986dd27508640452',
    'cat-schoenen': '/_blob/3fa09de26265afb3a92ed90702a867ce', 'cat-kleding': '/_blob/bb9730ca26aab2baa20074ae290bce05',
    'cat-handschoenen': '/_blob/576c366d46fdf08e691f351a8af86916', 'cat-pbm': '/_blob/69d3bb3a4c5c22bc3a90957a583a6813',
    'p-haix': '/_blob/46f4364adf2c6fcdde83e26778323e9f', 'p-handschoen': '/_blob/0253301706a21c19007a14f946f956f5',
    'p-havep': '/_blob/86877bea416e24339641f118d529da85', 'p-solidgear': '/_blob/b6cb072cf00b07c1c4b5979c78adf5a4',
}
MERK_LOGO = {
    'HAIX': '/_blob/ea570573ef87b8cab77592de82ad327a', 'Havep': '/_blob/f56842a87f12f497d2c61b2490da4075',
    'KASK': '/_blob/e124e7d3d2a0775e17ca8e38ae4a34e3', 'LOWA Work': '/_blob/ddc8f69f618971cb1c3beab339d5e0d7',
    'PUMA Safety': '/_blob/d9309ee79d0d07965b2775c1a3f602bf', 'Santino': '/_blob/23ff82094926bae989f72f53e530eaa7',
    'Snickers Workwear': '/_blob/1ecab9d540eee71e5d4c87291c076d45', 'Tricorp Workwear': '/_blob/482924746975dedfc61ad3b37b5c4211',
}

HEAD = '''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>[[TITLE]]</title>
<script src="./support.js"></script>
<link rel="stylesheet" href="ds/wg/tokens.css">
<link rel="stylesheet" href="ds/wg/components/bundle.css">
<script src="ds/wg/components/bundle.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&display=swap">
<style>
body{margin:0;background:#ffffff;color:#16212c;font-family:"Archivo",system-ui,-apple-system,"Segoe UI",sans-serif}
a{color:inherit;text-decoration:none}
.wg-display{font-size:clamp(52px,8vw,124px)}
.wg-mega{font-size:clamp(84px,14vw,216px)}
.wg-h2{font-size:clamp(34px,4.6vw,68px)}
.wg-nav a:hover,.wg-nav a[aria-current="page"]{text-decoration:underline;text-decoration-color:#ff6a13;text-decoration-thickness:3px;text-underline-offset:6px}
.wg-ul:hover{text-decoration:underline;text-decoration-color:#ff6a13;text-decoration-thickness:2px;text-underline-offset:4px}
.wg-tile:hover{border-color:#16212c}
.wg-pill:hover{border-color:#16212c}
.wg-menuknop:hover{border-color:#ff6a13}
.wg-iconknop:hover{border-color:#16212c}
.wg-mega-toep:hover{background:#f5f3ee}
.wg-faq summary{list-style:none;cursor:pointer}
.wg-faq summary::-webkit-details-marker{display:none}
.wg-faq[open] .wg-faq-plus{transform:rotate(45deg)}
.wg-step:hover{background:#16212c;color:#ffffff}
.wg-foto{display:block;width:100%;height:100%;object-fit:cover}
</style>
</helmet>
<div style="--gutter:clamp(20px,4.2vw,72px);width:100%;max-width:1440px;margin:0 auto;box-sizing:border-box;background:var(--surface);color:var(--ink);font-family:var(--font-sans)">
'''


def ico(naam, size=20):
    return '<x-import component-from-global-scope="Werkgoed.Icoon" naam="%s" size="%d"></x-import>' % (naam, size)


MEGA_SOORT = [
    ('jas', 'Werkkleding', ['Jassen', 'Broeken', 'Overalls', 'Shirts en truien', 'Softshells en bodywarmers', 'Regenkleding', 'Signaalkleding']),
    ('schoen', 'Werkschoenen', ['Lage werkschoenen', 'Hoge werkschoenen', 'Laarzen', 'Inlegzolen', 'Voetscan en maat']),
    ('handschoen', 'Werkhandschoenen', ['Montage', 'Snijbestendig', 'Lassen', 'Chauffeurs', 'Winter']),
    ('helm', 'PBM', ['Helmen', 'Gehoorbescherming', 'Adembescherming', 'Veiligheidsbrillen', 'Valbeveiliging']),
]
MEGA_MERKEN = ['HAIX', 'LOWA Work', 'Sixton', 'Solid Gear', 'Grisport Safety', 'PUMA Safety', 'Redbrick', 'Snickers Workwear', 'Tricorp Workwear', 'Santino', 'Dassy', 'Havep', 'BLS', 'KASK']
MEGA_TOEP = [('las', 'Lasser', 'Lasgoed.dc.html'), ('straat', 'Stratenmaker', 'Straatgoed.dc.html'), ('bouw', 'Bouwer', 'Bouwgoed.dc.html'),
             ('techniek', 'Monteur', 'Techniekgoed.dc.html'), ('magazijn', 'Magazijnmedewerker', 'Magazijngoed.dc.html'), ('chauffeur', 'Chauffeur', 'Chauffeursgoed.dc.html'), ('groen', 'Hovenier', 'Groengoed.dc.html'), ('schilder', 'Schilder', 'Schildersgoed.dc.html')]


def mega():
    kol = []
    for icn, kop, items in MEGA_SOORT:
        li = ''.join('<li><a class="wg-ul" href="Categorie.dc.html">%s</a></li>' % x for x in items)
        kol.append('<div style="display:flex;flex-direction:column;gap:14px"><span style="display:flex;align-items:center;gap:10px;font:700 18px/1.2 var(--font-sans);font-variation-settings:\'wdth\' 90">'
                   + ico(icn, 24) + kop + '</span><ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px;font:500 16px/1.3 var(--font-sans)">' + li + '</ul></div>')
    merken = ''.join('<li><a class="wg-ul" href="Merken.dc.html">%s</a></li>' % m for m in MEGA_MERKEN)
    toep = ''.join('<li><a class="wg-mega-toep" href="%s" style="display:flex;align-items:center;gap:12px;min-height:44px;padding:0 10px;border-radius:var(--radius-sm);font:600 16px/1.2 var(--font-sans)">'
                   '<span style="display:grid;place-items:center;width:32px;height:32px;border-radius:50%%;background:var(--beroep-%s);color:var(--beroep-%s-deep)">%s</span>%s</a></li>'
                   % (h, k, k, ico(k, 18), n) for k, n, h in MEGA_TOEP)
    return '''
<!-- uitklapmenu assortiment -->
<div id="assortiment" style="display:{{menuDisplay}};position:absolute;left:0;right:0;top:100%;z-index:20;background:var(--surface);color:var(--ink);border-top:1px solid var(--line);border-bottom:3px solid var(--vlam)">
<div style="display:flex;flex-wrap:wrap;gap:40px 40px;padding:40px var(--gutter) 48px">
<div style="flex:3 1 600px;min-width:0;display:flex;flex-direction:column;gap:24px">
<span class="wg-label" style="color:var(--ink-muted)">soort</span>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:32px 24px">''' + ''.join(kol) + '''</div>
</div>
<div style="flex:1 1 230px;min-width:0;display:flex;flex-direction:column;gap:24px;border-left:1px solid var(--line);padding-left:32px">
<span class="wg-label" style="color:var(--ink-muted)">merken</span>
<ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 20px;font:500 16px/1.3 var(--font-sans)">''' + merken + '''</ul>
<a class="wg-ul" href="Merken.dc.html" style="font:600 16px/1.3 var(--font-sans)">Alle merken →</a>
</div>
<div style="flex:1 1 240px;min-width:0;display:flex;flex-direction:column;gap:16px;border-left:1px solid var(--line);padding-left:32px">
<span class="wg-label" style="color:var(--ink-muted)">toepassing</span>
<ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:2px">''' + toep + '''</ul>
</div>
<a href="Showroom.dc.html" style="position:relative;flex:1 1 220px;min-width:0;max-width:300px;min-height:320px;border-radius:var(--radius-card);overflow:hidden;color:var(--on-night)">
<img class="wg-foto" src="''' + IMG['showroom'] + '''" alt="" style="position:absolute;inset:0">
<span style="position:absolute;left:0;right:0;bottom:0;padding:20px;display:flex;flex-direction:column;gap:6px;background:var(--marine)">
<span class="wg-label" style="color:var(--on-night-muted)">showroom</span>
<span style="font:700 22px/1.1 var(--font-sans);font-variation-settings:'wdth' 90">Pas je werkschoen bij ons in Hardinxveld</span>
</span>
</a>
</div>
</div>
'''


def topbar_header(active):
    nav_links = [('Per beroep', 'Main.dc.html#beroep'), ('Merken', 'Merken.dc.html'), ('Showroom', 'Showroom.dc.html'), ('Advies', 'tel:0184701212')]
    links = ''.join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if n == active else '', n) for n, h in nav_links)

    def usp(i, t):
        return '<span style="display:inline-flex;align-items:center;gap:8px">' + ico(i, 16) + t + '</span>'
    return '''
<!-- topbalk -->
<div class="wg-night" style="background:var(--marine);color:var(--on-night);font:500 13px/1.3 var(--font-sans)">
<div style="display:flex;flex-wrap:wrap;gap:6px 32px;justify-content:space-between;padding:10px var(--gutter)">
<div style="display:flex;flex-wrap:wrap;gap:4px 24px;color:var(--on-night-muted)">''' + usp('voorraad', 'Uit voorraad leverbaar') + usp('levering', 'Snelle levering') + usp('verzending', 'Gratis verzending vanaf €100 excl. btw') + '''</div>
<div style="display:flex;flex-wrap:wrap;gap:4px 24px;color:var(--on-night-muted)">''' + usp('klok', 'Showroom open van 08:30 tot 17:30') + '''<a href="tel:0184701212" style="display:inline-flex;align-items:center;gap:8px;color:var(--on-night)">''' + ico('telefoon', 16) + '''0184-701212</a></div>
</div>
</div>

<!-- header -->
<header style="position:relative;display:flex;flex-wrap:wrap;align-items:center;gap:16px 36px;padding:18px var(--gutter);border-bottom:1px solid var(--line)">
<a href="Main.dc.html" aria-label="Werkgoed, naar de homepage" style="display:block;line-height:0"><img src="''' + LOGO + '''" alt="Werkgoed, werkt beter" style="height:52px;width:auto"></a>
<nav class="wg-nav" aria-label="Hoofdmenu" style="display:flex;flex-wrap:wrap;align-items:center;gap:8px 28px;font:600 16px/1.3 var(--font-sans);flex:1 1 420px">
<button type="button" class="wg-menuknop" aria-expanded="{{menuOpen}}" aria-controls="assortiment" onClick="{{toggleMenu}}" style="display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 14px 0 16px;border-radius:var(--radius-pill);border:1px solid {{menuRand}};background:{{menuBg}};color:{{menuKleur}};font:600 16px/1 var(--font-sans);cursor:pointer">''' + ico('menu', 20) + '''Assortiment<span style="display:inline-flex;transform:{{menuDraai}}">''' + ico('omlaag', 18) + '''</span></button>
''' + links + '''
</nav>
<div style="display:flex;flex-wrap:wrap;gap:10px;align-items:center">
<label style="display:flex;align-items:center;gap:10px;border:1px solid var(--line-strong);border-radius:var(--radius-pill);padding:0 18px;height:48px;min-width:220px;box-sizing:border-box;color:var(--ink-muted)">''' + ico('zoek', 20) + '''<span style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">Zoek</span>
<input type="search" placeholder="Zoek schoen, jas of merk" style="border:0;outline:0;background:transparent;font:400 15px var(--font-sans);color:var(--ink);flex:1;min-width:0;height:44px">
</label>
<a href="#" class="wg-iconknop" aria-label="Klantportaal" style="display:grid;place-items:center;width:48px;height:48px;border-radius:50%;border:1px solid var(--line-strong)">''' + ico('account', 22) + '''</a>
<a href="Winkelwagen.dc.html" class="wg-iconknop" aria-label="Winkelwagen, 2 artikelen" style="position:relative;display:grid;place-items:center;width:48px;height:48px;border-radius:50%;background:var(--marine);color:var(--on-night)">''' + ico('wagen', 22) + '''<span aria-hidden="true" style="position:absolute;top:-2px;right:-2px;display:grid;place-items:center;min-width:20px;height:20px;padding:0 5px;box-sizing:border-box;border-radius:10px;background:var(--vlam);color:var(--on-vlam);font:700 12px/1 var(--font-sans)">2</span></a>
</div>
''' + mega() + '''</header>
'''


FOOTER = '''
<!-- footer -->
<footer class="wg-night" style="background:var(--marine);color:var(--on-night);padding:0 var(--gutter) 40px">
<div style="display:flex;flex-wrap:wrap;gap:40px 64px;padding:56px 0 48px">
<div style="flex:1 1 200px;display:flex;flex-direction:column;gap:12px;font:400 16px/1.4 var(--font-sans)">
<span class="wg-label" style="color:var(--on-night-muted)">per beroep</span>
<a class="wg-ul" href="Lasgoed.dc.html">Lasgoed</a><a class="wg-ul" href="Straatgoed.dc.html">Straatgoed</a><a class="wg-ul" href="Bouwgoed.dc.html">Bouwgoed</a><a class="wg-ul" href="Techniekgoed.dc.html">Techniekgoed</a><a class="wg-ul" href="Magazijngoed.dc.html">Magazijngoed</a><a class="wg-ul" href="Chauffeursgoed.dc.html">Chauffeursgoed</a><a class="wg-ul" href="Groengoed.dc.html">Groengoed</a><a class="wg-ul" href="Schildersgoed.dc.html">Schildersgoed</a>
</div>
<div style="flex:1 1 200px;display:flex;flex-direction:column;gap:12px;font:400 16px/1.4 var(--font-sans)">
<span class="wg-label" style="color:var(--on-night-muted)">assortiment</span>
<a class="wg-ul" href="Categorie.dc.html">Werkschoenen</a><a class="wg-ul" href="Categorie.dc.html">Werkkleding</a><a class="wg-ul" href="Categorie.dc.html">Werkhandschoenen</a><a class="wg-ul" href="Categorie.dc.html">Persoonlijke beschermingsmiddelen</a><a class="wg-ul" href="Merken.dc.html">Merken</a><a class="wg-ul" href="Showroom.dc.html">Showroom en voetscan</a>
</div>
<div style="flex:1 1 200px;display:flex;flex-direction:column;gap:12px;font:400 16px/1.4 var(--font-sans)">
<span class="wg-label" style="color:var(--on-night-muted)">klantenservice</span>
<a class="wg-ul" href="#">Over Werkgoed</a><a class="wg-ul" href="#">Verzending en levering</a><a class="wg-ul" href="#">Retourneren en ruilen</a><a class="wg-ul" href="#">Haix maattabel</a><a class="wg-ul" href="#">Klachten en feedback</a>
</div>
<div style="flex:1 1 200px;display:flex;flex-direction:column;gap:12px;font:400 16px/1.4 var(--font-sans)">
<span class="wg-label" style="color:var(--on-night-muted)">onze webshops</span>
<a class="wg-ul" href="#">Haix werkschoenen</a><a class="wg-ul" href="#">LOWA werkschoenen</a><a class="wg-ul" href="#">Cofra werkschoenen</a><a class="wg-ul" href="#">BLS adembescherming</a>
</div>
<div style="flex:1 1 220px;display:flex;flex-direction:column;gap:14px;font:400 16px/1.4 var(--font-sans)">
<span class="wg-label" style="color:var(--on-night-muted)">contact</span>
<span style="display:flex;gap:10px">''' + ico('locatie', 20) + '''<span>Wiedhaak 1<br>3371 KD Hardinxveld-Giessendam</span></span>
<a class="wg-ul" href="tel:0184701212" style="display:flex;gap:10px;align-items:center">''' + ico('telefoon', 20) + '''0184-701212</a>
<a class="wg-ul" href="mailto:info@werkgoed.nl" style="display:flex;gap:10px;align-items:center">''' + ico('mail', 20) + '''info@werkgoed.nl</a>
</div>
</div>
<div style="display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:24px;padding:8px 0 40px">
<img src="''' + LOGO_WIT + '''" alt="Werkgoed, werkt beter" style="height:clamp(56px,7vw,96px);width:auto">
<span style="font:700 clamp(28px,3.4vw,48px)/1.02 var(--font-sans);font-variation-settings:'wdth' 90;letter-spacing:-.03em;max-width:16ch;text-align:right">Past altijd goed. Bij &rsquo;t werk wat je doet.</span>
</div>
<div style="display:flex;flex-wrap:wrap;gap:12px 32px;justify-content:space-between;border-top:1px solid rgba(255,255,255,.2);padding-top:24px;font:400 14px/1.4 var(--font-sans);color:var(--on-night-muted)">
<span>2026 Werkgoed bedrijfskleding en PBM</span>
<span style="display:flex;flex-wrap:wrap;gap:8px 24px"><a class="wg-ul" href="#">Privacy en disclaimer</a><a class="wg-ul" href="#">Cookies</a><a class="wg-ul" href="#">Instagram</a><a class="wg-ul" href="#">LinkedIn</a><a class="wg-ul" href="#">YouTube</a></span>
</div>
</footer>

</div>
</x-dc>
'''

MENU_JS = '''      menuOpen: s.menu ? 'true' : 'false',
      menuDisplay: s.menu ? 'block' : 'none',
      menuBg: s.menu ? 'var(--marine)' : 'transparent',
      menuKleur: s.menu ? 'var(--on-night)' : 'var(--ink)',
      menuRand: s.menu ? 'var(--marine)' : 'var(--ink)',
      menuDraai: s.menu ? 'rotate(180deg)' : 'none',
      toggleMenu: () => this.setState({ menu: !s.menu }),
'''

BEROEPEN = [
    {'k': 'las', 'naam': 'las', 'href': 'Lasgoed.dc.html', 'regel': 'Vonken, spatten, hitte en lasrook.', 'risicos': ['vonk', 'hitte', 'stof']},
    {'k': 'straat', 'naam': 'straat', 'href': 'Straatgoed.dc.html', 'regel': 'Op je knieën, langs de weg, in elk weer.', 'risicos': ['zicht', 'knielen', 'regen']},
    {'k': 'bouw', 'naam': 'bouw', 'href': 'Bouwgoed.dc.html', 'regel': 'Hoogte, stof en lawaai op de bouwplaats.', 'risicos': ['hoogte', 'stof', 'lawaai']},
    {'k': 'techniek', 'naam': 'techniek', 'href': 'Techniekgoed.dc.html', 'regel': 'Kruipen, knielen en precies werken.', 'risicos': ['knielen', 'snijden', 'zicht']},
    {'k': 'magazijn', 'naam': 'magazijn', 'href': 'Magazijngoed.dc.html', 'regel': 'Tussen pallets, heftrucks en koude hallen.', 'risicos': ['zicht', 'kou', 'snijden']},
    {'k': 'chauffeur', 'naam': 'chauffeurs', 'href': 'Chauffeursgoed.dc.html', 'regel': 'Urenlang rijden, laden en lossen.', 'risicos': ['zicht', 'kou', 'snijden']},
    {'k': 'groen', 'naam': 'groen', 'href': 'Groengoed.dc.html', 'regel': 'Buiten met machines, takken en weer.', 'risicos': ['lawaai', 'regen', 'snijden']},
    {'k': 'schilder', 'naam': 'schilders', 'href': 'Schildersgoed.dc.html', 'regel': 'Spatten, dampen en lange dagen op de trap.', 'risicos': ['chemie', 'stof', 'hoogte']},
]
