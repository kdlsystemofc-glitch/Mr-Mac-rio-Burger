# assets.md — Inventário e Mapeamento de Assets

## Mapeamento de Slots para Arquivos Reais e Plates

| Slot no DESIGN.md | Arquivo Fonte Original | Arquivos WebP Gerados (site/assets) | Tipo de Ativo | Status / Fallback |
| :--- | :--- | :--- | :--- | :--- |
| **01. Hero Burger** | `assets/Hambúrguer duplo artesanal com bacon e cheddar-1.png` | `hero-burger-800.webp`<br>`hero-burger-1600.webp` | Plate RGBA transparente de alta fidelidade ao mockup | **Pronto.** Fallback real disponível: `imagens/imgi_11_...` |
| **02. Hero Dice (Dados 3D)** | `assets/Dois dados marfim flutuantes-2.png` | `dice-800.webp`<br>`dice-1600.webp` | Plate RGBA transparente | **Pronto.** |
| **03. Neon Doodle** | `assets/Contorno de bife em néon vermelho-10.png` | `neon-doodle-800.webp`<br>`neon-doodle-1600.webp` | Plate RGBA transparente | **Pronto.** Fallback: SVG nativo inline com filter drop-shadow |
| **04. Hero Flying Fries** | `design/secoes/01-hero.png` (crop & clean) | `flying-fries.webp` | Recorte RGBA transparente de alta fidelidade com salpicos | **Pronto.** |
| **05. Textura Vintage Global** | Síntese de Ruído Gaussiano Papel Kraft | `paper-noise.png` | Padrão contínuo RGBA em overlay multiplicativo | **Pronto.** |
| **06. Menu Destaque 1 (Burger Smash)** | `assets/Hambúrguer duplo artesanal com bacon e cheddar-1.png` | `hero-burger-800.webp`<br>`hero-burger-1600.webp` | Plate RGBA transparente no solo | **Pronto.** |
| **07. Menu Destaque 2 (Mr Burguinho)** | `assets/Cheesebúrguer artesanal com bacon e cheddar-3.png` | `menu-burguinho-800.webp`<br>`menu-burguinho-1600.webp` | Plate RGBA transparente no solo | **Pronto.** Fallback real: `imagens/imgi_10_...` |
| **08. Menu Destaque 3 (Loaded Fries)** | `assets/Batatas fritas com cheddar e bacon-5.png` | `menu-fries-800.webp`<br>`menu-fries-1600.webp` | Plate RGBA transparente no solo | **Pronto.** Fallback real: `imagens/imgi_13_...` |
| **09. The Griddle Craft (Banner)** | `assets/Smashburger a crepitar na chapa-4.png` | `griddle-craft-800.webp`<br>`griddle-craft-1600.webp` | Plate panorâmico 2172x724 | **Pronto.** Fallback real: `imagens/imgi_14_...` (chef) |
| **10. Lounge Mesa Jogos Esquerda** | `assets/Amigos a jogar cartas no restaurante-6.png` | `lounge-left-800.webp`<br>`lounge-left-1600.webp` | Plate fotográfico de cena com moldura madeira | **Pronto.** Fallback real: `imagens/imgi_13_...` (salão real) |
| **11. Lounge Mesa Jogos Direita** | `assets/Amigos a jogar cartas num restaurante-7.png` | `lounge-right-800.webp`<br>`lounge-right-1600.webp` | Plate fotográfico de cena com moldura madeira | **Pronto.** Fallback real: `imagens/imgi_3_...` (salão real) |
| **12. Troféu Dourado 5.0** | `assets/Troféu dourado 5,0 com cinco estrelas-8.png` | `trophy-5-800.webp`<br>`trophy-5-1600.webp` | Plate RGBA transparente dominante | **Pronto.** |
| **13. Rodapé Diner Retro** | `assets/Lanchonete vermelha retro com mesas cromadas-9.png` | `footer-diner-800.webp`<br>`footer-diner-1600.webp` | Plate panorâmico 2172x724 enquadrado nas margens | **Pronto.** |
| **14. Logotipo Oficial** | `imagens/imgi_2_470955742_906413548244684_6231596174404398718_n.jpg` | `logo-macario-800.webp`<br>`logo-macario-1600.webp` | Foto real / Selo oficial circular | **Pronto.** |
| **15. Fachada & Salão Reais** | `imagens/imgi_18_...` & `imgi_3_...` | `facade-real-800.webp`<br>`salon-real-800.webp` | Fotos reais do cliente | **Pronto.** |

## Notas de Auditoria
- **Nenhum slot ficou sem arquivo.** Todos os slots visuais do mockup foram atendidos por imagens de alta fidelidade geradas pelo usuário em `assets/` e convertidas para WebP em `site/assets/`.
- As fotos reais de `imagens/` também foram convertidas para WebP (800 e 1600px) e estão prontas como fallbacks factuais autênticos.
- *Nota de conformidade:* Os arquivos em `/design` e `/assets` brutos nunca são referenciados no HTML/CSS; o site consome exclusivamente os arquivos otimizados em `site/assets/*.webp` e `site/assets/*.png`.

## Etapa de Otimização (10/10/2026)

Nenhuma imagem nova foi gerada por IA nesta etapa — só redimensionamento (Lanczos, WebP q82,
alfa q100) dos arquivos já aprovados, via `scripts/gen_image_steps.py`. Mesmo recorte, mesma cor.

| Arquivo base | Degraus novos para `srcset` | Uso |
| :--- | :--- | :--- |
| `hero-burger-1600.webp` | `-480`, `-640`, `-720`, `-1200` | Hero (LCP) e Menu 1 |
| `menu-burguinho-1600.webp`, `menu-fries-1600.webp` | `-480`, `-720`, `-1200` | Menu 2 e 3 |
| `lounge-left-1600.webp`, `lounge-right-1600.webp` | `-480`, `-640`, `-1200` | Salão |
| `trophy-5-1600.webp` | `-480`, `-1200` | Troféu |
| `griddle-craft-1600.webp`, `footer-diner-1600.webp` | `-480`, `-1200` | Fundos de largura total |
| `dice-1600.webp` | `-160`, `-320` | Dados decorativos (exibidos a 61–125 px) |
| `neon-doodle-1600.webp` | `-120`, `-240` | Neon decorativo (exibido a 45–96 px) |

Outros arquivos:
- `paper-noise.webp` — conversão **sem perdas** de `paper-noise.png` (pixel-idêntica, 75 KB → 46 KB).
  O PNG continua como fallback no CSS.
- `torn-paper-top.svg`, `torn-paper-bottom.svg` — os mesmos paths que estavam inline no HTML,
  agora em arquivo externo cacheável (decorativo/CSS-like, não é foto).
- `site/fonts/*.woff2` — fontes auto-hospedadas (Google Fonts, licença SIL OFL 1.1, subset latin).
  Caveat e Plus Jakarta Sans recortadas ao peso usado com fontTools; Montserrat é o arquivo original.

Não usados pelo site (mantidos como reserva factual): `chef-real-*`, `facade-real-*`,
`logo-macario-*`, `menu-sweet-*`, `salon-real-*`.

## Etapa de SEO (10/10/2026)

| Arquivo | Origem | Observação |
| :--- | :--- | :--- |
| `site/assets/og-image.jpg` (1200x630) | Render do hero do próprio site (`scripts/gen_og_image.py`) | Sem texto pequeno, sem pessoas. Contém o hambúrguer do hero (mesmo arquivo já aprovado) |
| `site/favicon.ico` (16/32/48), `site/apple-touch-icon.png` (180), `site/icons/icon-192.png`, `icon-512.png`, `icon-maskable-512.png` | `logo-macario-1600.webp` (selo real, `imagens/imgi_2`), via `scripts/gen_icons.py` | Só redimensionado; o maskable tem margem na cor de fundo do próprio logo (#e6e3db) |

Nenhuma imagem nova gerada por IA nesta etapa.

## Classificação de origem — auditoria final (10/10/2026)

Comparação visual direta entre as fotos reais do cliente (`imagens/imgi_*`) e o que o site exibe.
**Corrige a tabela do topo deste arquivo**, que tratava os plates como "alta fidelidade" sem a marcação
exigida pelo CLAUDE.md.

| Arquivo no site | Origem real | Classificação |
| :--- | :--- | :--- |
| `hero-burger-*` (hero e Menu 1) | `assets/Hambúrguer duplo...-1.png` (Gemini). **Não é o hambúrguer do `imgi_11`**: o real tem pão escuro com farinha e alface; o do site tem pão brioche brilhante e bacon | **gerada por IA — NÃO é foto do cliente. Viola a regra de ouro (comida). Substituir antes de publicar.** |
| `menu-burguinho-*` | `assets/Cheesebúrguer...-3.png` (Gemini). Não corresponde ao `imgi_10` (lanche na panelinha de cobre) | **gerada por IA — NÃO é foto do cliente. Substituir.** |
| `menu-fries-*` | `assets/Batatas fritas...-5.png` (Gemini). O real (`imgi_13`) é servido na panelinha de cobre; o do site, em bandeja de papel xadrez | **gerada por IA — NÃO é foto do cliente. Substituir.** |
| `griddle-craft-*` | `assets/Smashburger a crepitar na chapa-4.png` (Gemini). Cena de cozinha com mão/espátula | **gerada por IA — retrata o preparo do cliente sem ser real. Substituir ou aprovar como ilustração.** |
| `lounge-left-*`, `lounge-right-*` | `assets/Amigos a jogar cartas...-6/-7.png` (Gemini). Pessoas e salão inexistentes; o salão real tem fliperamas e booths vermelhos | **gerada por IA — pessoas e salão inventados. Viola a regra de ouro. Substituir.** |
| `footer-diner-*` | `assets/Lanchonete vermelha retro...-9.png` (Gemini). Diner americano, não é o salão real | **gerada por IA — salão inventado. Substituir por foto real ou fundo CSS.** |
| `flying-fries.webp` | Recorte de `design/secoes/01-hero.png` (o **mockup**) | **Viola a regra "/design é só referência". Substituir por recorte de foto real ou remover.** |
| `logo-macario-*` (fonte dos favicons) | `imagens/imgi_2` (logo real) ampliado | **recriada por IA — confirmar com o cliente antes de publicar** (e pedir o arquivo original) |
| `trophy-5-*`, `dice-*`, `neon-doodle-*` | Plates decorativos (Gemini) | Permitido (decorativo/abstrato). O troféu cita a nota 5,0 real do Google |
| `paper-noise.*`, `torn-paper-*.svg` | Ruído sintético / SVG | Permitido (textura/forma) |
| `og-image.jpg` | Render do hero | **Herda o hambúrguer gerado por IA.** Regerar (`scripts/gen_og_image.py`) depois da troca |
| `chef-real-*`, `facade-real-*`, `salon-real-*`, `menu-sweet-*` | Fotos reais do cliente | Reais; não usadas no site (movidas para `reserva/` fora do deploy) |

**Fotos reais disponíveis para a substituição:** `imgi_11` (burger duplo), `imgi_10` (burger na
panelinha), `imgi_5` (sweet burger), `imgi_13` (mesa com batatas e lanches), `imgi_14` (chapeiro com
burger), `imgi_3`/`imgi_18` (fachada/salão — com pessoas, exigem autorização). Resolução de Instagram
(~1080 px): ampliar por IA a partir delas é permitido, com a marcação acima.
