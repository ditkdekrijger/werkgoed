import json,sys
C=[]
def t(n,l,d,u): C.append({"name":n,"value":{"light":l,"dark":d},"usage":u})
t("surface","#ffffff","#0f1720","Paginavlak en productvlak. Tekst erop is ink of ink-muted.")
t("surface-sunken","#f5f3ee","#17212b","Kalk. Warm afwisselend vlak voor secties en kaarten. Tekst erop is ink of ink-muted.")
t("canvas","#ebe5d8","#232c35","Canvas, de kleur van ongeverfd werkkatoen. Tweede warm vlak voor sheets en kaarten die rust moeten geven. Tekst erop is ink of ink-muted.")
t("ink","#16212c","#f3f1ec","Koppen en lopende tekst. Een zeer donker marine, geen zwart. Op surface, surface-sunken, canvas, signal en de beroepstinten.")
t("ink-muted","#57616b","#aeb6bd","Bijschriften, labels en secundaire tekst op surface, surface-sunken en canvas (minstens 4,5 op 1 in beide thema's).")
t("line","#16212c24","#ffffff26","Haarlijn tussen lijstregels en secties. Draagt geen betekenis.")
t("line-strong","#79818a","#7f8891","Rand van knoppen, tags en invoervelden (minstens 3 op 1 op surface, surface-sunken en canvas).")
t("marine","#1c2d3f","#22344a","Marine, de kleur van klassieke werkkleding. Het donkere vlak van het merk: topbalk, panelen, showroom en footer. Tekst erop is on-night.")
t("night","{marine}","{marine}","Alias van marine voor bestaande pagina's. Gebruik in nieuw werk marine.")
t("on-night","#ffffff","#ffffff","Tekst en lijnen op marine.")
t("on-night-muted","#c3ccd6","#c3ccd6","Bijschrift en lead op marine (ruim 4,5 op 1).")
t("signal","#ffd400","#ffd400","Signaalgeel van fluorescerende werkkleding. Het merkaccent: de hoofdknop, de markering in een kop en de streep. Spaarzaam, nooit als tekstkleur op wit. Tekst erop is on-signal.")
t("on-signal","#16212c","#16212c","Tekst op signal, in beide thema's.")
t("signal-soft","#fff3b3","#3a3200","Zachte tint van signal voor een gekozen rij of een uitgelichte kaart. Tekst erop is ink.")
t("vlam","#ff6a13","#ff6a13","Steunkleur, fluorescerend oranje. Voor badges, het actieve punt op de lichaamskaart, risico's en een enkele aanbieding. Nooit een groot vlak, nooit tekstkleur op wit. Tekst erop is on-vlam.")
t("on-vlam","#16212c","#16212c","Tekst op vlam (5,7 op 1).")
t("vlam-soft","#ffe6d6","#3d2414","Zachte tint van vlam voor een risicoregel of risicobadge. Tekst erop is ink of vlam-ink.")
t("vlam-ink","#b23f00","#ff9a5c","Oranje als tekst: het woord 'risico' of een waarschuwing op surface en vlam-soft (minstens 4,5 op 1).")
t("staal","#3c6382","#8fb3cf","Staalblauw. Informatie en normcodes, rand van een normlabel. Als tekst op surface en surface-sunken.")
t("focus","#16212c","#ffd400","Focusring van 3px op lichte vlakken. Op marine is de focusring signal.")
t("ok","#1b7a43","#5ccf8a","Status voorraad of gelukt, altijd met een woord erbij. Tekst op surface.")
t("alert","#c4271f","#ff8a80","Status fout of niet leverbaar, altijd met een woord erbij. Tekst op surface.")
B=[("las","Lasgoed","leer van een lasschort","#f2e0d0","#3a2a1f","#8a3f12","#f0b48a"),
("straat","Straatgoed","fluo van de weg","#fff0a0","#3a3410","#6b5600","#ffe46b"),
("bouw","Bouwgoed","canvas van de bouwbroek","#e7ddc9","#34302a","#5f4b26","#e3cfa6"),
("techniek","Techniekgoed","staal","#dae5ef","#1f2e3c","#2c5677","#9cc3e3"),
("magazijn","Magazijngoed","beton van de hal","#e3e6e9","#262b31","#3e4954","#c1cad3"),
("chauffeur","Chauffeursgoed","blauw van de cabine","#dfe2f2","#22263f","#343f80","#b3bcf0"),
("groen","Groengoed","blad","#dbe8d3","#20301c","#2f5a26","#a9d39b"),
("schilder","Schildersgoed","gebroken wit","#eeeae3","#2d2b28","#4f4a42","#d6d0c5")]
for k,n,w,tl,td,dl,dd in B:
  t("beroep-"+k,tl,td,f"Beroepstint {n} ({w}). Vlak van de beroepskaart, de hero en de lichaamskaart van {n}. Tekst erop is ink.")
  t("beroep-"+k+"-deep",dl,dd,f"Diepe beroepskleur {n}. Het woord 'goed' in het beroepswoordmerk, iconen en het figuur op de lichaamskaart. Op beroep-{k} minstens 4,5 op 1.")
tok=json.load(open(sys.argv[1]))
tok["version"]=2
tok["color"]["tokens"]=C
g=tok["type"]["groups"]
g[0]["styles"].insert(0,{"name":"wg-mega","fontSize":"176px","lineHeight":"0.84","fontWeight":800,"letterSpacing":"-0.05em","usage":"Beroepswoordmerk op een beroepspagina ('las' + 'goed'). Breedte-as 80%. Fluide: clamp(72px, 13vw, 200px)."})
g[1]["styles"].append({"name":"wg-code","fontSize":"13px","lineHeight":"1.2","fontWeight":600,"letterSpacing":"0.02em","usage":"Normcodes, artikelnummers en tijden in een werkdag. Breedte-as 75% en tabelcijfers via de klasse wg-code. Codes behouden hun eigen hoofdletters (EN ISO 20471)."})
json.dump(tok,open(sys.argv[1],"w"),ensure_ascii=False,indent=1)
