# Contexto para o Claude

- Projeto pessoal/acadêmico do Mica (micadw): Observatório da Arborização Urbana de São Paulo.
- **Só dados abertos.** Nunca usar informação obtida no exercício do cargo na PMSP. Manter o aviso de não oficialidade no README, no site e no `card.yml`. Nenhum uso comercial.
- Fluxo: Drive (dados brutos) → GitHub (código) → Colab (execução) → Quarto/GitHub Pages (site) → Zenodo (dados públicos com DOI).
- Dados nunca entram no git (`data/raw`, `data/interim` ignorados). Só agregados leves em `site_data/`.
- Commits em Conventional Commits, em português (`feat(coleta): ...`).
- Python segue PEP 8; funções reutilizáveis em `src/`, notebooks importam de lá.
- Antes de mudar visibilidade do repo, ativar Pages ou publicar no Zenodo: perguntar ao Mica.
- Documentação viva em `docs/`; atualize `docs/decisoes.md` a cada decisão relevante e `docs/backlog.md` ao fim de cada sprint.
