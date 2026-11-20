# Observatório da Arborização Urbana de São Paulo

> **Aviso:** projeto pessoal e acadêmico, construído só com **dados abertos**. Não representa posição oficial da Prefeitura de São Paulo nem de nenhum de seus órgãos.

Painel e base de dados sobre as árvores da cidade de São Paulo: plantios, podas, remoções e quedas, cobertura vegetal e de copa, carbono, espécies nativas da Mata Atlântica e orçamento aplicado. Tudo cruzado com as metas do Plano Diretor Estratégico (PDE), do Plano Municipal de Arborização Urbana (PMAU), do PlanClima SP e do Programa de Metas 2025-2028, em várias escalas (pixel, quadra, distrito e subprefeitura).

**Palavras-chave:** arborização urbana · floresta urbana · cobertura vegetal · infraestrutura verde · PlanClima · Programa de Metas · SIG · dados abertos · São Paulo

**Status:** sprint 1 (fundação) — ver [`docs/backlog.md`](docs/backlog.md).

## Perguntas

1. Onde a cidade está mais longe das metas de copa e arborização, considerando calor e vulnerabilidade social?
2. O saldo líquido de árvores (plantios − perdas) acompanha a Meta 3 do Programa de Metas 2025-2028?
3. Como a demanda por manejo (SP156) e a execução orçamentária se distribuem entre as subprefeituras?

## Documentação

| Documento | Conteúdo |
|---|---|
| [Catálogo de fontes](docs/01_catalogo_fontes.md) | APIs, camadas e bases, com status de verificação |
| [Matriz de metas](docs/02_matriz_metas.md) | PDE, PMAU, PlanClima e Programa de Metas |
| [Benchmarking](docs/03_benchmarking.md) | Painéis de referência e padrões de interface |
| [Indicadores e painel](docs/04_indicadores_painel.md) | Indicadores I01–I16 e wireframe |
| [Decisões](docs/decisoes.md) · [Backlog](docs/backlog.md) | Registro de decisões e próximos sprints |

## Como reproduzir

1. Abra o notebook de coleta no Colab:
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/micadw/arborizacao-sp/blob/main/notebooks/001_coleta.ipynb)
2. Monte o Drive quando o notebook pedir; os dados brutos vão para a pasta do projeto no Drive (nunca para o git).
3. Para o orçamento, gere um token gratuito da API-SOF e guarde-o nos *Secrets* do Colab como `SOF_TOKEN`.
4. Site local: `quarto preview` na raiz do repositório.

## Estrutura

```
├── _quarto.yml · index.qmd · painel.qmd   site Quarto (tema claro/escuro)
├── docs/            documentação viva (catálogo, metas, indicadores…)
├── notebooks/       001_coleta.ipynb (…002_eda, 003_modelagem)
├── src/             funções de coleta e agregação
├── data/README.md   onde estão os dados (Drive / Zenodo)
├── reports/figures/ figuras
├── paper/           manuscrito .qmd
├── card.yml         metadados do card no portfólio micadw.github.io
└── CITATION.cff · .zenodo.json · LICENSE
```

## Licença

Código sob [MIT](LICENSE). Textos e figuras sob CC BY 4.0. Os dados seguem a licença de cada fonte (ver catálogo).

## Citação

Ver [`CITATION.cff`](CITATION.cff).
