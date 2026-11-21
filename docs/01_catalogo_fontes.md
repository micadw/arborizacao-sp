---
title: "Catálogo de fontes"
---

# Catálogo de fontes — arborização urbana de São Paulo

Levantamento do sprint 1 (2026-11-20), atualizado no sprint 2 (mesma data) com os downloads reais. **Status:** `verificado` = página/metadado oficial consultado nesta data; `a confirmar` = existe indício, mas endpoint, formato ou cobertura ainda precisam ser testados no Colab.

Granularidade: **P** ponto/indivíduo · **px** pixel · **Q** quadra/lote · **D** distrito (96) · **S** subprefeitura (32) · **M** município.

## 1. Árvores e manejo

| # | Fonte | Órgão | Acesso / endpoint | Formato | Granul. | Cobertura | Atualização | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | GeoSampa — **Arborização Viária** (`geoportal:arvore`) | SMUL/SVMA | [WFS GeoSampa](https://wfs.geosampa.prefeitura.sp.gov.br/geoserver/geoportal/wfs?service=WFS&request=GetCapabilities) (máx. 30 mil feições por requisição) | WFS (GeoJSON/CSV) | P (com distrito e subprefeitura) | **652.976 árvores** (2026-11-20); espécie vazia em ~100% e porte/DAP/estado em só ~1,2% (dados SISGAU antigos, 2010–2017) | Manual e pontual | **verificado (baixado)** |
| 2 | **Inventário da Arborização Urbana** (PMAU Ação 01, mapeamento móvel laser 3D) | SVMA | Ainda não publicado; iniciado set/2025, ~650 mil árvores em até 3 anos | — | P | Em coleta (começou pela Vila Mariana) | — | verificado (notícia); dado indisponível |
| 3 | **SP156** — "Árvore: solicitar avaliação em calçadas e praças para fins de poda ou remoção" e afins | SMIT/SMSUB | [dados-do-sp156](https://dados.prefeitura.sp.gov.br/dataset/dados-do-sp156) | CSV | P (endereço/coord.) → D, S | 2012– (layout muda em 2015) | Periódica | verificado |
| 4 | GeoSampa — camadas SP156 (25 serviços) | SMUL/SMIT | WMS/WFS GeoSampa | WFS | P | Últimos 6 meses | Periódica | verificado (metadado) |
| 4a | GeoSampa — **pedidos urgentes SP156 de árvore** (`geoportal:sac_quadra_arvore_urgencia`) | SMIT/Defesa Civil | WFS | WFS | P (logradouro) | **947 pedidos** (a partir de 2020) | Carga periódica | **verificado (baixado)** |
| 4b | GeoSampa — **ocorrências de queda de árvore** (`geoportal:risco_ocorrencia_queda_arvore`, fonte SIGRC) | Defesa Civil | WFS | WFS | P → S | **1.836 quedas, jan–set/2026** | Carga em 16/11/2026 | **verificado (baixado)** — interface com o TCC |
| 5 | **SGZ** — relação prévia de podas/remoções autorizadas (Lei 10.365/1987; Lei 10.919/1990) | SMSUB | [página da SGZ](https://prefeitura.sp.gov.br/web/subprefeituras/w/zeladoria/349263) | PDF/planilha por subprefeitura | P → S | 2026 (página atual) | Contínua | verificado (página); formato a confirmar |
| 6 | **Relatório Anual da Gestão da Arborização Urbana** (PMAU Ação 30) | SVMA/DAU | [relatório 2022 (PDF)](https://www.capital.sp.gov.br/documents/d/meio_ambiente/relatorio-gestao-arborizacao_2022-pdf) | PDF (tabelas) | S, M | Anual (2022 localizado) | Anual | verificado |
| 7 | Plantios (balanço oficial) | SVMA/SECOM | Notícias e relatórios; série 2021–jun/2026 | Texto/PDF | M (às vezes S) | 2021– | Semestral | verificado (agregado) |
| 8 | Vegetação Significativa 2023 | SVMA | GeoSampa | WFS | polígono/P | 2023 | Pontual | verificado |
| 9 | Pedidos e-SIC (base de pedidos respondidos) | CGM | Portal de transparência | CSV | — | Desde implantação do e-SIC | Contínua | a confirmar (útil para dados não publicados) |

## 2. Cobertura vegetal, calor e carbono

| # | Fonte | Órgão | Acesso | Formato | Granul. | Cobertura | Status |
|---|---|---|---|---|---|---|---|
| 10 | **Mapeamento Digital da Cobertura Vegetal 2020** (`geoportal:cobertura_vegetal`; 16 categorias; voo 2017) | SVMA | WFS GeoSampa | WFS | polígono → px, D, S | **272.117 polígonos**; é a base da Meta 85 do PlanClima | **verificado (baixado)** |
| 11 | Ortofotos 2017 e 2020 (RGB) | SMUL | GeoSampa (Mapa Base) | WMS/raster | px | 2017, 2020 | verificado |
| 12 | **UrbVerde** (USP) — % de cobertura vegetal, temperatura de superfície, praças/parques + indicadores sociais | USP/IAU | [Plataforma UrbVerde](https://urbverde.iau.usp.br/) | painel; download a confirmar | px → setor, M | 1985–2024 (série) | verificado (plataforma); download a confirmar |
| 13 | **MapBiomas** — vegetação urbana (nota técnica) e coleções de uso e cobertura | MapBiomas | [MapBiomas](https://plataforma.brasil.mapbiomas.org/) (GEE / downloads) | raster 30 m | px | 1985– | verificado (nota técnica) |
| 14 | Inventário de emissões e remoções de GEE do município | SVMA/SECLIMA | Relatórios PlanClima | PDF | M | ciclos publicados | a confirmar |
| 15 | Fatores de estoque/sequestro por árvore (i-Tree Eco; literatura Mata Atlântica) | — | metodologia | — | P | — | a confirmar (método do sprint 3) |

## 3. Limites territoriais e contexto

| # | Fonte | Acesso | Granul. | Status |
|---|---|---|---|---|
| 16 | Distritos (`geoportal:distrito_municipal`, 96) | GeoSampa WFS | D | **verificado (baixado)** |
| 17 | Subprefeituras (`geoportal:subprefeitura`, 32) | GeoSampa WFS | S | **verificado (baixado)** |
| 18 | Quadras fiscais (`quadra_fiscal`) | GeoSampa WFS | Q | verificado (metadado) |
| 19 | Setores censitários e população (Censo 2022) | IBGE | setor → D | a confirmar |
| 20 | Sistema viário / largura de calçadas | GeoSampa | segmento | a confirmar (cruza com o TCC) |

## 4. Orçamento e metas

| # | Fonte | Acesso | Granul. | Status |
|---|---|---|---|---|
| 21 | **Execução orçamentária (base aberta do SOF)** — sem token | [execucao-orcamentaria](https://dados.prefeitura.sp.gov.br/dataset/execucao-orcamentaria) (2026, CC-BY) e [base-dados-execucao](https://dados.prefeitura.sp.gov.br/dataset/base-dados-execucao) (2003–2025, CC0), CSV com `;` e vírgula decimal | órgão, unidade, programa, ação, fonte | **verificado (baixado 2024–2026)** |
| 21a | API-SOF (empenhos e credores) | API-SOF — token *Bearer* da [Vitrine de APIs](https://apilib.prefeitura.sp.gov.br/store/) | empenho, credor | verificado (documentação); só necessária para nível de empenho |
| 22 | Consulta SOF web | [orcamento.sf.prefeitura.sp.gov.br](https://orcamento.sf.prefeitura.sp.gov.br/) | idem | verificado |
| 23 | Orçamento Climático Municipal (PdM 2025-2028, Meta 111) | Anexos LOA / SECLIMA | ação | a confirmar |
| 24 | Programa de Metas 2025-2028 | [programademetas.prefeitura.sp.gov.br](https://programademetas.prefeitura.sp.gov.br/) | meta | verificado |
| 25 | Relatórios de acompanhamento do PlanClima SP | [PlanClima SP](https://prefeitura.sp.gov.br/web/planclimasp) · [revisão 2025 (consulta)](https://participemais.prefeitura.sp.gov.br/legislation/processes/345/topics) | meta/ação | verificado |
| 26 | Plano de Ação das Subprefeituras | PDFs das audiências do PdM | S | a confirmar |

## Observações

- **Lacuna principal:** não há, por ora, base aberta e georreferenciada de *supressões* e *plantios* por endereço. Alternativas: SP156 (demanda), SGZ (autorizações), relatórios anuais (agregados por subprefeitura) e, futuramente, o Inventário. Se necessário, pedido via e-SIC — feito como cidadão, nunca com acesso do cargo.
- Antes de usar qualquer base, registrar no `data/README.md`: data do download, URL, licença e hash do arquivo.

## Ações orçamentárias ligadas a árvores (identificadas no sprint 2)

| Ação | Descrição | Liquidado 2025 (R$ mi) | Liquidado 2026 até a extração (R$ mi) |
|---|---|---|---|
| 2705 | Manutenção e Operação de Áreas Verdes e Vegetação Arbórea | 345,8 | 408,9 |
| 6655 | Promoção da Arborização Urbana | 14,2 | 13,4 |
| 6682 | Manutenção e Operação de Viveiros de Produção | 10,0 | 8,2 |

A ação 2705 inclui manejo de praças e áreas verdes, não só árvores — usar como teto, não como custo da arborização. Detalhe por subprefeitura em `site_data/orcamento_subprefeitura_ano.csv`.
