import json,sys
d=json.load(open(sys.argv[1]));T={x['name']:x['value'] for x in d['color']['tokens']}
def L(h):
  h=h.lstrip('#')[:6];c=[int(h[i:i+2],16)/255 for i in (0,2,4)]
  c=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in c];return .2126*c[0]+.7152*c[1]+.0722*c[2]
def v(n,th):
  x=T[n][th]
  while x.startswith('{'):x=T[x[1:-1]][th]
  return x
def cr(a,b,th):
  la,lb=L(v(a,th)),L(v(b,th));return (max(la,lb)+.05)/(min(la,lb)+.05)
pairs=[("ink","surface"),("ink","surface-sunken"),("ink","canvas"),("ink-muted","surface"),("ink-muted","surface-sunken"),("ink-muted","canvas"),("line-strong","surface"),("line-strong","canvas"),("on-night","marine"),("on-night-muted","marine"),("on-signal","signal"),("on-vlam","vlam"),("vlam-ink","surface"),("vlam-ink","vlam-soft"),("staal","surface"),("staal","surface-sunken"),("ink","vlam-soft"),("ink","signal-soft")]
for b in "las straat bouw techniek magazijn chauffeur groen schilder".split():
  pairs+= [("beroep-%s-deep"%b,"beroep-"+b),("ink","beroep-"+b),("ink-muted","beroep-"+b)]
for th in ("light","dark"):
  bad=[(a,b,round(cr(a,b,th),2)) for a,b in pairs if cr(a,b,th)<(3 if a=="line-strong" else 4.5)]
  print(th,"FAIL:",bad)
