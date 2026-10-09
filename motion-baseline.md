# motion-baseline.md — Linha de Base de Performance & Auditoria Pré-Motion
**Data:** 09/10/2026  
**Projeto:** Mr. Macário Burger  
**Ambiente:** Auditoria Lighthouse Mobile Oficial (Emulação Mobile Moto G4 / Slow 4G / Throttled CPU 4x)

---

## 1. Pontuações de Referência (Lighthouse Mobile)

| Categoria | Score de Referência | Status |
| :--- | :---: | :---: |
| **Performance** | **71 / 100** | Linha de Base |
| **Acessibilidade** | **100 / 100** | Perfeito |
| **Melhores Práticas** | **100 / 100** | Perfeito |
| **SEO** | **100 / 100** | Perfeito |

---

## 2. Core Web Vitals & Métricas de Carga

| Métrica | Valor de Referência | Classificação |
| :--- | :---: | :---: |
| **First Contentful Paint (FCP)** | 3.4 s | Moderado (devido a webfonts externas) |
| **Largest Contentful Paint (LCP)** | 5.8 s | Moderado (imagem hero burger 1600px) |
| **Total Blocking Time (TBT)** | **0 ms** | Excelente (zero bloqueio de thread principal) |
| **Cumulative Layout Shift (CLS)** | **0.007** | Excelente (estabilidade visual estrita) |
| **Speed Index (SI)** | 3.4 s | Estável |

---

## 3. Diretrizes de Tolerância para a Fase de Motion

Conforme as diretrizes globais do projeto:
- **Tolerância máxima de queda de desempenho:** O score de Performance do Lighthouse **NÃO deve cair mais de 3 pontos por fase** (limite mínimo tolerável: 68 na emulação throttled 4G).
- **CLS (Estabilidade de Layout):** Deve permanecer ≤ 0.05. Todas as animações devem manipular **estritamente `transform` e `opacity`** em nós-folha, nunca propriedades que gerem recalculo de layout (`top`, `left`, `margin`, `padding`, `width`, `height`).
- **TBT (Thread Principal):** Deve permanecer abaixo de 150ms. Scripts vendor carregam após `load` ou primeira interação.
- **Nenhum elemento acima da dobra depende de JS:** Em caso de JS desligado ou bloqueado por rede lenta, o layout estático já está 100% visível e navegável.
