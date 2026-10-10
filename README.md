# Mr. Macário Burger — landing page

Site de página única da hamburgueria artesanal **Mr. Macário Burger** (R. Dom Macário, 1063 —
Vila da Saúde, São Paulo). HTML/CSS/JS estático, sem framework, mobile-first, com motion em GSAP.

> ## ⚠️ Antes de publicar
> As fotos de **comida, chapa e salão** exibidas hoje foram **geradas por IA e não são do
> cliente**. As batatas voadoras do hero foram recortadas do mockup. O site não deve ir ao ar assim.
> Ver `PENDENCIAS-CLIENTE.md` (item 1) e `assets.md` → "Classificação de origem". O build avisa
> enquanto `imagensAprovadasParaPublicar` for `false` em `cliente.config.json`.

## Como ver o site

- **Sem instalar nada:** abra `site/index.html` no navegador (funciona em `file://`).
- **Servidor local:** `python -m http.server 8000 -d site` → http://localhost:8000

## Como trabalhar no código

Requisitos: Node 18+, Python 3.11+.

```bash
npm install                                        # terser, clean-css, lighthouse
pip install playwright tinycss2 pillow fonttools brotli
python -m playwright install chromium webkit
```

Edite **somente** `src/` e depois gere `site/`:

```bash
npm run build              # = python scripts/build.py
```

O build junta e minifica o CSS, calcula o CSS crítico medindo a página em 13 resoluções e **falha se
a primeira tela não ficar idêntica** com e sem o CSS completo. Também minifica o JS, aplica o
`cliente.config.json` (domínio, horário, preço, cardápio) e gera `robots.txt` e `sitemap.xml`.
`site/` vai commitado: abre direto e é o que se publica.

### Dados do cliente

Tudo que ainda falta confirmar fica em **`cliente.config.json`**. Preencha o valor, troque
`"confirmado"` para `true` e rode `npm run build`. O efeito de cada campo está em
`PENDENCIAS-CLIENTE.md`.

### Verificação

| Comando | O que faz |
| :--- | :--- |
| `python scripts/auditoria_final.py` | Chromium + WebKit × 15 telas (320 px a 5120 px) × modos (padrão, movimento reduzido, escuro, sem JS, `file://`): rolagem lateral, console, imagens, alvos de toque, h1, motion |
| `python scripts/test_responsive.py` | 12 telas: rolagem, console, toque, zoom 200% |
| `python scripts/test_phase_a.py`, `test_phase_c.py`, `test_*_motion.py` | Motion: núcleo, modos, loops, seções |
| `python scripts/visual_snapshots.py capture <dir>` / `compare <ref> <dir>` | Regressão de pixels nas 12 telas |
| `python scripts/lighthouse_runs.py <saida> 3 [--prod]` | Lighthouse mobile, mediana de 3 (`--prod` simula gzip + cache do DEPLOY.md) |

### Geração de imagens (só redimensiona arquivos aprovados)

`scripts/gen_image_steps.py` (degraus de `srcset`) · `scripts/gen_og_image.py` (imagem de
compartilhamento a partir do hero) · `scripts/gen_icons.py` (favicons a partir do logo).

## Estrutura

```
src/                  ← FONTE: index.html, css/, js/, seo/restaurant.json
site/                 ← PUBLICÁVEL (gerado + estáticos): index.html, styles.min.css, js/, fonts/,
                        assets/, icons/, favicon.ico, site.webmanifest, robots.txt, sitemap.xml
scripts/              ← build, testes, auditoria, geradores (scripts/_historico/: scripts antigos, fora de uso)
cliente.config.json   ← dados pendentes do cliente (arquivo único)
design/               ← mockups: SÓ referência visual, nunca usados no site
imagens/              ← fotos reais do cliente (originais)
assets/               ← imagens geradas por IA na fase de design (origem dos plates)
reserva/              ← fotos reais otimizadas ainda não usadas (fora do deploy)
```

## Documentação

| Arquivo | Conteúdo |
| :--- | :--- |
| `DESIGN.md` | Tokens, decisões de design e técnicas (§11 otimização, §12 SEO), pendências de conteúdo |
| `CLIENTE.MD` | Dados brutos do cliente (Google Maps/Instagram) — única fonte de fatos |
| `PENDENCIAS-CLIENTE.md` | O que falta do cliente e o efeito de cada item |
| `ROTEIRO-APARELHO-REAL.md` | Checklist de teste em iPhone/Android |
| `DEPLOY.md` | O que publicar, domínio, compressão e cabeçalhos de cache |
| `assets.md` | Origem de cada imagem (real × gerada por IA) |
| `PROGRESSO.md` | Histórico por etapa e estado atual |
| `motion-*.md`, `otimizacao-*.md` | Linhas de base e resultados das etapas de motion e otimização |

## Licenças

**Bibliotecas no site**
- **GSAP 3.15.0 e ScrollTrigger 3.15.0** — GreenSock Standard License
  (https://gsap.com/standard-license). Gratuita, inclusive para uso comercial; confira os termos
  vigentes antes de publicar.
- **Lenis 1.3.26** — MIT (darkroom.engineering).

**Fontes** (`site/fonts/`, avisos em `site/fonts/LICENSE.txt`) — todas SIL Open Font License 1.1:
Bebas Neue (Dharma Type), Caveat (Impallari Type), Montserrat (Julieta Ulanovsky), Plus Jakarta Sans
(Tokotype). Uso comercial e incorporação em sites permitidos.

**Ferramentas de desenvolvimento (não vão para o site):** Lighthouse e Playwright (Apache-2.0),
terser (BSD-2-Clause), clean-css (MIT), tinycss2 (BSD-3-Clause), Pillow (MIT-CMU), fontTools (MIT).

## Imagens geradas ou recriadas por IA

Conforme as regras do projeto (`CLAUDE.md`), comida, fachada, salão, pessoas e logo devem ser fotos
reais do cliente. Pode haver recorte, limpeza ou ampliação por IA *a partir do original*, mas nunca
um substituto inventado. Estado atual (detalhe em `assets.md`):

- **Geradas por IA, não são do cliente — substituir antes de publicar:** hambúrguer do hero/menu,
  Mr Burguinho, batatas, chapa, fotos de "mesa de jogos", salão do rodapé.
- **Recorte do mockup — substituir:** batatas voadoras do hero.
- **Recriada por IA a partir do original — confirmar com o cliente antes de publicar:** logotipo.
- **Decorativas (permitidas):** troféu, dados, neon, textura de papel, bordas rasgadas.
- **Imagem de compartilhamento** (`og-image.jpg`): herda o hambúrguer do hero; regerar depois da troca.
