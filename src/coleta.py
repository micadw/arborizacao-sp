"""Funções de coleta de dados abertos sobre arborização urbana em São Paulo.

Endpoints marcados "a confirmar" no catálogo (docs/01_catalogo_fontes.md)
devem ser testados no Colab antes de entrar no pipeline.
"""
from __future__ import annotations

import hashlib
import io
import os
from datetime import date
from pathlib import Path

import pandas as pd
import requests

CKAN_URL = "https://dados.prefeitura.sp.gov.br/api/3/action"
# A confirmar no sprint 2 (ver catálogo #1, #16, #17):
GEOSAMPA_WFS = os.environ.get(
    "GEOSAMPA_WFS",
    "https://wfs.geosampa.prefeitura.sp.gov.br/geoserver/geoportal/wfs",
)
SOF_URL = "https://gatewayapi.prodam.sp.gov.br:443/financas/orcamento/sof/v2.1"

TIMEOUT = 120
HEADERS = {"User-Agent": "arborizacao-sp (projeto academico; dados abertos)"}


# --- utilidades --------------------------------------------------------------
def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def registrar_download(registro: Path, fonte: str, url: str, arquivo: Path,
                       licenca: str = "a confirmar") -> None:
    """Acrescenta uma linha ao registro de downloads (CSV)."""
    linha = pd.DataFrame([{
        "data": date.today().isoformat(), "fonte": fonte, "url": url,
        "licenca": licenca, "arquivo": arquivo.name, "sha256": sha256(arquivo),
    }])
    linha.to_csv(registro, mode="a", index=False, header=not registro.exists())


# --- CKAN (dados.prefeitura.sp.gov.br) -----------------------------------------
def ckan_buscar(termo: str, linhas: int = 50) -> pd.DataFrame:
    """Lista datasets do portal de dados abertos que casam com `termo`."""
    r = requests.get(f"{CKAN_URL}/package_search",
                     params={"q": termo, "rows": linhas},
                     headers=HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    res = r.json()["result"]["results"]
    return pd.DataFrame([{
        "dataset": d["name"], "titulo": d["title"],
        "orgao": (d.get("organization") or {}).get("title"),
        "n_recursos": len(d.get("resources", [])),
        "modificado": d.get("metadata_modified"),
    } for d in res])


def ckan_recursos(dataset: str) -> pd.DataFrame:
    """Lista os recursos (arquivos) de um dataset CKAN."""
    r = requests.get(f"{CKAN_URL}/package_show", params={"id": dataset},
                     headers=HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    return pd.DataFrame([{
        "nome": x.get("name"), "formato": x.get("format"),
        "url": x.get("url"), "modificado": x.get("last_modified"),
    } for x in r.json()["result"]["resources"]])


def baixar(url: str, destino: Path) -> Path:
    """Baixa um arquivo em streaming para `destino`."""
    destino.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True, headers=HEADERS, timeout=TIMEOUT) as r:
        r.raise_for_status()
        with open(destino, "wb") as f:
            for bloco in r.iter_content(1 << 20):
                f.write(bloco)
    return destino


# --- GeoSampa (WFS) -------------------------------------------------------------
def wfs_camadas(url: str = GEOSAMPA_WFS) -> list[str]:
    """Nomes das camadas oferecidas pelo WFS (GetCapabilities)."""
    import xml.etree.ElementTree as ET
    r = requests.get(url, params={"service": "WFS", "request": "GetCapabilities"},
                     headers=HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    raiz = ET.fromstring(r.content)
    return sorted({el.text for el in raiz.iter() if el.tag.endswith("Name") and el.text
                   and ":" in el.text})


def wfs_camada(camada: str, url: str = GEOSAMPA_WFS, crs: str = "EPSG:31983",
               max_feicoes: int | None = None):
    """Baixa uma camada WFS como GeoDataFrame (GeoJSON)."""
    import geopandas as gpd
    params = {"service": "WFS", "version": "2.0.0", "request": "GetFeature",
              "typeNames": camada, "outputFormat": "application/json",
              "srsName": crs}
    if max_feicoes:
        params["count"] = max_feicoes
    r = requests.get(url, params=params, headers=HEADERS, timeout=TIMEOUT * 5)
    r.raise_for_status()
    gdf = gpd.read_file(io.BytesIO(r.content))
    return gdf.set_crs(crs, allow_override=True)


# --- API-SOF --------------------------------------------------------------------
def sof_despesas(ano: int, token: str, **filtros) -> pd.DataFrame:
    """Consulta despesas por dotação na API-SOF (token Bearer da Vitrine de APIs).

    Filtros aceitos dependem da versão da API — ver o manual SOF.
    """
    r = requests.get(f"{SOF_URL}/consultarDespesas",
                     params={"anoDotacao": ano, **filtros},
                     headers={**HEADERS, "Authorization": f"Bearer {token}"},
                     timeout=TIMEOUT)
    r.raise_for_status()
    js = r.json()
    lista = js.get("lstDespesas") or js.get("lstDespesa") or js
    return pd.json_normalize(lista)


# --- agregação ------------------------------------------------------------------
def contar_por_territorio(pontos, territorios, chave: str) -> pd.DataFrame:
    """Conta pontos (ex.: árvores, pedidos SP156) dentro de cada polígono."""
    import geopandas as gpd
    j = gpd.sjoin(pontos.to_crs(territorios.crs), territorios[[chave, "geometry"]],
                  predicate="within", how="inner")
    return j.groupby(chave).size().rename("n").reset_index()
