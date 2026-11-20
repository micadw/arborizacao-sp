---
title: "Backlog"
---

# Backlog

## Sprint 1 — fundação (2026-11-20) ✅
- [x] Catálogo de fontes, matriz de metas, benchmarking, indicadores e wireframe
- [x] Estrutura do repositório (template DSA + site Quarto claro/escuro)
- [x] Notebook `001_coleta` e funções de coleta em `src/coleta.py`

## Sprint 2 — dados reais e primeira versão do painel
- [ ] Rodar `001_coleta` no Colab; confirmar URL do WFS do GeoSampa e nomes das camadas (árvores, distritos, subprefeituras, cobertura 2020)
- [ ] Baixar SP156 (2015–) e filtrar serviços de árvore; geocodificar e agregar por distrito/subprefeitura
- [ ] Obter token da API-SOF; extrair dotação/empenho/liquidação das ações de plantio e manejo (SVMA + subprefeituras)
- [ ] Extrair metas de arborização da revisão 2025 do PlanClima (M8)
- [ ] Calcular I01–I04, I06–I08, I13, I15 por distrito e subprefeitura
- [ ] Publicar painel v0 (cartões + coroplético distrital) — ainda privado
- [ ] Levantar benchmarks brasileiros (Recife, Curitiba, BH, Rio)

## Sprint 3 — metas e equidade
- [ ] Saldo líquido (I09) e progresso da Meta 3 (I10); pedido e-SIC se faltarem remoções
- [ ] Déficit de copa (I05), custo por árvore (I14), calor × copa (I16)
- [ ] Índice de prioridade de plantio (déficit × vulnerabilidade × calor)

## Sprint 4 — granularidade fina e publicação
- [ ] Camada de pixel (tiles) e quadra
- [ ] Nativas da Mata Atlântica (I11) e carbono (I12) — quando o inventário for publicado
- [ ] Revisão do aviso institucional; tornar o repo público; GitHub Pages; card no portfólio; depósito no Zenodo com DOI
- [ ] Rascunho do artigo em `paper/`
