import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import shared, beroep_tpl, main_tpl, data
out = sys.argv[1]
def js(o): return json.dumps(o, ensure_ascii=False, indent=None)
for B in (data.LAS, data.STRAAT, data.BOUW):
    d = dict(B['data']); d['andere'] = [b for b in shared.BEROEPEN if b['k'] != B['k']]
    html = shared.HEAD.replace('[[TITLE]]', 'Werkgoed beroepspagina ' + B['titel']) + shared.topbar_header('Per beroep') + beroep_tpl.BODY + shared.FOOTER + beroep_tpl.SCRIPT
    rep = {'K': B['k'], 'NAAM': B['naam'], 'TITEL': B['titel'], 'TITELKLEIN': B['titel'].lower(), 'REGEL': B['regel'],
           'PERSOON': B['persoon'], 'MV': B['mv'], 'DAGINTRO': B['dagintro'], 'DAGFOTO': B['dagfoto'], 'HEROIMG': shared.IMG[B['heroimg']], 'HEROALT': B['heroalt'], 'MENU_JS': shared.MENU_JS, 'H': '8400', 'DATA': js(d)}
    for k, v in rep.items(): html = html.replace('[[%s]]' % k, v)
    assert '[[' not in html.replace('[i]', ''), [l for l in html.splitlines() if '[[' in l][:3]
    open(os.path.join(out, B['titel'] + '.dc.html'), 'w').write(html)
d = {'img': shared.IMG, 'logos': shared.MERK_LOGO, 'beroepen': shared.BEROEPEN, 'zones': [z for z in data.LAS['data']['zones'] if z['zone'] in ('hoofd', 'ogen', 'adem', 'romp', 'handen', 'voeten')], 'merken': main_tpl.MERKEN}
html = shared.HEAD.replace('[[TITLE]]', 'Werkgoed homepage') + shared.topbar_header(None) + main_tpl.BODY + shared.FOOTER + main_tpl.SCRIPT
html = html.replace('[[H]]', '7400').replace('[[MENU_JS]]', shared.MENU_JS).replace('[[DATA]]', js(d))
for k, v in shared.IMG.items(): html = html.replace('[[IMG_%s]]' % k, v)
assert '[[' not in html, [l for l in html.splitlines() if '[[' in l][:3]
open(os.path.join(out, 'Main.dc.html'), 'w').write(html)
