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

## Šta skener radi
- Likvidnost (OI ≥ 10M $, promet ≥ 50M $), OI 4h i pravi OI, BTC kontekst.
- Predlozi countova za Setup 1, 2 i 3 na 1h i 15m, sa ocenom (5/5 → 1R, 4/5 → 0.5R), ciljevima, R:R i veličinom pozicije.
- Dnevni limiti (+2R, 2 gubitka, 3 trejda, −4R nedeljno).

Count je heuristika. Potvrdu counta, alternativu i 5–3 na manjem TF-u radiš ručno na TradingView-u.
