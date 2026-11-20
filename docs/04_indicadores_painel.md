---
title: "Indicadores e desenho do painel"
---

# Indicadores e desenho do painel

## Indicadores

| Código | Indicador | Fórmula | Fonte (catálogo) | Granularidade | Sprint |
|---|---|---|---|---|---|
| I01 | Cobertura vegetal (%) | área vegetada / área total | #10, #12 | px, D, S, M | 2 |
| I02 | Cobertura arbórea em área urbanizada (%) | área de copa (classes arbóreas) / área urbanizada | #10 | D, S | 2 |
| I03 | Árvores viárias por km de via | nº de árvores viárias / km de via | #1, #20 | D, S | 2 |
| I04 | Árvores por habitante | nº de árvores viárias / população | #1, #19 | D, S | 2 |
| I05 | Déficit de copa | max(0, alvo distrital − I02) × área urbanizada | #10 + meta | D | 3 |
| I06 | Demanda por manejo | pedidos SP156 de poda/remoção por 1.000 árvores | #3, #1 | D, S | 2 |
| I07 | Atendimento SP156 | pedidos concluídos / pedidos abertos; tempo médio | #3 | S | 2 |
| I08 | Plantio (bruto) | nº de mudas plantadas no período | #6, #7 | S, M | 2 |
| I09 | Saldo líquido de árvores | plantios − (remoções + quedas) | #5, #6 (+ e-SIC) | S, M | 3 |
| I10 | Progresso da Meta 3 do PdM | I09 acumulado desde 2025 / 200.000 | M1 | M | 3 |
| I11 | % de espécies nativas da Mata Atlântica | árvores nativas / total (inventário) | #1, #2 | D | 4 |
| I12 | Estoque e sequestro de carbono | Σ biomassa(DAP, espécie) × fator de carbono | #1, #2, #15 | P → D | 4 |
| I13 | Execução orçamentária da arborização | liquidado / dotação atualizada (ações de plantio e manejo) | #21 | órgão, S | 2 |
| I14 | Custo por árvore plantada | liquidado em plantio / I08 | #21, #6 | S | 3 |
| I15 | Bosques urbanos e jardins de chuva | nº entregue / alvo | M3, M5 | M | 2 |
| I16 | Exposição ao calor × copa | correlação LST × I02 por distrito | #12, #10 | D | 3 |

## Wireframe do painel (`painel.qmd`)

```
┌──────────────────────────────────────────────────────────────┐
│ Observatório da Arborização · SP     [☀/☾ tema]  [sobre]      │
├──────────────────────────────────────────────────────────────┤
│ CARTÕES DE META                                              │
│ [Meta 3 PdM: xx% de 200 mil] [Bosques: 30/50] [Jardins: x/1000]│
│ [Cobertura vegetal 54%]  [Execução orç. 2026: xx%]           │
│ cada cartão: valor · barra alvo×realizado · fonte e data      │
├──────────────────────────────────────────────────────────────┤
│ FILTROS: indicador ▾ · granularidade (px|quadra|distrito|sub)│
│          ano ▾ · camada base (ruas|ortofoto) · só nativas ☐  │
├───────────────────────────────┬──────────────────────────────┤
│ MAPA (MapLibre/Leaflet)       │ RANKING                       │
│ coroplético do indicador      │ distritos ordenados por        │
│ legenda sequencial verde      │ déficit / demanda              │
│ clique → ficha do território  │ mini-série temporal           │
├───────────────────────────────┴──────────────────────────────┤
│ FICHA DO TERRITÓRIO: indicadores I01–I16 · pedidos SP156 ·   │
│ orçamento da subprefeitura · download CSV                    │
├──────────────────────────────────────────────────────────────┤
│ Rodapé: fontes, data de atualização, aviso de não oficialidade│
└──────────────────────────────────────────────────────────────┘
```

**Decisões de interface:** Quarto + Observable JS (estático, roda no GitHub Pages sem servidor); dados pré-agregados em GeoJSON/Parquet leves em `site_data/`; camada de pixel como tiles raster pré-gerados (sprint 4); acessibilidade: contraste AA nos dois temas e tabela alternativa ao mapa.
