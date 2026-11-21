---
title: "Backlog"
---

# Backlog

## Sprint 1 — fundação (2026-11-20) ✅
- [x] Catálogo de fontes, matriz de metas, benchmarking, indicadores e wireframe
- [x] Estrutura do repositório (template DSA + site Quarto claro/escuro)
- [x] Notebook `001_coleta` e funções de coleta em `src/coleta.py`

## Sprint 2 — dados reais e primeira versão do painel (2026-11-20, parcial)
- [x] WFS do GeoSampa confirmado; camadas baixadas: árvores (652.929), cobertura vegetal (272.117 polígonos), distritos, subprefeituras, quedas 2026 (1.836), urgências SP156 de árvore (947)
- [x] Cobertura vegetal e arbórea por distrito por interseção exata de polígonos (`src/agregados.py`)
- [x] Execução orçamentária 2024–2026 das ações 2705, 6655, 6682 por órgão e subprefeitura, **sem token** (base aberta do SOF no CKAN; `src/orcamento.py`)
- [x] Metas de arborização da revisão 2025 do PlanClima extraídas (Metas 52, 53, 55, 84, 85, 67, 68)
- [x] Painel v0.2: cartões + mapa por distrito/subprefeitura + tabela
- [ ] Conferir numeração das metas do PlanClima na versão final (jan/2026)
- [ ] Base completa do SP156 (dataset `dados-do-sp156`): filtrar serviços de poda/remoção e agregar por distrito
- [ ] Renderizar o site (`quarto render`) e revisar o painel nos temas claro e escuro
- [ ] Levantar benchmarks brasileiros (Recife, Curitiba, BH, Rio)

## Sprint 3 — metas e equidade
- [ ] Saldo líquido (I09) e progresso da Meta 3 (I10); pedido e-SIC se faltarem remoções
- [ ] Déficit de copa (I05), custo por árvore (I14), calor × copa (I16)
- [ ] Índice de prioridade de plantio (déficit × vulnerabilidade × calor)

## Sprint 4 — granularidade fina e publicação
- [ ] Camada de pixel (tiles) e quadra
- [ ] Nativas da Mata Atlântica (I11) e carbono (I12) — dependem do inventário: a camada atual tem espécie vazia e DAP em só ~1,2% das árvores
- [ ] Revisão do aviso institucional; tornar o repo público; GitHub Pages; card no portfólio; depósito no Zenodo com DOI
- [ ] Rascunho do artigo em `paper/`
