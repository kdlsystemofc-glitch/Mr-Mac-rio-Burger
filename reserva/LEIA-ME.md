# reserva/ — fora do deploy

Imagens otimizadas que **não** são usadas pelo site, mantidas fora de `site/` para não serem publicadas.

- `chef-real-*`, `facade-real-*`, `salon-real-*`, `menu-sweet-*` — fotos **reais** do cliente
  (`imagens/imgi_*`), candidatas a substituir as imagens geradas por IA (PENDENCIAS-CLIENTE.md, item 1).
  As que mostram pessoas (fachada/salão/chef) exigem autorização de imagem.
- `logo-macario-*` — logo real ampliado (recriado por IA, confirmar com o cliente). É a fonte de
  `scripts/gen_icons.py`.
