"""Baixa camadas do GeoSampa (WFS) e gera agregados por distrito e subprefeitura.

Uso:  python -m src.agregados --raw data/raw --out site_data

Camadas confirmadas em 2026-11-20 (GetCapabilities):
  geoportal:arvore                         ~653 mil árvores viárias (atributos SISGAU)
  geoportal:cobertura_vegetal              ~272 mil polígonos (Mapeamento 2020, voo 2017)
  geoportal:risco_ocorrencia_queda_arvore  ocorrências de queda (SIGRC/Defesa Civil)
  geoportal:sac_quadra_arvore_urgencia     pedidos urgentes SP156 ligados a árvores
  geoportal:distrito_municipal (96) · geoportal:subprefeitura (32)
"""
from __future__ import annotations

import argparse
import io
import json
from pathlib import Path

import geopandas as gpd
import pandas as pd
import requests

WFS = "https://wfs.geosampa.prefeitura.sp.gov.br/geoserver/geoportal/wfs"
HEADERS = {"User-Agent": "arborizacao-sp (projeto academico; dados abertos)"}
PAGINA = 30_000  # limite por requisição do GeoServer do GeoSampa

# Categorias arbóreas do Mapeamento Digital da Cobertura Vegetal 2020 são
# identificadas pela descrição (ver docs/01_catalogo_fontes.md, fonte #10).
PADRAO_ARBOREO = r"arb[oó]re|floresta|bosque"


def wfs_csv(camada: str, props: list[str] | None = None) -> pd.DataFrame:
    """Baixa uma camada WFS como CSV, em páginas, sem geometria quando possível."""
    partes, inicio = [], 0
    while True:
        params = {"service": "WFS", "version": "2.0.0", "request": "GetFeature",
                  "typeNames": f"geoportal:{camada}", "outputFormat": "csv",
                  "count": PAGINA, "startIndex": inicio,
                  "sortBy": props[0] if props else None}
        if props:
            params["propertyName"] = ",".join(props)
        r = requests.get(WFS, params=params, headers=HEADERS, timeout=600)
        r.raise_for_status()
        df = pd.read_csv(io.StringIO(r.content.decode("utf-8")), low_memory=False)
        partes.append(df)
        print(f"  {camada}: +{len(df)}")
        if len(df) < PAGINA:
            break
        inicio += PAGINA
    return pd.concat(partes, ignore_index=True)


def wfs_geo(camada: str) -> gpd.GeoDataFrame:
    r = requests.get(WFS, params={"service": "WFS", "version": "2.0.0",
                                  "request": "GetFeature",
                                  "typeNames": f"geoportal:{camada}",
                                  "outputFormat": "application/json"},
                     headers=HEADERS, timeout=600)
    r.raise_for_status()
    return gpd.read_file(io.BytesIO(r.content)).set_crs(31983, allow_override=True)


def cobertura_por_distrito(dist: gpd.GeoDataFrame) -> pd.DataFrame:
    """Área de cada categoria de vegetação por distrito, por interseção de polígonos."""
    lim = dist[["sg_distrito_municipal", "geometry"]]
    partes, inicio = [], 0
    while True:
        r = requests.get(WFS, params={
            "service": "WFS", "version": "2.0.0", "request": "GetFeature",
            "typeNames": "geoportal:cobertura_vegetal",
            "outputFormat": "application/json", "count": PAGINA,
            "startIndex": inicio, "sortBy": "cd_identificador_vegetacao",
            "propertyName": "cd_identificador_vegetacao,"
                            "tx_descricao_categoria_subcategoria,ge_poligono"},
            headers=HEADERS, timeout=900)
        r.raise_for_status()
        g = gpd.read_file(io.BytesIO(r.content)).set_crs(31983, allow_override=True)
        if g.empty:
            break
        g["geometry"] = g.geometry.make_valid()
        x = gpd.overlay(g, lim, how="intersection", keep_geom_type=True)
        x["area"] = x.area
        x["arboreo"] = x["tx_descricao_categoria_subcategoria"].str.contains(
            PADRAO_ARBOREO, case=False, regex=True, na=False)
        partes.append(x.groupby(["sg_distrito_municipal",
                                 "tx_descricao_categoria_subcategoria", "arboreo"])
                      ["area"].sum().reset_index())
        print(f"  cobertura: página {inicio // PAGINA} ({len(g)})")
        if len(g) < PAGINA:
            break
        inicio += PAGINA
    return (pd.concat(partes)
            .groupby(["sg_distrito_municipal", "tx_descricao_categoria_subcategoria",
                      "arboreo"])["area"].sum().reset_index())


def main(raw: Path, out: Path, cob_csv: str | None = None) -> None:
    raw.mkdir(parents=True, exist_ok=True)
    out.mkdir(parents=True, exist_ok=True)

    print("limites")
    dist = wfs_geo("distrito_municipal")
    sub = wfs_geo("subprefeitura")

    print("árvores viárias")
    arv = wfs_csv("arvore", ["cd_identificador", "sg_distrito_municipal",
                             "nm_distrito_municipal", "nm_subprefeitura",
                             "dc_nm_popular", "dc_tipo_porte", "dc_tipo_estado_geral",
                             "qt_diametro_peito_dap", "dt_atualizacao_sisgau"])
    arv = arv.drop_duplicates("cd_identificador")
    arv.to_parquet(raw / "arvore.parquet")

    print("cobertura vegetal (interseção exata com os distritos — demora ~30 min)")
    if cob_csv and Path(cob_csv).exists():
        cob = pd.read_csv(cob_csv)
    else:
        cob = cobertura_por_distrito(dist)
        cob.to_csv(raw / "cob_area_distrito_categoria.csv", index=False)

    print("quedas e urgências")
    queda = wfs_csv("risco_ocorrencia_queda_arvore")
    queda.to_parquet(raw / "queda_arvore.parquet")
    urg = wfs_csv("sac_quadra_arvore_urgencia")
    urg.to_parquet(raw / "sac_arvore_urgencia.parquet")

    # ---- agregados por distrito ---------------------------------------------
    d = dist[["sg_distrito_municipal", "nm_distrito_municipal",
              "cd_identificador_subprefeitura", "qt_area_metro", "geometry"]].copy()

    n_arv = arv.groupby("sg_distrito_municipal").size().rename("arvores_viarias")
    com_especie = arv["dc_nm_popular"].notna()
    pct_especie = (arv[com_especie].groupby("sg_distrito_municipal").size()
                   / arv.groupby("sg_distrito_municipal").size()).rename("pct_com_especie")

    area_veg = cob.groupby("sg_distrito_municipal")["area"].sum()
    area_arb = cob[cob["arboreo"]].groupby("sg_distrito_municipal")["area"].sum()

    d = d.set_index("sg_distrito_municipal")
    d["arvores_viarias"] = n_arv
    d["pct_com_especie"] = (pct_especie * 100).round(1)
    d["pct_cobertura_vegetal"] = (area_veg / d["qt_area_metro"] * 100).round(1)
    d["pct_cobertura_arborea"] = (area_arb / d["qt_area_metro"] * 100).round(1)
    d["arvores_por_km2"] = (d["arvores_viarias"] / (d["qt_area_metro"] / 1e6)).round(0)
    d = d.reset_index()

    # subprefeitura: quedas (SIGRC) e urgências SP156 vêm com nome/sigla da sub
    queda["sg_sub"] = queda["nm_subprefeitura"].str.split(" - ").str[0].str.strip()
    s = sub[["sg_subprefeitura", "nm_subprefeitura", "cd_identificador_subprefeitura",
             "qt_area_metro", "geometry"]].copy()
    s["chave_sub"] = s["nm_subprefeitura"].str.upper().str.replace(r"[^A-Z]", "",
                                                                    regex=True)
    s["quedas_registradas"] = s["sg_subprefeitura"].map(queda.groupby("sg_sub").size())
    s["arvores_viarias"] = s["nm_subprefeitura"].map(arv.groupby("nm_subprefeitura").size())
    s["quedas_por_10mil_arvores"] = (s["quedas_registradas"] / s["arvores_viarias"]
                                     * 1e4).round(1)
    agg_d = d.groupby("cd_identificador_subprefeitura")[
        ["arvores_viarias"]].sum()  # conferência
    s["conf_arvores_soma_distritos"] = s["cd_identificador_subprefeitura"].map(
        agg_d["arvores_viarias"])

    # ---- saídas leves para o site --------------------------------------------
    for gdf, nome in [(d, "distrito"), (s, "subprefeitura")]:
        g = gdf.to_crs(4326)
        g["geometry"] = g.geometry.simplify(0.0003, preserve_topology=True)
        g.to_file(out / f"{nome}.geojson", driver="GeoJSON")
        g.drop(columns="geometry").to_csv(out / f"{nome}.csv", index=False)

    resumo = {
        "arvores_viarias_total": int(len(arv)),
        "arvores_com_especie_pct": round(float(com_especie.mean() * 100), 1),
        "cobertura_vegetal_pct_municipio": round(float(
            area_veg.sum() / d["qt_area_metro"].sum() * 100), 1),
        "cobertura_arborea_pct_municipio": round(float(
            area_arb.sum() / d["qt_area_metro"].sum() * 100), 1),
        "quedas_registradas": int(len(queda)),
        "quedas_periodo": [str(queda["dt_ocorrencia"].min()),
                           str(queda["dt_ocorrencia"].max())],
        "urgencias_sp156_arvore": int(len(urg)),
        "fonte_cobertura": "Mapeamento Digital da Cobertura Vegetal (voo 2017)",
    }
    (out / "resumo.json").write_text(json.dumps(resumo, ensure_ascii=False, indent=1))
    print(json.dumps(resumo, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", type=Path, default=Path("data/raw"))
    ap.add_argument("--out", type=Path, default=Path("site_data"))
    ap.add_argument("--cob-csv", default=None,
                    help="reaproveita a interseção já calculada (cob_area_distrito_categoria.csv)")
    a = ap.parse_args()
    main(a.raw, a.out, a.cob_csv)
