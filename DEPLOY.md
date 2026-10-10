# DEPLOY.md — Publicação do site Mr. Macário Burger

Este documento **não escolhe hospedagem**. Ele lista o que publicar e quais cabeçalhos HTTP
configurar, seja qual for o servidor (Nginx, Apache, CDN, hospedagem estática etc.).

## O que publicar

Publique **somente o conteúdo de `site/`** (é a raiz do site):

```
site/
├── index.html          ← gerado pelo build (CSS crítico inline)
├── styles.min.css      ← gerado pelo build
├── js/motion-*.min.js  ← gerados pelo build
├── js/vendor/          ← GSAP, ScrollTrigger, Lenis (minificados de origem)
├── fonts/*.woff2       ← fontes auto-hospedadas
├── assets/             ← imagens WebP/PNG/SVG (+ og-image.jpg de compartilhamento)
├── icons/, favicon.ico, apple-touch-icon.png, site.webmanifest
└── robots.txt, sitemap.xml   ← gerados pelo build a partir de seo.config.json
```

Não publique `src/`, `scripts/`, `design/`, `imagens/`, `assets/` (raiz), `node_modules/` nem os `.md`.

Antes de publicar, depois de qualquer mudança em `src/`:

```bash
npm install          # uma vez (terser, clean-css, lighthouse)
npm run build        # = python scripts/build.py (precisa de Python + Playwright + tinycss2)
```

O build falha se o CSS crítico não produzir estilos idênticos ao CSS completo na primeira tela.

## Domínio (SEO) — um único campo

Enquanto o domínio não existir, `seo.config.json` fica `{ "domain": null }`. Nesse estado o build
deixa **comentadas** no HTML as tags que exigem URL absoluta (canonical, `og:url`, `og:image`,
`twitter:image`), sem `@id`/`url`/`image`/`logo` no JSON-LD, com a linha `Sitemap:` comentada no
`robots.txt` e sem nenhuma `<url>` no `sitemap.xml`.

Quando o domínio for definido:

```json
{ "domain": "https://www.dominio-do-cliente.com.br" }
```

rode `npm run build`. Tudo acima é publicado com o domínio (só `https://`, sem barra no fim; o build
recusa outro formato). Não há outro lugar para editar.

Imagem de compartilhamento (`assets/og-image.jpg`) e ícones são gerados por
`python scripts/gen_og_image.py` e `python scripts/gen_icons.py` e só precisam ser refeitos se o hero
ou o logo mudarem.

## Cabeçalhos recomendados

### Compressão (o ganho mais importante)

Ative **Brotli** (preferível) ou **gzip** para tipos de texto:
`text/html`, `text/css`, `application/javascript` (ou `text/javascript`), `image/svg+xml`,
`application/manifest+json`, `application/xml`.

Não comprima `woff2`, `webp` e `png`, que já são comprimidos.

Efeito medido (gzip nível 9): `index.html` 41 KB → 11 KB · `styles.min.css` 27 KB → 6 KB ·
`gsap.min.js` 71 KB → 28 KB · `ScrollTrigger.min.js` 44 KB → 18 KB.

### Cache-Control

Os nomes de arquivo **não têm hash de conteúdo**, então CSS/JS não podem ser `immutable`:
uma atualização demoraria a chegar. Recomendação para os nomes atuais:

| Arquivos | `Cache-Control` | Motivo |
| :--- | :--- | :--- |
| `index.html` (e `/`) | `no-cache` | Sempre revalida (ETag/Last-Modified); traz CSS crítico e referências novas na hora |
| `styles.min.css`, `js/*.min.js` | `public, max-age=86400, stale-while-revalidate=604800` | 1 dia + 7 dias servindo do cache enquanto revalida |
| `js/vendor/*.js` | `public, max-age=2592000` | Bibliotecas de terceiros, mudam raramente (30 dias) |
| `fonts/*.woff2` | `public, max-age=31536000, immutable` | Para trocar uma fonte, crie arquivo com nome novo |
| `assets/*.webp`, `*.png`, `*.svg`, `*.jpg` | `public, max-age=2592000, stale-while-revalidate=86400` | 30 dias. Para trocar uma imagem, prefira um nome novo |
| `favicon.ico`, `apple-touch-icon.png`, `icons/*`, `site.webmanifest` | `public, max-age=604800` | 7 dias (nomes fixos, pedidos pelo navegador) |
| `robots.txt`, `sitemap.xml` | `public, max-age=3600` | Lidos por buscadores; mudança deve valer rápido |

**Se no futuro o build passar a gerar nomes com hash** (ex.: `styles.3f9a1c.min.css`), CSS, JS e
imagens podem usar `public, max-age=31536000, immutable`.

### Outros cabeçalhos

| Cabeçalho | Valor | Observação |
| :--- | :--- | :--- |
| `Content-Type` das fontes | `font/woff2` | Alguns servidores não conhecem `.woff2` |
| `Content-Type` do WebP | `image/webp` | Idem |
| `Content-Type` do manifest | `application/manifest+json` | `.webmanifest` |
| `Content-Type` do sitemap | `application/xml` | |
| `Vary` | `Accept-Encoding` | Quando houver compressão |
| `X-Content-Type-Options` | `nosniff` | Segurança básica |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | Padrão moderno |
| `Strict-Transport-Security` | `max-age=31536000` | Só depois de o HTTPS estar confirmado no domínio |

**CORS das fontes:** as fontes são servidas da mesma origem do HTML, então nenhum cabeçalho CORS
é necessário. Se forem para um CDN em outro domínio, esse CDN precisa enviar
`Access-Control-Allow-Origin` para o domínio do site (o preload usa `crossorigin`).

**HTTP/2 ou HTTP/3:** recomendado. A página faz ~25 requisições no primeiro carregamento.

## Como conferir depois de publicar

```bash
curl -sI -H "Accept-Encoding: br, gzip" https://SEU-DOMINIO/styles.min.css   # content-encoding + cache-control
curl -sI https://SEU-DOMINIO/fonts/bebas-neue-400-latin.woff2                 # content-type: font/woff2
```

Para estimar o efeito localmente sem servidor real: `python scripts/lighthouse_runs.py saida 3 --prod`
(servidor de teste com gzip e com os mesmos `Cache-Control` desta tabela).
