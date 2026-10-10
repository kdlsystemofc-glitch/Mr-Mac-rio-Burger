# otimizacao-baseline.md — Linha de base antes da etapa de Otimização

**Data:** 10/10/2026 · **Commit medido:** `3165c98` (tag `motion-pronto`)
**Ferramenta:** Lighthouse 12 (CLI), mobile, throttling simulado (RTT 150 ms, 1,6 Mbps, CPU 4x),
Chrome headless, `site/` servido por `http.server` do Python (sem gzip, sem cabeçalho de cache).
**Método:** 3 execuções (`scripts/lighthouse_runs.py`), valor = mediana.

## Scores (mediana)

| Categoria | Run 1 | Run 2 | Run 3 | **Mediana** |
| :--- | :---: | :---: | :---: | :---: |
| Performance | 65 | 68 | 68 | **68** |
| Acessibilidade | 100 | 100 | 100 | **100** |
| Melhores práticas | 96 | 96 | 96 | **96** |
| SEO | 100 | 100 | 100 | **100** |

> O PROGRESSO.md registrava 71 antes do motion; a variação 65–68 é ruído normal de execução
> e do Lighthouse 12. Esta é a referência válida para a comparação desta etapa.

## Métricas (mediana)

| Métrica | Valor |
| :--- | :---: |
| First Contentful Paint | 3,8 s |
| Largest Contentful Paint | 6,5 s |
| Total Blocking Time | 0 ms |
| Cumulative Layout Shift | 0,009 |
| Speed Index | 3,8 s |

**Elemento LCP:** `img.hero-burger-img` (`hero-burger-800.webp`, 146 KB) — renderizado com 363 px de
largura em 412 px. Decomposição: TTFB 455 ms · atraso de carga 0 · **atraso de renderização 6.013 ms (93%)**.

## Principais oportunidades apontadas

| Auditoria | Economia estimada | Causa |
| :--- | :---: | :--- |
| Recursos que bloqueiam renderização | ~2.750 ms | `@import` do Google Fonts dentro de `tokens.css` (cadeia HTML → CSS → CSS do Google → WOFF2), mais `tokens.css`, `reset.css` e `style.css` bloqueantes |
| Preconnect a origens necessárias | ~200 ms | `fonts.gstatic.com` |
| Imagens com tamanho inadequado | ~402 KiB | `neon-doodle-800` (115 KB exibido a 48 px), `dice-800` (exibido a 61 px), `trophy-5-800`, `hero-burger-800`, fotos do menu e do salão sem `srcset`/`sizes` |
| Formatos modernos de imagem | ~52 KiB | `paper-noise.png` |
| Minificar CSS | ~8 KiB | `style.css` |
| Minificar JS | ~13 KiB | `motion-sections.js`, `motion-core.js` |
| JS não usado | ~80 KiB | GSAP/ScrollTrigger (carregados após `load`, não afetam LCP) |
| Compressão de texto / cache | — | Dependem do servidor de produção (ver DEPLOY.md) |

**Melhores práticas 96:** única falha é `font-size` (texto < 12 px em selos decorativos
`.stamp-text`, `.lounge-subtitle`, `.stamp-mint-text`). É decisão visual do mockup — fora do
escopo desta etapa (proibido mudar visual).

## Regressão visual — referência

Capturas página inteira nas 12 resoluções, JS desligado (estado estático/pose final), salvas em
`screenshots/otimizacao/baseline/` (pasta ignorada pelo git). Duas capturas seguidas deram 0,000%
de diferença — a captura é determinística.

Tolerância numérica (`scripts/visual_snapshots.py`): pixel difere se algum canal variar > 24/255;
cada resolução passa com ≤ 1% de pixels diferentes e altura de página idêntica.

## Testes existentes no baseline

`test_responsive`, `test_phase_a`, `test_phase_c`, `test_hero_motion`, `test_menu_motion`,
`test_griddle_motion`, `test_lounge_motion`, `test_footer_motion`: todos passando.
