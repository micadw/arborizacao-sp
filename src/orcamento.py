"""Execução orçamentária da arborização a partir da base aberta do SOF (CKAN).

Não precisa de token: usa os CSVs de `execucao-orcamentaria` e `base-dados-execucao`
em dados.prefeitura.sp.gov.br (licença CC-BY / CC0).

Uso:  python -m src.orcamento --raw data/raw/sof --out site_data
"""
from __future__ import annotations

import argparse
import unicodedata
from pathlib import Path

import pandas as pd
import requests

CKAN = "https://dados.prefeitura.sp.gov.br/api/3/action/package_show"
# Ações (projeto/atividade) ligadas a árvores, identificadas em 2026-11-20
ACOES = {
    "2705": "Manutenção e Operação de Áreas Verdes e Vegetação Arbórea",
    "6655": "Promoção da Arborização Urbana",
    "6682": "Manutenção e Operação de Viveiros de Produção",
    "1712": "Construção e Implantação de Viveiros Estacionais",
    "6686": "Manutenção e Operação de Viveiros Estacionais",
    "7129": "Ampliação, Reforma e Requalificação de Viveiros de Produção",
}
VALORES = ["Vl_Orcado_Ano", "Vl_Orcado_Atualizado", "Vl_EmpenhadoLiquido",
           "Vl_Liquidado", "Vl_Pago"]


def _urls() -> dict[int, str]:
    """URL do CSV anual mais recente de cada ano (2024 em diante)."""
    out: dict[int, str] = {}
    for ds in ("base-dados-execucao", "execucao-orcamentaria"):
        res = requests.get(CKAN, params={"id": ds}, timeout=60).json()["result"]
        for r in res["resources"]:
            u = r["url"]
            if r["format"].upper() != "CSV" or "consolidados" in u or "dicionario" in u:
                continue
            for ano, chaves in {2024: ["1224"], 2025: ["1225"], 2026: ["_2026"]}.items():
                if any(k in u for k in chaves):
                    out[ano] = u
    return out


def _sem_acento(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", str(s))
                   if not unicodedata.combining(c)).upper().strip()


def ler(raw: Path) -> pd.DataFrame:
    raw.mkdir(parents=True, exist_ok=True)
    partes = []
    for ano, url in sorted(_urls().items()):
        arq = raw / Path(url).name
        if not arq.exists():
            arq.write_bytes(requests.get(url, timeout=600).content)
        for enc in ("utf-8", "latin1"):  # a codificação varia entre os anos
            try:
                df = pd.read_csv(arq, sep=";", decimal=",", low_memory=False,
                                 dtype={"ProjetoAtividade": str}, encoding=enc)
                break
            except UnicodeDecodeError:
                continue
        df["ano"] = ano
        partes.append(df)
    df = pd.concat(partes, ignore_index=True)
    df["acao"] = df["ProjetoAtividade"].str.zfill(4)
    return df[df["acao"].isin(ACOES)]


def main(raw: Path, out: Path) -> None:
    df = ler(raw)
    por_acao = (df.groupby(["ano", "acao"])[VALORES].sum().reset_index())
    por_acao["ds_acao"] = por_acao["acao"].map(ACOES)
    por_acao.to_csv(out / "orcamento_acao_ano.csv", index=False)

    # Subprefeituras: órgãos cujo nome começa com "Subprefeitura"
    sub = df[df["Ds_Orgao"].str.match(r"(?i)^subprefeitura", na=False)].copy()
    sub["nm_sub"] = (sub["Ds_Orgao"].str.replace(r"(?i)^subprefeitura( d[eoa]s?)?", "",
                                                 regex=True).map(_sem_acento)
                     .replace({"CASA VERDE/LIMAO/CACHOEIRINHA": "CASA VERDE/CACHOEIRINHA"}))
    por_sub = (sub.groupby(["ano", "nm_sub"])[VALORES].sum().reset_index())
    # chave comum com a camada de subprefeituras do GeoSampa
    por_sub["chave_sub"] = (por_sub["nm_sub"].str.replace(r"[^A-Z]", "", regex=True)
                            .replace({"PERUSANHANGUERA": "PERUS",
                                      "SAOMIGUELPAULISTA": "SAOMIGUEL"}))
    por_sub["pct_liquidado"] = (por_sub["Vl_Liquidado"]
                                / por_sub["Vl_Orcado_Atualizado"] * 100).round(1)
    por_sub.to_csv(out / "orcamento_subprefeitura_ano.csv", index=False)

    orgaos = (df.groupby(["ano", "Ds_Orgao"])["Vl_Liquidado"].sum()
              .reset_index().sort_values(["ano", "Vl_Liquidado"], ascending=[True, False]))
    orgaos.to_csv(out / "orcamento_orgao_ano.csv", index=False)

    # Quem executa cada ação: SVMA, SMSUB (central), subprefeituras, SME, outros
    def grupo(orgao: str) -> str:
        o = str(orgao).lower()
        if o.startswith("subprefeitura"):
            return "Subprefeituras (32)"
        if "subprefeituras" in o:
            return "SMSUB (central)"
        if "verde e do meio ambiente" in o:
            return "SVMA"
        if "educa" in o:
            return "SME (escolas)"
        return "Outros órgãos"
    df["grupo_orgao"] = df["Ds_Orgao"].map(grupo)
    ga = (df.groupby(["ano", "acao", "grupo_orgao"])[VALORES].sum().reset_index())
    ga["ds_acao"] = ga["acao"].map(ACOES)
    ga.to_csv(out / "orcamento_grupo_acao_ano.csv", index=False)
    print(por_acao.round(0).to_string())
    print(por_sub[por_sub.ano == por_sub.ano.max()].sort_values(
        "Vl_Liquidado", ascending=False).head(10).to_string())


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", type=Path, default=Path("data/raw/sof"))
    ap.add_argument("--out", type=Path, default=Path("site_data"))
    a = ap.parse_args()
    main(a.raw, a.out)
