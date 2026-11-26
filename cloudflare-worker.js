// Cloudflare Worker: prosleđuje javne Bybit tržišne podatke i dodaje CORS zaglavlje,
// da bi skener radio iz browsera na telefonu. Bez ključeva i bez naloga na Bybitu.
export default {
  async fetch(req) {
    const url = new URL(req.url);
    const cors = { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET, OPTIONS' };
    if (req.method === 'OPTIONS') return new Response(null, { headers: cors });
    if (req.method !== 'GET' || !url.pathname.startsWith('/v5/market/')) {
      return new Response('Samo GET /v5/market/*', { status: 404, headers: cors });
    }
    const r = await fetch('https://api.bybit.com' + url.pathname + url.search, { headers: { 'User-Agent': 'ew-skener/1.0' } });
    const h = new Headers(cors);
    h.set('Content-Type', 'application/json');
    h.set('Cache-Control', 'no-store');
    return new Response(r.body, { status: r.status, headers: h });
  }
};
