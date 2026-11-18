import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import shared, beroep_tpl, main_tpl, data, data2, pages_tpl
out = sys.argv[1]
def js(o): return json.dumps(o, ensure_ascii=False, indent=None)
for B in [data.LAS, data.STRAAT, data.BOUW] + data2.ALLE:
    d = dict(B['data']); d['andere'] = [b for b in shared.BEROEPEN if b['k'] != B['k']]
    html = shared.HEAD.replace('[[TITLE]]', 'Werkgoed beroepspagina ' + B['titel']) + shared.topbar_header('Per beroep') + beroep_tpl.BODY + shared.FOOTER + beroep_tpl.SCRIPT
    if 'heroimg' in B:
        hero = '<div style="flex:1 1 320px;min-width:0;max-width:520px;aspect-ratio:4/5;background:var(--surface);border-radius:var(--radius-sheet);overflow:hidden">\n<img class="wg-foto" src="%s" alt="%s">\n</div>' % (shared.IMG[B['heroimg']], B['heroalt'])
    else:
        hero = '<div style="flex:1 1 320px;min-width:0;max-width:520px;aspect-ratio:4/5;border-radius:var(--radius-sheet);overflow:hidden;background:var(--surface)">\n<x-import component-from-global-scope="Werkgoed.FotoPlek">%s</x-import>\n</div>' % B['fotoplek']
    rep = {'HEROBLOK': hero, 'K': B['k'], 'NAAM': B['naam'], 'TITEL': B['titel'], 'TITELKLEIN': B['titel'].lower(), 'REGEL': B['regel'],
           'PERSOON': B['persoon'], 'MV': B['mv'], 'DAGINTRO': B['dagintro'], 'DAGFOTO': B['dagfoto'], 'MENU_JS': shared.MENU_JS, 'H': '8400', 'DATA': js(d)}
    for k, v in rep.items(): html = html.replace('[[%s]]' % k, v)
    assert '[[' not in html.replace('[i]', ''), [l for l in html.splitlines() if '[[' in l][:3]
    open(os.path.join(out, B['titel'] + '.dc.html'), 'w').write(html)
d = {'img': shared.IMG, 'logos': shared.MERK_LOGO, 'beroepen': shared.BEROEPEN, 'zones': [z for z in data.LAS['data']['zones'] if z['zone'] in ('hoofd', 'ogen', 'adem', 'romp', 'handen', 'voeten')], 'merken': main_tpl.MERKEN}
html = shared.HEAD.replace('[[TITLE]]', 'Werkgoed homepage') + shared.topbar_header(None) + main_tpl.BODY + shared.FOOTER + main_tpl.SCRIPT
html = html.replace('[[H]]', '7400').replace('[[MENU_JS]]', shared.MENU_JS).replace('[[DATA]]', js(d))
for k, v in shared.IMG.items(): html = html.replace('[[IMG_%s]]' % k, v)
assert '[[' not in html, [l for l in html.splitlines() if '[[' in l][:3]
open(os.path.join(out, 'Main.dc.html'), 'w').write(html)

for P in pages_tpl.PAGES:
    html = shared.HEAD.replace('[[TITLE]]', P['title']) + shared.topbar_header(P['active']) + P['body'] + pages_tpl.LAT + shared.FOOTER + pages_tpl.script(P['h'], P['init'], P['data'], P['js'])
    assert '[[' not in html.replace('[MATEN', '').replace('[i]', ''), [l for l in html.splitlines() if '[[' in l][:3]
    open(os.path.join(out, P['file']), 'w').write(html)
