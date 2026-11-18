"""Bouwt de klikbare Werkgoed-site uit de canvaspagina's. Gebruik: python3 site.py <canvas/project> <ds/project> <beelden-root> <uit>"""
import json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
import shared, prod

cv, ds, beeld, out = sys.argv[1:5]
os.makedirs(os.path.join(out, 'img'), exist_ok=True)
os.makedirs(os.path.join(out, 'wg'), exist_ok=True)

# beelden: blob-id -> lokaal bestand
blob = {}
for k, u in shared.IMG.items():
    blob[u] = ('img/wg-%s.jpg' % k, os.path.join(beeld, 'site/up/wg-%s.jpg' % k))
blob[shared.LOGO] = ('img/logo-werkgoed.svg', os.path.join(beeld, 'site/up/logo-wg.svg'))
blob[shared.LOGO_WIT] = ('img/logo-werkgoed-wit.svg', os.path.join(beeld, 'site/up/logo-wg-wit.svg'))
mk = {'HAIX': 'haix', 'Havep': 'havep', 'KASK': 'kask', 'LOWA Work': 'lowa', 'PUMA Safety': 'puma', 'Santino': 'santino', 'Snickers Workwear': 'snickers', 'Tricorp Workwear': 'tricorp'}
for n, u in shared.MERK_LOGO.items():
    blob[u] = ('img/merk-%s.png' % mk[n], os.path.join(beeld, 'site/merk/out/merk-%s.png' % mk[n]))
for k, d in prod.P.items():
    blob[d['foto']] = ('img/wg-p-%s.jpg' % k, os.path.join(beeld, 'site/prod/wg-p-%s.jpg' % k))
for u, (dst, src) in blob.items():
    shutil.copy(src, os.path.join(out, dst))

TITELS = {'home': 'Werkgoed', 'categorie': 'Werkjassen | Werkgoed', 'product': 'Havep Gore-Tex jas Revolve 50468 | Werkgoed',
          'merken': 'Merken | Werkgoed', 'showroom': 'Showroom en voetscan | Werkgoed', 'winkelwagen': 'Winkelwagen | Werkgoed'}


def pid(stem):
    return 'home' if stem == 'Main' else stem.lower()


def fix(s):
    for u, (dst, _) in blob.items():
        s = s.replace(u, dst)
    s = re.sub(r'([A-Z][A-Za-z]+)\.dc\.html(#[\w-]+)?', lambda m: '#' + pid(m.group(1)), s)
    return s


pages = []
for f in sorted(os.listdir(cv)):
    if not f.endswith('.dc.html'):
        continue
    stem = f[:-8]
    src = open(os.path.join(cv, f)).read()
    body = src[src.index('<x-dc>') + 6:src.index('</x-dc>')]
    body = re.sub(r'<helmet>.*?</helmet>', '', body, flags=re.S)
    code = re.search(r'<script type="text/x-dc" data-dc-script[^>]*>(.*?)</script>', src, re.S).group(1)
    i = pid(stem)
    titel = TITELS.get(i, stem + ' | Werkgoed')
    pages.append('WG_PAGES[%s] = { title: %s, tpl: %s, logic: function (DCLogic) {\n%s\nreturn Component;\n} };' % (
        json.dumps(i), json.dumps(titel), json.dumps(fix(body)), fix(code)))
open(os.path.join(out, 'pages.js'), 'w').write('window.WG_PAGES = {};\nvar WG_PAGES = window.WG_PAGES;\n' + '\n'.join(pages) + '\n')

# design system: licht thema vast
tok = open(os.path.join(cv, 'ds/wg/tokens.css')).read()
tok = re.sub(r'\[data-theme="dark"\] \{.*?\}\n', '', tok, flags=re.S)
tok = tok.replace(':root, [data-theme="light"] {', ':root, [data-theme="light"], [data-theme="dark"] {\n  color-scheme: light;', 1)
open(os.path.join(out, 'wg/tokens.css'), 'w').write(tok)
shutil.copy(os.path.join(ds, 'components/bundle.css'), os.path.join(out, 'wg/bundle.css'))
shutil.copy(os.path.join(ds, 'components/bundle.js'), os.path.join(out, 'wg/bundle.js'))
shutil.copy(os.path.join(os.path.dirname(__file__), 'runtime.js'), os.path.join(out, 'runtime.js'))

helm = re.search(r'<style>(.*?)</style>', shared.HEAD, re.S).group(1)
index = '''<title>Werkgoed 2.0</title>
<meta name="description" content="Klikbaar ontwerp van de nieuwe werkgoed.nl">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&display=swap">
<link rel="stylesheet" href="wg/tokens.css">
<link rel="stylesheet" href="wg/bundle.css">
<style>''' + helm + '''
html, body { background: #ffffff; }
#app { min-height: 100vh; background: var(--surface); }
.wg-laden { display: grid; place-items: center; min-height: 60vh; font: 600 18px/1.4 "Archivo", system-ui, sans-serif; color: #57616b; }
</style>
<div id="app"><div class="wg-laden">Werkgoed laadt…</div></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react/18.3.1/umd/react.production.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.3.1/umd/react-dom.production.min.js"></script>
<script src="wg/bundle.js"></script>
<script src="pages.js"></script>
<script src="runtime.js"></script>
'''
open(os.path.join(out, 'index.html'), 'w').write(index)
print('paginas', len(pages), 'beelden', len(blob))
