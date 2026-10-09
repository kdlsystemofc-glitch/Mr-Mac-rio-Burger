# PROGRESSO.md — Mr. Macário Burger

## Status do Projeto
**Fase Atual:** Etapa 1 Concluída — Análise Visual, Fatiamento e Arquitetura de Design (DESIGN.md)  
**Data:** 09/10/2026  
**Próxima Fase:** Aprovação do DESIGN.md e Preparação de Assets antes da Construção do Site  

---

## 1. O que foi feito nesta etapa
- [x] Leitura e confronto aprofundado entre `CLIENTE.MD` e `imagens/` vs. a referência `design/mockup-full.png`.
- [x] Inspeção minuciosa de todas as 8 imagens reais em `imagens/` (identificando produtos reais, panelinhas de cobre, salão com cabines vermelhas capitonê e fliperamas retrô, logo oficial redondo e fachada na Vila da Saúde).
- [x] Fatiamento do mockup por blocos de conteúdo limpos, salvo em `design/secoes/`:
  - `01-hero.png` (Hero section)
  - `02-menu-highlights.png` (Destaques do Cardápio)
  - `03-griddle-craft.png` (Técnica da Chapa / Crosta Maillard)
  - `04-board-game-lounge.png` (Salão / Experiência / Prova Social)
  - `05-footer-conversion.png` (Rodapé / Conversão)
- [x] Criação do documento central `DESIGN.md` contemplando:
  - Leitura honesta do mockup vs. realidade (identificando elementos fictícios de stock photo e incoerências).
  - Identificação dos elementos de assinatura e viabilidade técnica em CSS/SVG (borda de papel rasgado, fita de filme, selos, adesivos neon).
  - Paleta em HEX amostrada diretamente do mockup com auditoria e correção matemática WCAG 2.1.
  - Seleção tipográfica do Google Fonts (Bebas Neue / Montserrat / Plus Jakarta Sans / Caveat), respeitando a proibição de Inter/Roboto/Arial.
  - Tabela de camadas por seção (CSS / SVG / Foto Real / Plate).
  - Reinterpretação de elementos complexos em código real e responsivo.
  - Especificação detalhada de animações (motion phase, zero dependência de JS acima da dobra).
  - **Plano de Imagens Completo:** slots com fotos reais mapeadas e prompts prontos para plates gerados e ajustes em fotos reais.
  - Lista de perguntas objetivas para o usuário (decisões subjetivas).
  - Lista de pendências com o cliente e texto pronto de mensagem para envio via WhatsApp/E-mail.

---

## 2. O que falta fazer
- [ ] Validação das 4 perguntas subjetivas pelo usuário.
- [ ] Geração/ajuste dos assets visuais (recorte de fundo do burger hero, isolamento da batata e burger doce, vetorização do logo).
- [ ] Construção mobile-first do site (`index.html`, `styles.css`, `main.js`) seguindo estritamente as variáveis do `DESIGN.md`.
- [ ] Testes de contraste e responsividade de cada seção.
- [ ] Implementação de animações CSS/motion progressivo.
