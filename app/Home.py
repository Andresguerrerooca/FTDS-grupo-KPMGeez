"""Página de inicio de la plantilla Streamlit. No es el dashboard final del caso."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

APP_DIR = Path(__file__).resolve().parent
ROOT = APP_DIR.parent
for candidate in (ROOT, ROOT / "src", APP_DIR):
    text = str(candidate)
    if text not in sys.path:
        sys.path.insert(0, text)

from components.charts import render_placeholder_bar
from components.data import connection_status, placeholder_filter_data

st.set_page_config(page_title="AlbaMarket · plantilla", layout="wide")

st.title("AlbaMarket — plantilla de dashboard")
st.caption(
    "Fundamentos Tecnológicos en Data Science · entrega 2. "
    "Esta pantalla es una estructura de trabajo, no una solución."
)

st.markdown(
    """
Esta aplicación debe **consultar PostgreSQL** (vistas o tablas `core` / `analytics`).
No sustituyáis la conexión leyendo los CSV o Excel originales.

**Arranque**

```bash
streamlit run app/Home.py
```

Configuración: copiad `.env.example` a `.env`. Alternativa: `.streamlit/secrets.toml.example`.
Nunca subáis credenciales reales.
"""
)

ok, message = connection_status()
if ok:
    st.success(message)
else:
    st.warning("Base de datos no configurada o no disponible.")
    st.info(message)
    with st.expander("Cómo configurar la conexión"):
        st.markdown(
            """
1. Copiad `.env.example` a `.env`.
2. Completad `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER` y `DB_PASSWORD`.
3. Comprobad que PostgreSQL está en marcha (instalación local o `docker compose up -d`).
4. Reiniciad Streamlit. Si cambiasteis `.env` con la app abierta, limpiaos la caché.
5. SQLite solo es admisible con **justificación técnica documentada**, no por comodidad.
            """
        )

st.divider()
st.subheader("Filtro de ejemplo (datos ficticios de plantilla)")
st.caption("Este control no analiza el caso. Sirve para probar la interacción de Streamlit.")

demo = placeholder_filter_data()
zonas = ["Todas"] + sorted(demo["zona"].tolist())
zona = st.selectbox("Zona de demostración", zonas)
filtrado = demo if zona == "Todas" else demo[demo["zona"] == zona]
st.dataframe(filtrado, use_container_width=True, hide_index=True)
render_placeholder_bar(
    filtrado,
    "zona",
    "indicador_demo",
    "Indicador de plantilla (no usar en la entrega)",
)

st.divider()
st.subheader("Espacios de trabajo para el equipo")
st.markdown(
    """
Completad, como mínimo:

1. **Una tabla** con datos reales de la base (agregados; evitad listar clientes u pedidos individuales si no aporta).
2. **Tres visualizaciones** con título, unidades y propósito analítico.
3. Filtros solo si añaden valor para dirección.

Recomendación: no superéis ~10 elementos entre tablas, gráficos e indicadores.
Más elementos no implica mejor nota.
"""
)

col_a, col_b, col_c = st.columns(3)
with col_a:
    st.markdown("**TODO · Visualización 1**")
    st.info("Definid la pregunta de negocio y la consulta parametrizada.")
with col_b:
    st.markdown("**TODO · Visualización 2**")
    st.info("Elegid el tipo de gráfico en función del mensaje, no al revés.")
with col_c:
    st.markdown("**TODO · Visualización 3**")
    st.info("Incluid contexto, periodo y cautelas de calidad si aplica.")

st.markdown("**TODO · Tabla ejecutiva**")
st.dataframe(
    pd.DataFrame({"columna": ["pendiente"], "valor": ["conectar a analytics o core"]}),
    use_container_width=True,
    hide_index=True,
)

st.caption(
    "Caché: `get_engine` usa cache_resource (conexión). "
    "`fetch_dataframe` usa cache_data con TTL de 300 s (resultados). "
    "No concateneis SQL con texto del usuario; usad parámetros."
)
