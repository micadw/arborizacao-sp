---
title: "Catálogo de fontes"
---

# Catálogo de fontes — arborização urbana de São Paulo

Levantamento do sprint 1 (2026-11-20). **Status:** `verificado` = página/metadado oficial consultado nesta data; `a confirmar` = existe indício, mas endpoint, formato ou cobertura ainda precisam ser testados no Colab.

Granularidade: **P** ponto/indivíduo · **px** pixel · **Q** quadra/lote · **D** distrito (96) · **S** subprefeitura (32) · **M** município.

## 1. Árvores e manejo

| # | Fonte | Órgão | Acesso / endpoint | Formato | Granul. | Cobertura | Atualização | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | GeoSampa — **Arborização Viária** (camada `arvore`) | SMUL/SVMA | Metadado: `metadados.geosampa.prefeitura.sp.gov.br/geonetwork/srv/api/records/6c4db956-6522-4630-bbb1-631bc3def5ea` · WMS/WFS GeoServer | WFS (GeoJSON/GML), shapefile | P | Árvores em calçadas, canteiros, rotatórias e calçadas de praças | Manual e pontual (por OS) | verificado (metadado); URL WFS a confirmar |
| 2 | **Inventário da Arborização Urbana** (PMAU Ação 01, mapeamento móvel laser 3D) | SVMA | Ainda não publicado; iniciado set/2025, ~650 mil árvores em até 3 anos | — | P | Em coleta (começou pela Vila Mariana) | — | verificado (notícia); dado indisponível |
| 3 | **SP156** — "Árvore: solicitar avaliação em calçadas e praças para fins de poda ou remoção" e afins | SMIT/SMSUB | CKAN: `dados.prefeitura.sp.gov.br/dataset/dados-do-sp156` | CSV | P (endereço/coord.) → D, S | 2012– (layout muda em 2015) | Periódica | verificado |
| 4 | GeoSampa — camadas SP156 (25 serviços) | SMUL/SMIT | WMS/WFS GeoSampa | WFS | P | Últimos 6 meses | Periódica | verificado (metadado) |
| 5 | **SGZ** — relação prévia de podas/remoções autorizadas (Lei 10.365/1987; Lei 10.919/1990) | SMSUB | `prefeitura.sp.gov.br/web/subprefeituras/w/zeladoria/349263` | PDF/planilha por subprefeitura | P → S | 2026 (página atual) | Contínua | verificado (página); formato a confirmar |
| 6 | **Relatório Anual da Gestão da Arborização Urbana** (PMAU Ação 30) | SVMA/DAU | PDF (ex.: `capital.sp.gov.br/documents/d/meio_ambiente/relatorio-gestao-arborizacao_2022-pdf`) | PDF (tabelas) | S, M | Anual (2022 localizado) | Anual | verificado |
| 7 | Plantios (balanço oficial) | SVMA/SECOM | Notícias e relatórios; série 2021–jun/2026 | Texto/PDF | M (às vezes S) | 2021– | Semestral | verificado (agregado) |
| 8 | Vegetação Significativa 2023 | SVMA | GeoSampa | WFS | polígono/P | 2023 | Pontual | verificado |
| 9 | Pedidos e-SIC (base de pedidos respondidos) | CGM | Portal de transparência | CSV | — | Desde implantação do e-SIC | Contínua | a confirmar (útil para dados não publicados) |

## 2. Cobertura vegetal, calor e carbono

| # | Fonte | Órgão | Acesso | Formato | Granul. | Cobertura | Status |
|---|---|---|---|---|---|---|---|
| 10 | **Mapeamento Digital da Cobertura Vegetal 2020** (15 categorias; ortofotos 2017/18 + LiDAR) | SVMA | GeoSampa (Verde/Recursos naturais) + relatório `RelCobVeg2020` | WFS / shapefile | polígono → px, D, S | 2017/18 | verificado |
| 11 | Ortofotos 2017 e 2020 (RGB) | SMUL | GeoSampa (Mapa Base) | WMS/raster | px | 2017, 2020 | verificado |
| 12 | **UrbVerde** (USP) — % de cobertura vegetal, temperatura de superfície, praças/parques + indicadores sociais | USP/IAU | Plataforma UrbVerde | painel; download a confirmar | px → setor, M | 1985–2024 (série) | verificado (plataforma); download a confirmar |
| 13 | **MapBiomas** — vegetação urbana (nota técnica) e coleções de uso e cobertura | MapBiomas | Google Earth Engine / downloads | raster 30 m | px | 1985– | verificado (nota técnica) |
| 14 | Inventário de emissões e remoções de GEE do município | SVMA/SECLIMA | Relatórios PlanClima | PDF | M | ciclos publicados | a confirmar |
| 15 | Fatores de estoque/sequestro por árvore (i-Tree Eco; literatura Mata Atlântica) | — | metodologia | — | P | — | a confirmar (método do sprint 3) |

## 3. Limites territoriais e contexto

| # | Fonte | Acesso | Granul. | Status |
|---|---|---|---|---|
| 16 | Distritos (`distrito_municipal`) | GeoSampa WMS/WFS | D | verificado (metadado) |
| 17 | Subprefeituras | GeoSampa WFS | S | a confirmar (nome da camada) |
| 18 | Quadras fiscais (`quadra_fiscal`) | GeoSampa WFS | Q | verificado (metadado) |
| 19 | Setores censitários e população (Censo 2022) | IBGE | setor → D | a confirmar |
| 20 | Sistema viário / largura de calçadas | GeoSampa | segmento | a confirmar (cruza com o TCC) |

## 4. Orçamento e metas

| # | Fonte | Acesso | Granul. | Status |
|---|---|---|---|---|
| 21 | **API-SOF** (execução orçamentária: dotação, empenhado, liquidado, credor) | `gatewayapi.prodam.sp.gov.br/financas/orcamento/sof/v2.1/...` — token *Bearer* gratuito pela Vitrine de APIs; manual SOF | órgão, unidade, programa, ação, subprefeitura | verificado (documentação) |
| 22 | Consulta SOF web | `orcamento.sf.prefeitura.sp.gov.br/orcamento/execucao.php` | idem | verificado |
| 23 | Orçamento Climático Municipal (PdM 2025-2028, Meta 111) | Anexos LOA / SECLIMA | ação | a confirmar |
| 24 | Programa de Metas 2025-2028 | `programademetas.prefeitura.sp.gov.br` + PDF | meta | verificado |
| 25 | Relatórios de acompanhamento do PlanClima SP | `prefeitura.sp.gov.br/web/planclimasp` | meta/ação | verificado |
| 26 | Plano de Ação das Subprefeituras | PDFs das audiências do PdM | S | a confirmar |

## Observações

- **Lacuna principal:** não há, por ora, base aberta e georreferenciada de *supressões* e *plantios* por endereço. Alternativas: SP156 (demanda), SGZ (autorizações), relatórios anuais (agregados por subprefeitura) e, futuramente, o Inventário. Se necessário, pedido via e-SIC — feito como cidadão, nunca com acesso do cargo.
- Antes de usar qualquer base, registrar no `data/README.md`: data do download, URL, licença e hash do arquivo.
