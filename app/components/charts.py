"""Espacio para gráficos reutilizables. Completad los TODO en la entrega 2."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st


def render_placeholder_bar(frame: pd.DataFrame, category: str, value: str, title: str) -> None:
    fig = px.bar(frame, x=category, y=value, title=title)
    fig.update_layout(margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig, use_container_width=True)
