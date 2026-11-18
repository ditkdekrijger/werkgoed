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
.wg-tile:hover{border-color:#16212c;background:#f5f3ee}
.wg-pill:hover{border-color:#16212c}
.wg-faq summary{list-style:none;cursor:pointer}
.wg-faq summary::-webkit-details-marker{display:none}
.wg-faq[open] .wg-faq-plus{transform:rotate(45deg)}
.wg-step:hover{background:#16212c;color:#ffffff}
</style>
</helmet>
<div style="--gutter:clamp(20px,4.2vw,72px);width:100%;max-width:1440px;margin:0 auto;box-sizing:border-box;background:var(--surface);color:var(--ink);font-family:var(--font-sans)">
'''

def topbar_header(active):
    nav = [('Per beroep', 'Main.dc.html#beroep'), ('Werkkleding', 'Main.dc.html#soort'), ('Werkschoenen', 'Main.dc.html#soort'),
           ('Handschoenen', 'Main.dc.html#soort'), ('PBM', 'Main.dc.html#soort'), ('Merken', 'Main.dc.html#merken'), ('Showroom', 'Main.dc.html#showroom')]
    links = ''.join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if n == active else '', n) for n, h in nav)
    return '''
<!-- topbalk -->
<div class="wg-night" style="background:var(--marine);color:var(--on-night);font:500 13px/1.3 var(--font-sans)">
<div style="display:flex;flex-wrap:wrap;gap:6px 32px;justify-content:space-between;padding:10px var(--gutter)">
<div style="display:flex;flex-wrap:wrap;gap:4px 24px;color:var(--on-night-muted)"><span>Uit voorraad leverbaar</span><span>Snelle levering</span><span>Gratis verzending vanaf €100 excl. btw</span></div>
<div style="display:flex;flex-wrap:wrap;gap:4px 24px;color:var(--on-night-muted)"><span>Showroom open van 08:30 tot 17:30</span><a href="tel:0184701212" style="color:var(--on-night)">0184-701212</a></div>
</div>
</div>

<!-- header -->
<header style="display:flex;flex-wrap:wrap;align-items:center;gap:16px 32px;padding:20px var(--gutter);border-bottom:1px solid var(--line)">
<a href="Main.dc.html" aria-label="Werkgoed, naar de homepage" style="display:flex;flex-direction:column;line-height:1">
<span style="font:800 34px/1 var(--font-sans);font-variation-settings:'wdth' 90;letter-spacing:-.045em">werkgoed<span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--signal);margin-left:3px"></span></span>
<span class="wg-small" style="color:var(--ink-muted);margin-top:4px">bedrijfskleding &amp; PBM</span>
</a>
<nav class="wg-nav" aria-label="Hoofdmenu" style="display:flex;flex-wrap:wrap;gap:8px 28px;font:600 16px/1.3 var(--font-sans);flex:1 1 420px">
''' + links + '''
</nav>
<div style="display:flex;flex-wrap:wrap;gap:12px;align-items:center">
<label style="display:flex;align-items:center;gap:8px;border:1px solid var(--line-strong);border-radius:var(--radius-pill);padding:0 20px;height:48px;min-width:200px;box-sizing:border-box">
<span class="wg-small" style="color:var(--ink-muted)">Zoek</span>
<input type="search" placeholder="schoen, jas, handschoen" style="border:0;outline:0;background:transparent;font:400 15px var(--font-sans);color:var(--ink);flex:1;min-width:0;height:44px">
</label>
<x-import component-from-global-scope="Werkgoed.Button" variant="outline" arrow="{{no}}" href="#">Klantportaal</x-import>
<x-import component-from-global-scope="Werkgoed.Button" variant="ink" arrow="{{no}}" href="#">Winkelwagen</x-import>
</div>
</header>
'''

FOOTER = '''
<!-- footer -->
<footer class="wg-night" style="background:var(--marine);color:var(--on-night);padding:0 var(--gutter) 40px">
<div style="display:flex;flex-wrap:wrap;gap:40px 64px;padding:56px 0 48px">
<div style="flex:1 1 200px;display:flex;flex-direction:column;gap:12px;font:400 16px/1.4 var(--font-sans)">
<span class="wg-label" style="color:var(--on-night-muted)">per beroep</span>
<a class="wg-ul" href="Lasgoed.dc.html">Lasgoed</a><a class="wg-ul" href="Straatgoed.dc.html">Straatgoed</a><a class="wg-ul" href="Bouwgoed.dc.html">Bouwgoed</a><a class="wg-ul" href="Main.dc.html#beroep">Alle beroepen</a>
</div>
<div style="flex:1 1 200px;display:flex;flex-direction:column;gap:12px;font:400 16px/1.4 var(--font-sans)">
<span class="wg-label" style="color:var(--on-night-muted)">assortiment</span>
<a class="wg-ul" href="#">Werkschoenen</a><a class="wg-ul" href="#">Werkkleding</a><a class="wg-ul" href="#">Werkhandschoenen</a><a class="wg-ul" href="#">Persoonlijke beschermingsmiddelen</a><a class="wg-ul" href="#">Diensten</a>
</div>
<div style="flex:1 1 200px;display:flex;flex-direction:column;gap:12px;font:400 16px/1.4 var(--font-sans)">
<span class="wg-label" style="color:var(--on-night-muted)">klantenservice</span>
<a class="wg-ul" href="#">Over Werkgoed</a><a class="wg-ul" href="#">Verzending en levering</a><a class="wg-ul" href="#">Retourneren en ruilen</a><a class="wg-ul" href="#">Haix maattabel</a><a class="wg-ul" href="#">Klachten en feedback</a>
</div>
<div style="flex:1 1 200px;display:flex;flex-direction:column;gap:12px;font:400 16px/1.4 var(--font-sans)">
<span class="wg-label" style="color:var(--on-night-muted)">onze webshops</span>
<a class="wg-ul" href="#">Haix werkschoenen</a><a class="wg-ul" href="#">LOWA werkschoenen</a><a class="wg-ul" href="#">Cofra werkschoenen</a><a class="wg-ul" href="#">BLS adembescherming</a>
</div>
<div style="flex:1 1 200px;display:flex;flex-direction:column;gap:12px;font:400 16px/1.4 var(--font-sans)">
<span class="wg-label" style="color:var(--on-night-muted)">contact</span>
<span>Wiedhaak 1<br>3371 KD Hardinxveld-Giessendam</span><a class="wg-ul" href="tel:0184701212">0184-701212</a><a class="wg-ul" href="mailto:info@werkgoed.nl">info@werkgoed.nl</a>
</div>
</div>
<div style="overflow:hidden;padding:8px 0 24px">
<div style="font:800 clamp(72px,19vw,280px)/.9 var(--font-sans);font-variation-settings:'wdth' 90;letter-spacing:-.05em">werkgoed<span style="display:inline-block;width:.1em;height:.1em;border-radius:50%;background:var(--signal);margin-left:.02em"></span></div>
</div>
<div style="display:flex;flex-wrap:wrap;gap:12px 32px;justify-content:space-between;border-top:1px solid rgba(255,255,255,.2);padding-top:24px;font:400 14px/1.4 var(--font-sans);color:var(--on-night-muted)">
<span>2026 Werkgoed bedrijfskleding en PBM</span>
<span style="display:flex;flex-wrap:wrap;gap:8px 24px"><a class="wg-ul" href="#">Privacy en disclaimer</a><a class="wg-ul" href="#">Cookies</a><a class="wg-ul" href="#">Instagram</a><a class="wg-ul" href="#">LinkedIn</a><a class="wg-ul" href="#">YouTube</a></span>
</div>
</footer>

</div>
</x-dc>
'''

BEROEPEN = [
    {'k': 'las', 'naam': 'las', 'href': 'Lasgoed.dc.html', 'regel': 'Vonken, spatten, hitte en lasrook.', 'risicos': ['vonk', 'hitte', 'stof']},
    {'k': 'straat', 'naam': 'straat', 'href': 'Straatgoed.dc.html', 'regel': 'Op je knieën, langs de weg, in elk weer.', 'risicos': ['zicht', 'knielen', 'regen']},
    {'k': 'bouw', 'naam': 'bouw', 'href': 'Bouwgoed.dc.html', 'regel': 'Hoogte, stof en lawaai op de bouwplaats.', 'risicos': ['hoogte', 'stof', 'lawaai']},
    {'k': 'techniek', 'naam': 'techniek', 'href': '#', 'regel': 'Kruipen, knielen en precies werken.', 'risicos': ['knielen', 'snijden', 'zicht']},
    {'k': 'magazijn', 'naam': 'magazijn', 'href': '#', 'regel': 'Tussen pallets, heftrucks en koude hallen.', 'risicos': ['zicht', 'kou', 'snijden']},
    {'k': 'chauffeur', 'naam': 'chauffeurs', 'href': '#', 'regel': 'Urenlang rijden, laden en lossen.', 'risicos': ['zicht', 'kou', 'snijden']},
    {'k': 'groen', 'naam': 'groen', 'href': '#', 'regel': 'Buiten met machines, takken en weer.', 'risicos': ['lawaai', 'regen', 'snijden']},
    {'k': 'schilder', 'naam': 'schilders', 'href': '#', 'regel': 'Spatten, dampen en lange dagen op de trap.', 'risicos': ['chemie', 'stof', 'hoogte']},
]
