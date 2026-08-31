"""Acceso a datos para el dashboard. Las consultas parametrizadas viven aquí, no concatenadas en la UI."""

from __future__ import annotations

from typing import Any

import pandas as pd
import streamlit as st
from sqlalchemy import text
from sqlalchemy.engine import Engine

from course_project.config import ConfigError
from course_project.db import create_db_engine, ping


@st.cache_resource(show_spinner=False)
def get_engine() -> Engine:
    """Motor SQLAlchemy reutilizado entre reruns.

    cache_resource guarda el motor en memoria del proceso. Si cambiáis .env,
    usad «Clear cache» en Streamlit o reiniciad la app.
    """
    return create_db_engine()


def connection_status() -> tuple[bool, str]:
    try:
        engine = get_engine()
        ping(engine)
        return True, "Conexión correcta."
    except ConfigError as exc:
        return False, str(exc)
    except Exception as exc:  # noqa: BLE001
        return False, (
            "No se pudo conectar a la base de datos. "
            "Revisad host, puerto, nombre, usuario y que PostgreSQL esté en marcha. "
            f"Detalle técnico: {exc.__class__.__name__}."
        )


@st.cache_data(ttl=300, show_spinner=False)
def fetch_dataframe(sql: str, params: dict[str, Any] | None = None) -> pd.DataFrame:
    """Ejecuta SQL con parámetros enlazados. No interpoléis f-strings con input de usuario.

    cache_data guarda el resultado 300 s. Si actualizáis datos en PostgreSQL,
    el gráfico puede tardar en refrescar hasta que expire la caché.
    """
    engine = get_engine()
    with engine.connect() as connection:
        return pd.read_sql(text(sql), connection, params=params or {})


def placeholder_filter_data() -> pd.DataFrame:
    """Datos mínimos de demostración de controles. No son datos del caso."""
    return pd.DataFrame(
        {
            "zona": ["Norte", "Sur", "Este", "Oeste"],
            "indicador_demo": [12, 9, 15, 7],
        }
    )
