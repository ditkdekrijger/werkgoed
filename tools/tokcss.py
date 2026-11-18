import json,sys
d=json.load(open(sys.argv[1]));out=["/* Werkgoed - generated from tokens.json */"]
T=d['color']['tokens']
def val(x,th):
  v=x['value'][th] if isinstance(x['value'],dict) else x['value']
  return 'var(--%s)'%v[1:-1] if v.startswith('{') else v
for th,sel in (("light",':root, [data-theme="light"]'),("dark",'[data-theme="dark"]')):
  out.append(sel+" {");out+=["  --%s: %s;"%(x['name'],val(x,th)) for x in T];out.append("}")
out.append(":root {")
for fam in ("spacing","radius"):
  out+=["  --%s: %s;"%(x['name'],x['value']) for x in d[fam]['tokens']]
out.append('  --font-sans: %s;'%d['type']['families']['sans']);out.append("}")
for g in d['type']['groups']:
  for s in g['styles']:
    ls=("; letter-spacing: %s"%s['letterSpacing']) if 'letterSpacing' in s else ""
    out.append(".%s { font-family: var(--font-sans); font-size: %s; line-height: %s; font-weight: %s%s; }"%(s['name'],s['fontSize'],s['lineHeight'],s['fontWeight'],ls))
open(sys.argv[2],'w').write("\n".join(out)+"\n")
