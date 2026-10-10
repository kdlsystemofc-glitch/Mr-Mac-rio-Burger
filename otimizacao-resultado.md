# otimizacao-resultado.md — Resultado da etapa de Otimização

**Data:** 10/10/2026 · Referência: [otimizacao-baseline.md](otimizacao-baseline.md)
Mesmo Lighthouse 12, mesmo perfil mobile, 3 execuções, mediana.

## Lighthouse mobile

| | Baseline | Depois (servidor puro, igual à baseline) | Depois (modo produção: gzip + cache do DEPLOY.md) |
| :--- | :---: | :---: | :---: |
| **Performance** | 68 | **89** (87–90) | **92** (89–92) |
| Acessibilidade | 100 | 100 | 100 |
| Melhores práticas | 96 | 96 | 96 |
| SEO | 100 | 100 | 100 |
| FCP | 3,8 s | 0,92 s | 0,77 s |
| LCP | 6,5 s | 3,76 s | 3,39 s |
| TBT | 0 ms | 35 ms | 44 ms |
| CLS | 0,009 | 0 | 0 |
| Speed Index | 3,8 s | 0,95 s | 0,88 s |

**Meta 90–92:** atingida (92) no modo produção. No servidor sem compressão a mediana ficou
em 89. A diferença é só a compressão do HTML/CSS, que o DEPLOY.md manda ativar.

**Por que o LCP simulado não cai mais:** a primeira pintura do hero leva ~120–200 ms no Chrome
headless (blur do header, blend da textura, drop-shadows — tudo visual, intocável). No localhost,
as imagens lazy abaixo da dobra terminam de baixar antes disso, e o modelo pessimista do Lighthouse
(Lantern) as conta no caminho do LCP. Numa rede real elas não terminam antes da pintura. Atrasá-las
via JS ou esconder seções violaria progressive enhancement e "nada acima da dobra depende de JS"
(o menu aparece na primeira tela em celulares), então não foi feito.

TBT subiu de 0 para ~40 ms: é o recálculo de estilo do CSS completo, agora feito *depois* da
primeira pintura em vez de antes. Continua bem abaixo do limite de 150 ms do motion-baseline.

## Pesos (bruto / gzip)

| Arquivo | Antes | Depois |
| :--- | :--- | :--- |
| HTML | 24,2 KB | 41,6 KB / 11,1 KB (inclui 18,5 KB de CSS crítico inline) |
| CSS | 3 arquivos, 35 KB, bloqueantes + `@import` do Google | `styles.min.css` 27,2 KB / 6,2 KB, não bloqueante |
| `motion-core` | 8,6 KB / 2,6 KB | 4,1 KB / 1,6 KB |
| `motion-sections` | 21,9 KB / 4,4 KB | 8,6 KB / 2,2 KB |
| Vendor (GSAP, ScrollTrigger, Lenis) | 133 KB / 50,7 KB | igual (já minificados; carregam após `load`) |
| Fontes | Google CDN: Montserrat 38 + Jakarta 27 + Caveat 75 + Bebas 14 KB, 2 origens externas | locais: 38 + 20 + 51 + 14 KB, 0 origens externas |
| Hero (LCP) no perfil Lighthouse | `hero-burger-800` 146 KB | `hero-burger-640` 83 KB |
| Dados/neon do hero | 30 + 115 KB | 4 + 6 KB |
| Textura de papel | PNG 75 KB | WebP sem perdas 46 KB (PNG como fallback) |

## Regressão

- **Geometria:** posição e tamanho de 176 elementos idênticos ao commit anterior nas 12 resoluções.
- **CSS crítico:** estilos computados e geometria da primeira tela idênticos com só o crítico e com
  o CSS completo, em 13 resoluções (verificado a cada build).
- **Pixels** (JS desligado, página inteira; pixel difere se algum canal variar > 24/255, limite 1%):
  11 de 12 resoluções passam (0,13%–0,82%). **390×844 fica em 1,06%.** Toda a diferença está
  *dentro das fotos* (textura do hambúrguer, das fotos do salão): é a reamostragem do degrau 480w,
  que substitui o 800w. Diferença média 1,6/255. Texto, bordas e layout são idênticos. Derivar os
  degraus do -800 em vez do -1600 foi testado e piorou (1,095%).
- **Testes existentes:** `test_responsive` (12 telas: rolagem, console, toque), `test_phase_a`,
  `test_phase_c`, e os 5 de motion por seção — todos passam, em `file://` e HTTP.
  `test_responsive` passou a usar `ThreadingHTTPServer`: o `HTTPServer` de thread única recusava
  conexões (fila de 5) quando o Chrome abria 6 em paralelo. Nenhuma asserção mudou.
- **Motion:** os 135 parâmetros de tempo (duration/delay/stagger/ease/repeat…) são idênticos após a
  minificação.

## Elementos pesados avaliados

| Elemento | Decisão |
| :--- | :--- |
| SVG das bordas rasgadas (inline, 2 paths longos) | **Movido** para `assets/torn-paper-{top,bottom}.svg`: cacheável, funciona em `file://`, `transform: none` preservado (testes de elemento contínuo passam) |
| Textura `paper-noise` (overlay fixo em toda a página) | **Mantida** em `background-image` (já era externa); ganhou WebP sem perdas |
| Carregador de motion inline | **Mantido inline**, só minificado: externo custaria mais uma requisição antes de tudo |
| Efeitos de pintura (blur, blend, sombras) | **Mantidos**: são visuais |

## Como reproduzir

```bash
npm run build                                          # gera site/ a partir de src/
python scripts/lighthouse_runs.py lh 3                  # servidor puro (comparável à baseline)
python scripts/lighthouse_runs.py lh 3 --prod           # gzip + cache do DEPLOY.md
python scripts/visual_snapshots.py capture <pasta>      # regressão de pixels
python scripts/visual_snapshots.py compare <ref> <nova>
```
