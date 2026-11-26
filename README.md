# EW Skener

Skener za rutinu pre sesije po strategiji „EW strategija: 5 talasa“. Radi u browseru, sa javnim Bybit podacima, bez naloga i API ključeva.

## Na telefonu
Otvori `https://<tvoj-nalog>.github.io/ew-skener/` i klikni **Skeniraj**.

Ako dobiješ grešku „Browser nije dobio odgovor od Bybita“, Bybit ne dozvoljava pozive iz browsera. Tada:
1. Otvori dash.cloudflare.com (besplatan nalog) → **Workers & Pages** → **Create** → **Create Worker** → **Deploy**.
2. **Edit code**, obriši sve, nalepi sadržaj fajla `cloudflare-worker.js` i klikni **Deploy**.
3. Kopiraj adresu Workera (npr. `https://ew-proxy.tvojnalog.workers.dev`).
4. U skeneru: **Podešavanja → API adresa**, nalepi adresu i ponovo klikni **Skeniraj**.

## Na računaru
Dvaput klikni na `ew-skener.html`. Ako browser blokira pozive, pokreni `python3 serve.py` (na Windowsu `py serve.py`).

## Brojanje talasa
- **Timeframe:** biraš do 3 TF-a (5m, 15m, 30m, 1h, 2h, 4h). Svaka kartica ima oznaku TF-a.
- **Niži stepen:** svaki talas se proverava na nižem TF-u (5m → 1m, 15m → 5m, 30m → 5m, 1h → 15m, 2h → 30m, 4h → 1h):
  - impulsni talasi traže 5 podtalasa (impuls ili dijagonala),
  - korekcije traže 3 (zigzag, flat ili prošireni flat).
  - Podtalasi se crtaju isprekidano (i–v, a–b–c).
- **Ekstenzija:** označava produžen talas 1, 3 ili 5 i ono što iz toga sledi:
  - produžen 3 → talas 5 ≈ talas 1,
  - produžen 5 → cilj je dno podtalasa ii unutar pete,
  - talas 3 kraći od talasa 1 → cilj talasa 5 je ograničen.
- **Truncation:** prepoznaje skraćenu petu (posle jakog talasa 3, samo uz 5 podtalasa) i odbacuje Setup 3 kad je rizik skraćenja velik.
- **Više countova:** na svakom TF-u se prikazuju glavni i alternativni count. Ako važi više od 2 counta, sve ide u B (pravilo iz strategije).

## Šta skener radi
- Likvidnost (OI ≥ 10M $, promet ≥ 50M $), OI 4h i pravi OI, BTC kontekst.
- Predlozi countova za Setup 1, 2 i 3 na 1h i 15m, sa ocenom (5/5 → 1R, 4/5 → 0.5R), ciljevima, R:R i veličinom pozicije.
- Dnevni limiti (+2R, 2 gubitka, 3 trejda, −4R nedeljno).

Count je heuristika. Potvrdu counta, alternativu i 5–3 na manjem TF-u radiš ručno na TradingView-u.
