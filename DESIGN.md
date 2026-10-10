# DESIGN.md — Análise Visual, Decomposição & Arquitetura de Design
**Projeto:** Mr. Macário Burger  
**Referência Visual:** `design/mockup-full.png` (fatias em `design/secoes/`)  
**Dados Factuais:** `CLIENTE.MD` e `imagens/`

---

## 1. Leitura Honesta do Mockup vs. A Realidade

Uma auditoria visual rigorosa comparando a referência de design (`mockup-full.png`) com a documentação do negócio (`CLIENTE.MD`) e o acervo fotográfico real (`imagens/`):

| Elemento | Mockup (`mockup-full.png`) | Realidade do Negócio (`CLIENTE.MD` / `imagens/`) | Veredito & Decisão |
| :--- | :--- | :--- | :--- |
| **Logotipo** | Apenas um texto genérico sem serifa em caixa alta: "MR. MACÁRIO BURGER" centralizado no topo. | O cliente possui um selo circular vintage completo (`imgi_2`, `imgi_3`, `imgi_18`): hambúrguer com queijo, faixa curva preta com tipografia serifada retrô, arcos "HAMBURGUERIA ARTESANAL" e "SINCE 2023" com estrelas. | **Incoerente no mockup.** O logotipo real do cliente tem forte personalidade artesanal e identidade histórica. Devemos manter o logotipo oficial vetorizado/restaurado em alta definição, usando o texto limpo apenas em contextos de acessibilidade ou subtítulos. |
| **Hambúrguer Hero** | Smash quádruplo americano perfeito com fatias compridas de bacon e queijo derretido de estúdio (banco de imagens / stock 3D). | Hambúrgueres artesanais fartos reais (`imgi_10`, `imgi_11`, `imgi_14`), com crosta Maillard evidente, queijo cheddar cremoso e bacon artesanal, servidos de forma muito característica em panelinhas de cobre individuais. | **Fictício no mockup.** Conforme a Regra de Ouro do projeto, comida nunca é gerada por IA. Usaremos o recorte tratado da foto real mais imponente (`imgi_11` ou `imgi_14`), preservando a textura apetitosa e verdadeira do produto. |
| **Destaques do Cardápio** | Três itens de stock photo: 1 smash duplo genérico, 1 burger simples com alface de fast-food ("MR BURGUINHO"), e 1 barquinha americana xadrez de papelão com batatas fritas de diner. | Cardápio real conta com lanches servidos em frigideirinhas de cobre (`imgi_10`, `imgi_13`), batatas rústicas com cheddar e cubos de bacon em panelinha de cobre (`imgi_13`), lanches no pão australiano (`imgi_11`) e uma exclusiva sobremesa artesanal: hambúrguer de brigadeiro com granulado e bombom (`imgi_5`). | **Fictício no mockup.** Substituiremos as fotos de banco pelas fotos reais recortadas dos produtos do Mr. Macário, valorizando a apresentação signature nas panelinhas de cobre. |
| **Chapa / Cozinha ("The Griddle Craft")** | Chapa de fundição pesada com duas prensas de smash, faíscas incandescentes saindo da carne (estilo solda/showcooking teatral), fumaça cenográfica e cubos inteiros de manteiga derretendo ao lado. | Cozinha de chapa artesanal real de bairro paulistano (Vila da Saúde). O produto tem crosta Maillard autêntica, mas as faíscas de estúdio e a fumaça de espetáculo são pura encenação de imagem de stock. | **Cenográfico/Fictício.** O conceito de crosta Maillard é factual e valoriza o método artesanal do cliente. Podemos manter a atmosfera escura de chapa e textura de ferro fundido, mas priorizando a foto real do chapeiro/chef (`imgi_14`) ou um plate de apoio sem exageros circenses. |
| **Salão & Experiência ("The Board Game Lounge")** | Fotos estilo stock photo com atores jovens sentados em mesas verdes de madeira clara jogando cartas e jogos de tabuleiro analógicos ("JOGOS NO SALÃO // AMBIENTE DESCONTRAÍDO"). | O salão real (`imgi_3`, `imgi_13`, `imgi_18`) tem atmosfera moderna urbana com grafites vibrantes de hambúrguer nas paredes, cabines/booths estofados em capitonê vermelho sangue com botões pretos, e **telas/monitores de videogame e fliperamas retrô embutidos ao lado de cada mesa**! | **Distorção no mockup.** O cliente tem "jogos no salão", mas são **games/fliperamas retrô digitais** nas mesas, e não jogos de cartas em mesas de madeira verde! A realidade do cliente é ainda mais interessante e atrativa que a invenção do mockup. |
| **Rodapé / Conversão** | Diner americano anos 50 com paredes vermelhas lisas, mesas de fórmica branca com pés tubulares cromados e saleiros de vidro de lanchonete dos EUA. | Fachada real na Vila da Saúde com toldo preto e grafite (`imgi_18`), salão com booths vermelhos e paredes grafitadas (`imgi_13`). | **Estrangeiro/Cenográfico no mockup.** Manteremos a vibração das cores vermelhas e dos botões neon, mas com suporte responsivo limpo via CSS em vez de tentar sobrepor botões em uma foto estática de mesa com perspectiva distorcida. |
| **Textos & Idioma** | Mistura confusa de termos em inglês e português ("HERO", "MENU HIGHLIGHTS", "THE GRIDDLE CRAFT", "THE BOARD GAME LOUNGE", "FOOTER & CONVERSION", misturado com "PREÇO JUSTO", "VILA DA SAÚDE", "100% CARNE FRESCA"). | Hamburgueria local paulistana, público 100% brasileiro, clientes do bairro da Saúde e pedidos via WhatsApp/delivery. | **Incoerente no mockup.** Toda a interface deve comunicar em português brasileiro autêntico, acolhedor e focado em conversão. |
| **WhatsApp no Rodapé** | O mockup apresenta dois números divergentes: `(11) 96514-2258` no primeiro botão e um número errado com dígito trocado `(11) 98814-2258` no terceiro botão. | O número oficial do cliente é único: `(11) 96514-2258` (confirmado na fachada `imgi_18` e no Google Maps `CLIENTE.MD`). | **Erro de digitação no mockup corrigido.** Todos os CTAs usarão o número verificado `(11) 96514-2258`. |

---

## 2. Elementos Decorativos de Assinatura & Viabilidade Técnica

O mockup possui 4 grandes elementos de assinatura visual. Avaliação honesta de complexidade e viabilidade:

### 1. Borda de Papel Rasgado Contínua (*Torn Paper / Rip Edge Mask*)
- **No mockup:** Envolve o topo e a base da seção escura da chapa ("The Griddle Craft"), criando um rasgo orgânico entre o creme claro e o grafite escuro.
- **Viabilidade técnica:** **Totalmente viável e performática.**
- **Como implementar:** NUNCA usar uma imagem rasterizada (PNG) pesada e fixa, pois perderia nitidez e quebraria em telas ultrawide ou mobile. A implementação ideal é via **SVG vetorial inline** aplicado como máscara (`mask-image: url(...)`) ou via pseudo-elementos `::before` e `::after` com o path de papel rasgado em SVG esticado horizontalmente (`preserveAspectRatio="none"` ou repetição horizontal). Leve (< 2KB), responsivo de 320px a 4K e sem impacto de carregamento.

### 2. Stickers, Selos Redondos Inclinados e Doodles Neon
- **No mockup:**
  - Selo "VILA DA SAÚDE" (pílula verde-menta);
  - Selo "CROSTA MAILLARD" (círculo salmão/coral com traço de burger);
  - Selo "PREÇO JUSTO R$ 20-40" (círculo menta com carimbo);
  - Selo azul de topo e carimbo "BOM DEMAIS";
  - Traços orgânicos neon vermelho (fio de neon aceso simulando bacon/molho).
- **Viabilidade técnica:** **100% viável e recomendada em CSS/SVG nativo.**
- **Como implementar:** Os selos são elementos HTML/CSS puros com `border-radius: 50%`, `transform: rotate(-8deg)` e SVG icons no interior. Os doodles de neon são SVGs vetoriais com `filter: drop-shadow(0 0 6px rgba(255, 60, 60, 0.8))`. Não necessitam de imagens rasterizadas, escalam sem perda e aceitam animações CSS ultra suaves.

### 3. Elementos 3D Flutuantes (Dados, Fritas e Comandas)
- **No mockup:** Dois dados brancos 3D suspensos no ar, palitos de batata frita voando e pequenos canhotos de comandas de papel.
- **Viabilidade técnica:** **Totalmente viável, desde que isolados.**
- **Como implementar:**
  - Os dados e as batatas fritas podem ser assets leves em PNG com fundo transparente (< 40KB cada), posicionados como camadas absolutas decorativas (`aria-hidden="true"`), com animação sutil de flutuação via CSS `@keyframes translateY`.
  - As comandas fiscais de papel podem ser micro-componentes HTML/CSS com borda em zig-zag (`repeating-linear-gradient` para o picote) ou pequenos SVGs.

### 4. Divisória de Fita de Cinema / Negativo 35mm
- **No mockup:** Faixa preta com perfurações quadradas no topo da seção vermelha de conversão.
- **Viabilidade técnica:** **Simples e 100% CSS puro.**
- **Como implementar:** CSS `background` com `repeating-linear-gradient` ou SVG `mask-image` repetido no eixo X. Custo zero de assets e resolução infinita.

### 5. Alerta de Inviabilidade / Antipattern: Mesas do Rodapé
- **No mockup:** Os botões de pedido estão sobrepostos sobre uma foto recortada de duas mesinhas de diner branco com saleiros.
- **Alerta de risco:** Em telas mobile (360px–420px), sobrepor múltiplos botões largos sobre fotos de mesas gera colisão de layout desastrosa (o texto cobre as mesas ou as mesas encolhem até virarem borrões ilegíveis).
- **Solução recomendada:** Fazer o container do rodapé com o tom vermelho vibrante do salão do cliente (`#bd3b2b`), borda perfurada no topo e os botões em grid/flexbox fluido com efeito neon, sem prender a usabilidade a uma imagem estática de mesa.

---

## 3. Paleta Cromática em HEX & Auditoria de Contraste WCAG 2.1

Cores extraídas diretamente da amostragem de pixels do mockup (`mockup-full.png`) e testadas contra a norma WCAG 2.1 (mínimo de 4.5:1 para texto normal, 3.0:1 para texto grande/componentes de UI, e 7.0:1 para AAA):

```css
:root {
  /* Fundos */
  --bg-cream: #f2e9e2;            /* Fundo principal quente vintage */
  --bg-cream-card: #f9f4ef;       /* Fundo de cards e caixas de destaque */
  --bg-griddle-black: #0b0e13;    /* Preto carvão / chapa de ferro fundido */
  --bg-diner-red: #bd3b2b;        /* Vermelho vibrante diner / estofado do salão */
  --bg-tape-paper: #eae2d3;       /* Bege fita crepe do depoimento */

  /* Textos Principais */
  --text-espresso: #2c150f;       /* Marrom café expresso profundo / quase preto */
  --text-white: #ffffff;          /* Branco puro */
  --text-cream-light: #ffefe8;    /* Branco quente para seções escuras */

  /* Acentos & Selos */
  --accent-gold-raw: #be9032;     /* Dourado do mockup (REPROVADO em texto normal) */
  --accent-gold-ui: #987328;      /* Dourado escurecido acessível (3.64:1 em fundo claro) */
  --accent-gold-text: #856423;    /* Dourado para texto corrido (4.56:1 - WCAG AA) */
  --accent-mint-bg: #82c399;      /* Fundo verde-menta do selo 'Vila da Saúde' */
  --accent-mint-text: #21432f;    /* Verde floresta escuro para texto no selo menta */
  --accent-coral-bg: #ef7367;     /* Fundo coral/salmão do selo 'Crosta Maillard' */
  --accent-coral-text: #2c150f;   /* Texto escuro no selo coral */
  --accent-neon-green: #25d366;   /* Verde WhatsApp oficial e botões de ação */
  --accent-neon-glow: #91ed96;    /* Brilho e borda neon pulsante */
  --accent-trophy-gold: #dfa422;  /* Dourado metálico do troféu 5.0 */
}
```

### Tabela de Auditoria de Contraste WCAG 2.1

| Par de Cores (Texto / Fundo) | Amostrado no Mockup | Razão Original | Status Original | Ajuste / Correção de Contraste | Razão Corrigida | Conformidade |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Texto Principal s/ Fundo Claro** | `#2c150f` em `#f2e9e2` | **14.35:1** | **APROVADO** | Mantido sem alteração. | 14.35:1 | **WCAG AAA** (Excelente) |
| **Tipografia "MR. MACÁRIO" Hero** | `#be9032` em `#f2e9e2` | **2.43:1** | ❌ **REPROVADO** | Usar `#987328` para texto grande display, ou tratar o letreiro gigante de fundo como elemento gráfico decorativo (`aria-hidden="true"`), com o `<h1>` semântico acessível no DOM. | 3.64:1 | **WCAG AA** (Texto Grande >= 24px) |
| **Texto no Selo "Vila da Saúde"** | `#21432f` em `#82c399` | **5.66:1** | **APROVADO** | Mantido com verde floresta escuro no texto e menta na pílula. | 5.66:1 | **WCAG AA** |
| **Texto no Selo "Crosta Maillard"** | `#2c150f` em `#ef7367` | **5.99:1** | **APROVADO** | Mantido com marrom expresso sobre o círculo coral. | 5.99:1 | **WCAG AA** |
| **Texto Branco s/ Chapa Escura** | `#ffefe8` em `#0b0e13` | **17.27:1** | **APROVADO** | Mantido no bloco "The Griddle Craft". | 17.27:1 | **WCAG AAA** (Máxima legibilidade) |
| **Texto Branco s/ Vermelho Rodapé** | `#ffffff` em `#bd3b2b` | **5.49:1** | **APROVADO** | Mantido nos horários e dados de endereço. | 5.49:1 | **WCAG AA** |
| **Botão Neon Verde no Rodapé** | `#91ed96` em `#bd3b2b` | **3.86:1** | ⚠️ Parcial | Fazer o botão com fundo sólido `#25d366` e texto preto/escuro `#0b1a0e` (contraste de **11.2:1**), mantendo o halo neon externo `#91ed96` via `box-shadow`. | 11.20:1 | **WCAG AAA** |
| **Texto na Fita Crepe (Depoimento)** | `#2c150f` em `#eae2d3` | **13.36:1** | **APROVADO** | Mantido sem alteração. | 13.36:1 | **WCAG AAA** |
| **Pílula "Abre 18:45"** | `#bd3b2b` em `#ffffff` | **5.49:1** | **APROVADO** | Texto vermelho sobre pílula branca. | 5.49:1 | **WCAG AA** |

---

## 4. Tipografia Google Fonts

*Conforme regra estrita do `CLAUDE.md`: Proibido utilizar Inter, Roboto ou Arial.*

### 1. Títulos de Impacto / Display (Headlines das Seções)
- **Opção A (Recomendada): `Bebas Neue`** (Google Fonts)  
  *Justificativa:* Fonte display condensada icônica, com desenho geométrico e proporções sólidas que reproduzem fielmente os títulos do mockup ("MENU HIGHLIGHTS", "THE GRIDDLE CRAFT", "THE BOARD GAME LOUNGE"). Possui personalidade de diner artesanal, excelente impacto em caixas altas e renderização nítida em qualquer dispositivo.
- **Opção B (Alternativa): `Anton`** (Google Fonts)  
  *Justificativa:* Mais encorpada e robusta que a Bebas Neue, adiciona ainda mais peso visual e sensação de "poster" vintage americano. Excelente alternativa caso se deseje uma presença tipográfica mais pesada.

### 2. Subtítulos, Selos, Badges & Botões de Ação (UI Elements)
- **Opção A (Recomendada): `Montserrat`** (Google Fonts — pesos 600, 700, 800)  
  *Justificativa:* Sans-serif geométrica com raízes em letreiramento urbano clássico. Em caixa alta e tracking levemente espaçado (`letter-spacing: 0.05em`), confere clareza impecável aos selos ("VILA DA SAÚDE", "PREÇO JUSTO", "CROSTA MAILLARD") e aos botões de conversão do WhatsApp.
- **Opção B (Alternativa): `Oswald`** (Google Fonts — pesos 500, 600)  
  *Justificativa:* Fonte sem serifa levemente condensada, harmoniza com o estilo industrial das hamburguerias e mantém os botões compactos em telas estreitas de smartphones.

### 3. Corpo de Texto, Endereço, Horários & Cardápio (Legibilidade)
- **Opção A (Recomendada): `Plus Jakarta Sans`** (Google Fonts — pesos 400, 500, 700)  
  *Justificativa:* Tipografia moderna de proporções generosas e toque humanista contemporâneo. Garante leitura limpa e confortável em textos corridos, avaliações do Google e especificações de endereço sem o aspecto corporativo e sem graça de fontes genéricas.
- **Opção B (Alternativa): `Outfit`** (Google Fonts — pesos 400, 500, 600)  
  *Justificativa:* Fonte geométrica acolhedora, desenhada especificamente para interfaces digitais, muito agradável para exibição de cardápios e descrições de lanches.

### 4. Manuscrita Autêntica (Depoimento em Fita Crepe)
- **Opção A (Recomendada): `Caveat`** (Google Fonts — peso 600)  
  *Justificativa:* Fluida, expressiva e natural. Parece genuinamente uma anotação feita com caneta esferográfica sobre fita crepe, casando perfeitamente com a frase de depoimento do cliente.
- **Opção B (Alternativa): `Kalam`** (Google Fonts — peso 700)  
  *Justificativa:* Estilo caligráfico de marcador permanente/pilot, confere autenticidade de anotação de cozinha.

---

## 5. Tabela de Camadas por Seção (*Layer Stack Architecture*)

Separação estrita de responsabilidades entre código CSS, vetores SVG, fotos reais do cliente e plates gerados:

| Seção | Camada 1: Fundo / Base (CSS) | Camada 2: Texturas & Divisórias (CSS / SVG) | Camada 3: Tipografia & Gráficos de Fundo (CSS/SVG) | Camada 4: Mídia Principal (FOTO REAL / PLATE) | Camada 5: Badges, Stickers & Doodles (CSS/SVG) | Camada 6: Ações & Conversão (CSS/HTML) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01. Hero** | `background-color: var(--bg-cream)` | Salpicos de sal e manchas suaves em SVG decorativo | Texto gigante "MR. MACÁRIO" em CSS clamp com cor ocre acessível | **FOTO REAL:** Recorte de alta resolução do hambúrguer smash duplo suculento (`imgi_11`) | Selo "VILA DA SAÚDE" (CSS/SVG), pílula "ABRE 18:45" (CSS), neon doodle curvo (SVG) e dados 3D (Plate isolado) | Botão CTA principal de pedido no delivery / WhatsApp |
| **02. Menu Highlights** | `background-color: var(--bg-cream)` | Linha ondulada sutil de transição em CSS | Título "DESTAQUES DO CARDÁPIO" (`Bebas Neue`) | **FOTOS REAIS:**<br>1. Smash artesanal (`imgi_10`)<br>2. Batata rústica com cheddar e bacon na panelinha (`imgi_13`)<br>3. Burger doce artesanal de brigadeiro (`imgi_5`) | Selo circular "PREÇO JUSTO / R$ 20-40 // BEM SERVIDO" (CSS/SVG) e pílula dourada do nome do lanche | Cards clicáveis direcionando para o cardápio interativo |
| **03. The Griddle Craft** | `background-color: var(--bg-griddle-black)` | Bordas superior e inferior em **SVG de papel rasgado** (`clip-path` ou máscara inline) | Título "A TÉCNICA DA CHAPA" e subtítulo sobre Crosta Maillard | **FOTO REAL / PLATE:** Foto real do chapeiro segurando o lanche com crosta perfeita (`imgi_14`) ou Plate macro de apoio de smash na chapa com fumaça | Selo coral circular "CROSTA MAILLARD" com ícone vetorial de hambúrguer e seta indicativa (SVG) | Texto explicativo sobre o ponto e a selagem da carne fresca |
| **04. Salão, Games & Avaliações** | `background-color: var(--bg-cream)` | Sombreamentos sutis de profundidade nos cards | Título "SALÃO & FLIPERAMAS RETRÔ" com subtítulo de ambiente descontraído | **FOTOS REAIS:** Polaroids autênticos do salão com mesas em capitonê vermelho e fliperamas retrô (`imgi_13`, `imgi_3`) | Troféu dourado de 5.0 estrelas (SVG rico ou Plate isolado), selo "63 AVALIAÇÕES GOOGLE" (CSS) e fita crepe com depoimento real (`Caveat`) | Link direto para as 63 avaliações 5 estrelas no Google Maps |
| **05. Rodapé & Conversão** | `background-color: var(--bg-diner-red)` | Faixa perfurada de rolo de filme/negativo 35mm no topo em CSS puro | Título "PEÇA AGORA // MR. MACÁRIO" | **FOTO REAL:** Fachada noturna autêntica com toldo e letreiro iluminado (`imgi_18` / `imgi_3`) | Efeito de brilho neon verde pulsante nos contornos dos botões | Botões de conversão rápida: WhatsApp direto `(11) 96514-2258`, horário e endereço na Vila da Saúde |

---

## 6. Reinterpretação de Elementos Decorativos Complexos em CSS/SVG Real

Para garantir carregamento instantâneo, responsividade em todas as resoluções e aderência às regras do projeto, nenhum elemento de layout será fatiado como imagem estática:

### 1. Borda de Papel Rasgado (*Torn Paper Border*)
- **Abordagem:** Utilização de um path SVG otimizado em dente de serra irregular repetível ou máscara esticada com `preserveAspectRatio="none"`.
```html
<!-- Exemplo arquitetural do divisor SVG responsivo -->
<div class="torn-paper-divider top" aria-hidden="true">
  <svg viewBox="0 0 1200 30" preserveAspectRatio="none">
    <path d="M0,0 L0,18 Q30,28 60,15 T120,22 T180,12 T240,25 T300,16 T360,28 T420,14 T480,24 T540,15 T600,26 T660,13 T720,27 T780,18 T840,25 T900,12 T960,26 T1020,15 T1080,27 T1140,16 T1200,22 L1200,0 Z" fill="var(--bg-cream)" />
  </svg>
</div>
```
- **Vantagem:** Pesa menos de 1KB, não estoura no mobile e escala perfeitamente até 4K.

### 2. Faixa Perfurada de Rolo de Filme do Rodapé
- **Abordagem:** 100% CSS puro sem requisições HTTP adicionais.
```css
.film-strip-divider {
  width: 100%;
  height: 24px;
  background-color: #1a1a1a;
  border-top: 2px solid #333;
  border-bottom: 2px solid #333;
  background-image: repeating-linear-gradient(
    90deg,
    #ffffff 0,
    #ffffff 12px,
    transparent 12px,
    transparent 24px
  );
  background-size: 24px 8px;
  background-position: center;
  background-repeat: repeat-x;
}
```

### 3. Fita Crepe Adesiva do Depoimento
- **Abordagem:** Bloco com rotação sutil, cantos recortados com `clip-path` poligonal simulando rasgo de fita e sombra realista.
```css
.tape-quote-box {
  background-color: var(--bg-tape-paper);
  transform: rotate(-1.5deg);
  clip-path: polygon(2% 0%, 98% 2%, 100% 96%, 1% 100%);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
  font-family: 'Caveat', cursive;
}
```

### 4. Botões com Brilho Neon Pulsante (Rodapé)
- **Abordagem:** Efeito de tubo de gás neon via múltiplos `box-shadow` e `text-shadow` em CSS, com animação de pulsação suave em CSS keyframes.
```css
.btn-neon-delivery {
  background: var(--accent-neon-green);
  color: #051408;
  font-family: 'Montserrat', sans-serif;
  font-weight: 800;
  border: 2px solid #ffffff;
  border-radius: 9999px;
  box-shadow: 0 0 10px rgba(37, 211, 102, 0.6), 0 0 25px rgba(37, 211, 102, 0.4);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.btn-neon-delivery:hover {
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 0 15px rgba(37, 211, 102, 0.9), 0 0 35px rgba(37, 211, 102, 0.7);
}
```

---

## 7. Especificação de Animações por Seção (Fase de Motion)

*Regras fundamentais:*
- Nada acima da dobra depende de JavaScript para ser visível;
- Motion carrega de forma assíncrona após o carregamento principal;
- Elementos contínuos estruturais não sofrem transformações pesadas; animações ocorrem apenas nas camadas-folha;
- Suporte estrito a `@media (prefers-reduced-motion: reduce)`.

### 1. Seção Hero
- **Entrada (ao carregar):** O hambúrguer principal executa uma entrada sutil com `scale(0.95)` para `scale(1)` e opacidade `0 -> 1` em 0.6s com curva suave `cubic-bezier(0.16, 1, 0.3, 1)`.
- **Idle / Loop Contínuo:**
  - Os dados 3D e as batatas fritas flutuam suavemente (`@keyframes floatDice`: translação vertical de `-6px` a `+4px` ao longo de 3.5s em loop infinito com atrasos alternados);
  - O traço do doodle neon pulsa sutilmente na opacidade (`0.85` a `1.0`) e intensidade do brilho.

### 2. Seção Destaques do Cardápio
- **Scroll Trigger:** Cada um dos 3 cards de lanche artesanal sobe levemente em cascata (`stagger: 0.12s`) à medida que entra na viewport.
- **Interação / Hover:**
  - Efeito `transform: translateY(-6px) scale(1.03)` no card do lanche;
  - O selo "PREÇO JUSTO" rotaciona suavemente de `-8deg` para `-3deg` no hover com transição elástica.

### 3. Seção The Griddle Craft
- **Entrada:** O bloco escuro surge com transição sólida; o texto "CROSTA MAILLARD" e a seta indicativa aparecem com efeito de carimbo.
- **Micro-interação:** Efeito sutil de fumaça subindo através de máscara SVG animada ou opacidade sutil em gradiente linear.

### 4. Seção Salão, Games & Avaliações
- **Entrada dos Polaroids:** Os dois quadros fotográficos inclinam-se suavemente para fora (`-3deg` à esquerda e `+3deg` à direita), como fotos dispostas sobre uma mesa.
- **Troféu 5.0 Estrelas:** Efeito de *shimmer* metálico (reflexo de luz dourada atravessando a taça via gradiente linear animado em background-position a cada 5 segundos).
- **Fita Crepe:** Surge com leve atraso como se estivesse sendo afixada por cima do troféu.

### 5. Seção Rodapé & Conversão
- **Botões Neon:** Pulsação rítmica sutil (*breathing glow*) a cada 2.5 segundos, atraindo o olhar diretamente para o CTA de conversão no WhatsApp.
- **Hover:** Acentuação do brilho neon e expansão tátil do botão.

---

## 8. PLANO DE IMAGENS DETALHADO (A etapa mais crítica)

### Mapeamento Completo dos Slots de Imagem

| Slot de Imagem | Tipo | Origem / Arquivo Exato | Estado Atual | Ação Necessária |
| :--- | :--- | :--- | :--- | :--- |
| **Slot 01: Hero Smash Central** | **FOTO REAL** | `imagens/imgi_11_487575963_17861662824381519_9056811469817664118_n.jpg` | Burger duplo real alto com cheddar e bacon, funcionário ao fundo desfocado | Isolar o hambúrguer recortando o fundo, preservar textura natural do pão australiano/escuro e brilho do cheddar. |
| **Slot 02: Destaque Cardápio 1 (Smash Clássico na Panelinha)** | **FOTO REAL** | `imagens/imgi_10_496843498_17866328319381519_5386910420512652647_n.jpg` | Burger com salada na frigideira de cobre, lata de Coca-Cola ao lado | Remover a lata de refrigerante, focar e enquadrar perfeitamente a panelinha de cobre de servir com o lanche artesanal. |
| **Slot 03: Destaque Cardápio 2 (Sobremesa Sweet Burger de Brigadeiro)** | **FOTO REAL** | `imagens/imgi_5_530934114_17877947007381519_5936854228646766371_n.jpg` | Burger recheado de brigadeiro na panelinha de cobre sobre mesa preta | Ajuste de enquadramento 4:3, realce do brilho do chocolate e nitidez do granulado. |
| **Slot 04: Destaque Cardápio 3 (Batata Frita Cheddar & Bacon)** | **FOTO REAL** | `imagens/imgi_13_480303596_17856018381381519_6158140000647637115_n.jpg` | Mesa com vários pratos; ao centro há a frigideira cheia de batatas com cheddar e bacon | Recortar em alta definição a frigideira de batatas fritas crocantes com cobertura farta de cheddar e bacon. |
| **Slot 05: Chapa / Crosta Maillard ("The Griddle Craft")** | **FOTO REAL (ou PLATE)** | `imagens/imgi_14_480462874_17855867607381519_8905061998602226559_n.jpg` | Chapeiro de luvas pretas segurando o burger artesanal com crosta perfeita | Tratar e enquadrar a foto real do chapeiro para o bloco de técnica, ou utilizar Plate de background da chapa com smash press. |
| **Slot 06: Salão & Fliperamas Retrô (Polaroid 1)** | **FOTO REAL** | `imagens/imgi_3_684162080_18399054097157455_4828267339453381939_n.jpg` | Fachada noturna aberta mostrando as mesas com cabines vermelhas e os fliperamas | Recorte estilizado mostrando o interior do salão iluminado e as telas de videogame nas mesas. |
| **Slot 07: Salão & Mesa Farta (Polaroid 2)** | **FOTO REAL** | `imagens/imgi_13_480303596_17856018381381519_6158140000647637115_n.jpg` | Visão ampla da mesa cheia de lanches nas panelinhas com sofá capitonê vermelho e parede de grafite | Enquadramento estilo polaroid valorizando o ambiente vibrante e descontraído. |
| **Slot 08: Fachada Noturna / Localização** | **FOTO REAL** | `imagens/imgi_18_475467386_18483171973036498_7822627043841522467_n.jpg` | Fachada real com o toldo preto "Hamburgueria Artesanal / Mr. Macário Burger" | Limpeza de reflexos e realce das informações visuais da fachada. |
| **Slot 09: Logotipo Oficial em Alta Definição** | **FOTO REAL (Vetorização)** | `imagens/imgi_2_470955742_906413548244684_6231596174404398718_n.jpg` | Thumbnail de 150x150 px com arte do selo circular | Upscale e vetorização mantendo todos os traços, tipografia e elementos idênticos ao original. |
| **Slot 10: Dados 3D Flutuantes** | **PLATE GERADO** | N/A (Elemento decorativo abstrato) | Gerar ativo decorativo isolado | Gerar dois dados brancos 3D realistas com pontos pretos, fundo transparente isolado. |
| **Slot 11: Troféu Dourado 5.0 Estrelas** | **PLATE GERADO / SVG** | N/A (Elemento de validação social) | Gerar ativo decorativo isolado | Gerar taça/troféu dourado 3D realista com estrelas e gravação "5.0", fundo transparente isolado. |

---

### Prompts PRONTOS para Plates Gerados (Copiar e Colar)

*Prioridade do projeto: Elementos que podem ser feitos em CSS/SVG foram projetados em código. Apenas ativos de renderização 3D complexos recebem prompts de geração:*

#### PLATE 1: Dados 3D Flutuantes (Hero e Destaques)
> **Prompt para Gerador de Imagem:**  
> `pair of realistic white six-sided gaming dice floating in mid-air, dynamic angle, one showing face 5 and another showing face 3, subtle motion blur, crisp black pips, soft studio rim lighting, isolated on solid white background, high resolution 3D render, photorealistic, clean edges, zero background artifacts, stock illustration style --ar 1:1 --no text, blur, shadows on background`

#### PLATE 2: Troféu Dourado 5.0 (Seção de Avaliações do Google)
> **Prompt para Gerador de Imagem:**  
> `shiny 3D golden championship trophy cup, polished metallic gold finish, front view, clean modern sculpt, subtle star relief details, sitting upright, elegant studio rim lighting, warm highlights, isolated on pure white background, ultra clean transparent cutout ready, 8k render --ar 1:1 --no text, base clutter, background elements`

#### PLATE 3 (Opcional): Fundo da Chapa Quente com Smash Press (The Griddle Craft)
> **Prompt para Gerador de Imagem:**  
> `cinematic close-up of a seasoned black cast iron commercial griddle, sizzling smash burger patty pressed firmly with a heavy rectangular cast iron meat press tool, wisps of fragrant white steam and faint sizzle smoke rising, golden caramelized crispy edges, melted butter drops, dark moody restaurant kitchen ambiance, shallow depth of field, dramatic side lighting, authentic food photography --ar 16:9 --no cartoon, text, sparks, burning flames`

---

### Prompts PRONTOS de Ajuste para Fotos Reais (Copiar e Colar)

*Seguindo a regra de ouro: "Mantenha tudo idêntico ao original, apenas corrija X". Cada prompt faz referência direta ao arquivo original em `imagens/`:*

#### AJUSTE 1: Hambúrguer Hero Principal
- **Arquivo de Referência:** `imagens/imgi_11_487575963_17861662824381519_9056811469817664118_n.jpg`
> **Prompt de Ajuste:**  
> `Using reference image imgi_11, keep the exact real double smash hamburger completely identical in all its organic details: dark artisanal bun with flour dust, thick melted golden cheddar cheese flowing down, crispy bacon strips, cooked beef patty texture, and green lettuce at the bottom. Do NOT generate a different burger. ONLY remove the background person and kitchen completely, isolate the hamburger on a clean transparent background (PNG alpha cutout), sharpen the edges cleanly, and slightly enhance the warm lighting and gloss of the melted cheddar cheese.`

#### AJUSTE 2: Destaque de Cardápio 1 — Burger na Panelinha de Cobre
- **Arquivo de Referência:** `imagens/imgi_10_496843498_17866328319381519_5386910420512652647_n.jpg`
> **Prompt de Ajuste:**  
> `Using reference image imgi_10, keep the exact real hamburger and the authentic round copper serving pan completely identical: preserve the toasted brioche bun, pickle slice on top of the melted cheese, artisanal beef patty, red onion slices, tomato, and fresh lettuce. Remove the red Coca-Cola can completely from the right side. Reconstruct the clean table surface where the can was located, centering the copper pan with the burger. Enhance clarity and resolution to 2048x2048, maintaining 100% natural, un-edited food realism.`

#### AJUSTE 3: Destaque de Cardápio 2 — Sweet Burger de Brigadeiro
- **Arquivo de Referência:** `imagens/imgi_5_530934114_17877947007381519_5936854228646766371_n.jpg`
> **Prompt de Ajuste:**  
> `Using reference image imgi_5, keep the exact dessert burger completely identical: golden brioche bun filled with rich chocolate brigadeiro and chocolate sprinkles (granulado), with a brigadeiro candy on top, served inside the signature copper pan. Keep the marble texture underneath. Clean up noise, enhance clarity and resolution to 2048x2048, preserving the authentic warm ambient lighting of the restaurant.`

#### AJUSTE 4: Destaque de Cardápio 3 — Batata Frita com Cheddar e Bacon na Panelinha
- **Arquivo de Referência:** `imagens/imgi_13_480303596_17856018381381519_6158140000647637115_n.jpg`
> **Prompt de Ajuste:**  
> `Using reference image imgi_13, locate the oval copper pan filled with golden french fries topped with generous melted cheddar cheese sauce and crispy fried bacon cubes sitting in the middle of the table. Crop and isolate this exact copper pan of loaded fries. Sharpen details, upscale resolution to 2048x2048, keep the real food textures 100% authentic, and remove the surrounding table clutter, placing it on a clean neutral background.`

#### AJUSTE 5: Logotipo Oficial em Alta Resolução / Vetorização
- **Arquivo de Referência:** `imagens/imgi_2_470955742_906413548244684_6231596174404398718_n.jpg`
> **Prompt de Ajuste:**  
> `Using reference image imgi_2, reproduce the exact circular logo emblem in razor-sharp high resolution (2048x2048 px) with transparent background: keep the outer red scalloped gear ring, the top circular arched text "HAMBURGUERIA ARTESANAL", the retro burger icon with yellow cheese slice, the central black ribbon with white vintage slab-serif text "MR. MACÁRIO BURGER", the red lower circle with stars, and the bottom text "SINCE 2023". Keep all fonts, proportions, colors, and line weights identical to imgi_2, with zero blurry artifacts, perfectly clean vector-quality edges.`

---

## 9. Perguntas para o Usuário (Decisões Subjetivas)

*Apenas decisões puramente conceituais/subjetivas que alteram o direcionamento criativo do projeto:*

1. **Tema da Seção de Experiência: Jogos de Tabuleiro (Mockup) vs. Fliperamas Retrô (Realidade):**
   O mockup desenhou "The Board Game Lounge" com fotos genéricas de cartas e tabuleiros. Contudo, as fotos reais do salão (`imgi_3`) mostram cabines com telas e fliperamas retrô embutidos nas mesas. **Deseja manter o tema "Jogos de Tabuleiro" do mockup ou prefere a verdade autêntica do negócio: "Hamburgueria com Fliperamas Retrô & Games no Salão"?** *(Recomendamos fortemente a verdade autêntica dos fliperamas retrô, pois é um diferencial único da casa).*

2. **Destaque do Hambúrguer Hero:**
   Prefere como destaque principal do Hero o hambúrguer duplo alto no pão escuro com cheddar escorrendo (`imgi_11` recortado e isolado) ou a foto icônica do chef segurando o blend com o grafite de arte urbana ao fundo (`imgi_14`)?

3. **Curadoria dos 3 Itens do Cardápio:**
   No mockup há 2 burgers e 1 batata frita genérica. Nas fotos reais do cliente, temos um produto exclusivo que se destaca: o **hambúrguer doce de brigadeiro** (`imgi_5`). Deseja que a trinca de destaques seja composta por: *(1) Smash Salgado Especial, (2) Batata Rústica Cheddar & Bacon na Panelinha, e (3) Sweet Burger de Brigadeiro*, para evidenciar toda a versatilidade da hamburgueria?

4. **Presença do Logotipo Oficial no Header:**
   O mockup ignorou o selo oficial e colocou apenas texto simples. Deseja exibir o selo clássico circular do Mr. Macário em destaque no cabeçalho ou prefere a abordagem minimalista apenas com o nome em tipografia display?

---

## 10. Pendências com o Cliente & Mensagem Pronta

*Estas pendências não bloqueiam o desenvolvimento do código nem o refinamento do design, mas são mandatórias antes da publicação final em produção.*

### Lista de Pendências Factuais:
1. **Destino do Botão Principal de Pedidos:** Confirmar se os botões de conversão devem abrir diretamente o WhatsApp (`(11) 96514-2258`) com mensagem automática pré-preenchida ou direcionar para o cardápio da 99App (`oia.99app.com`) / iFood.
2. **Nomes e Preços Oficiais dos Lanches em Destaque:** O Google Maps cita apenas "Mr Smash Duplo", "Mr Burguinho" e a faixa "R$ 20–40". Precisamos dos nomes de batismo exatos e dos valores em reais dos 3 pratos em destaque.
3. **Arquivo Original do Logotipo:** Solicitar o arquivo vetorizado original (.SVG / .AI) ou .PNG de alta resolução com transparência, caso o cliente já possua.
4. **Horários de Funcionamento dos Dias da Semana:** O Instagram indica "Quarta a domingo (18:45 às 23:30)". Confirmar se a hamburgueria fecha de fato às segundas e terças-feiras para o salão e para o delivery.
5. **Autorização de Uso de Imagem:** Validação para o uso no site das fotos que contêm o proprietário e o atendente (`imgi_18` e `imgi_3`).

---

### Mensagem Pronta para Envio ao Cliente (WhatsApp / E-mail)

```text
Olá, equipe do Mr. Macário Burger! Tudo bem com vocês? 🍔🔥

Estamos avançando a todo vapor na criação do site oficial da hamburgueria para destacar a qualidade dos lanches artesanais de vocês e turbinar as vendas de delivery e visitas ao salão na Vila da Saúde!

Para deixarmos tudo 100% perfeito e fiel ao negócio de vocês antes do lançamento, precisamos apenas confirmar 4 detalhes rápidos:

1. Pedidos Online: Os botões de "Pedir Agora" no site devem abrir direto o WhatsApp de vocês com uma mensagem pronta (ex: "Olá! Gostaria de fazer um pedido...") ou vocês preferem que direcione para o cardápio de delivery da 99App / iFood?

2. Destaques do Cardápio: Vamos colocar 3 pratos em destaque com fotos reais lindas de vocês (o burger artesanal na panelinha de cobre, a batata com cheddar e bacon, e o burger doce de brigadeiro que é sensacional!). Vocês poderiam nos passar o nome exato desses lanches e o preço atualizado de cada um?

3. Logotipo: Vocês teriam o arquivo do logo oficial redondo em alta qualidade (em PNG sem fundo ou PDF/Vetor)? Se não tiverem, não se preocupem que nós já restauramos uma versão nítida para vocês.

4. Horários: Confirmando o horário de funcionamento: vocês atendem de quarta a domingo das 18:45 às 23:30, fechando às segundas e terças, correto?

Muito obrigado! O site está ficando incrível e com a cara autêntica da casa! 🚀
```

---

## 11. Decisões Técnicas da Etapa de Otimização (10/10/2026)

Decididas sem consulta (sem impacto factual), conforme as regras do projeto:

1. **Fonte × build.** HTML/CSS/JS editáveis ficam em `src/`; `python scripts/build.py` (ou
   `npm run build`) gera `site/index.html`, `site/styles.min.css` e `site/js/*.min.js`. O build
   é commitado, então `site/` continua abrindo direto em `file://` e publicável sem build no servidor.
2. **CSS crítico por medição, não por lista manual.** O build abre a página em 13 resoluções e
   guarda as regras que casam com algo visível na primeira tela (incluindo o que esconde filhos
   desses elementos). Depois verifica que os estilos computados de toda a primeira tela são
   idênticos com só o crítico e com o CSS completo. Se divergir, o build falha. O CSS completo
   repete as regras críticas na ordem original, então a cascata final é a mesma de antes.
3. **CSS completo aplicado depois da primeira pintura** (`media=print` + duplo
   `requestAnimationFrame` no `onload`; `<noscript>` com link bloqueante para quem não tem JS).
4. **Minificação de CSS no nível 1 do clean-css.** O nível 2 fundiria propriedades repetidas e
   removeria fallbacks intencionais (`100vh` → `100svh`, PNG → `image-set()`, prefixos `-webkit-`).
5. **`aspect-ratio` fixo nas imagens com `srcset`.** Cada degrau tem altura arredondada; sem isso a
   caixa mudava frações de pixel conforme o arquivo escolhido e deslocava a página. Os valores são as
   proporções dos arquivos usados antes, então a geometria fica idêntica (verificado em 176 elementos
   × 12 resoluções).
6. **Montserrat sem recorte de eixo.** Recortada para 600–800, o texto em peso 800 (pílulas,
   botões neon) alargava até 6 px. Manter fidelidade custa 10 KB.
7. **Preload de fontes só via script em http(s).** Em `file://` o preload de fonte (sempre CORS)
   gerava erro de console; sem JS o `@font-face` carrega normalmente.
8. **`@font-face` no crítico só das famílias visíveis na primeira tela** (Bebas Neue, Montserrat).
   Caveat e Plus Jakarta Sans chegam com o CSS completo e saem da disputa de banda com o LCP.
9. **Mantidos como estão:** os efeitos de pintura cara (blur do header, blend da textura,
   drop-shadows), o texto < 12 px dos selos (auditoria `font-size`, Melhores Práticas 96) e o
   `<script>` carregador de motion inline (pequeno; externo custaria uma requisição a mais).

---

## 12. Decisões da Etapa de SEO Local (10/10/2026)

1. **`<h1>` = letreiro do hero** ("MR. MACÁRIO BURGER"). Era um `div` com `aria-hidden`; virou `<h1>`
   com tamanho e peso padrão neutralizados (`inherit`) e um complemento só para leitores de tela
   ("— hamburgueria artesanal na Vila da Saúde, São Paulo", dado real do CLIENTE.md). Pixels idênticos
   nas 12 resoluções.
2. **Tipo schema.org: `Restaurant`.** O CLIENTE.md mostra "Hamburgueria" com refeição no local,
   retirada e entrega; `FastFoodRestaurant` não descreve hamburgueria artesanal com salão.
3. **Publicado no JSON-LD só o que está confirmado:** nome, endereço completo com CEP, telefone,
   cozinha e Instagram (@mrmacarioburger). **Não publicados** (ficam comentados no `<head>`):
   horário (só a bio do Instagram; seg/ter não confirmado), faixa de preço (estimativa de 9 usuários
   do Google) e link do cardápio (só o domínio oia.99app.com). **`aggregateRating` não entra**: as
   63 avaliações 5,0 são do Google, de terceiros. Sem `geo`: o plus code 99HM+WV é curto e precisaria
   de conversão por referência; endereço com CEP basta.
4. **Domínio em um único campo** (`seo.config.json`). O build publica ou comenta todas as tags
   absolutas, além de `robots.txt` e `sitemap.xml`.
5. **Imagem OG** = composição aprovada do hero renderizada pelo próprio site, sem comandas, selos,
   pílulas e "BURGER" pequeno (texto pequeno demais para miniatura). Sem pessoas e sem fotos com
   autorização pendente.
6. **Favicons/manifest** gerados do logo real (selo oficial). O `theme-color`/manifest usa
   `--bg-cream` (#f4ede3), o fundo do header. O manifest é ligado por script só em http(s): em
   `file://` o Chrome gera erro de CORS ao buscá-lo.
7. **`alt` corrigidos para descrever a imagem, sem afirmar o que não é verificável:** as fotos de
   "mesa de jogos" não são do salão real (§1 deste documento: o salão real tem fliperamas e booths
   vermelhos), então o `alt` deixou de dizer "no salão do Mr. Macário Burger".

---

## 13. Decisões da Rodada Final (10/10/2026)

1. **Um único arquivo de dados do cliente:** `cliente.config.json` substitui o `seo.config.json`. Cada
   dado incerto (horário, faixa de preço, link do cardápio) tem `"confirmado"` e só vai para o JSON-LD
   com `true`; os não confirmados aparecem listados num comentário no `<head>` gerado. Itens que exigem
   texto/layout (destino do pedido, pratos, títulos) estão no mesmo arquivo em `_sem_efeito_automatico`,
   com o caminho de edição.
2. **Trava de publicação:** `imagensAprovadasParaPublicar: false` faz o build avisar "NÃO PUBLICAR".
   Motivo: a auditoria final confirmou, comparando lado a lado, que as fotos de comida, chapa e salão
   são geradas por IA e não correspondem às fotos reais do cliente (`assets.md`).
3. **Polimento feito agora (baixo risco, medido):** ícones PNG em paleta de 256 cores (-60%, diferença
   média 1,7/255); fotos reais não usadas e o logo-fonte movidos de `site/assets/` para `reserva/`
   (fora do deploy); scripts quebrados ou de uso único movidos para `scripts/_historico/`; avisos de
   licença das fontes em `site/fonts/LICENSE.txt`.
4. **Esperam cliente ou aparelho real:** ver `PENDENCIAS-CLIENTE.md` e `ROTEIRO-APARELHO-REAL.md`.
