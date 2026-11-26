# USDT.P Skener

Skener za korake 3 i 4 rutine pre sesije: likvidnost i aktivnost na Bybit USDT perpetual ugovorima. Radi u browseru, sa javnim Bybit podacima, bez naloga i API ključeva. Elliott talase ne broji: listu proveravaš sam na TradingView-u.

## Šta radi
- **Likvidnost (korak 3):** samo Bybit USDT.P, OI ≥ 10M $, promet 24h ≥ 50M $, bez coinova mlađih od 14 dana i bez delistinga. Coinove iz polja „Isključi“ preskače.
- **Aktivnost (korak 4):**
  - OI 4h i cena 4h, pravi OI = promena OI − promena cene.
  - Prag OI je 5%; prelazi na 8% ako ih ima previše, a na 3% ako ih ima manje od 5.
  - Najveći rast i pad za 24h.
- **Lista za danas:** do 15 coinova po |pravom OI|, uz najveći rast i pad i coinove iz „Uvek na listi“.
- **Tumačenje za 4h:** novi longovi, novi shortovi, zatvaranje shortova ili zatvaranje longova. Funding je preračunat na 8h, a ekstreman funding je označen.
- **EWO_LB (LazyBear, EMA 5 − EMA 35)** na 4h, 1h, 15m i 5m, sa mini grafikom cene i EWO-a.
- **Divergencija talasa 3 i 5:** najjači EWO je talas 3, EWO se vrati do nule (talas 4), a cena napravi nov vrh ili dno uz niži EWO (talas 5). Prijavljuje samo divergencije iz poslednjih 12 sveća gde je EWO talasa 5 najviše 90% vrha talasa 3.
- **Upozorenje dok je skener otvoren:** zvuk, vibracija i traka „Nove divergencije“. Radi samo dok je stranica otvorena.
- **Kopiraj za TradingView:** lista u obliku `BYBIT:SOLUSDT.P,BYBIT:ETHUSDT.P,...`.

## Na telefonu
Otvori `https://sarunac25-wq.github.io/ew-skener/` i klikni **Skeniraj**.

Ako dobiješ grešku „Browser nije dobio odgovor od Bybita“:
1. Na dash.cloudflare.com: **Workers & Pages → Create → Create Worker → Deploy**.
2. **Edit code**, nalepi `cloudflare-worker.js`, pa **Deploy**.
3. Adresu Workera upiši u skeneru: **Podešavanja → API adresa**.

## Na računaru
Dvaput klikni na `ew-skener.html`. Ako browser blokira pozive, pokreni `python3 serve.py` (Windows: `py serve.py`).
