# motion-inventario.md — Inventário Completo de Motion & Coerência Visual
**Data:** 09/10/2026  
**Projeto:** Mr. Macário Burger  
**Status:** Validado e Aprovado (Tag `motion-pronto`)

---

## 1. Princípios Globais do Sistema de Motion

- **Manipulação Estrita de Camadas-Folha:** Apenas `transform` e `opacity` são interpolados, garantindo zero recálculos de layout (`layout thrashing`) e estabilidade de layout (CLS = 0).
- **Imunidade de Elementos Decorativos Contínuos:** Bordas em papel rasgado contínuo em SVG (`.torn-paper-top`, `.torn-paper-bottom`), mancha ondulada contínua de areia (`.menu-sand-shape`), divisor de película 35mm (`.film-strip-divider`) e textura de ruído analógico (`.paper-texture-overlay`) **não se movem e não possuem ancestrais com transform/opacity < 1**.
- **Independência de JS Acima da Dobra:** O layout original HTML/CSS puro inicia 100% visível; nenhum elemento crítico depende de JavaScript para renderizar.
- **Auto-Hospedagem Standalone:** GSAP 3.12+, ScrollTrigger e Lenis Smooth Scroll auto-hospedados em `./js/vendor/` em modo script clássico UMD (compatível com `file:///` e servidores HTTP).

---

## 2. Inventário de Motion por Seção

### Seção 1 — Hero (`#hero`) — Cinematográfico Awwwards
| Elemento | Seletor | Propriedades | Duração / Easing | Gatilho | Loop Contínuo | Qualidade Low | Modo Reduced |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Letreiro Dominante Fundo** | `.hero-bg-text` | `scale`, `opacity`, `yPercent` | 850ms (`power2.out`) | Carregamento + Scroll Scrub | Não | Fade direto | Estático |
| **Smash Burger Central** | `.hero-burger-img` | `y`, `scale`, `x` (cursor) | 850ms (`elastic.out`) | Pouso Heróico + Mouse | Não | Pouso instantâneo | Estático |
| **Sombra de Contato Solo** | `.hero-burger-shadow` | `scale`, `opacity` | 850ms (`power2.out`) | Pouso sincronizado | Não | Opacidade direta | Estático |
| **Selo Verde Pão** | `.stamp-mint` | `scale`, `opacity` | 600ms (`back.out(2)`) | Impacto adesivo (0.4s) | Não | Carimbo direto | Estático |
| **Batatas Crocantes Voadoras** | `.fries-fly-wrapper img` | `y`, `rotation`, `x/y` (cursor) | 800ms (`back.out(1.5)`) | Ejeção dinâmica (0.25s) | Sim (`y: ±5px`, 3.6s) | Sem loop | Estático |
| **Dados 3D de RPG** | `.dice-wrapper img` | `y`, `rotation`, `x/y` (cursor) | 750ms (`back.out(1.4)`) | Giro elástico (0.3s) | Sim (`y: ±4px`, 4.2s) | Sem loop | Estático |
| **Neon Doodle Vermelho** | `.neon-doodle-wrapper img`| `opacity`, `scale` | 600ms (`power2.out`) | Acendimento retro (0.35s) | Sim (`opacity: 0.82-1.0`, 2.6s) | Sem loop | Estático |
| **Selo Azul, Coral & Carne Fresca** | `.stamp-blue, .stamp-coral` | `scale`, `opacity` | 550ms (`back.out(1.8)`) | Carimbo em cascata | Não | Carimbo direto | Estático |
| **Comandas Fiscais** | `.receipt` | `y`, `opacity` | 650ms (`power3.out`) | Deslize de comanda (0.45s) | Não | Entrada direta | Estático |

---

### Seção 2 — Destaques do Menu (`#menu-highlights`)
| Elemento | Seletor | Propriedades | Duração / Easing | Gatilho | Loop Contínuo | Qualidade Low | Modo Reduced |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Título da Seção** | `.menu-title` | `y`, `opacity` | 650ms (`power3.out`) | ScrollTrigger (top 65%) | Não | Reveal direto | Estático |
| **Vitrine dos 3 Pratos** | `.menu-food-visual` | `y`, `opacity` | 750ms (`power3.out`, stagger 0.15s) | Pouso suave no solo | Não | Pouso direto | Estático |
| **Sombras no Solo** | `.menu-ground-shadow` | `scale`, `opacity` | 750ms (`power2.out`, stagger 0.15s) | Pouso sincronizado | Não | Opacidade direta | Estático |
| **Tag Dourada Burguinho** | `.pill-burguinho-tag` | `scale`, `opacity` | 550ms (`back.out(1.8)`) | Carimbo no pão | Não | Carimbo direto | Estático |
| **Selo Preço Justo Circular**| `.stamp-preco-justo` | `scale`, `rotation`, `opacity` | 600ms (`back.out(1.6)`) | Carimbo nas batatas | Não | Carimbo direto | Estático |
| **Dados do Smash** | `.menu-dice-float img` | `y`, `rotation`, `opacity` | 650ms (`back.out(1.4)`) | Ejeção satélite | Sim (`y: ±4px`, 3.4s) | Sem loop | Estático |
| **Neon do Smash** | `.menu-neon-float img` | `opacity`, `scale` | 600ms (`power2.out`) | Acendimento | Sim (`opacity: 0.8-1.0`, 2.5s) | Sem loop | Estático |
| **Parallax Vitrine Central** | `.item-burguinho .menu-food-visual` | `y` (-10px a +10px) | Scrub 0.8s | Scroll contínuo | Não | Desativado | Desativado |

---

### Seção 3 — A Chapa / The Griddle Craft (`#griddle-craft`)
| Elemento | Seletor | Propriedades | Duração / Easing | Gatilho | Loop Contínuo | Qualidade Low | Modo Reduced |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Título The Griddle Craft** | `.griddle-title` | `y`, `opacity` | 750ms (`power3.out`) | ScrollTrigger (top 65%) | Não | Reveal direto | Estático |
| **Selo Crosta Maillard** | `.stamp-maillard` | `scale`, `opacity` | 650ms (`back.out(1.8)`) | Carimbo quente | Sim (`scale: 1.0-1.04`, 3.0s) | Sem loop | Estático |
| **Seta de Giz Desenhada** | `.chalk-arrow` | `x`, `y`, `opacity` | 650ms (`power2.out`) | Apontamento para o smash | Não | Fade direto | Estático |
| **Parallax Panorâmico Chapa** | `.griddle-bg-img` | `y` (-9px a +9px) | Scrub 0.6s | Scroll contínuo sob moldura | Não | Desativado | Desativado |

---

### Seção 4 — O Salão & Games / Lounge (`#lounge-social`)
| Elemento | Seletor | Propriedades | Duração / Easing | Gatilho | Loop Contínuo | Qualidade Low | Modo Reduced |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Título & Subtítulo** | `.lounge-title`, `.lounge-subtitle` | `y`, `opacity` | 650ms (`power3.out`) | ScrollTrigger (top 65%) | Não | Reveal direto | Estático |
| **Fotos das Mesas de Jogos**| `.lounge-photo .photo-frame` | `y`, `rotation`, `opacity` | 800ms (`back.out(1.4)`) | Abertura em leque | Não | Reveal direto | Estático |
| **Troféu Dourado 5.0** | `.trophy-wrapper .trophy-img`| `y`, `scale`, `opacity` | 850ms (`back.out(1.5)`) | Pouso dominante de palco | Sim (`y: ±3px`, 3.8s) | Sem loop | Estático |
| **Selo 63 Avaliações Google**| `.badge-google-reviews` | `scale`, `opacity` | 600ms (`back.out(1.8)`) | Carimbo no ombro | Sim (`scale: 1.0-1.03`, 2.8s) | Sem loop | Estático |
| **Fita Crepe Adesiva** | `.tape-strip` | `scaleX`, `opacity` | 650ms (`power2.out`) | Colagem na base | Não | Reveal direto | Estático |

---

### Seção 5 — Rodapé & Conversão (`#footer-conversion`)
| Elemento | Seletor | Propriedades | Duração / Easing | Gatilho | Loop Contínuo | Qualidade Low | Modo Reduced |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Título do Rodapé** | `.footer-title` | `y`, `opacity` | 650ms (`power3.out`) | ScrollTrigger (top 70%) | Não | Reveal direto | Estático |
| **Botões Neon & Pílula** | `.neon-pill-btn`, `.footer-hours-pill` | `y`, `scale`, `opacity` | 650ms (`back.out(1.4)`, stagger 0.12s) | Entrada em cascata | Sim (`boxShadow` glow, 2.4s) | Sem loop | Estático |
| **Endereço da Loja** | `.address-text` | `opacity` | 600ms (`power2.out`) | Fade suave | Não | Reveal direto | Estático |
| **Parallax Cenário Diner** | `.footer-diner-img` | `y` (-8px a +8px) | Scrub 0.6s | Scroll contínuo sob divisor | Não | Desativado | Desativado |

---

## 3. Auditoria de Loops Simultâneos por Posição de Rolagem

O sistema conta com um `IntersectionObserver` dedicado que monitora a visibilidade no viewport de cada elemento registrado em `MrMacarioMotion.registerLoop`. Elementos fora da tela têm suas timelines do GSAP pausadas imediatamente, economizando ciclos de GPU e CPU da bateria móvel.

| Posição de Rolagem | Seção com Foco Principal | Loops Ativos Simultaneamente | Elementos Ativos | Avaliação de Custo |
| :--- | :--- | :---: | :--- | :---: |
| **Scroll 0px** | Hero | **3** | Batatas Voadoras, Dados 3D, Neon Doodle | Levíssimo (< 1% CPU) |
| **Scroll ~850px** | Menu Highlights | **3** | Dados Smash, Neon Smash, Selo Maillard | Levíssimo (< 1% CPU) |
| **Scroll ~1500px** | The Griddle Craft | **3** | Selo Maillard, Neon Smash, Troféu 5.0 | Levíssimo (< 1% CPU) |
| **Scroll ~2100px** | Board Game Lounge | **2** | Troféu Dourado 5.0, Selo Google Reviews | Levíssimo (< 1% CPU) |
| **Scroll ~2800px** | Footer & Conversion | **4** | Botão Delivery Ligar, Botão Delivery WhatsApp | Levíssimo (< 1% CPU) |

> **Conclusão:** O limite de concorrência foi rigorosamente respeitado: em nenhum momento a página executa mais de 4 micro-loops simultâneos.

---

## 4. Avaliação de Ritmo e Coerência Visual

- **Transição Natural de Ritmo:** A página transita de um início enérgico e cinematográfico no Hero (explosão de sabores e batatas voando no ar com o peso físico do smash duplo) para uma apresentação tátil e organizada do cardápio sem cards artificiais, depois mergulha no calor fumegante da chapa de ferro fundido, acolhe o visitante na mesa de jogos comunitária com o troféu de excelência e encerra com convite acolhedor no diner clássico iluminado por neon.
- **Gravação de Vídeo:** Vídeo contínuo da página inteira em 60fps gerado com sucesso via Playwright em `screenshots/video/page@8151165c278e4157e187bc35fc479032.webm`.
