---
title: "Benchmarking de painéis"
---

# Benchmarking — painéis de floresta urbana

Referências escolhidas pelo que oferecem de ideia de interface. Os links internacionais não puderam ser testados daqui (bloqueio a robôs); confira ao abrir.

| Painel | O que mostra | Indicadores | Ideias para o painel de SP |
|---|---|---|---|
| [**NYC Street Tree Map**](https://tree-map.nycgovparks.org/) (NYC Parks) | Cada árvore viária do censo, com espécie, DAP e histórico de manejo | Benefícios ecossistêmicos por árvore (água pluvial, energia, CO₂, ar), em US$ | Ficha por árvore com "benefício anual"; histórico de serviços; registrar cuidado cidadão |
| [**Melbourne Urban Forest Visual**](https://melbourneurbanforestvisual.com.au/) | Mapa de todas as árvores públicas com espécie, idade e expectativa de vida útil | Expectativa de vida útil, diversidade de espécies, meta de copa por bairro | Camada "expectativa de vida útil" → risco de perda futura; metas de copa por distrito |
| [**Treepedia**](https://senseable.mit.edu/treepedia) (MIT Senseable City Lab) | Índice de Verde Visível (GVI) a partir de imagens de rua | GVI por segmento de via e por cidade (ranking global) | Indicador de "verde percebido" por via; dialoga com o TCC (macrogeometria viária) |
| [**Paris — "Les arbres"**](https://opendata.paris.fr/explore/dataset/les-arbres/) (Open Data Paris) | Base aberta das árvores de alinhamento, parques e equipamentos | espécie, circunferência, altura, estágio | Modelo de dataset aberto e API para cobrar formato equivalente em SP |
| [**Barcelona — arbrat viari**](https://opendata-ajuntament.barcelona.cat/data/es/dataset/arbrat-viari) (Open Data BCN) / Pla del Verd | Árvores viárias e de parques; metas do plano do verde | cobertura de copa, m² de verde por habitante | Painel orientado a metas (alvo × realizado) por distrito |
| [**UrbVerde (USP)**](https://urbverde.iau.usp.br/) — referência nacional | Cobertura vegetal, temperatura de superfície, praças e indicadores sociais nos 645 municípios paulistas | % de cobertura vegetal, LST, distância a praças, renda/gênero/raça | Cruzar verde × vulnerabilidade social; linguagem acessível; série 1985–2024 |
| [**MapBiomas**](https://plataforma.brasil.mapbiomas.org/) — vegetação urbana, referência nacional | Ranking de municípios por vegetação intraurbana | % de vegetação na área urbanizada | Comparar SP com outras capitais (benchmark nacional) |

## Padrões de interface adotados

1. **Três níveis de leitura:** cartões de meta (topo) → mapa coroplético (meio) → tabela/ficha (fundo).
2. **Seletor de granularidade:** pixel ↔ quadra ↔ distrito ↔ subprefeitura, com o mesmo indicador.
3. **Tema claro/escuro** nativo do Quarto (`theme: light/dark`) e paleta sequencial verde validada para os dois.
4. **"Alvo × realizado"** sempre com fonte e data abaixo do número.
5. **Equidade em primeiro plano:** ordenar distritos por déficit de copa ponderado pela população vulnerável, não pela cobertura bruta.

## A levantar (sprint 2)

Capitais brasileiras com censo arbóreo aberto (Recife, Curitiba, Belo Horizonte, Rio de Janeiro), London i-Tree / mapa de copa, e Toronto Tree Canopy.
