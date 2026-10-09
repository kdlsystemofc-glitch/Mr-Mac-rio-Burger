# PROGRESSO.md — Mr. Macário Burger

## Status do Projeto
**Fase Atual:** Construção Completa do Site (Etapas 0 a 4 Concluídas)  
**Data:** 09/10/2026  
**Status do Repositório:** Todos os commits locais realizados. Token remoto (GH_TOKEN) não configurado no ambiente — push suspenso conforme regras do projeto.

---

## 1. O que foi feito nesta etapa
- [x] **Etapa 0:** Inicialização do repositório Git, configuração do `.gitignore` (`node_modules/`, `screenshots/`, `.playwright/`), e commit inicial `"design pronto"`.
- [x] **Etapa 1 — Inventário de Assets:**
  - Conversão de todas as imagens para WebP otimizado (800px e 1600px com canal alfa transparente preservado quando aplicável).
  - Geração do documento [`assets.md`](file:///c:/Oficial/Mr.%20Mac%C3%A1rio%20Burger/assets.md) mapeando cada slot do `DESIGN.md` para arquivos de alta fidelidade e registrando fallbacks reais do cliente.
- [x] **Etapa 2 — Fundação:**
  - Criação de `site/tokens.css` contendo variáveis de cor com contraste auditado (WCAG), fontes do Google (`Bebas Neue`, `Montserrat`, `Plus Jakarta Sans`, `Caveat`) e escalas fluidas (`clamp`).
  - Criação de `site/reset.css` com suporte a `prefers-reduced-motion` e foco acessível.
  - Implementação da regra obrigatória de **Full-Bleed**: cada seção controla seu próprio fundo de ponta a ponta da viewport, sem encapsulamento em container fixo único com sombras.
  - Instalação e configuração do Playwright Chromium e criação de `scripts/screenshot.py` com servidor local headless.
- [x] **Etapa 3 — Construção Seção por Seção (Layout Estático):**
  - **Hero:** Letreiro gigante "MR. MACÁRIO", burger principal duplo farto, dados 3D, neon doodle, selos circulares, pílulas "Vila da Saúde" e "Abre 18:45". Fechado na rodada 2 e commit `"hero pronta"`.
  - **Destaques do Cardápio:** Grid fluido com os 3 itens, tag "MR BURGUINHO", selo "PREÇO JUSTO R$ 20-40", badges e preços. Fechado na rodada 2 e commit `"destaques do cardápio pronta"`.
  - **A Técnica da Chapa:** Fundo escuro texturizado, divisores superior e inferior em **SVG de papel rasgado orgânico**, selo coral "CROSTA MAILLARD" e seta em giz. Fechado na rodada 2 e commit `"a técnica da chapa pronta"`.
  - **Salão & Avaliações:** Polaroids inclinados, troféu dourado 5.0, selo Google 63 avaliações e fita crepe com depoimento real em fonte manuscrita. Fechado na rodada 2 e commit `"salão e avaliações pronta"`.
  - **Rodapé & Conversão:** Faixa perfurada de filme 35mm em CSS, cenário retro diner, botões com brilho neon pulsante, WhatsApp oficial `(11) 96514-2258` corrigido e dados de localização. Fechado na rodada 1 e commit `"rodapé e conversão pronta"`.
  - *Conformidade de Assets:* 100% dos assets consumidos vêm de `site/assets/`. Nenhum arquivo de `/design` ou imagens brutas foi usado no HTML/CSS.
- [x] **Etapa 4 — Validação Visual Final:**
  - Capturas de tela da página inteira em 1440px (desktop), 768px (tablet) e 390px (mobile) salvas em `screenshots/final_full_*.png`.
  - Verificação de ausência de overflow horizontal e transições perfeitas entre seções.

---

## 2. Diferenças em Relação ao Mockup de Referência (Decisões de Engenharia & Verdade Factual)
1. **Full-Bleed Real vs. Cartaz Fixo:** O mockup foi gerado com proporções de cartaz vertical (768x1376px). O site foi construído para expandir em full-bleed de borda a borda em qualquer tela (1440px, 1920px, 4K), com o conteúdo centralizado fluidamente.
2. **Correção de Telefone no Rodapé:** O mockup continha um número com dígito incorreto em um dos botões (`(11) 98814-2258`). Unificamos todos os CTAs para o WhatsApp real e verificado do cliente: `(11) 96514-2258`.
3. **Contraste Acessível (WCAG):** O dourado original do letreiro hero e o verde neon dos botões foram calibrados com valores que garantem conformidade WCAG AA (texto legível e acessível).
4. **Bordas de Papel Rasgado em SVG:** Em vez de usar imagens PNG fixas que quebrariam na responsividade, o papel rasgado foi implementado com vetores SVG que mantêm definição infinita em qualquer resolução.
5. **Idioma:** Substituição de jargões mistos em inglês ("MENU HIGHLIGHTS", "THE GRIDDLE CRAFT", "THE BOARD GAME LOUNGE") por chamadas autênticas em português brasileiro ("Destaques do Cardápio", "A Técnica da Chapa", "Salão & Fliperamas Retrô", "Peça Agora").
