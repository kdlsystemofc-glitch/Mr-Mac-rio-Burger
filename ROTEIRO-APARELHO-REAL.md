# ROTEIRO-APARELHO-REAL.md — Teste em iPhone e Android

O que a automação (Chromium + WebKit no Windows, 15 telas, 5 modos) **não consegue garantir**:
Safari real do iOS, GPU de celular, toque de verdade, rede móvel, fontes e barras do sistema.
Faça este roteiro depois de publicar numa URL de teste em HTTPS (não use `file://` no celular).

**Aparelhos mínimos:** 1 iPhone recente (Safari) · 1 iPhone antigo/SE ou com iOS uma versão atrás ·
1 Android médio (Chrome) · 1 Android de entrada (≤ 4 GB de RAM), se possível.

Anote para cada item: ✅ ok · ⚠️ estranho (print + descrição) · ❌ quebrado.

---

## 1. Primeira carga (rede móvel 4G, não Wi-Fi)
- [ ] O hero aparece completo (letreiro, hambúrguer, selos) sem "piscar" nem trocar de layout.
- [ ] As fontes trocam de fallback para as definitivas sem empurrar o conteúdo.
- [ ] Tempo até ver o hambúrguer do hero: anote em segundos.
- [ ] Rolando rápido até o rodapé: nenhuma seção fica sem estilo ou sem imagem por mais de ~1 s.

## 2. Layout e leitura (retrato e paisagem)
- [ ] Sem rolagem lateral em nenhuma seção (arraste a página para os lados).
- [ ] Barra de endereço do Safari/Chrome aparecendo e sumindo: o hero não "pula" (usa `100svh`).
- [ ] Notch / Dynamic Island / barra de gestos não cobrem texto ou botões.
- [ ] Gire para paisagem e volte: nada fica cortado ou sobreposto.
- [ ] Textos pequenos dos selos (comandas, "63 AVALIAÇÕES") — anote se estão ilegíveis.
- [ ] Zoom de pinça até 200%: o texto continua legível e não sobrepõe.
- [ ] Tamanho de fonte do sistema no máximo (Acessibilidade): nada estoura.

## 3. Toque e conversão
- [ ] Botões "Pedir Delivery", telefone e WhatsApp fáceis de acertar com o polegar.
- [ ] "PEDIR NO DELIVERY // (11) 96514-2258" abre o discador com o número certo.
- [ ] Botão do WhatsApp abre o app com a mensagem pronta e o número certo (iPhone e Android).
- [ ] Links do menu do topo levam à seção certa, sem parar atrás do header fixo.
- [ ] Botão "PAUSAR" (canto inferior) pausa e retoma as animações; não cobre conteúdo importante.

## 4. Motion e desempenho
- [ ] Animações de entrada fluidas (sem travadas visíveis) no aparelho mais fraco.
- [ ] Rolagem suave e sem "pulos" (no celular a rolagem é nativa; Lenis só no desktop).
- [ ] Ative "Reduzir movimento" (iOS: Acessibilidade › Movimento; Android: Remover animações) e
      recarregue: nada anima, tudo aparece.
- [ ] Deixe a página aberta 2 minutos parada: o aparelho não esquenta nem trava (loops pausam fora da tela).
- [ ] Troque de aba/app e volte: as animações retomam sem erro.
- [ ] Modo economia de bateria ligado: a página continua usável.

## 5. Visual
- [ ] Modo escuro do sistema ligado: o site continua com as cores do design (não inverte).
- [ ] Textura de papel e bordas rasgadas sem "costuras" ou linhas finas entre seções.
- [ ] Blur do header (Safari) funciona e o texto do menu continua legível por cima das fotos.
- [ ] Brilhos neon dos botões do rodapé sem serrilhado.

## 6. Compartilhamento e ícones (depois de definir o domínio)
- [ ] Cole o link no WhatsApp: aparece título, descrição e imagem 1200x630.
- [ ] "Adicionar à Tela de Início" (iOS) e "Instalar/Adicionar" (Android): ícone com o logo, nome
      "Mr. Macário".
- [ ] Favicon aparece na aba.

## 7. Leitor de tela (rápido)
- [ ] VoiceOver (iOS) / TalkBack (Android): o título lido é "Mr. Macário Burger — hamburgueria
      artesanal na Vila da Saúde"; as imagens decorativas são puladas; os botões têm nome claro.

---

**Ao terminar:** registre aparelho, sistema, navegador e resultado no PROGRESSO.md. Itens ⚠️/❌ viram
correção (layout) ou pendência (conteúdo).
