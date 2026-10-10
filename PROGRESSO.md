# PROGRESSO.md — Mr. Macário Burger

## Status do Projeto
**Fase Atual:** Rodada final concluída (tag `v1.0-rc`) — tecnicamente pronto, **bloqueado para publicação** até a troca das imagens geradas por IA (PENDENCIAS-CLIENTE.md, item 1)  
**Data:** 10/10/2026  
**Status do Repositório:** Lighthouse mobile 92 (modo produção) / 89 (servidor puro), contra 68 na baseline. Regressão nas 12 resoluções.

> **Dados do cliente:** arquivo único `cliente.config.json` (substituiu `seo.config.json`).
>
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


---

## 9. Etapa de SEO Local (Concluída)
- [x] `<title>` (64 caracteres) e meta description (150) só com dados do CLIENTE.md; `lang="pt-BR"`,
  `theme-color`, `robots`.
- [x] Open Graph + Twitter Card (`summary_large_image`); imagem `assets/og-image.jpg` 1200x630 = hero
  aprovado sem texto miúdo e sem pessoas.
- [x] JSON-LD `Restaurant` só com dados confirmados. Horário, faixa de preço e link do cardápio ficam
  comentados; sem `aggregateRating` (avaliações do Google, de terceiros).
- [x] `seo.config.json` com um único campo (`domain`, hoje `null`): canonical, og:url, og:image,
  twitter:image, `@id`/url/image/logo do JSON-LD, `Sitemap:` e `<loc>` ficam comentados até ele existir
  (testado também com um domínio de exemplo).
- [x] `robots.txt`, `sitemap.xml` (gerados pelo build), favicons (.ico 16/32/48, apple-touch 180,
  192, 512, maskable) a partir do logo real, `site.webmanifest`.
- [x] Semântica: um `<h1>` (letreiro do hero) + 4 `<h2>` em ordem; `alt` em todas as imagens
  informativas, `alt=""` nas decorativas; `alt` das fotos de jogos sem afirmar que são do salão real.
- [x] Regressão: **0,000% de pixels diferentes** nas 12 resoluções; 8 testes passam; Lighthouse SEO 100,
  Acessibilidade 100. Performance 87–89 nesta máquina (o commit anterior medido junto: 89–92), dentro do ruído.

### Pendências de conteúdo VISÍVEL (não alteradas: etapa sem mudança visual) — decidir com o cliente
Textos que vieram do mockup ou não estão no CLIENTE.md, contrariando a regra "nenhum texto do mockup vira final":
1. Títulos `<h2>` em inglês, herdados do mockup: "MENU HIGHLIGHTS", "THE GRIDDLE CRAFT",
   "THE BOARD GAME LOUNGE" e **"FOOTER & CONVERSION"** (rótulo de wireframe, péssimo como título
   para SEO e para o usuário).
2. Comanda do hero "TOTAL: R$ 34,90": preço inventado (não há preço confirmado; pendência 2).
3. Selo "100% CARNE FRESCA": afirmação não confirmada pelo cliente.
4. Depoimento da fita crepe: é uma junção editada da avaliação de Maria Do Carmo no Google, não uma
   citação literal.
5. Fotos "mesa de jogos" (pessoas jogando cartas): não retratam o salão real (fliperamas/booths
   vermelhos, DESIGN.md §1), e pessoas devem ser fotos reais do cliente pela regra de ouro.
6. Fazer o build com o domínio quando ele existir (`seo.config.json`).


---

## 10. Rodada Final (Concluída — 10/10/2026)
- [x] **Auditoria completa** (`scripts/auditoria_final.py`): Chromium + WebKit × 15 telas (320 px a 5120 px,
  incluindo 3440×1440, 3840×2160 e 5120×1440) × modos padrão, movimento reduzido, escuro, sem JS e
  `file://` = **135/135 sem problema** (rolagem lateral, console, imagens, toque ≥ 44 px, um h1, alt,
  seções de borda a borda, motion iniciado/modo reduzido respeitado, conteúdo visível).
- [x] **Bug corrigido:** em 3840×2160 o título e os botões do rodapé nunca apareciam com motion (o
  gatilho de revelação ficava além da rolagem máxima). `revealStart()` limita o início à rolagem
  máxima; nas telas comuns os pontos são os mesmos. `clamp()` do ScrollTrigger foi testado e não
  resolveu o limite superior.
- [x] **Lighthouse mobile (mediana de 3):** modo produção **89** (86–89); servidor puro **86** (85–97,
  alta variância nesta máquina). Acessibilidade 100 · Melhores práticas 96 · SEO 100 · CLS 0.
  Na otimização a mediana de produção foi 92 (89–92): a diferença está dentro da faixa observada.
- [x] **Regressão:** pixels idênticos (0,000%) à etapa de SEO nas 12 telas; 8 testes existentes passam.
- [x] **Config único** `cliente.config.json` (domínio, horário, faixa de preço, cardápio, trava de imagens)
  — testado ligando os 3 campos confirmados e voltando.
- [x] **Achado:** as fotos de comida/chapa/salão são geradas por IA e não correspondem às fotos reais;
  batatas voadoras recortadas do mockup. Classificação em `assets.md`; trava no build.
- [x] **Polimento feito:** ícones -60% (paleta, diferença média 1,7/255); fotos não usadas → `reserva/`
  (fora do deploy); scripts quebrados/únicos → `scripts/_historico/`; `site/fonts/LICENSE.txt`.
- [x] **Documentos:** README.md, PENDENCIAS-CLIENTE.md, ROTEIRO-APARELHO-REAL.md.

### Polimento que espera decisão (não feito)
- Trocar imagens geradas por IA por fotos reais (exige rodada de design) — cliente.
- Textos do mockup visíveis (títulos em inglês, "FOOTER & CONVERSION", "R$ 34,90", "100% carne fresca")
  — cliente.
- Telas com mais de 2560 px de CSS (ex.: 5120×1440): conteúdo fica limitado a ~1440 px no centro, com
  laterais vazias. Funciona, mas pede decisão de design (escalar o conteúdo acima de 2560 px?).
- Texto < 12 px nos selos (Melhores Práticas 96) — decisão visual.
- Regressão de 1,06% em 390×844 (reamostragem de foto) — aceita na otimização.
- Nomes de arquivo com hash para cache longo — depende da hospedagem.
- Sensação real de motion, Safari iOS, barra de endereço, toque — `ROTEIRO-APARELHO-REAL.md`.

### Push
Sem remoto Git configurado e sem `GH_TOKEN` no ambiente: feitos só commit e tag locais.
