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
- [x] Site renderizado e revisado nos temas claro e escuro
- [ ] Levantar benchmarks brasileiros (Recife, Curitiba, BH, Rio)

## Sprint 2.1 — site (2026-11-21) ✅
- [x] Painel na página inicial; mapa com destaque e ficha ao passar o mouse
- [x] Página **Metas** com atingimento visual e Meta 85 por distrito
- [x] Página **Orçamento**: ações ligadas a árvores (2705, 6655, 6682…), executores (subprefeituras, SMSUB, SME, SVMA) e subprefeituras em 2026
- [x] Página **Sprints**; rótulo no botão de tema; links clicáveis nas fontes e referências
- [x] Publicação no GitHub Pages (workflow) e card no portfólio

## Sprint 3 — metas e equidade
- [ ] Separar poda × remoção × plantio pelos empenhos/contratos (API-SOF com token ou Portal da Transparência)
- [ ] Saldo líquido (I09) e progresso da Meta 3 (I10); pedido e-SIC se faltarem remoções
- [ ] Déficit de copa (I05), custo por árvore (I14), calor × copa (I16)
- [ ] Índice de prioridade de plantio (déficit × vulnerabilidade × calor)

## Sprint 4 — granularidade fina e publicação
- [ ] Camada de pixel (tiles) e quadra
- [ ] Nativas da Mata Atlântica (I11) e carbono (I12) — dependem do inventário: a camada atual tem espécie vazia e DAP em só ~1,2% das árvores
- [ ] Revisão do aviso institucional; tornar o repo público; GitHub Pages; card no portfólio; depósito no Zenodo com DOI
- [ ] Rascunho do artigo em `paper/`
