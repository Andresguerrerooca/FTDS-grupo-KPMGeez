"""Página adicional de plantilla. No es obligatorio usarla en la entrega."""

from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

st.set_page_config(page_title="Página plantilla", layout="wide")

st.title("Página plantilla")
st.write(
    "Streamlit descubre automáticamente los archivos de `app/pages/`. "
    "Podéis añadir páginas (por ejemplo, detalle operativo) o trabajar solo en `Home.py`. "
    "No es un requisito usar varias páginas."
)

st.markdown(
    """
TODO del equipo:

- ¿Esta página aporta algo a una audiencia de alta gerencia?
- Si no aporta, no la incluyáis en la narrativa de la defensa.
- Si la usáis, conectadla a la misma base de datos y a las mismas reglas de calidad.
"""
)
