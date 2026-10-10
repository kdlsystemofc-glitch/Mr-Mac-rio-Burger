# scripts/_historico — fora de uso

Mantidos só como registro das etapas anteriores. **Não rode**:

| Arquivo | Por que saiu de uso |
| :--- | :--- |
| `add_css.py` | Anexava CSS a `site/style.css`, que não existe mais (fonte em `src/css/`, build gera `site/styles.min.css`) |
| `update_torn.py`, `generate_torn.py`, `torn_*.txt` | Uso único para desenhar as bordas rasgadas. `update_torn.py` sobrescreveria o `site/index.html` gerado. As bordas agora são `site/assets/torn-paper-*.svg` |
| `run_lighthouse.py`, `parse_lh.py`, `lighthouse_mobile.json` | Substituídos por `scripts/lighthouse_runs.py` (3 execuções, mediana, modo `--prod`) |
| `loop_audit.json` | Saída da auditoria de loops da fase de motion (ver `motion-inventario.md`) |
