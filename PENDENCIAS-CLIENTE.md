# PENDENCIAS-CLIENTE.md — O que falta do cliente

**Atualizado em:** 10/10/2026 · Dados configuráveis ficam em **um arquivo só**: `cliente.config.json`.
Depois de preencher: `npm run build` (detalhes no README e no DEPLOY.md).

Legenda: 🔴 bloqueia a publicação · 🟡 publicável, mas com perda (SEO/conversão/credibilidade) · ⚪ melhoria

---

## 🔴 1. Fotos reais de comida, chapa e salão

**Situação:** o hambúrguer do hero, os 3 pratos do menu, a chapa, as 2 fotos de "mesa de jogos" e o
salão do rodapé são **imagens geradas por IA**. Não são do Mr. Macário Burger (detalhe em
`assets.md` → "Classificação de origem"). As batatas voadoras do hero foram recortadas do mockup.
Isso contraria a regra principal do projeto e pode enganar o cliente final: o lanche anunciado não
é o lanche servido.

**O que pedir:** fotos atuais dos lanches em destaque, da batata, da chapa e do salão (fliperamas,
booths). Alternativa: autorização para usar recortes ampliados das fotos que já temos
(`imgi_11`, `imgi_10`, `imgi_5`, `imgi_13`, `imgi_14`).

**Efeito quando resolvido:** troca dos arquivos em `site/assets/` (mesmos nomes e degraus via
`scripts/gen_image_steps.py`), revisão dos `alt`, nova imagem de compartilhamento
(`scripts/gen_og_image.py`), e `"imagensAprovadasParaPublicar": true` no config. É a única pendência
que exige uma rodada de design (os recortes reais têm outra proporção e luz).

## 🔴 2. Textos visíveis herdados do mockup

| Texto no site | Problema | O que pedir |
| :--- | :--- | :--- |
| "MENU HIGHLIGHTS", "THE GRIDDLE CRAFT", "THE BOARD GAME LOUNGE" | Títulos em inglês do mockup | Títulos aprovados em português (ou o aceite do inglês) |
| **"FOOTER & CONVERSION"** | Rótulo de wireframe exibido como título | Título real (ex.: chamada para pedido) |
| Comanda "TOTAL: R$ 34,90" | Preço inventado | Remover, ou preço real de um lanche |
| Selo "100% CARNE FRESCA" | Afirmação não confirmada | Confirmar ou remover |
| Fita crepe: "Uma delícia, lanche maravilhoso e atendimento impecável!" | Junção editada de uma avaliação pública do Google (Maria Do Carmo) | Autorização para citar, ou trocar por trecho literal com atribuição |

**Efeito:** edição direta em `src/index.html` + `npm run build`. O H2 "FOOTER & CONVERSION" hoje
prejudica o SEO.

## 🟡 3. Destino dos botões de pedido

WhatsApp (atual, com mensagem pronta) ou cardápio da 99App/iFood?
**Efeito:** muda `href` e rótulos dos botões em `src/index.html`.

## 🟡 4. Horário de funcionamento

Hoje vem só da bio do Instagram (qua–dom, 18:45–23:30). Confirmar se fecha segunda e terça.
**Onde:** `cliente.config.json` → `horario` (`"confirmado": true`).
**Efeito:** publica `openingHoursSpecification` no JSON-LD (horário no Google). Se mudar, editar também
"ABRE 18:45" e "QUA A DOM // 18:45 - 23:30" em `src/index.html`.

## 🟡 5. Faixa de preço

"R$ 20–40" é estimativa de 9 usuários do Google.
**Onde:** `cliente.config.json` → `faixaDePreco`. **Efeito:** publica `priceRange` no JSON-LD.

## 🟡 6. Link exato do cardápio online

O Google mostra só o domínio `oia.99app.com`.
**Onde:** `cliente.config.json` → `linkCardapio.url`. **Efeito:** publica `hasMenu` no JSON-LD (e
pode virar botão, se o item 3 decidir assim).

## 🟡 7. Domínio

**Onde:** `cliente.config.json` → `dominio`.
**Efeito:** publica canonical, Open Graph/Twitter com imagem (prévia no WhatsApp/Instagram/Facebook),
URL e imagem no JSON-LD, `Sitemap:` no `robots.txt` e a URL no `sitemap.xml`. Sem domínio, a prévia
de link sai sem imagem.

## 🟡 8. Nomes oficiais e preços dos pratos em destaque

Hoje: "Mr Smash Duplo" e "Mr Burguinho" (do Google), terceiro prato sem nome.
**Efeito:** `alt` e eventuais legendas em `src/index.html`; depende do item 1 (as fotos atuais nem são
desses pratos).

## ⚪ 9. Logotipo original

O logo do site é uma ampliação por IA de uma miniatura (`imgi_2`) e diz "SINCE 2025". Pedir o arquivo
original (SVG/AI/PNG grande) e confirmar o ano.
**Efeito:** favicons e ícones refeitos com `python scripts/gen_icons.py`.

## ⚪ 10. Autorização de imagem

Fotos com o proprietário e o atendente (`imgi_18`, `imgi_3`, e `imgi_14` com o chapeiro). Hoje não são
usadas. **Efeito:** libera essas fotos para o item 1.

## ⚪ 11. Hospedagem

Escolha da hospedagem (fora do escopo do projeto). **Efeito:** aplicar compressão e cabeçalhos do
DEPLOY.md, o que vale cerca de 3 pontos no Lighthouse.

---

### Mensagem curta para o cliente

> Olá! O site do Mr. Macário Burger está pronto tecnicamente. Para publicar, precisamos de:
> 1) fotos atuais dos lanches em destaque, da batata, da chapa e do salão (ou autorização para usar as
> fotos do Instagram que já temos); 2) os nomes e preços dos lanches em destaque; 3) confirmar o
> horário (quarta a domingo, 18:45–23:30? fecha segunda e terça?); 4) se os botões de pedido levam ao
> WhatsApp ou ao app de delivery (e o link do cardápio); 5) o domínio do site; 6) o arquivo original
> do logo; 7) se o selo "100% carne fresca" procede; 8) se podemos citar a avaliação da Maria do Carmo
> no site. Obrigado!
