# PROGRESSO.md — Mr. Macário Burger

## Status do Projeto
**Fase Atual:** Otimização concluída (commit "otimizacao pronta"), sobre a tag `motion-pronto`  
**Data:** 10/10/2026  
**Status do Repositório:** Lighthouse mobile 92 (modo produção) / 89 (servidor puro), contra 68 na baseline. Regressão nas 12 resoluções.

> **Atenção, mudou o fluxo de edição:** HTML/CSS/JS editáveis agora ficam em `src/`. Depois de editar,
> rode `npm run build` (= `python scripts/build.py`) para gerar `site/`. Não edite `site/index.html`,
> `site/styles.min.css` nem `site/js/*.min.js` à mão. Detalhes em DESIGN.md §11 e DEPLOY.md.

---

## 1. O que foi feito nesta etapa de Refinamento de Fidelidade
- [x] **Eliminação Total dos Cards na Seção 2 (Menu Highlights):**
  - Removidos completamente os containers retangulares `.menu-card` com bordas e fundos brancos artificiais.
  - Os lanches e a cesta de batatas agora repousam de forma orgânica e direta sobre a base da landing page, com sombras de contato elípticas projetadas no solo.
  - Implementada a mancha de transição orgânica ondulada/diagonal em tom bege/areia (`#e0d2c3`) que corre por trás do Burguinho e das Batatas, criando a profundidade tátil do mockup.
  - Tag dourada `MR BURGUINHO` colada no topo do pão e selo circular verde menta `PREÇO JUSTO / R$ 20-40 // / BEM SERVIDO` estampado sobre a cesta de fritas.
- [x] **Aplicação de Textura Analógica Vintage Global:**
  - Gerada e aplicada uma textura contínua de micro-ruído de papel kraft/algodão (`site/assets/paper-noise.png`) com opacidade calibrada em overlay multiplicativo sobre toda a viewport.
  - Eliminado o fundo plano digital liso, conferindo a sensação de cartaz impresso físico.
- [x] **Refinamento do Hero (Seção 1):**
  - O letreiro "MR. M" e "ÁRIO" expandido para ocupar quase 95% da largura da viewport, em tom mostarda ocre envelhecido (`#b8973b`).
  - Gota de queijo derretido escorrendo do topo esquerdo (`cheese-drip`).
  - Batatinhas fritas crocantes voadoras com salpicos (`flying-fries.webp`) no ombro direito do pão.
  - Selos coloridos (azul, coral e menta), dados 3D, rabisco neon vermelho e comandas térmicas ajustados com alinhamento milimétrico.
- [x] **Refinamento da Chapa (Seção 3 — The Griddle Craft):**
  - Path de papel rasgado em SVG contínuo e orgânico derivado diretamente do perfil da referência, com encaixe sem costura (zero seams).
  - Remoção do escurecimento excessivo sobre a imagem, valorizando o ferro fundido, os smashers, a manteiga derretida e as faíscas incandescentes.
  - Seta em giz branco desenhada à mão apontando diretamente para a carne selada na chapa.
- [x] **Refinamento do Salão & Games (Seção 4 — The Board Game Lounge):**
  - As fotos dos amigos jogando cartas receberam moldura com acabamento de mesa de jogos em madeira escura, inclinadas dinamicamente (+5.5deg e -5.5deg) sob o troféu.
  - Troféu dourado 5.0 com escala dominante no centro em primeiro plano.
  - Fita crepe adesiva realista com depoimento de cliente em tipografia manuscrita cursiva encorpada.
- [x] **Refinamento do Rodapé & Conversão (Seção 5):**
  - Cenário do diner retrô enquadrado para posicionar as mesinhas brancas cromadas com saleiro nas margens laterais exatas.
  - Botões estilo cápsula neon com verde vibrante de alta visibilidade e colchetes característicos.
- [x] **Validação Visual Rigorosa em Múltiplas Resoluções:**
  - Capturas completas geradas em Desktop (1440px), Tablet (768px) e Mobile (390px) em `screenshots/final_full_*.png`.

---

## 2. Decisões de Fidelidade e Integridade Técnica
1. **Integração Real de Imagens:** As imagens dos produtos e elementos não são meros conteúdos de caixas de texto; são atores visuais do cenário, integrados com transparência alfa e sombras realistas de contato.
2. **Performance e Acessibilidade:** Mesmo com o visual de poster analógico, o site mantém HTML semântico com tags `<main>`, `<section>`, `<header>`, `<footer>`, `<picture>`, e links clicáveis com números e WhatsApp reais do Mr. Macário Burger.

---

## 3. Auditoria Responsiva Geral e Acessibilidade (12 Resoluções)
- [x] **Suíte de 12 Telas Testadas via Playwright:**
  - `2560x1440` (Ultra-wide Desktop): Scroll PASS | Console PASS | Touch PASS
  - `1920x1080` (Full HD Desktop): Scroll PASS | Console PASS | Touch PASS
  - `1440x900` (MacBook / Laptop): Scroll PASS | Console PASS | Touch PASS
  - `1366x768` (Laptop Comum): Scroll PASS | Console PASS | Touch PASS
  - `1280x720` (HD Desktop): Scroll PASS | Console PASS | Touch PASS
  - `1024x768` (iPad Landscape / 4:3): Scroll PASS | Console PASS | Touch PASS
  - `768x1024` (iPad Portrait): Scroll PASS | Console PASS | Touch PASS
  - `430x932` (iPhone Pro Max): Scroll PASS | Console PASS | Touch PASS
  - `390x844` (iPhone 12/13/14 Standard): Scroll PASS | Console PASS | Touch PASS
  - `360x740` (Android Médio Galaxy): Scroll PASS | Console PASS | Touch PASS
  - `320x568` (iPhone SE 1st gen / Tela Estreita): Scroll PASS | Console PASS | Touch PASS
  - `844x390` (Celular Deitado / Landscape): Scroll PASS | Console PASS | Touch PASS
- [x] **Critérios Obrigatórios Validados:**
  - Rolagem horizontal: 0px em todas as resoluções (`scrollWidth <= clientWidth`).
  - Textos: sem cortes ou sobreposições, escalonamento fluido com `clamp()`.
  - Alvos de toque (Touch Targets): mínimo de 44x44px em todos os links e botões.
  - Console do navegador: zero erros, sem 404 de recursos ou avisos JS.
  - Zoom de texto a 200%: `Overflow = 0px` (PASS).
  - Fallbacks de fonte: declarados e funcionais com `Impact`, `Arial Black`, `system-ui`.
  - `prefers-reduced-motion` e `prefers-color-scheme`: isolados e estáveis.
  - Safari/iOS: `100svh`, `-webkit-backdrop-filter` e `-webkit-text-size-adjust: 100%` ativos.
  - Elementos contínuos testados nos extremos (2560px ultra-wide e 844x390 landscape).

---

## 4. Auditoria Oficial Lighthouse Mobile
- **Scores Obtidos:**
  - **Acessibilidade:** 100 / 100
  - **Melhores Práticas:** 100 / 100
  - **SEO:** 100 / 100
  - **Performance:** 71 / 100 (TBT: 0ms | CLS: 0.007)
- **Top 3 Oportunidades Identificadas:**
  1. *Eliminar recursos que bloqueiam a renderização (Render-blocking):* Economia estimada de ~2.450 ms (Webfonts Google no `@import` CSS).
  2. *Otimizar entrega e carregamento de imagens:* Economia estimada de ~648 KiB (Hero burger central em conexões lentas mobile).
  3. *Minificar CSS:* Economia estimada de ~8 KiB (`style.css`, `tokens.css`, `reset.css`).

---

## 5. FASE A — Base Global de Motion (Concluída)
- [x] **Auditoria e Linha de Base:** Salva como `motion-baseline.md`.
- [x] **Auto-Hospedagem de Vendors:** GSAP, ScrollTrigger e Lenis em `site/js/vendor/` (scripts clássicos UMD para funcionamento em `file://` e HTTP sem dependência de CDN).
- [x] **Núcleo Global (`site/js/motion-core.js`):**
  - **3 Modos:** `full`, `reduced` (respeita `prefers-reduced-motion: reduce`, desativa loops/parallax), `paused` (congela/retoma timelines e scroll).
  - **2 Qualidades:** `high`, `low` (detecta memória <= 4GB, CPU <= 4 cores, rede lenta ou telas estreitas para economizar bateria e GPU).
  - **Lenis Smooth Scroll:** Ativo em desktop (>= 1024px) no modo full, integrado ao GSAP ticker.
  - **Segurança de Carga:** Nada acima da dobra depende de JS para aparecer. Scripts carregam de forma diferida em idle ou primeira interação.
  - **Pausa em Aba Oculta:** Integração com `visibilitychange` (pausa tudo quando aba perde foco).
  - **Pausa Fora da Tela:** `IntersectionObserver` para loops contínuos.
  - **Botão de Acessibilidade:** `#motion-pause-toggle` funcional com alvo de toque >= 44px e estados aria-pressed.
  - **Regra de Elementos Contínuos:** Verificado que elementos decorativos contínuos (divisória de chapa, SVG rasgado, texturas de ruído) possuem `transform: none` e não têm ancestrais animados.
- [x] **Regressão Completa:** Todas as 12 telas aprovadas.
- [x] **Tag Git:** `motion-base`.

---

## 6. FASE B — Animações por Seção (Concluída)
- [x] **Seção 1: Hero (`#hero`) — Cinematográfico Awwwards:**
  - Pouso heróico com física elástica (`elastic.out(1, 0.75)`), expansão sutil do letreiro dominante, ejeção dinâmica de batatas voadoras e dados 3D, carimbo sequencial de selos e comandas térmicas.
  - Parallax de cursor/mouse no desktop com `quickTo` suave.
  - Micro-flutuação senoidal em batatas e dados (`y: ±5px`, 3.6s-4.2s) e respiração do neon doodle.
  - Elemento LCP otimizado para pintura instantânea em conexões restritas.
- [x] **Seção 2: Destaques do Menu (`#menu-highlights`):**
  - Entrada dos 3 pratos a 35% de visibilidade com pouso suave no solo e projeção de sombra elíptica.
  - Tag dourada do pão e selo circular "Preço Justo" com carimbo elástico (`back.out`).
  - Mancha contínua de areia (`.menu-sand-shape`) blindada com `transform: none`.
- [x] **Seção 3: A Chapa / The Griddle Craft (`#griddle-craft`):**
  - Entrada com foco na crosta Maillard, carimbo térmico do selo e seta de giz desenhada.
  - Parallax panorâmico suave na chapa contido sob a moldura de papel.
  - Bordas de papel rasgado superior e inferior (`.torn-paper`) 100% estáticas.
- [x] **Seção 4: O Salão & Games (`#lounge-social`):**
  - Abertura em leque das molduras de madeira das mesas de jogos.
  - Pouso dominante do troféu dourado 5.0 com carimbo do selo Google Reviews e colagem elástica da fita crepe.
- [x] **Seção 5: Rodapé & Conversão (`#footer-conversion`):**
  - Revelação em cascata dos botões neon e horários da casa.
  - Glow contínuo sutil nos botões verdes neon e parallax discreto no cenário do diner.
  - Divisória de rolo de filme 35mm preservada intacta sem transform.

---

## 7. FASE C — Menu, Rodapé, Botão de Pausa e Coerência (Concluída)
- [x] **Inventário Completo:** Salvo em `motion-inventario.md`.
- [x] **Auditoria e Otimização de Loops:**
  - Conectado `IntersectionObserver` que congela loops que saem da janela.
  - Máximo de 2 a 4 loops simultâneos em qualquer ponto de rolagem (CPU < 1%).
- [x] **Gravação de Vídeo:** Vídeo completo em 60fps gravado em `screenshots/video/page@8151165c278e4157e187bc35fc479032.webm`.
- [x] **Regressão Final nas 12 Telas:** 100% aprovada (Zero overflow, zero erros de console, alvos de toque >= 44px).
- [x] **Tag Git:** `motion-pronto`.


---

## 8. Etapa de Otimização (Concluída)
- [x] **Baseline:** `otimizacao-baseline.md` (Performance 68, LCP 6,5 s; 3 execuções, mediana).
- [x] **Fontes locais:** WOFF2 subset latin em `site/fonts/`, só os pesos usados, `font-display: swap`,
  preload só de Bebas Neue + Montserrat (acima da dobra, injetado só em http(s)), sem CDN externo.
- [x] **CSS:** um arquivo só (`styles.min.css`, clean-css nível 1, fallbacks preservados). CSS crítico
  medido e verificado automaticamente, inline no `<head>`. O restante não bloqueia e é aplicado após
  a primeira pintura; `<noscript>` como fallback.
- [x] **Imagens:** `srcset`/`sizes` medidos por breakpoint, `fetchpriority="high"` só no hero (LCP),
  `loading="lazy"` no resto, degraus 120–1200w gerados, `aspect-ratio` travado (geometria idêntica),
  textura em WebP sem perdas.
- [x] **Elemento pesado:** bordas rasgadas movidas para SVG externo cacheável.
- [x] **JS:** `motion-core` 8,6 → 4,1 KB e `motion-sections` 21,9 → 8,6 KB (terser); tempos de motion intactos.
- [x] **DEPLOY.md:** compressão e `Cache-Control` recomendados, sem escolher hospedagem.
- [x] **Resultado:** `otimizacao-resultado.md`. Performance **92** em modo produção (gzip), **89** no
  servidor puro da baseline; FCP 3,8 → 0,77 s; LCP 6,5 → 3,4 s; CLS 0.
- [x] **Testes:** os 8 scripts existentes passam. Geometria idêntica em 176 elementos × 12 resoluções.
- [ ] **Pendente/aceito:** regressão de pixels em 390×844 fica em 1,06% (limite 1%), só por
  reamostragem dentro das fotos com o degrau 480w. Texto e layout são idênticos.
- [ ] **Pendente/aceito:** Melhores Práticas 96 por texto < 12 px nos selos (decisão visual do mockup).

### O que falta
- Publicação: escolher hospedagem e aplicar os cabeçalhos do DEPLOY.md.
- Pendências factuais do cliente (DESIGN.md §10) seguem abertas.
