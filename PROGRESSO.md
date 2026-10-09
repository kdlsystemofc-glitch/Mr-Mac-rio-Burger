# PROGRESSO.md — Mr. Macário Burger

## Status do Projeto
**Fase Atual:** Passada Responsiva Geral e Auditoria Lighthouse Concluídas  
**Data:** 09/10/2026  
**Status do Repositório:** Validado em 12 resoluções, Lighthouse Mobile auditado, pronto para commit.

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
